<script>
    import Main from '../components/Main.svelte';
    import { apiRoute, getAllItems, getItems } from '$lib/LandingPage';
    import { onMount } from 'svelte';

    

console.log(getAllItems());

/* let returnItems = {};
onMount(async () => {
    returnItems = await getItems();
}); */

/* 
console.log(returnItems) */

</script>

{#await getAllItems()}
    <p>loading...</p>    
{:then data}
    <Main landingPageItems={data}/> <!--  -->
{/await}