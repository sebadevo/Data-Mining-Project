(window.odspNextWebpackJsonp=window.odspNextWebpackJsonp||[]).push([[33],{158:function(e,t,n){"use strict";var a;!function(e){e[e.created=0]="created",e[e.started=1]="started",e[e.completed=2]="completed",e[e.failed=3]="failed",e[e.canceled=4]="canceled",e[e.expired=5]="expired"}(a||(a={})),t.e=a},212:function(e,t,n){"use strict";var a;!function(e){e[e.multiple=0]="multiple",e[e.renameItems=1]="renameItems",e[e.deleteItems=2]="deleteItems",e[e.pointInTimeRestore=3]="pointInTimeRestore",e[e.restoreItems=4]="restoreItems",e[e.uploadItems=5]="uploadItems",e[e.moveItems=6]="moveItems",e[e.copyItems=7]="copyItems",e[e.rotateItems=8]="rotateItems",e[e.addItemsToAlbum=9]="addItemsToAlbum",e[e.addCoverPhotos=10]="addCoverPhotos",e[e.removeCoverPhotos=11]="removeCoverPhotos",e[e.createAlbumFromFolder=12]="createAlbumFromFolder",e[e.createColumn=13]="createColumn",e[e.editColumn=14]="editColumn",e[e.deleteColumn=15]="deleteColumn",e[e.checkInItem=16]="checkInItem",e[e.checkOutItem=17]="checkOutItem",e[e.undoCheckOutItem=18]="undoCheckOutItem",e[e.createFolder=19]="createFolder",e[e.updateBundle=20]="updateBundle",e[e.shareItem=21]="shareItem",e[e.reportAbuse=22]="reportAbuse",e[e.requestReview=23]="requestReview",e[e.setAlbumCoverPhoto=24]="setAlbumCoverPhoto",e[e.createAlbum=25]="createAlbum",e[e.uploadVideos=26]="uploadVideos",e[e.saveItem=27]="saveItem",e[e.createItem=28]="createItem",e[e.publishItem=29]="publishItem",e[e.unPublishItem=30]="unPublishItem",e[e.applyOfficeLens=31]="applyOfficeLens",e[e.removeOfficeLens=32]="removeOfficeLens",e[e.updateMetadata=33]="updateMetadata",e[e.makeHomepage=34]="makeHomepage",e[e.triggerFlow=35]="triggerFlow",e[e.downloadAsZip=36]="downloadAsZip",e[e.saveAutoAlbum=37]="saveAutoAlbum",e[e.discardAutoAlbum=38]="discardAutoAlbum",e[e.addToOneDrive=39]="addToOneDrive",e[e.removeFromSharedList=40]="removeFromSharedList",e[e.setupApprovalFlow=41]="setupApprovalFlow",e[e.setupReminderFlow=42]="setupReminderFlow",e[e.sharepointPointInTimeRestore=43]="sharepointPointInTimeRestore",e[e.sharingReport=44]="sharingReport",e[e.editViewColumns=45]="editViewColumns",e[e.runModelOnItems=46]="runModelOnItems",e[e.importModel=47]="importModel",e[e.downloadItem=48]="downloadItem",e[e.deleteSmartTemplate=49]="deleteSmartTemplate",e[e.publishSmartTemplate=50]="publishSmartTemplate",e[e.unpublishSmartTemplate=51]="unpublishSmartTemplate",e[e.universalAnnotationSync=52]="universalAnnotationSync"}(a||(a={})),t.e=a},224:function(e,t,n){"use strict";var a=function(){function e(){this.id=++e._lastBatchId}return e._lastBatchId=0,e}();t.e=a},391:function(e,t,n){"use strict";var a=n(20),i=n(35),r=n(793),o=function(e){function t(t){var n=e.call(this,t)||this;n.key=t.key;var a=n.observables,i=t.count,r=void 0===i?a.create(1):i,o=t.isAvailable,c=void 0===o?a.create(!0):o,d=t.onExecute,l=void 0===d?s:d;return n.count=r,n.isAvailable=c,n._onExecute=l.bind(t.operation),n}return Object(a.__extends)(t,e),t.prototype.dispose=function(){e.prototype.dispose.call(this),this._onExecute=s},t.prototype.execute=function(){return this._onExecute()},t}(i.n);function s(){return r.t.wrap()}t.e=o},392:function(e,t,n){"use strict";n(385);var a=n(403),i=n("knockout-lib"),r=function(){function e(e,t){var n=this;this._source=e,this._getKey=t,this._groupsByKeyId={},this.groups=i.observableArray(),this._initializeGroups(),Object(a.e)(this.groups,function(){n._mapping.dispose()})}return e.group=function(t,n){return new e(t,n).groups},e.prototype._initializeGroups=function(){var e=this;this._mapping=this._source.map({mappingWithDisposeCallback:function(t){var n=e._getKey(t),a=JSON.stringify(n),r=e._groupsByKeyId[a];return r?r.values.push(t):(r={key:n,values:i.observableArray([t])},e._groupsByKeyId[a]=r,e.groups.push(r)),{mappedValue:a,dispose:function(){r.values.peek().length>1?r.values.remove(t):(delete e._groupsByKeyId[a],e.groups.remove(r))}}}})},e}();t.e=r},425:function(e,t,n){"use strict";var a=n(20),i=function(e){function t(t){var n=e.call(this,t)||this;return n.errorType=t.errorType||0,n.payloads=t.payloads||{},n}return Object(a.__extends)(t,e),t}(n(50).e);t.e=i},451:function(e,t,n){"use strict";n.d(t,"e",function(){return m});var a=n(20),i=n(35),r=n(158),o=n(224),s=n(212),c=n(391),d=function(e){function t(t){var n=e.call(this,{})||this,i=n.observables;n.name=t.name,n.iconName=t.iconName,n.state=i.create(r.e.created),n.warning=i.create(""),n.error=i.create(),n.count=i.create(1);var c=Object(a.__assign)({minimum:0,maximum:0,current:0},t.progress||{});return n.progress={minimum:i.create(c.minimum),maximum:i.create(c.maximum),current:i.create(c.current)},n.type=i.create(t.type||s.e.multiple),n.batch=t.batch||new o.e,n._initializeActions(t.actions),n.payloads=i.create(t.payloads||{}),n.visibility=i.create(t.visibility||0),n}return Object(a.__extends)(t,e),t.prototype.dispose=function(){this.actions({}),this.payloads({}),e.prototype.dispose.call(this)},t.prototype._initializeActions=function(e){void 0===e&&(e={});var t={};for(var n in e){var a=e[n];t[n]=this.scope.attach(new c.e({key:n,operation:this,isAvailable:a.isAvailable,onExecute:a.execute}))}this.actions=this.observables.create(t)},t}(i.n),l=n(648),u=n(392),f=n(1132),p=function(e){function t(t,n){void 0===t&&(t={});var a=e.call(this,t,n)||this,i=a.observables,r=new o.e;a._observers=i.createArray();var s=a.operations=i.createArray(),c=a.scope.attached(l.e),d=a.groups=a.addDisposable(u.e.group(s,function(e){return e.batch}).map({mappingWithDisposeCallback:function(e){var t=new c({batch:e.key,operations:e.values});return{mappedValue:t,dispose:function(){t.dispose()}}}}));return a.overall=new(a.managed(l.e))({batch:r,operations:d}),a.isLocked=a.createPureComputed(a._computeIsLocked),a.createBackgroundComputed(a._computeRemoveAllWhenUnlocked).extend({deferred:!0}),a}return Object(a.__extends)(t,e),t.prototype.lock=function(){var e=this,t={};return this._observers.push(t),{dispose:function(){e._observers.remove(t)}}},t.prototype.register=function(e){var t=new d(e);return 2!==t.visibility.peek()&&this.operations.push(t),t},t.prototype.deleteGroupOperation=function(e){var t=Object(a.__spreadArray)([],e.operations.peek(),!0);this.operations.removeAll(t),t.forEach(function(e){e.dispose()})},t.prototype.cleanup=function(e){void 0===e&&(e=!1);for(var t=[],n=0,a=this.groups.peek();n<a.length;n++){var i=a[n],o=i.state.peek();if(o===r.e.completed||!e&&(o===r.e.expired||o===r.e.canceled||o===r.e.failed))for(var s=i.operations.peek(),c=void 0,d=0;d<s.length;d++){c=!0;var l=s[d];if(o===r.e.failed&&l.actions)for(var u=l.actions.peek(),f=Object.keys(u),p=0;p<f.length;p++)if("cancel"!==f[p]&&u[f[p]].isAvailable.peek()){c=!1;break}c&&t.push(s[d])}}this.operations.removeAll(t),t.forEach(function(e){e.dispose()})},t.prototype._computeRemoveAllWhenUnlocked=function(){this.isLocked()||this.cleanup()},t.prototype._computeIsLocked=function(){return this._observers().length>0},t}(i.n),m=Object(f.r)("OperationProvider",p)},482:function(e,t,n){"use strict";n.d(t,"e",function(){return i});var a=n(35),i=new(n(402).t)({name:"".concat("UserStateProvider.key",".updateQuota"),factory:{dependencies:{observablesFactoryType:a.a},create:function(e){var t=new(0,e.observablesFactoryType);return{instance:t.create(!1),disposables:t}}}})},638:function(e,t,n){"use strict";n.r(t),n.d(t,"encodeItemSetParentKeyKey",function(){return T}),n.d(t,"resourceKey",function(){return F});var a=n(20),i=(n(385),n(35)),r=n(451),o=n(159),s=n(137),c=n(793),d=n(96),l=n(52),u=n(402),f=(new u.t("dataStore"),new u.t("userSettingsStore"),new u.t("userInfoStore"),new u.t("smartFiltersStore")),p=n(158),m=n(224),_=n(212),h=n(425),b=function(e){this.items=new Array(e||0),this.groupings=null,this.partialResultRequestCount=0,this.partialResultStatus=0},g=n("knockout-lib"),v=n(306),y=function(e,t,n){this.key=e||"",this.content=g.observable(new b(n)),this.content.equalityComparer=v.n,this.schema=g.observableArray([]),this.schema.equalityComparer=v.e,this.context=g.utils.extend({},t),this.contentTypes=g.observableArray([]),this.isPlaceholder=!0,this.version=0};function S(e,t){for(var n=t.start,a=Math.min(t.end,e.length),i=n;i<a;i++)if(!e[i])return!1;return!0}var D=n(790),I=n(1132),x=n(139),C=n(1134),O=n(482),w="__next__",E=function(){function e(e,t,n,a){this._context=e,this._store=t,this._isTokenBaseApi=n,this._tokenBasedExtraItemCount=a}return e.prototype.initialize=function(e,t){if(this._skipDataFetch=!1,!this._context.group&&this._context.noIndexBasedDataFetch){var n=e&&e.content.peek().groupings,a=n&&n.length&&n[0].itemGroups;this._context.group=this._getGroupStartingOnIndex(t,a)}e&&e.isExpired&&(this._context.group=null),this._isExpandingGroup=this._context.noIndexBasedDataFetch&&this._context.group&&this._context.group.groupingId!==w&&!this._context.groupReplace,this._isFetchingNextGroup=this._context.group&&this._isTokenBaseApi&&this._context.group.groupingId===w;var i=e&&e.content.peek().groupings;this._isAllCollapsedQuery=i&&i.length>0&&i[0].isAllCollapsed&&i[0].isAllCollapsed.peek()&&!this._isExpandingGroup},e.prototype.isResultSetValid=function(e,t){var n=this._skipDataFetch;return n||(n=this._isAllCollapsedQuery?!this._isExpandingGroup&&!this._context.requestToken:(this._isTokenBaseApi||!this._context.skipInMemoryCache)&&S(e,t)&&!(this._isFetchingNextGroup&&this._context.endIndex>e.length)),n},e.prototype.computeNewChildren=function(e,t,n,a,i){var r,o=!1;if(this._context.groupReplace&&(this._isFetchingNextGroup=!!e.nextRequestToken),r=i&&!n.isExpired?n.content.peek().items:[],e.nextRequestToken?(!t.requestToken&&r.length>e.totalChildren&&(r[e.totalChildren]=null),e.totalChildren+=this._tokenBasedExtraItemCount,this._store.setNextRequestToken(t.parentKey,a,e.nextRequestToken),o=!0,n&&(n.isTokenBasedApi=o)):this._store.setNextRequestToken(t.parentKey,a,"end"),t.requestToken&&(t.startIndex=r.length-this._tokenBasedExtraItemCount,e.totalChildren+=r.length-this._tokenBasedExtraItemCount),this._isFetchingNextGroup||this._isAllCollapsedQuery){var s=e.children.length,c=e.startIndex+s;e.nextRequestToken&&(c+=this._tokenBasedExtraItemCount),e.totalChildren=Math.max(e.totalChildren,Math.max(r.length,c))}if(e.item&&e.totalChildren>=0){var d;this._isExpandingGroup||(r.length>0&&0===e.totalChildren?r=[]:r.length=e.totalChildren),d=t.groupReplace?t.startIndex:void 0!==e.startIndex?e.startIndex:this._isExpandingGroup?t.group.startIndex:t.startIndex;for(var l=0,u=0;l<r.length;l++)l>=d&&u<e.children.length&&(r[l]=this._store.getItem(e.children[u].key),(t.remoteItem||t.isMountPointFolder)&&(r[l].peek().isMountPointFolder=!0,r[l].peek().remoteWebUrl=t.isMountPointFolder?t.remoteWebUrl:t.remoteItem.SiteUrl),u++)}return{allChildren:r,hasNextRequestToken:o}},e.prototype.computeNewGroupings=function(e,t,n,a,i){var r=this._isExpandingGroup?a.group:null,o=a.itemsPerGroup,s=e&&e.length>0?e[0].itemGroups:null,c=null;s&&s.length>0&&s[s.length-1].isPlaceholder&&(c=s.pop());var d=this._mergeGroupings(e,t,i,n);if(r&&d&&(d[0].isAllCollapsed(!1),r.state({isCollapsed:!1})),n&&n.length>0&&!n[n.length-1]&&(s=d&&d.length>0?d[0].itemGroups:null)&&s.length>0){var l=s[s.length-1];this._context.groupReplace&&this._isFetchingNextGroup&&(l.hasMoreData=!0);var u=n[l.startIndex+(-1!==o?Math.min(l.count,o):l.count)-1]&&!(this._context.groupReplace&&l.count<o),f=d[0].isAllCollapsed.peek();if(u||this._isFetchingNextGroup||f){var p=l.startIndex+l.count;c?c.startIndex=p:c={groupingId:w,startIndex:p,count:1,isPlaceholder:!0,state:g.observable({isCollapsed:!1})},n.length<p&&(n.length=p+1),s.push(c)}}return d},e.prototype._mergeGroupings=function(e,t,n,a){var i=e;if(i&&i.length>0){if(t&&t.length>0)for(var r=0;r<t.length;r++){var o=i[r].isAllCollapsed.peek();i[r].itemGroups=n?this._retainItemGroupState(i[r].itemGroups,t[r].itemGroups):this._mergeItemGroups(i[r].itemGroups,t[r].itemGroups,o,null,a)}}else i=t;return i},e.prototype._mergeItemGroups=function(e,t,n,a,i){var r=e;if(e&&e.length>0){if(t&&t.length>0)for(var o=function(e){var t=!1;n&&e.state({isCollapsed:!0});for(var o=function(i){var o=r[i];if(e.groupingId===o.groupingId){if(s._context.noIndexBasedDataFetch||!s._context.isTokenBasedApi)if(s._context.groupReplace?(o.count+=e.count,o.hasMoreData&&i<r.length-1&&(o.hasMoreData=!1)):o.count=e.count,o.children=s._mergeItemGroups(o.children,e.children,n,o),0===i)o.startIndex=a?a.startIndex:0;else{var c=r[i-1],d=c.startIndex+c.count-o.startIndex;o.startIndex+=d,o.children&&o.children.forEach(function(e){e.startIndex+=d})}else{var l=e.startIndex+s._context.startIndex,u=e.startIndex+s._context.startIndex+e.count;o.startIndex=Math.min(o.startIndex,l),o.count=Math.max(u,o.startIndex+o.count)-o.startIndex}return t=!0,"break"}},c=0;c<r.length&&"break"!==o(c);c++);if(!t){var d=r[r.length-1],l=d.startIndex+d.count-e.startIndex;e.startIndex+=l,e.children&&e.children.forEach(function(e){e.startIndex+=l});var u=Math.min(e.count,30),f=0;if(i)for(var p=e.startIndex;p<e.startIndex+u;p++)i[p]||f++;f&&(e.emptyItemCount=f),r.push(e)}},s=this,c=0,d=t;c<d.length;c++)o(d[c])}else r=t;return r},e.prototype._retainItemGroupState=function(e,t,n){var a=t;if(t&&t.length>0&&e&&e.length>0){for(var i={},r=0,o=e;r<o.length;r++){var s=o[r];i[s.groupingId]=s}for(var c=0,d=a;c<d.length;c++){var l=d[c],u=i[l.groupingId];u&&(l.state(u.state.peek()),l.children=this._retainItemGroupState(u.children,l.children,u))}}return a},e.prototype._getGroupStartingOnIndex=function(e,t){if(t&&t.length>0)for(var n=0;n<t.length;n++){var a=t[n];if(!(a&&a.startIndex<=e))break;var i=a.startIndex+a.count-1;if(a.children){if(i>=e)return this._getGroupStartingOnIndex(e,a.children)}else{if(a.startIndex===e)return a.state.peek().isCollapsed?null:a;if(i>=e){var r=n<t.length-1?t[n+1]:null;if(r&&!r.state.peek().isCollapsed)return this._skipDataFetch=!0,null}}}return null},e}(),A=n(189),L=n(4),k=new u.t({name:"".concat("SharedItemsScopeExperiment.key",".isUseItemsScopeInSharedEnabled"),factory:new u.e(Object(L.Vr)(L.sr))}),M=n(3),P=100,T=new u.t({name:"".concat("ItemProvider",".encodeItemSetParentKey"),factory:new u.e(Object(L.Vr)(L.xr))}),U=function(e){function t(t,n){var a=e.call(this,t,n)||this;return a._registeredProjections={},a._pendingGetItemRequests={},a._store=n.itemsStore,a._operationProvider=n.operationProvider,a._schemaDataSource=n.schemaDataSource,a._updateQuota=n.updateQuota,a._groupThrottle=n.groupThrottle,a._encodeItemSetParentKey=n.encodeItemSetParentKey||!1,a._smartFiltersStore=n.smartFiltersStore,a}return Object(a.__extends)(t,e),t.prototype.getItem=function(e){return this._getItem(e)},t.prototype.getItemSetKey=function(e,t){var n="parentKey="+(this._encodeItemSetParentKey?encodeURIComponent(e.parentKey):e.parentKey);function a(e,t){t&&(n+="&".concat(e,"=").concat(t))}a("ownerId",e.ownerId),a("groupingType",e.groupingType),n+="&sortField="+(e.sortField||""),n+="&isAscending="+("boolean"==typeof e.isAscending?e.isAscending:"");var i=e.filters;if(i)for(var r in i)n+="&"+r+"="+i[r];a("groupBy",e.groupBy),a("viewId",e.baseViewId),a("viewXml",e.viewXml),a("additionalFiltersXml",e.additionalFiltersXml);var o=!t&&e.itemSetProjections;if(o){var s="";for(var c in o)s+=c+"_"+o[c];n+="&projection="+s}return e.supportsNestedGroups&&(n+="&ng=1"),n},t.prototype.getSpecifiedItems=function(e){return e&&e.needToClearParentSmartFiltersInfo&&e.parentKey&&this._smartFiltersStore&&this._smartFiltersStore.invalidate(e.parentKey),this._getItemDataSource().then(function(t){return t.getSpecifiedItems(e)})},t.prototype.getItemSync=function(e){var t=this.getItemSetKey(e),n=e.parentKey,a=this._store.getItem(n),i=this._getItemSet(t,e);if(!a){var r=new o.e(n),s=e.queryType,c=void 0===s?r.queryType:s;r.queryType=c,this._store.setItem(r),a=this._store.getItem(n)}if(!i){var d=a.peek(),l=d&&d.folder,u=l&&l.childCount||0;(i=new y(t,e,u)).item=a;var f=e.needSchema;if(void 0===f||f){var p=this._schemaDataSource,m=p&&p.getColumns(d);m&&m.length>0&&i.schema(m)}this._store.setItemSet(t,i)}return i},t.prototype.invalidateItem=function(e,t){var n=void 0===t?{}:t,i=n.triggerFetch,r=void 0!==i&&i,o=n.emptyAllOtherSets,s=void 0!==o&&o,c=n.refreshSchema,d=void 0!==c&&c,l=n.updateGrouping,u=void 0!==l&&l,f=n.purgeCache,p=void 0!==f&&f;if(s&&this._store.emptyAllOtherSets([e]),d&&(m=this._store.getItemSetFromItemKey(e))&&m.schema([]),u||this._store.invalidateItem(e,{purgeCache:p}),this._smartFiltersStore&&this._smartFiltersStore.invalidate(e),r){var m=this._store.getItemSetFromItemKey(e);this._getItem(Object(a.__assign)(Object(a.__assign)({parentKey:e},m&&m.context||{}),{skipCache:!0,updateGrouping:u}))}},t.prototype.removeFromRecent=function(e){var t=this;return this._getItemDataSource().then(function(t){return t.removeFromRecent(e)}).then(function(n){return n&&t.invalidateItem(e.parentKey),n})},t.prototype.removeMountPoint=function(e){var t=this;return this._getItemDataSource().then(function(t){return t.removeMountPoint(e)}).then(function(n){return n&&t.invalidateItem(e.parentKey),n})},t.prototype.createMountPoint=function(e){return this._getItemDataSource().then(function(t){return t.createMountPoint(e)}).then(function(e){return e},function(e){return c.t.wrapError(e)})},t.prototype.createDocument=function(e,t,n,a,i){var r=this;return this._getItemDataSource().then(function(o){return o.createDocument(e,t,n,a).then(function(t){if(i&&o.updateContentType){var n=t.match(/{(.*)}/),a=n&&n[1];return a?o.updateContentType(e,a,i).then(function(){return r.invalidateItem(e),r._updateQuota(!0),t}):t}return r.invalidateItem(e),r._updateQuota(!0),t})})},t.prototype.createCustomDocument=function(e,t,n){var a=this;return this._getItemDataSource().then(function(a){return a.createCustomDocument(e,t,n)}).then(function(t){return t?(a.invalidateItem(e),a._updateQuota(!0),a.getItem({parentKey:e}).then(function(e){return a.peekUnwrapObservable(a._store.getItem(t))})):c.t.wrapError()})},t.prototype.updateBundle=function(e,t){var n=this,a=[new x.e(e.item.key,e.item)];return t.update(a),this._getItemDataSource().then(function(t){return t.updateBundle(e)}).then(function(){n.invalidateItem(e.item.UNSAFE_parent?e.item.UNSAFE_parent.key:e.item.key),a=a.map(function(e){return e.succeed()}),t.update(a)},function(i){n.invalidateItem(e.item.UNSAFE_parent?e.item.UNSAFE_parent.key:e.item.key);var r=new Error(i);return a=a.map(function(e){return e.fail(r)}),t.update(a),c.t.wrapError(r)})},t.prototype.removeFromSharedList=function(e){var t=this;return this._getItemDataSource().then(function(t){return t.removeFromSharedList(e)}).then(function(n){return t.invalidateItem(e.parentKey),t.resources.consume(k)&&t.resources.consumeAsync(l.l).then(function(t){t.invalidateItems(e.parentKey)}),n})},t.prototype.updateViewCount=function(e){return this._getItemDataSource().then(function(t){return t.updateViewCount(e)})},t.prototype.reportAbuse=function(e){var t=new m.e,n=this._operationProvider.register({name:e.item.name||"",type:_.e.reportAbuse,payloads:{reportAbuse:{item:e.item}},iconName:e.item.iconName,batch:t}),a=this._getItemDataSource().then(function(t){return t.reportAbuse(e)});return n.state(p.e.started),n.progress.maximum(1),a.then(function(e){return n.state(p.e.completed),n.progress.current(1),e},function(e){return n.state(p.e.failed),n.error(new h.e({message:e})),c.t.wrapError(e)})},t.prototype.requestReview=function(e){for(var t=this,n=new m.e,a=e.items.map(function(e){var a=t._operationProvider.register({name:e.name||"",type:_.e.requestReview,payloads:{requestReview:{item:e}},iconName:e.iconName,batch:n});return a.progress.maximum(1),a.progress.current(0),a}),i=this._getItemDataSource().then(function(t){return t.requestReview(e)}),r=0,o=a;r<o.length;r++)o[r].state(p.e.started);return i.then(function(n){for(var i=0,r=a;i<r.length;i++){var o=r[i];o.progress.current(1),o.state(p.e.completed)}var s=e.items[0].UNSAFE_parent;return s&&t.invalidateItem(s.key),n},function(e){for(var t=0,n=a;t<n.length;t++){var i=n[t];i.error(new h.e({message:e})),i.state(p.e.failed)}return c.t.wrapError(e)})},t.prototype.saveSortOrder=function(e){return this._getItemDataSource().then(function(t){return t.saveSortOrder(e)}).then(function(e){return e},function(e){})},t.prototype.addCoverPhotos=function(e){return this._updateCoverPhotos(e,_.e.addCoverPhotos,this._addCoverPhotos)},t.prototype.removeCoverPhotos=function(e){return this._updateCoverPhotos(e,_.e.removeCoverPhotos,this._removeCoverPhotos)},t.prototype.changeFolderType=function(e){var t=this;return this._getItemDataSource().then(function(t){return t.changeFolderType(e)}).then(function(n){return t.invalidateItem(e.item.key,{triggerFetch:!0}),n})},t.prototype.updateItemProperty=function(e){var t=this;return this._getItemDataSource().then(function(t){return t.updateItemProperty(e)}).then(function(n){return t.invalidateItem(e.item.key,{triggerFetch:!0}),n})},t.prototype.getOpenInClientDetails=function(e){return this._getItemDataSource().then(function(t){return t.getOpenInClientDetails(e)}).then(function(e){return e},function(e){})},t.prototype.getWorkProgress=function(e){return this._getItemDataSource().then(function(t){return t.getWorkProgress(e)})},t.prototype.processReferral=function(e,t){return this._getItemDataSource().then(function(n){return n.processReferral(e,t)})},t.prototype.getItemOcrTextContent=function(e){return this._getItemDataSource().then(function(t){return t.getItemOcrTextContent(e)})},t.prototype.updateItemOcrInfo=function(e,t,n){var a=this;return this._getItemDataSource().then(function(a){return a.updateItemOcrInfo(e,t,n)}).then(function(t){return a.invalidateItem(e.key,{triggerFetch:!0}),t},function(e){return e})},t.prototype.rotateItems=function(e,t){var n=this,a={},i=e.items.map(function(e){return a[e.key]=new x.e(e.key,e)});return t.update(i),this._getItemDataSource().then(function(t){return t.rotateItems(e)}).then(function(){i=i.map(function(e){return e.succeed()}),t.update(i)},function(e){var r=e.data||[];i=[];for(var o=0,s=r;o<s.length;o++){var c=s[o],d=a[c.key];n._store.setItem(d.input),delete a[c.key],i.push(d.fail(c.error))}for(var l in a)d=a[l],delete a[l],i.push(d.succeed());t.update(i)})},t.prototype.registerProjection=function(e,t){this._registeredProjections[e]=t},t.prototype.computeProjectedItemSet=function(e,t,n,a){var i=n.itemSetProjections,r=a?null:this._store.getItemSet(e),o=!r||r.isPlaceholder||r.isExpired||r.version!==t.version;if(!r||o){for(var s in r||((r=new y(e,n)).item=t.item,r.isTokenBasedApi=t.isTokenBasedApi,r.isPlaceholder=t.isPlaceholder,r.isExpired=t.isExpired,r.version=t.version),i){var c=this._registeredProjections[s];c&&c.projectItemSet(r,t,i[s])}a||this._store.setItemSet(e,r)}return r},t.prototype.redeemPermissionToken=function(e){return this._getItemDataSource().then(function(t){return t.redeemPermissionToken(e)})},t.prototype._getItem=function(e){var n,i=this,r=D.e(e),o=this._store;e.keyAlias?(n=this.getItemSync({parentKey:e.keyAlias}).item,e.parentKey=n.peek().key):n=this.getItemSync(e).item;var s=e.skipCache,d=void 0!==s&&s,u=this.getItemSetKey(e),f=e.itemSetProjections?this.getItemSetKey(e,!0):u,p=this._getItemSet(u,e),m=p&&p.content.peek().items,_=e.isTokenBasedApi||!!p&&!!p.isTokenBasedApi,h=!d&&n&&!n.peek().revision&&p&&!p.isExpired&&!p.isPlaceholder&&(!e.requestAllChildren||S(m,{start:0,end:m.length})),b=e.startIndex,g=void 0===b?0:b,v=e.pageSize,I=void 0===v?P:v,x=e.endIndex||g+I;x=m&&m.length>0&&!_?Math.min(m.length,x):x,g=Math.max(0,Math.min(x,g));var O=M.e.isActivated("73b2b18a-27b0-433f-95cf-c7f77326ff37","11/09/2021","Not set requestToken if itemSet is expired")||p&&!p.isExpired?o.getNextRequestToken(f):void 0;e.requestToken="end"===O?"":O;var w=new E(e,o,_,t.TOKEN_BASED_API_EXTRA_ITEMS);w.initialize(p,g);var L=!1,k=p&&p.content.peek();if(!k||1!==k.partialResultStatus&&2!==k.partialResultStatus||(L=!0,1===k.partialResultStatus&&p.content({items:k.items,groupings:k.groupings,partialResultRequestCount:0,partialResultStatus:2})),h&&!L&&w.isResultSetValid(m,{start:g,end:x}))return c.t.wrap(p);if(n&&n.peek().isStub){var T=e.startKey;if(T&&o.getItem(T)){p.content.peek().items=[o.getItem(T)],p.isPlaceholder=!0,p.isExpired=!1;var U=this._schemaDataSource,F=U&&U.getColumns(n.peek());F&&F.length>0&&p.schema(F),p.content.valueHasMutated&&p.content.valueHasMutated()}return c.t.wrap(p)}var H=p&&!p.isExpired&&p.content.peek().groupings;H&&H.length>0&&(e.isGrouped=!0),this._normalizeContext(e,m,g,x,!h);var R=this._getRequestKey(e),N=this._pendingGetItemRequests[R];return N?e.itemSetProjections?N.getPromise().then(function(t){return i.computeProjectedItemSet(u,t,e)}):N.getPromise():(_&&!O&&(e.startIndex=0),this._pendingGetItemRequests[R]=N=new C.e,this.resources.consumeAsync(l.o.bypass).then(function(t){return t.getItem(Object(a.__assign)(Object(a.__assign)({},e),{itemSetKey:u}))}).then(function(t){r.updateContextBasedOnResult&&e.updateContextBasedOnResult&&(r.updateContextBasedOnResult(r,t),e.updateContextBasedOnResult(e,t),u=i.getItemSetKey(r));var a=e.itemSetProjections?i.getItemSetKey(e,!0):u;n=o.getItem(e.parentKey);var s=o.getItemSet(a);h=!(!n||!s);var c=w.computeNewChildren(t,e,s,a,!!h),d=c.allChildren,l=c.hasNextRequestToken;if(l&&(_=l),t.item&&!e.ignoreChildren&&!e.skipStoreResults){h||((s=new y(a,e)).item=o.getItem(e.parentKey),s.isTokenBasedApi=_,o.setItemSet(a,s));var f=!!s.isExpired;s.sortField=t.sortField,s.isAscending=t.isAscending,s.isPlaceholder=!1,s.isExpired=!1;var p=e.needSchema;if(void 0===p||p){var m=t.schema;s.schema(m&&m.length>0&&m||[]),t.customViewRenderer?s.customViewRenderer=i.observables.create(t.customViewRenderer):s.customViewRenderer=i.observables.create(void 0)}var b=t.groupings;_&&e.mergeGroupings&&(b=w.computeNewGroupings(s.content.peek().groupings,t.groupings,d,e,f)),t.contentTypes&&s.contentTypes&&s.contentTypes(t.contentTypes);var g=s.content.peek(),v=g.partialResultStatus,I=g.partialResultRequestCount,x=void 0===I?0:I;if(!(b&&b.length&&b[0]))if(l&&(t.children&&t.children.length<30||!t.children)){var C=x+1;C<=5?x=C:v=1}else void 0===v||0===v||l?2===v&&t.children&&30===t.children.length&&(v=0):v=3;s.content({items:d,groupings:b,partialResultRequestCount:x,partialResultStatus:v});var O=s.version,E=void 0===O?0:O;s.version=E+1}if(delete i._pendingGetItemRequests[R],e.requestAllChildren&&!S(d,{start:0,end:t.totalChildren})){var A=D.e(e),L=A.startIndex,k=void 0===L?0:L;return A.startIndex=k+P,i._getItem(A)}return t.isFromBrowserCache?(r.skipCache=!0,i._getItem(r)):(e.itemSetProjections&&(s=i.computeProjectedItemSet(u,s,e)),s)},function(e){return delete i._pendingGetItemRequests[R],c.t.wrapError(e)}).then(function(e){N.complete(e)},function(t){i._groupThrottle&&!i._groupThrottle()&&t&&t.errorCode===Number(A.t.queryThrottled)&&!e.noGroupReplace?i._groupThrottle(!0):N.error(t)}),N.getPromise())},t.prototype._normalizeContext=function(e,t,n,a,i){var r=e.pageSize||P;if(!e.avoidSeamSnapping){if(!i&&n-n%r!=a-a%r&&t)for(;n<a&&t[n];)n++;e.startIndex=n-n%r}"number"!=typeof e.pageSize&&(e.pageSize=P);for(var o=e.startIndex,s=void 0===o?0:o;a-s>e.pageSize;)e.pageSize+=P},t.prototype._getRequestKey=function(e){var t=this.getItemSetKey(e,!0);return e.requestToken?t+=e.requestToken:t+="&startIndex="+e.startIndex,t+"&pageSize="+e.pageSize},t.prototype._getItemSet=function(e,t){var n=this._store,a=n.getItemSet(e);if(t.itemSetProjections){var i=this.getItemSetKey(t,!0),r=n.getItemSet(i);r&&(a=this.computeProjectedItemSet(e,r,t))}return a},t.prototype._updateCoverPhotos=function(e,t,n){for(var a=this,i=new m.e,r=e.target,o=e.items.map(function(e){var n=a._operationProvider.register({name:e.name||"",type:t,payloads:{coverPhotos:{parent:r,item:e}},iconName:e.iconName,batch:i});return n.progress.maximum(1),n.progress.current(0),n}),s=n.call(this,e),c=0,d=o;c<d.length;c++)d[c].state(p.e.started);return s.then(function(t){a.invalidateItem(r.key),(null==e?void 0:e.itemsScopeInvalidate)&&a.resources.consumeAsync(l.l).then(function(e){e.invalidateItems(null==r?void 0:r.key)});for(var n=0,i=o;n<i.length;n++){var s=i[n];s.progress.current(1),s.state(p.e.completed)}return t},function(){for(var e=0,t=o;e<t.length;e++)t[e].state(p.e.failed)})},t.prototype._addCoverPhotos=function(e){return this._getItemDataSource().then(function(t){return t.addCoverPhotos(e)})},t.prototype._removeCoverPhotos=function(e){return this._getItemDataSource().then(function(t){return t.removeCoverPhotos(e)})},t.prototype._getItemDataSource=function(){return c.t.resolve(this.resources.consumeAsync(l.u))},t.dependencies=Object(a.__assign)(Object(a.__assign)({},i.n.dependencies),{groupThrottle:d.a.optional,schemaDataSource:l.p.optional,itemsStore:s.e,operationProvider:r.e,smartFiltersStore:f.optional,updateQuota:O.e,encodeItemSetParentKey:T.optional}),t.TOKEN_BASED_API_EXTRA_ITEMS=2,t}(i.n),F=(t.default=U,Object(I.r)("ItemProvider",U))},648:function(e,t,n){"use strict";var a=n(20),i=n(212),r=n(158),o=n(391),s=n(793),c=n(35),d=n("knockout-lib");function l(e,t){var n,a=function(e){t(t.peek()+e)},i=e.subscribe(function(){n=e.peek()},null,"beforeChange"),r=e.subscribe(function(){a(e.peek()-n)});return a(e.peek()),{dispose:function(){i.dispose(),r.dispose(),a(-e.peek())}}}var u=n(392),f=function(e){function t(t){var n=e.call(this,t)||this;return n.operations=t.operations,n.name="",n.iconName="",n.progress={minimum:n.createObservable(0),maximum:n.createObservable(0),current:n.createObservable(0)},n.batch=t.batch,n.error=n.createObservable(),n.count=n.createObservable(0),n._initializeType(),n.payloads=n.createPureComputed(n._computePayloads),n.actions=n.createObservable({}),n.states=n.createObservable({created:0,started:0,completed:0,failed:0,canceled:0,expired:0}),n._initializeOperations(),n.state=n.createPureComputed(n._computeState),n.visibility=n.createPureComputed(n._computeVisibility),n}return Object(a.__extends)(t,e),t.prototype._initializeType=function(){var e=this.addDisposable(u.e.group(this.operations,function(e){return e.type()}));this.type=this.createPureComputed(function(){return 1===e().length&&e()[0].key||i.e.multiple})},t.prototype._computePayloads=function(){var e=this.operations()[0];return e&&e.payloads()||{}},t.prototype._initializeOperations=function(){var e=this;this.addDisposable(this.operations.map({mappingWithDisposeCallback:function(t){var n,a,i,o,s,c,u=e.createPureComputed(function(){return r.e[t.state()]}),f=e.addDisposable(l(t.progress.minimum,e.progress.minimum)),p=e.addDisposable(l(t.progress.maximum,e.progress.maximum)),m=e.addDisposable(l(t.progress.current,e.progress.current)),_=e.addDisposable((n=u,a=e.states,o=function(e,t){var n=a.peek();void 0!==e&&n[e]--,void 0!==t&&(n[t]=(n[t]||0)+1),a.valueHasMutated()},s=n.subscribe(function(){i=n.peek()},null,"beforeChange"),c=n.subscribe(function(){o(i,n.peek())}),o(void 0,n.peek()),{dispose:function(){s.dispose(),c.dispose(),o(n.peek(),void 0)}})),h=e.addDisposable(function(e,t){var n=e.peek(),a=e.subscribe(function(){n=e.peek()},null,"beforeChange"),i=d.computed(function(){!t()&&e()&&t(e())}),r=e.subscribe(function(e){!e&&n&&t.peek()===n&&t(void 0)});return{dispose:function(){i.dispose(),r.dispose(),a.dispose()}}}(t.error,e.error)),b=e.addDisposable(l(t.count,e.count)),g=e.createComputed(function(){var n=!1,a=e.actions.peek();for(var i in t.actions())i in a||(a[i]=e._initializeAction(i),n=!0);n&&e.actions.valueHasMutated()});return{mappedValue:t,dispose:function(){u.dispose(),f.dispose(),p.dispose(),m.dispose(),_.dispose(),g.dispose(),h.dispose(),b.dispose()}}}}))},t.prototype._computeState=function(){var e=this.states();return e.started||e.created&&(e.failed||e.completed||e.canceled)?r.e.started:e.created?r.e.created:e.failed?r.e.failed:e.completed?r.e.completed:e.canceled?r.e.canceled:r.e.expired},t.prototype._computeVisibility=function(){return this.operations().reduce(function(e,t){var n=t.visibility.peek();return n<e?n:e},2)},t.prototype._initializeAction=function(e){var t=this.addDisposable(this.operations.filter(function(t){var n=t.actions()[e];return n&&n.isAvailable()}));return this.addDisposable(new o.e({count:this.createPureComputed(function(){return t().length}),key:e,operation:this,isAvailable:this.createPureComputed(function(){return!!t().length}),onExecute:function(){return s.t.all(t().slice().map(function(t){var n=t.actions.peek()[e];return n&&n.execute()||s.t.wrap()}))}}))},t}(c.n);t.e=f}}]);