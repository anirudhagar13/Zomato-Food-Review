import httplib, urllib, urllib2, json

class zomatoApi:
	'''
		this class
			- makes the query (make_query) 
			- executes the query (execute_query)
			- manipulates the data (parse,json_parse)
	'''
	def __init__(self,api_key,output_type):

		self.api_key = api_key
		self.output_type = output_type
		#validate the api_key

		valid_output_types = {"xml":"application/xml","json":"application/json"}
		
		#validate output_type and throw exception if invalid

	def make_query(self,func,args={}):

		'''
			func - the call made to the API. eg. cities/reviews etc
			args - arguments to be passed alongwith a particular func
		'''
		#exit if func variable is empty

		#construct the query
		query = zomatoApiRequest(func,args,self.api_key)
		#execute the query
		return self.execute_query(query)

	def execute_query(self,query,headers = {}):

		'''
			query - object of class zomatoApiRequest
			headers - dict of meta data for API call
		'''
		request = urllib2.Request(query.full_url)
		request.add_header('X-Zomato-API-Key', self.api_key)
		
		'''
		for header, value in headers.iteritems():
      		request.add_header(header, value)
      	'''
      		
		response = urllib2.urlopen(request)
		self.response = response.read() # change name of self.response later

		#self.printdata(self.parse())
		return self.parse()

	def printdata(self,data):

		for key,value in data.iteritems():
			print(str(key) + " : " + str(value))
		
	def parse(self):

		data = self.json_parse()
		return data

	def json_parse(self):

		json_data = json.loads(self.response)
		return json_data


class zomatoApiRequest:
	'''
		this class
			- makes the URI(= URL + func)
			- encodes arguments into the URL
	'''
	def __init__(self,func,args,api_key):

		self.url = "https://developers.zomato.com/api/v2.1/"
		self.uri = ""
		self.full_url = ""
		self.func = func
		self.args = args
		self.api_key = api_key

		self.uri = self.make_uri()
		self.full_url = self.encode_args()
		#validate the uri generated

	def make_uri(self):

		#check if func is valid against all the funcs provided in the zomato api
		return self.url + self.func

	def encode_args(self):

		#validate_args() before encoding them
		if self.validate_args():
			#if method == "GET"
			return self.uri + '?' + urllib.urlencode(self.args)
			
			#if method == "POST"
			#do something else # later

	def validate_args(self):

		'''
			validates the arguments passed for the particular API call
			TODO
		'''
		return True

if __name__ == "__main__":
	api_key = "906f9fa4a8b8ec2cbafad0c5bb27272d"
	output_type = "json"
	z = zomatoApi(api_key,output_type)
	
	func = "categories"
	args = dict()
	categories = z.make_query(func,args)
	print categories
	
	#args["city_ids"] = 1
