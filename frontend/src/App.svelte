<script lang="ts">
  import Counter from './lib/Counter.svelte'
  import { Navigation } from '@skeletonlabs/skeleton-svelte'
  import { House, Grid2X2Plus, LayoutPanelLeft, ChartNoAxesCombined } from '@lucide/svelte'
  import HomePage from './pages/HomePage.svelte'
  import AddPage from './pages/AddPage.svelte'
  import ArrangePage from './pages/ArrangePage.svelte'
  import DataPage from './pages/DataPage.svelte'

  let value = $state('home');
</script>

<main class="w-dvw h-dvh">
  <div class="card border-surface-100-900 grid h-full w-full grid-cols-[auto_1fr] border-[1px]">
    <Navigation.Rail {value} onValueChange={(v) => (value = v)}>
      {#snippet header()}
      <Navigation.Tile id='home' label='Home'><House/></Navigation.Tile>
      {/snippet}
      
      {#snippet tiles()}
        <Navigation.Tile id='add' label='Add Item'><Grid2X2Plus/></Navigation.Tile>
        <Navigation.Tile id='arrange' label='Arrange'><LayoutPanelLeft/></Navigation.Tile>
        <Navigation.Tile id='data' label='Data'><ChartNoAxesCombined/></Navigation.Tile>
      {/snippet}

    </Navigation.Rail>
    
    <!-- Grid Go Here? -->
    <div class="flex items-center justify-center">
      {#if value == 'home'}
        <HomePage></HomePage>
      {:else if value == 'add'}
        <AddPage></AddPage>
      {:else if value == 'arrange'}
        <ArrangePage></ArrangePage>
      {:else if value == 'data'}
        <DataPage></DataPage>
      {:else}
        <p class="opacity-20">(Content)</p>
      {/if}
    </div>
  </div>
</main>

<style>

</style>
