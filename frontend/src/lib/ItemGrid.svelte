<script lang="ts">
  import Item  from '../lib/Item.svelte'
  import type { ItemData } from '../api/entities.ts'

  export let data: Array<ItemData> = [];
  export let columns: number = 3;
</script>

<div class="grid gap-4 p-4" style="grid-template-columns: repeat({columns}, minmax(0, 1fr));">
  {#each data as item, i}
      <Item item={item}/>
  {/each}
</div>
