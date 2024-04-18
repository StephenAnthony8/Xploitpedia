<script>
    import Main from '../components/Main.svelte';
    import { getAllItems } from '$lib/LandingPage';

    console.log(getAllItems())

</script>

{#await getAllItems()}
    <p>...</p>    
{:then data}
    <Main landingPageItems={data}/> <!--  -->
{/await}