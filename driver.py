import zomatoApiModule

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

if __name__ == "__main__":
	api_key = "906f9fa4a8b8ec2cbafad0c5bb27272d"
	output_type = "json"
	d = Driver(api_key,output_type)
	#print d.getCategories()
	city_id = d.getCityDetails("Delhi")['id']
	#d.getCollections(city_id)
	cuisines =  d.getCuisines(city_id) # list of dicts
	