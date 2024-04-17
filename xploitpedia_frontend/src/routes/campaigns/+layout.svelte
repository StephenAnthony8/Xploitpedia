<script>
    import { page } from '$app/stores';  
    import List from "../../components/List.svelte";
    import { fetchStiixIDS } from '$lib/SecondPage';
    let pageName = 'Campaigns';
    const pageNameID = $page.url.pathname.split('/')[2];

</script>

<div class="flex flex-row">

    <List category={pageName}/>
    <slot/>
</div>