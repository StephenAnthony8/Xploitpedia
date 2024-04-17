<script>
    import List from "../../components/List.svelte";
    let pageName = 'Campaigns';
    import { fetchStiixIDS } from '$lib/SecondPage';

</script>

<div class="flex flex-row">

    <List category={pageName}/>
    <slot/>
</div>