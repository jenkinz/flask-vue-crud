<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="overflow-hidden bg-white shadow sm:rounded-lg">
    <div class="m-auto flex px-4 py-5 sm:px-6">
      <h3 class="mr-auto text-lg font-medium leading-6 text-gray-900">Books</h3>
      <a class="btn btn-primary ml-auto mt-0" href="#">Add Book</a>
    </div>
    <div class="border-t border-gray-200">
      <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
        <div class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
          <ul
            role="list"
            class="divide-y divide-gray-200 rounded-md border border-gray-200"
          >
            <li
              class="flex items-center justify-between py-3 pl-3 pr-4 text-sm"
            >
              <div class="flex w-0 flex-1 items-center">
                <PaperClipIcon
                  class="h-5 w-5 flex-shrink-0 text-gray-400"
                  aria-hidden="true"
                />
                <span class="ml-2 w-0 flex-1 truncate"> Book Title 1 </span>
              </div>
              <div class="ml-4 flex-shrink-0">
                <a href="#" class="btn btn-primary mt-0"> Update </a>
                <a href="#" class="btn btn-danger ml-2 mt-0"> Delete </a>
              </div>
            </li>
            <li
              class="flex items-center justify-between py-3 pl-3 pr-4 text-sm"
            >
              <div class="flex w-0 flex-1 items-center">
                <PaperClipIcon
                  class="h-5 w-5 flex-shrink-0 text-gray-400"
                  aria-hidden="true"
                />
                <span class="ml-2 w-0 flex-1 truncate"> Book Title 2 </span>
              </div>
              <div class="ml-4 flex-shrink-0">
                <a href="#" class="btn btn-primary mt-0"> Update </a>
                <a href="#" class="btn btn-danger ml-2 mt-0"> Delete </a>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { PaperClipIcon } from '@heroicons/vue/solid';
</script>
