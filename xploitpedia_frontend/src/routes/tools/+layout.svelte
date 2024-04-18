<script>
    let pageName = 'Intrusion Tools';
    import { page } from '$app/stores';  
    import List from "../../components/List.svelte";
    import { getItems } from '$lib/LandingPage';
    const pageNameID = $page.url.pathname.split('/')[2];

</script>

<div class="flex flex-row">
    {#await getItems('stiix/' + 'tool')}
    <p></p>
        
    {:then data}
    <List category={ pageName } currentId={ pageNameID } listItems={data}/>
        
    {/await}

    <slot/>
</div>