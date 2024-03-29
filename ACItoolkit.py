from acitoolkit.acitoolkit import *

# See capabilities
# dir()

url = 'https://192.168.1.241'
user = 'admin'
pw = 'admin@123'

# Create the session object
session = Session(url, user, pw)

# Login to the session
session.login()

# Get tenants
tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)
    print(tenant.descr)
    print('*' * 30)
    print(' ')

# Create a new Tenant
new_tenant = Tenant("Tenant_Name_Here")
new_tenant.get_url()
new_tenant.get_json()


# Create the application profile and the EPG
anp = AppProfile('soni_app', new_tenant)
epg = EPG('soni_epg', anp)

# Create the L3 Namespace
context = Context('soni_VRF', new_tenant)
bridge_domain = BridgeDomain('soni_bd', new_tenant)

# Associate the BD with the L3 Namespace
bridge_domain.add_context(context)
epg.add_bd(bridge_domain)

##### Tenant Creation is completed #####
print(new_tenant.get_url())
print(new_tenant.get_json())
response = session.push_to_apic(
    new_tenant.get_url(), data=new_tenant.get_json())
print(response)

tenants = Tenant.get(session)
for tenant in tenants:
    if tenant.name == 'Tenant_Name_Here':
        print(tenant.name)
    else:
        print(tenant.name)
        print(tenant.descr)
        print('*' * 30)
        print(' ')

# new_tenant.mark_as_deleted()
#session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())
