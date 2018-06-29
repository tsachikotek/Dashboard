import jenkins

def get_server_instance():
    jenkins_url = 'http://localhost:8080'
    server = jenkins.Jenkins(jenkins_url, username='tkotek', password='28929537')
    return server

"""Get job details of each job that is running on the Jenkins instance"""
def get_job_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    jobs = server.get_jobs()

    for j in jobs:
        job_instance = server.get_job(j[0])
        print("Get job - Done ===================================")
        print ('Job Name:%s' %(job_instance.name))
        print ('Job Description:%s' %(job_instance.get_description()))
        print ('Is Job running:%s' %(job_instance.is_running()))
        print ('Is Job enabled:%s' %(job_instance.is_enabled()))

if __name__ == '__main__':
    print (get_server_instance().get_version())


# server = jenkins.Jenkins('http://localhost:8080', username='tkotek', password='28929537')
server = get_server_instance();
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
print (server.jobs_count())


#server.delete_job('empty')
#server.delete_job('empty_copy')

server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
jobs = server.get_jobs()
#print (jobs)

server.build_job('empty')
server.disable_job('empty')
server.copy_job('empty', 'empty_copy')
server.enable_job('empty_copy')


# my_job = server.get_job_config('cool-job')
# print(my_job) # prints XML configuration
server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)

server.delete_job('empty')
server.delete_job('empty_copy')



# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'
server.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})



last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']


print(last_build_number)
print ('Done =============================================')

build_info = server.get_build_info('api-test', last_build_number)
print (build_info)

print ('Done =============================================')
# get all jobs from the specific view
jobs = server.get_jobs(view_name='All')
print (jobs)

get_job_details()

print("Hello World")
print("Hi there...")
