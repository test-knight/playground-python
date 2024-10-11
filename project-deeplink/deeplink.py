import re

# regex = "^(https:\/\/www.pandora.com(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:-]+\?corr=[a-z0-9-_]+&part=ug|https:\/\/pdora.co\/[a-zA-Z0-9]+|https:\/\/mobile-test.savagebeast.com:[0-9]{1,5}(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:]+\?corr=[a-z0-9-_]+&part=ug)$"
# regex = "^(http:\/\/www.pandora.com(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:-]+\?shareImp=true&part=ug&corr=[a-z0-9-_]+)|(https:\/\/www.pandora.com(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:-]+\?part=ug&corr=[a-z0-9-_]+|(https:\/\/www.pandora.com(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:-]+\?corr=[a-z0-9-_]+&part=ug|https:\/\/pdora.co\/[a-zA-Z0-9]+|htts:\/\/pdora.co\/[a-zA-Z0-9]+|https:\/\/mobile-test.savagebeast.com:[0-9]{1,5}(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:]+\?corr=[a-z0-9-_]+&part=ug)|http:\/\/mobile-test.savagebeast.com:[0-9]{1,5}(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:]+\?corr=[a-z0-9-_]+&part=ug)$"
# regex_suggested = "^((http)|(https)):\/\/((pdora.co\/[a-zA-Z0-9]+)|(((www.)?pandora.com(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:-]+)|(mobile-test.savagebeast.com:[0-9]{1,5}(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:]+))(\\?(shareImp=true&)?)?(part=ug&corr=[a-z0-9-_]+|corr=[a-z0-9-_]+&part=ug))$"
#
# regex_created = "^((http)|(https)):\/\/((pdora.co\/[a-zA-Z0-9]+)|(((www.)?pandora.com(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:-]+)|(mobile-test.savagebeast.com:[0-9]{1,5}(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:]+))(\\?(shareImp=true&)?)?(part=((ug)|(ug-mobile))&corr=[a-z0-9-_]+|corr=[a-z0-9-_]+&part=((ug)|(ug-mobile))))$"
#
# regex_new = "^((http)|(https)):\/\/(((www.)?(pandora.com)(\/(land\/station|station\/play)\/[0-9]+)?)|((pdora.co\/[a-zA-Z0-9]+)|(((www.)?pandora.com(\/([a-z0-9-]+){1,4}\/[a-zA-Z0-9:-]+|(land\/station|station\/play)\/[0-9]+))|(mobile-test.savagebeast.com:[0-9]{1,5}(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:]+))(\\?(shareImp=true&)?)?(part=((ug)|(ug-mobile))&corr=[a-z0-9-]+|corr=[a-z0-9-]+&part=((ug)|(ug-mobile)))|((pandora.app.link|pandora.test-app.link)\/[a-zA-Z0-9]+)))$"

#regex_new2 = "^((http)|(https)):\/\/((pdora.co\/[a-zA-Z0-9]+)|(((www.)?pandora.com(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:-]+)|(mobile-test.savagebeast.com:[0-9]{1,5}(\/[a-z0-9-]+){1,4}\/[a-zA-Z0-9:]+))(\\?(shareImp=true&)?)?(part=((ug)|(ug-mobile))&corr=[a-z0-9-]+|corr=[a-z0-9-]+&part=((ug)|(ug-mobile)))|((pandora.app.link|pandora.test-app.link)\/[a-zA-Z0-9]+))$"

regex_created = "^((http)|(https)):\/\/(www.)?((pandora.com)|(mobile-test.savagebeast.com:(7001|7443))|(pdora.co)|(pandora.app.link)|(pandora.test-app.link))((\/(land\/station|station\/play|podcast|playlist|artist|genre|station|[a-zA-Z0-9\-]*))(\/[a-zA-Z0-9\-\:]*)*((\?part=(ug|ug-mobile)&corr=[0-9]*)|(\?corr=[0-9]*&part=(ug|ug-mobile))|(\?shareImp=true&part=(ug|ug-mobile)&corr=[0-9]*))?)?$"

