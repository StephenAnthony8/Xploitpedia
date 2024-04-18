
/* general */
export const apiRoute = "http://localhost:5000/api/v1/";
export const frontendRoute = "/";


/* Header */
export const tabs = [
    {name: 'Campaigns', link: '/campaigns', color: 'hover:text-cyan-400'},
    /* {name: 'IOCs', link: '/iocs', color: 'hover:text-emerald-400'}, */
    {name: 'Malware', link: '/malware', color: ' hover:text-rose-400'},
    {name: 'Threat Groups', link: '/threat_groups', color: 'hover:text-orange-400'},
    {name: 'Tools', link: '/tools', color: 'hover:text-red-400'},
    {name: 'About', link: 'https://github.com/StephenAnthony8/Xploitpedia', color: 'hover:text-inherit'},
]


/* Main */
/* For testing purposes */
const objectPlaceholder = {
    name: 'Remcos Rat',
    campaigns : 'Unknown',
    discovery: '28/8/97',
    description: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dignissimos amet sunt molestiae vitae ex tenetur tempora cum quo sed eum excepturi rerum, in, accusantium quod dolor sint iste? Consequuntur, fuga.'
}

/* Main page data */
export const categories = [
    /* link should be the full link (route + name of the category in lowercase  with spaces replaced by '_')*/
    {name: 'Campaigns', description: 'Unauthorized operations undertaken by one or more threat groups against a given target', link: '/campaigns', body: objectPlaceholder},
    
    /* {name: 'Indicators Of Compromise', description: 'Forensic evidence of potential inrusions by threat actors on a system or network', link: '/iocs', body: objectPlaceholder}, */
    
    {name: 'Malware', description: 'Intrusive software developed by cybercriminals to commit various neafious activities', link: '/malware', body: objectPlaceholder},
    /* {name: 'Malware Families', description: 'Categorizations of malware according to similar characteristics and operations', link: '#', body: objectPlaceholder}, */
    {name: 'Threat Groups', description: 'Individuals or groups tracked by analysts that carry out cybercriminal activities', link: '/threat_groups', body: objectPlaceholder},
    
    {name: 'Intrusion Tools', description: 'Commercial / open source software that is used by a defender, pentester, red-teamer or adversary to conduct Exploit procedures', link: '/tools', body: objectPlaceholder},


];



/* Main page functions */
export const getItems = async (item) => {
    const response = await fetch(apiRoute + item);
    const returnItems = await response.json();
    const filteredData = returnItems;
    
    
    return filteredData;
}

export const getAllItems = async () => {
    const response_stiix = await getItems('stiix/display_items');
    const response_ioc = await getItems('iocs/display_item');

    const stiix = await response_stiix;
    const iocs = await response_ioc;
    return [stiix, iocs];
}

/* footer imports */
export const links = [
    {name: 'LinkedIn', link: 'https://www.linkedin.com/in/antony-steve-949008220/', identifier: 'Anthony Stephen'},
    {name: 'Github',link: 'https://github.com/StephenAnthony8', identifier: 'StephenAnthony8'}
]

export const linkedLinks ={
    'intrusion-set': frontendRoute + "threat_groups/",
    'tool': frontendRoute + 'tools/',
    'malware': frontendRoute + 'malware/'
}

export function capitalizeLetter (x) {
    const firstLetter = x.charAt(0).toUpperCase();

    /* const firstLetterCap = firstLetter.toUpperCase(); */

    const remainingLetters = x.slice(1);

    return(firstLetter + remainingLetters);
}


