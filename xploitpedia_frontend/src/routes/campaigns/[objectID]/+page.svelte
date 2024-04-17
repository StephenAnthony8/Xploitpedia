<script>
    import { page } from '$app/stores';
    import Stiix from '../../../components/Stiix.svelte';
        /* include js imports here */

    const pageName = $page.url.pathname.split('/')[2];
    const returnContent = [
        {name: 123, url: 'http://beatbox.com'},
        {name: 123, url: 'http://beatbox.com'}
    ] 

</script>

<Stiix referenceContent={returnContent}/>

