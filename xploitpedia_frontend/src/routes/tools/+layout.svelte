<script>
    let pageName = 'Intrusion Tools';
    import { page } from '$app/stores';  
    import List from "../../components/List.svelte";
    import Placeholder from '../../components/Placeholder.svelte';
    import { getItems } from '$lib/LandingPage';
    const pageNameID = $page.url.pathname.split('/')[2];

</script>

<div class="flex flex-row">
    {#key $page.url.pathname}
        
        {#await getItems('stiix/' + 'campaigns')}
            <Placeholder />
            
        {:then data}
            <List category={ pageName } currentId={ pageNameID } listItems={data}/>
            <slot/>
            
        {/await}
    {/key}

</div>