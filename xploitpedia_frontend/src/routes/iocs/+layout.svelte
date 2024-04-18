<script>
    let pageName = 'Indicators Of Compromise';
    import { page } from '$app/stores';  
    import List from "../../components/List.svelte";
    import Placeholder from '../../components/Placeholder.svelte';
    import { getItems } from '$lib/LandingPage';
    const pageNameID = $page.url.pathname.split('/')[2];

</script>

<div class="flex flex-row">
    {#await getItems('iocs/' + 'categories')}
    <Placeholder />
        
    {:then data}
    <List category={ pageName } currentId={ pageNameID } listItems={data}/>
        
    <slot/>
    {/await}

</div>