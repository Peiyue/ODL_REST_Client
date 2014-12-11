
data={
	"edgeProperties":[
						{
					"edge":{
			"tailNodeConnector":{
							"node":{
									"id":"00:00:00:00:00:00:00:02",
									"type":"OF"
									},
							"id":"2",
							"type":"OF"
								},
			"headNodeConnector":{
							"node":{
									"id":"00:00:00:00:00:00:00:51",
									"type":"OF"
									},
							"id":"2",
							"type":"OF"
								}
							},
			"properties":{
						"timeStamp": {
										"value": 1379527162648,
										"name": "creation",
									},
							"name": {
									"value": "s2-eth3"
									},
							"state": {
										"value": 1
									},
							"config": {
										"value": 1
										},
							"bandwidth": {
											"value": 10000000000
											}
						}
						},
{
"edge":{
"tailNodeConnector":{
"node":{
"id":"00:00:00:00:00:00:00:51",
"type":"OF"
},
"id":"2",
"type":"OF"
},
"headNodeConnector":{
"node":{
"id":"00:00:00:00:00:00:00:02",
"type":"OF"
},
"id":"2",
"type":"OF"
}
},
"properties":{
"timeStamp": {
"value": 1379527162648,
"name": "creation",
}
}
}
]
}
numoflinks=len(data['edgeProperties'])

print str(numoflinks),'links detected'

for link_index_old in range(numoflinks):
    s1=data['edgeProperties'][link_index_old]['edge']['tailNodeConnector']['node']['id'] #switch ID
    p1=data['edgeProperties'][link_index_old]['edge']['tailNodeConnector']['id'] #Port ID
    s2=data['edgeProperties'][link_index_old]['edge']['headNodeConnector']['node']['id'] #switch ID
    p2=data['edgeProperties'][link_index_old]['edge']['headNodeConnector']['id'] #Port ID
    print' Switch ',s1,' port ',p1,' connected to ',' Switch ',s2,' port ',p2
    