urls = ["https://www.pandora.com/playlist/PL:844424981908358:1756780791?corr=11908444&part=ug", "https://www.pandora.com/artist/metallica/metallica/enter-sandman/TRfVq9bxPxjtn6V?corr=11904070&part=ug", "https://www.pandora.com/artist/ariana-grande/thank-u-next-explicit/ALP39zPKlbJvw6K?corr=11902078&part=ug", "https://www.pandora.com/podcast/the-internet-of-things-podcast/PC:776?corr=1190776&part=ug", "https://www.pandora.com/podcast/the-internet-of-things-podcast/episode-215-what-google-killing-works-with-nest-means/PE:1524874?corr=11901524&part=ug", "https://pdora.co/2WWkWKo", "https://pdora.co/2WNTEWP", "https://mobile-test.savagebeast.com:7443/artist/breaking-benjamin/dear-agony/ALvbncjVd4zdd7w?corr=53721240&part=ug", "https://www.pandora.com/station/play/4172880106952276627?corr=1190776&part=ug", "https://www.pandora.com/genre/love-songs?corr=1190776&part=ug", "https://www.pandora.com/genre/2010s-dance-?corr=1190776&part=ug", "https://www.pandora.com/land/station/52536825952009869?corr=83225253&part=ug", "https://www.pandora.com/artist/marshmello/joytime-2/paralyzed/TR2tt9bptbvvXfw?part=ug&corr=82511293", "https://www.pandora.com/playlist/PL:844424943709097:1756780791?part=ug&corr=82518444", "https://pandora.com/artist/toro-y-moi/outer-peace/fading/TRz9dl76nzXcnK4?corr=27051628&part=ug",
"http://mobile-test.savagebeast.com:7001/artist/toro-y-moi/outer-peace/ALJZPJg4b9JzlxV?part=ug&corr=27052018",
"https://pandora.com/artist/toro-y-moi/outer-peace/ALJZPJg4b9JzlxV?part=ug&corr=27052018","http://mobile-test.savagebeast.com:7001/playlist/PL:562949953557521:7756167?part=ug&corr=27055629",
"https://pandora.com/playlist/PL:562949953557521:7756167?part=ug&corr=27055629",
"http://mobile-test.savagebeast.com:7001/podcast/serial/s01-episode-04-inconsistencies/PE:31?part=ug&corr=270531",
"https://pandora.com/podcast/serial/s01-episode-04-inconsistencies/PE:31?part=ug&corr=270531",
"http://mobile-test.savagebeast.com:7001/podcast/the-compass/PC:293?part=ug&corr=2705293",
"https://pandora.com/podcast/the-compass/PC:293?part=ug&corr=2705293",
"http://mobile-test.savagebeast.com:7001/tyler-creator/wolf/pigs/TRmj36t2vt6VtwV?shareImp=true&part=ug&corr=35525683",
"http://pandora.com/tyler-creator/wolf/pigs/TRmj36t2vt6VtwV?shareImp=true&part=ug&corr=35525683",
"https://www.pandora.com/artist/metallica/metallica/enter-sandman/TRfVq9bxPxjtn6V?corr=11904070&part=ug",
"https://pdora.co/2Yw7ORi",
"http://pdora.co/2Yw7ORi",
"https://www.pandora.com/playlist/PL:562949953557521:7756167?part=ug&corr=27055629",
"http://www.pandora.com/tyler-creator/wolf/pigs/TRmj36t2vt6VtwV?shareImp=true&part=ug&corr=35525683",
"https://www.pandora.com/artist/goldlink/spectrum-redlight-remix-single/spectrum-redlight-remix/TRm72vd3tghKqp9?part=ug-mobile&corr=17685818",
        "http://www.pandora.com/gramatik/sb2/chillaxin-by-sea/TRdVcfbrr2rtznP?shareImp=true&part=ug-mobile&corr=54974565",
        "https://pandora.app.link/by5cgYnjT3"]

for url in urls:
    if re.search(regex_created, url) is not None:
        print('VALID: %s'%(url))   
    else:
        print('INVALID: %s'%(url))