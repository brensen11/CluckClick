<script lang="ts">
  import type { ItemData } from '../api/entities.ts'
  import svelteLogo from '../assets/svelte.svg';


  export let item: ItemData;
  export let onClick: ((item: ItemData) => void) | null = null;
  function handleClick() {
    onClick?.(item)
  }
</script>

<button type="button" on:click={handleClick} class="flex flex-col btn btn-lg preset-filled-primary-50-950">
    <img src={svelteLogo} alt="Svelte Logo">
    {item.name}
</button>
