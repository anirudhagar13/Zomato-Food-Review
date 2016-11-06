import zomatoApiModule
import json
import pickle

class Driver:
	def __init__(self,api_key,output_type):
		self.z = zomatoApiModule.zomatoApi(api_key,output_type)

	def getCategories(self):
		func = "categories"
		args = dict()
		output = self.z.make_query(func,args)
		categories = list()
		for i in output[output.keys()[0]] :
			#categories.append(i)
			categories.append(i[i.keys()[0]])
			#for key,value in i[i.keys()[0]].iteritems() :
			#	pass
				#print str(key) + " : " + str(value) 
		return categories

	def getCityDetails(self,city_name):
		func = "cities"
		args = dict()
		args["q"] = city_name
		output = self.z.make_query(func,args)
		return output['location_suggestions'][0]

	def getCollections(self,city_id):
		func = "collections"
		args =dict()
		args["city_id"] = city_id
		output = self.z.make_query(func,args)
		print output	

	def getCuisines(self,city_id):
		'''
			get list of all cuisines available
			in the city
		'''
		func ="cuisines"
		args = { 'city_id':city_id }
		cuisines = list()
		output = self.z.make_query(func,args)
		for i in output['cuisines'] :
			cuisines.append(i['cuisine'])
		#print output
		return cuisines

	def getEstablishments(self):
		#todo
		pass

	def getLocation(self, location_name):
		'''	
			get details of most relevant
			locations searched by name
		'''
		func = "locations"
		args = { 'query': location_name }
		output = self.z.make_query(func,args)
		return output['location_suggestions'][0]

	def getLocationDetails(self,entity_id,entity_type):
		'''
			get Foodie Index, Nightlife Index, 
			Top Cuisines, Best rated restaurants
		'''
		func = "location_details"
		args = { 'entity_id' : entity_id, 'entity_type' : entity_type } 
		output = self.z.make_query(func,args)
		#todo

	def search(self,city_name,cuisine_id,start=0,count=5):
		#TODO the default for entity_type
		'''
			get restaurants for the given location(entity_id)
			other args - cuisines/collections/category
						/establishment type/...
		'''
		func = "search"
		#loc_params = self.getLocation(city_name)
		#print loc_params
		#entity_id = loc_params['entity_id']
		#print "entity_id = ", entity_id
		args = { 'entity_id':1, 'cuisines':cuisine_id, 'start':start, 'count':count }
		output = self.z.make_query(func,args)
		#print output
		return output

	def exhaustiveSearch(self,city_name,cuisine_id):
		'''
			todo
		'''
		start = 0
		cnt = 20
		offset = start
		all_restaurants = dict()
		output = self.search(city_name,cuisine_id,start=offset,count=0)
		total_results = output['results_found']
		restro_ids = list()
		print "total_results = ", total_results
		
		while(offset + cnt < total_results):
			output = self.search(city_name,cuisine_id,start=offset,count=cnt)
			if output['restaurants']:
				for i in output['restaurants'] : # try extending instead of appending - rid the for loop
					restro_ids.append(i['restaurant']['id'])
					all_restaurants[i['restaurant']['id']] = i['restaurant']['location']['city']
			if not output['restaurants']:
				pass
				#print "search returned empty dict"	#change this	
			
			offset += cnt

		if(offset <= total_results):
			output = self.search(city_name,cuisine_id,start=offset,count=(total_results-offset))	
			if output['restaurants']:
				for i in output['restaurants'] :
					restro_ids.append(i['restaurant']['id'])
					all_restaurants[i['restaurant']['id']] = i['restaurant']['location']['city']
		
		#print len(restro_ids)
		#print restro_ids
		return all_restaurants

	def getReviews(self,res_id,start=0,count=5):
		'''
			get reviews of the given res_id
		'''
		func = "reviews"
		args = { 'res_id':res_id, 'start':start, 'count':count }
		all_reviews = list()
		output = self.z.make_query(func,args)
		for i in output['user_reviews']:
			review = list()
			review.append(i['review']['review_text'])
			review.append(i['review']['rating'])
			all_reviews.append(review)
		return all_reviews

	def exhaustivegetReviews():
		pass

	def getRestaurantDetails(self,res_id,count=20):
		#todo
		pass

	def getDailyMenu(self,res_id):
		func = "dailymenu"
		args = {'res_id':res_id}
		menu_items= list()
		output = self.z.make_query(func,args)
		print output
		'''
		for i in output['daily_menu']:
			# i is a dict
			for d in i['dishes']:
				#d is a dict
				menu_items.append(d)
		return menu_items
		'''
	def getCuisineId(self,city_name,cuisine_name):
		'''
			get cuisine id
			params - city_name - name of the city (string)
				   - cuisine_name - name of the cuisine (string)
		'''
		city = self.getCityDetails(city_name)['id']
		#print "city id = ", city
		for cuisine in self.getCuisines(city):
			if cuisine['cuisine_name'] == cuisine_name:
				return cuisine['cuisine_id']

			
if __name__ == "__main__":
	
	api_key = "906f9fa4a8b8ec2cbafad0c5bb27272d" #your zomato api_key here
	output_type = "json"
	d = Driver(api_key,output_type)
	#all_cuisines = d.getCuisines(1) # get all cuisines in city whose id is param
	cuisine_id = d.getCuisineId("Delhi","Chettinad")
	restros = d.exhaustive_search("Delhi",cuisine_id)	
	
	#print len(restros)
	#print restros

	with open('restros.pickle', 'wb') as handle:
		pickle.dump(restros, handle)
	
	'''
	with open('restros.pickle', 'rb') as handle:
		b = pickle.load(handle)

	if restros == b:
		print "pickle success"
	'''
	#restros = d.search("Delhi",cuisine_id,count=0)
	#print restros
	'''
	for i in restros:
		print d.getReviews(i,5)	
	'''
	
	#print d.getCategories()
	#city_id = d.getCityDetails("Delhi")['id']
	#d.getCollections(city_id)
	#cuisines =  d.getCuisines(city_id) # list of dicts
	#location_params = d.getLocation("Indiranagar, Bangalore") # dict of location params
		



	#d.getLocationDetails(location_params['entity_id'],location_params['entity_type'])
	#print location_params
	#all_restaurants = d.search(location_params['entity_id'],location_params['entity_type'],count=1)
	#print all_restaurants
	#print len(set(all_restaurants))
	#print all_restaurants
	'''
	res_reviews = dict()
	for res_id in all_restaurants:
		res_reviews[res_id] = d.getReviews(res_id,count=2)
	#print res_reviews
	'''
	'''
	menu = list() # a list of dicts
	for res in all_restaurants:
		menu.append(d.getDailyMenu(res))

	'''
	'''
	with open('Restaurant_IDs.json','w') as outfile:
		json.dump(all_restaurants,outfile)

	print "rest_ids dumped json"
	with open('Menu_Items.json','w') as outfile:
		json.dump(menu,outfile)
	'''