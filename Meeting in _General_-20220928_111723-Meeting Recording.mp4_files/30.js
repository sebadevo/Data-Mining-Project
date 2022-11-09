(window.odspNextWebpackJsonp=window.odspNextWebpackJsonp||[]).push([[30],{287:function(e,t,n){"use strict";n.d(t,"e",function(){return i});var a=n(110);function i(){return window.CUSTOMERPROMISE_MANAGER=window.CUSTOMERPROMISE_MANAGER||Object(a.t)()}},523:function(e,t,n){"use strict";n.d(t,"e",function(){return l});var a=n(20),i=n(359),r=n(55),o=n(77),s=n(110),c=n(287),d="Missing Perf Goal",l=function(e){function t(t){var n=e.call(this,t)||this;return(null==t?void 0:t.perfGoalInMs)&&n.setTimeout(null==t?void 0:t.perfGoalInMs,{resultType:o.e.Failure,errorCode:d}),n}return Object(a.__extends)(t,e),t.prototype.end=function(t){return t&&t.extraData&&this.data.extraData&&(t=Object(a.__assign)(Object(a.__assign)({},t),{extraData:Object(a.__assign)(Object(a.__assign)({},this.data.extraData),t.extraData)})),t&&t.errorCode!==d&&(t=this._assessPerf(t)),e.prototype.end.call(this,t)},t.prototype._assessPerf=function(e){if(!this.endTime){var t=e.perfGoalInMs||this.data.perfGoalInMs;t&&e.resultType!==o.e.Failure&&t<s.e.getTime()-this.startTime&&(e=Object(a.__assign)(Object(a.__assign)({},e),{resultType:o.e.Failure,errorCode:d,extraData:e.errorCode?Object(a.__assign)(Object(a.__assign)({},e.extraData),{innerErrorCode:e.errorCode}):void 0}))}return e},t}(Object(i.e)({eventName:"CustomerPromise,",shortEventName:"CustomerPromise",requiresParent:!1},{scenario:{isKey:!0,isPrefixingDisabled:!0,type:r.e.String},errorCode:{isPrefixingDisabled:!0,type:r.e.String},resultType:{typeRef:o.e,isPrefixingDisabled:!0,type:r.e.Enum},resultCategory:{isPrefixingDisabled:!0,type:r.e.String},extraData:r.e.Object,httpStatus:{isPrefixingDisabled:!0,type:r.e.Number},perfGoalInMs:{isPrefixingDisabled:!0,type:r.e.Number},duration:{isPrefixingDisabled:!0,type:r.e.Number}})).withManager(Object(c.e)())},926:function(e,t,n){"use strict";n.d(t,"t",function(){return i}),n.d(t,"e",function(){return r});var a=n(402),i=new a.t({name:"".concat("ListItemsDataSourceParams.key",".useFolderScopedSearch"),factory:new a.e(!0)}),r=new a.t({name:"".concat("ListItemsDataSourceParams.key",".listShouldRenderFilesTitle"),factory:new a.e(void 0)})},1020:function(e,t,n){"use strict";var a;n.d(t,"e",function(){return a}),function(e){e[e.Click=1]="Click",e[e.Tap=2]="Tap",e[e.Keyboard=3]="Keyboard",e[e.Drop=4]="Drop"}(a||(a={}))},1027:function(e,t,n){"use strict";var a=n(20),i=n(743),r=n(1020),o=n(35),s=n(52),c=n(793),d=n(43),l=n(188),u=n(58),f=n(77),p=n(221),m=n(230),_=n(50),h=n(523),b=n(101),g=function(e){function t(t,n){void 0===t&&(t={}),void 0===n&&(n={});var a=e.call(this,t,n)||this;a.name="BaseAction";var i=a,r=i.resources,o=i.observables,c=n.urlDataSource,d=void 0===c?r.consume(s.v.optional):c,l=n.instrumentationProvider,u=void 0===l?r.consume(p.n.optional):l;a._BaseAction_urlDataSource=d,a._BaseAction_instrumentationProvider=u,a.isQosLogged=!0,a.logStartEnd=!1,a.enableCustomerPromiseLogging=!1,a._executingInstanceCount=o.create(0);var f={deferEvaluation:!0};return a.isAvailable=o.pureCompute(a._computeIsAvailable,f),a.isToggled=o.pureCompute(a._computeIsToggled,f),a.isExecuting=o.pureCompute(a._computeIsExecuting,f),a}return Object(a.__extends)(t,e),t.prototype.execute=function(e){var t,n,a=this,i=this.isQosLogged?this.onCreateQosEvent(e):void 0,r=i?this.getEngagement():void 0;try{if(i&&(this._logEngagementEvent(i.data.extraData,r),this.trackUserAction(this.name)),!(t=this.instrumentOnExecutionWithCustomerPromise(this.onExecute(e,i))))throw new Error("Action did not return a promise")}catch(e){d.e.log(e),n=e}return t?(this._executingInstanceCount(this._executingInstanceCount.peek()+1),t.then(function(e){a._executingInstanceCount(a._executingInstanceCount.peek()-1),i&&i.end(e)},function(t){a._executingInstanceCount(a._executingInstanceCount.peek()-1),t&&!c.t.isCanceled(t)&&d.e.log(t),i&&i.end(a.onCreateErrorEventArg(e,t,!1))})):(i&&i.end(this.onCreateErrorEventArg(e,n,!0)),t=c.t.reject(n)),t},t.prototype.onCreateQosEvent=function(e){var t=this._BaseAction_urlDataSource;return new i.e({name:this.name,pageType:t&&l.e[t.getPageType()]||"",queryType:t&&u.e[t.getQueryType()]||"",logStartEnd:this.logStartEnd})},t.prototype.onCreateErrorEventArg=function(e,t,n){return t&&c.t.isCanceled(t)?{resultType:f.e.ExpectedFailure,resultCode:"Canceled"}:t instanceof _.e?{resultType:t.isExpected?f.e.ExpectedFailure:f.e.Failure,resultCode:t.code,error:t.message,extraData:{CorrelationId:t.correlationId}}:{resultType:f.e.Failure,resultCode:n?"NoPromiseReturned":"PromiseFailed",error:t?"".concat(t.message||""):void 0}},t.prototype.onExecute=function(e,t){var n={resultType:f.e.Failure};return c.t.resolve(n)},t.prototype.instrumentOnExecutionWithCustomerPromise=function(e){var t=e;if(this.enableCustomerPromiseLogging){var n=this._BaseAction_urlDataSource,i=new h.e({scenario:this.name,extraData:{pageType:n&&l.e[n.getPageType()]||"",queryType:n&&u.e[n.getQueryType()]||""}});t=e.then(function(e){var t=e.resultCode,n=e.resultType,r=e.error,o=e.extraData;return i.end({resultType:n,errorCode:t,extraData:Object(a.__assign)(Object(a.__assign)({},o),{error:r})}),e}).catch(function(e){var t;if(c.t.isCanceled(e))t={resultType:f.e.ExpectedFailure,errorCode:"Canceled"};else{var n=Object(b.e)(e),r=n.resultType,o=n.resultCode,s=n.error,d=n.extraData;t={resultType:r,errorCode:o,extraData:Object(a.__assign)(Object(a.__assign)({},d),{error:s})}}throw i.end(t),e})}return t},t.prototype.onIsAvailable=function(){return!0},t.prototype.onIsToggled=function(){return!1},t.prototype.getEngagement=function(){return this.resources.consume(m.e)},t.prototype.trackUserAction=function(e){var t=this._BaseAction_instrumentationProvider;if(t){var n=this.getEngagement();t.userExecuteAction({name:e,engagement:n})}},t.prototype._computeIsAvailable=function(){return!!this.onIsAvailable()},t.prototype._computeIsToggled=function(){return!!this.onIsToggled()},t.prototype._computeIsExecuting=function(){return this._executingInstanceCount()>0},t.prototype._logEngagementEvent=function(e,t){if(void 0===t&&(t=this.isQosLogged?this.getEngagement():void 0),t){var n=this._BaseAction_instrumentationProvider;t.logData({name:this.name,isIntentional:this.isExecutionIntentional,location:"NA",usageType:r.e[r.e.Click],currentPage:n&&n.currentPageName()||"NA",previousPage:n&&n.previousPageName()||"NA",extraData:Object(a.__assign)(Object(a.__assign)({},e||{}),n&&n.getEngagementData()||{})})}},t.dependencies=Object(a.__assign)(Object(a.__assign)({},o.n.dependencies),{urlDataSource:s.v,instrumentationProvider:p.n.optional}),t}(o.n);t.e=g},1207:function(e,t,n){"use strict";n.d(t,"e",function(){return a});var a=new(n(402).t)("MoveCopyCapabilities")},1416:function(e,t,n){"use strict";n.r(t),n.d(t,"exposeKnockoutResources",function(){return q});var a,i=n(96),r=n(52),o=n(221),s=n(40),c=n(1132),d=n(402),l=(n(926),new d.t({name:"ListItemsDataSource.key",loader:new c.t(function(){return Promise.all([n.e("ondemand.resx-ondemand"),n.e("deferred.resx-deferred"),n.e(69)]).then(n.bind(null,1412)).then(function(e){return e.resourceKey})})})),u=n(20),f=n(128),p=function(e){function t(t){void 0===t&&(t={});var n,a=e.call(this)||this,i=a.listUrl;if(a._pageContext=t.pageContext||a.resources.consume(s.i),t.listRootFolderWebRelativeUrl||t.listRootFolderServerRelativeUrl||!t.listFullUrl?t.listRootFolderWebRelativeUrl?n=Object(f.n)(a._pageContext)+"/"+t.listRootFolderWebRelativeUrl:t.listRootFolderServerRelativeUrl&&(n=t.listRootFolderServerRelativeUrl):n=decodeURIComponent(t.listFullUrl).split(Object(f.a)(a._pageContext))[1],!i||n!==i){for(var r=0,o=Object.keys(a);r<o.length;r++)delete a[o[r]];a.listUrl=n,a.listId=t.listId}return!a.listTitle&&a._pageContext&&(a.listTitle=a._pageContext.listTitle),a.customWidthDictionary||(a.customWidthDictionary={}),a}return Object(u.__extends)(t,e),t}(n(307).e),m=n(106),_=n(79),h=new d.t({name:"ListContext.key",factory:{dependencies:{pageContext:s.i,navigation:m.e,resources:d.r},create:function(e){var t=e.pageContext,n=e.navigation;return{instance:new(e.resources.injected(p))({listId:t.listId||n.viewParams[_.n.listIdKey],listRootFolderServerRelativeUrl:t.listUrl||n.viewParams[_.n.listUrlKey]})}}}}),b=n(1207),g=n(7),v=new d.t({name:"MoveCopyCapabilities",factory:{dependencies:{},create:function(){return{instance:{supportsMoveCopy:!0,supportsMoveCopyOnShared:!1,supportsMoveCopyFilterParams:!0,supportsCopyCrossSite:Object(g.isFeatureEnabled)(g.CopyCrossSiteFromTeamSite),supportsMoveCrossSite:Object(g.isFeatureEnabled)(g.MoveCrossSite),supportsThrottling:!0,supportsProgressCaching:!0}}}}}),y=new d.t({name:"MicroServiceDataSource.key",loader:new c.t(function(){return Promise.resolve().then(n.bind(null,484)).then(function(e){return e.resourceKey})})}),S=(new d.t({name:"".concat("MicroServiceDataSource.key",".type"),loader:new c.t(function(){return Promise.resolve().then(n.bind(null,484)).then(function(e){return e.typeResourceKey})})}),n(484)),D=n(389),I=n(793),x=n(35),C=n(68),O=n(1134),w=n(985),E=n(90),A=n(77),L=[1,0],k=new C.e,M=function(){function e(){this._started=!1,this._done=!1,this._bundleGroups={},this._queuedBundles=[]}return Object.defineProperty(e.prototype,"hasStarted",{get:function(){return this._started},enumerable:!1,configurable:!0}),e.prototype.start=function(){var e=this;this._started||(this._started=!0,k.setTimeout(function(){return e._next()},1e3))},e.prototype.queueLoad=function(e,t,n){var a=this._getGroup(e,n),i=this._generateModuleRequest(a,e,t,n);return this._queueBundle(a),i.signal.getPromise()},e.prototype.waitFor=function(e,t){var n=this._getGroup(e,t);return this._generateModuleRequest(n,e,0,t).signal.getPromise()},e.prototype.loadNow=function(e,t){var n=this._getGroup(e,t),a=this._generateModuleRequest(n,e,0,t);return n.isResolved||this._requestBundle(n).done(),a.signal.getPromise()},e.prototype._getGroup=function(e,t){var n=window.require.toUrl(e),a=this._bundleGroups[n];return a||(a=this._createGroup(e,n,t),this._bundleGroups[n]=a),a},e.prototype._createGroup=function(e,t,n){var a=window.require.specified(t),i={bundleUrl:t,requestedPath:e,getModule:n,modules:a?null:{},isResolved:a,isQueued:!1};if(!a)for(var r=0,o=L;r<o.length;r++){var s=o[r];i.modules[s]=[]}return i},e.prototype._createModuleRequest=function(e,t){return{path:e,getModule:t,signal:new O.e,isResolved:!1}},e.prototype._addNewModule=function(e,t,n,a){var i=this._createModuleRequest(t,a);return e.modules[n].push(i),i},e.prototype._generateModuleRequest=function(e,t,n,a){var i;return e.isResolved?(i=this._createModuleRequest(t,a),this._resolveModule(i)):i=this._addNewModule(e,t,n,a),i},e.prototype._queueBundle=function(e){e.isQueued||(this._queuedBundles.push(e),e.isQueued=!0,this._done&&(this._done=!1,this._next()))},e.prototype._next=function(){var e=this;if(this._started){var t=this._getNextGroup();if(t){var n=this._requestBundle(t);n&&n.then(function(){k.setTimeout(function(){return e._next()},500)}).done()}}},e.prototype._getNextGroup=function(){for(var e=this._queuedBundles.shift();e;){if(!e.isResolved)return e;e=this._queuedBundles.shift()}this._done=!0},e.prototype._processBundlePriorityLevel=function(e,t){if(!e.modules)return I.t.wrap();for(var n=[],a=0,i=e.modules[t];a<i.length;a++){var r=i[a];this._resolveModule(r),n.push(r.signal.getPromise())}return I.t.all(n).then(function(){},function(){})},e.prototype._processBundle=function(e){for(var t=this,n=function(n,a){return a.then(function(){return t._processBundlePriorityLevel(e,n)})},a=I.t.wrap(),i=0,r=L;i<r.length;i++)a=n(r[i],a);return a.then(function(){e.isResolved=!0,e.modules=null})},e.prototype._requestBundle=function(e){var t=this,n=new E.e({name:"DeferredBundleLoad"});return Object(w.e)({path:e.requestedPath,getModule:e.getModule}).then(function(){return n.end({resultType:A.e.Success,extraData:{path:e.requestedPath,url:e.bundleUrl}}),t._processBundle(e)},function(t){n.end({resultType:A.e.Failure,error:t,extraData:{path:e.requestedPath,url:e.bundleUrl}})})},e.prototype._resolveModule=function(e){e.isResolved=!0,e.path&&Object(w.e)({path:e.path,getModule:e.getModule}).then(function(t){e.signal.complete(t)})},e}(),P=n(43),T=function(e){function t(t){var n=e.call(this,t)||this;return n._resources=[],n._finished=new O.e,n.finishedProcessing=n._finished.getPromise(),n.isLoaded=n.createObservable(!1),n.createBackgroundComputed(n._computeShouldProcess),n}return Object(u.__extends)(t,e),t.prototype.expose=function(e,t){this._resources.push({key:e,getModule:t}),this.isLoaded.peek()&&this._processResources()},t.prototype._processResources=function(){for(var e=this,t=I.t.resolve(),n=0,a=this._resources;n<a.length;n++){var i=a[n];t=this._processResource(t,i)}t.then(function(){e._resources.length=0,e._finished.complete()})},t.prototype._processResource=function(e,t){var n=this;return e.then(function(){return t.getModule()}).then(function(e){try{var a=new(n.managed(e.default))({});n.resources.expose(t.key,a)}catch(n){P.e.logError(n,{rawResult:"(".concat(typeof e,"): ").concat(e.default),resourceKey:"(".concat(t.key.id,"): ").concat(t.key.name)})}})},t.prototype._computeShouldProcess=function(){this.isLoaded()&&this._processResources()},t}(x.n),U=n(229),F=n(44),H=function(e){function t(t){void 0===t&&(t={});var n=e.call(this,t)||this;n._queue=new M;var a=n._pageLoadMonitor=n.resources.consume(U.e),i=n.isPageLoaded=n.observables.create(a.isPageLoaded),o=n.isPageRenderingComplete=n.observables.create(a.isPageRenderingComplete);if(a.isPageLoaded?n._onPageLoaded():a.waitForPLT().then(function(){i(a.isPageLoaded),n._onPageLoaded()}),a.isPageRenderingComplete||a.waitForPageRenderingComplete().then(function(){o(a.isPageRenderingComplete)}),n.resources.isExposed(r.t)){var s=n.resources.consume(r.t);n._bundles=s.getBundles()}else n._bundles={};return n}return Object(u.__extends)(t,e),t.prototype.pageLoaded=function(e){Object(F.e)(0),this._pageLoadMonitor.pageLoaded(e)},t.prototype.pageRenderingIsComplete=function(e){this._pageLoadMonitor.pageRenderingIsComplete(e)},t.prototype.queueLoad=function(e,t){return this._queue.queueLoad(e,0,t)},t.prototype.queueBundle=function(e,t){var n=this.getBundleInfo(e);this.queueLoad(n.path,t||n.getModule).then(function(){n.isLoaded(!0)})},t.prototype.createDeferredContext=function(e){var t=this.getBundleInfo(e),n=new(this.managed(T))({});return t.path&&this._queue.queueLoad(t.path,1,t.getModule).then(function(){n.finishedProcessing.then(function(){t.isLoaded(!0)}),n.isLoaded(!0)}),n},t.prototype.waitFor=function(e,t){return this._queue.waitFor(e,t)},t.prototype.loadNow=function(e,t){return this._queue.loadNow(e,t)},t.prototype.getBundleInfo=function(e){if(e){var t=this._bundles[e];return t||(t={path:"",getModule:function(){return I.t.as(void 0)},isLoaded:this.createObservable(!1)},this._bundles[e]=t),t}},t.prototype.waitForPLT=function(){return this._pageLoadMonitor.waitForPLT()},t.prototype.waitForPageRenderingComplete=function(){return this._pageLoadMonitor.waitForPageRenderingComplete()},t.prototype._onPageLoaded=function(){this._queue.hasStarted||this._queue.start()},t}(x.n),R=new d.t({name:"".concat("MoveCopyDataSource.key",".MoveCopyDataSource"),loader:new c.t(function(){return n.e(22).then(n.bind(null,1443)).then(function(e){return e.resourceKey})})}),N=R,B=n(1027),j=function(e){function t(){var t=null!==e&&e.apply(this,arguments)||this;return t.name="Unsupported",t}return Object(u.__extends)(t,e),t.prototype.onIsAvailable=function(){return!1},t}(B.e),V=j;!function(e){e[e.none=0]="none",e[e.htmlFileUpload=1]="htmlFileUpload",e[e.folderUpload=2]="folderUpload",e[e.downlevelUpload=3]="downlevelUpload",e[e.silverlightUpload=4]="silverlightUpload"}(a||(a={}));var z=a,G=function(e){function t(t){var n=this,a=t.load,i=t.actionParams,r=(n=e.call(this,i)||this).resources.consume(o.e.optional);n.isQosLogged=!1,n.name="Deferred".concat(t.modulePath).replace(/Action|\.|\//g,""),n._action=n.createObservable();var s=new O.e;return(r?r.waitForPLT().then(a):I.t.resolve(a())).done(function(e){return s.complete(e)},function(e){return s.error(e)}),n._getActionPromise=n.trackPromise(s.getPromise().then(function(e){return new(n.managed(e))(i)})),n._getActionPromise.done(function(e){return n._action(e)}),n.inputType=n.createPureComputed(n._computeInputType),n}return Object(u.__extends)(t,e),t.prototype.onIsAvailable=function(){return!!this._action()&&this._action().isAvailable()},t.prototype.onIsToggled=function(){return!!this._action()&&this._action().isToggled()},t.prototype.onExecute=function(e,t){return this._getActionPromise.then(function(t){return t.execute(e)})},t.prototype._computeInputType=function(){var e=this._action();return e&&e.inputType?e.inputType():z.none},t}(B.e),K=n(506),W=function(e){function t(){var t,a=e.call(this)||this;return a.MoveCopyAction=(t=function(){return Promise.all([n.e("ondemand.resx-ondemand"),n.e("deferred.resx-deferred"),n.e(13)]).then(n.bind(null,1422))},function(e,t){var n;function a(){return n||(n=t())}return function(e){function t(t){return e.call(this,{load:a,modulePath:"@ms/odsp-next/lib/odsp-next/actions/odb/moveCopy/MoveCopyAction",actionParams:t})||this}return Object(u.__extends)(t,e),t}(G)}(0,function(){return t().then(K.e)})),a}return Object(u.__extends)(t,e),t}(function(){this.AddCoverPhotoAction=V,this.AddExistingAppViewAction=V,this.AddFlowAction=V,this.AddPhotosToAlbumAction=V,this.EditSmartTemplateAction=V,this.DeleteSmartTemplateAction=V,this.DeleteSmartTemplateWithProgressAction=V,this.PublishSmartTemplateAction=V,this.PublishSmartTemplateWithProgressAction=V,this.UnPublishSmartTemplateAction=V,this.UnPublishSmartTemplateWithProgressAction=V,this.ActivateUniversalAnnotationAction=V,this.AddToAlbumAction=V,this.AddToBundleAction=V,this.AddToFolderAction=V,this.AddToFolderAction=V,this.AddToQuickLaunchAction=V,this.AddToSharedListAction=V,this.AddToSpotlightAction=V,this.AlertAction=V,this.ApplyOfficeLensAction=V,this.ApproveRejectAction=V,this.AuthenticationPolicyWarningAction=V,this.AutoExecuteAction=V,this.CancelEditAction=V,this.ChangeAppViewVisibilityAction=V,this.ChangeFolderTypeAction=V,this.CheckInAction=V,this.CheckOutAction=V,this.ClearFilterAction=V,this.ClearSelectionAction=V,this.ComplianceDetailsAction=V,this.ContentTypeNavigationAction=V,this.LaunchConfigureFlowsPanelAction=V,this.CopyFieldAction=V,this.CopyFormAction=V,this.CreateAlbumAction=V,this.CreateAlbumFromFolderAction=V,this.CreateAppViewAction=V,this.CreateColumnAction=V,this.CreateCustomDocumentAction=V,this.CreateDocumentAction=V,this.CreateFileRequestAction=V,this.CreateFolderAction=V,this.CreateItemAction=V,this.CreateMountPointAction=V,this.CreateNewFolderAction=V,this.CreateSitePageAction=V,this.CustomActionNavigationAction=V,this.CustomizeClientFormAction=V,this.CustomizeFormsNavigationAction=V,this.CustomizeViewAction=V,this.DefaultClickAction=V,this.DeleteAction=V,this.DeleteTemplateAction=V,this.DeleteAppAction=V,this.DeleteViewAction=V,this.DiscardAutoAlbumAction=V,this.DownloadAction=V,this.OpenSWAAction=V,this.DownloadZipContentsAction=V,this.EditAction=V,this.EditItemAction=V,this.EditItemCancelAction=V,this.EditItemSaveAction=V,this.EditNewAppViewAction=V,this.EditNewMenuAction=V,this.EditNewMenuPaneAction=V,this.EditPdfAction=V,this.EditRenditionsAction=V,this.EditTagsAction=V,this.EmbedAction=V,this.EmptyRecycleBinAction=V,this.ExportListAction=V,this.ExternalNavigateAction=V,this.FeedbackAction=V,this.FileHandlerOpenAction=V,this.FilterAction=V,this.FilterSearchAction=V,this.FilterSearchByDateAction=V,this.GetLinkAction=V,this.GroupItemsAction=V,this.ImplicitSaveAutoAlbumAction=V,this.InvokeFirstRunExperienceAction=V,this.LanguagePickerAction=V,this.LaunchApprovalDetailsDialogAction=V,this.LaunchChangeTheLookPanelAction=V,this.LaunchColumnCustomizationPaneAction=V,this.LaunchColumnManagementPanelAction=V,this.LaunchCreateAppViewPanelAction=V,this.LaunchCreateGroupPanelAction=V,this.LaunchCreateListDialog=V,this.LaunchCreateShortcutPanel=V,this.LaunchDocLibSettingPanelAction=V,this.LaunchFilterPanelAction=V,this.LaunchFlowWidgetPanelAction=V,this.LaunchFormatViewPaneAction=V,this.LaunchGroupifyPanelAction=V,this.LaunchGroupMembershipPanelAction=V,this.LaunchListCreationPanelAction=V,this.LaunchListFormAction=V,this.LaunchMoveCopyPanelAction=V,this.LaunchPdfExtractionAction=V,this.LaunchSitePermissionsPanelAction=V,this.LaunchSiteSettingsPanelAction=V,this.LaunchGlobalNavSettingsPanelAction=V,this.LaunchWebTemplatesGalleryAction=V,this.LaunchUserExpirationPanelAction=V,this.LaunchVivaConnectionsSettingsPanelAction=V,this.ListFormActivityPaneToggleAction=V,this.MakeHomepageAction=V,this.VaultAction=V,this.ModifyColumnAction=V,this.ModifyShowInFiltersPaneAction=V,this.MoveCopyAction=V,this.MoveLeftSpotlightAction=V,this.MoveRightSpotlightAction=V,this.NavigateToItemAction=V,this.NavigateToSharePointHomeAction=V,this.NavigationAction=V,this.OneDriveSortAction=V,this.OpenAction=V,this.OpenChatAction=V,this.OpenAppAction=V,this.OpenDocSetAction=V,this.OpenHyperlinkAction=V,this.OpenInExplorerAction=V,this.OpenInfoPathAction=V,this.OpenInImageEditorAction=V,this.OpenInOfficeClientAction=V,this.OpenInOfficeOnlineAction=V,this.OpenInImmersiveReaderAction=V,this.OpenInSharePointAction=V,this.OpenInDesktopAction=V,this.OpenInTextEditorAction=V,this.OpenInClipChampAction=V,this.OpenNeedsAttentionViewAction=V,this.OpenPdfInBrowserAction=V,this.OpenInPowerBIAction=V,this.OpenShortcutAction=V,this.OpenSiteAction=V,this.OrderPrintsAction=V,this.PinToMruAction=V,this.PlayAudioAction=V,this.PlaySlideShowAction=V,this.PolicyTipAction=V,this.PreviewAction=V,this.PrintPdfAction=V,this.PublishAction=V,this.RedeemAction=V,this.RedeemCodeAction=V,this.RemoveCoverPhotoAction=V,this.RemoveFromAlbumAction=V,this.RemoveFromBundleAction=V,this.RemoveFromRecentAction=V,this.RemoveFromSharedListAction=V,this.RemoveFromSpotlightAction=V,this.RemoveMountPointAction=V,this.RemoveOfficeLensAction=V,this.RemoveTagAction=V,this.RemoveTagFromItemAction=V,this.RenameAction=V,this.RenameColumnAction=V,this.ReportAbuseAction=V,this.RequestReviewAction=V,this.RestoreAction=V,this.RestoreAllAction=V,this.RestoreFilesAction=V,this.RotateAction=V,this.SaveAction=V,this.SaveAutoAlbumAction=V,this.SaveSortOrderAction=V,this.SaveViewAction=V,this.SeeAllAppsAction=V,this.SelectAction=V,this.SelectAllAction=V,this.SetAlbumCoverPhotoAction=V,this.SetDefaultViewAction=V,this.SetFocusAction=V,this.SetPhotosRootAction=V,this.SetUpApprovalFlowAction=V,this.SetUpReminderFlowAction=V,this.ShareAction=V,this.ShareByLinkAction=V,this.ShowExistingFlowsAction=V,this.ShowFiltersAction=V,this.ShowItemAnalyticsAction=V,this.ShowSuggestedFilesAction=V,this.ShowKeyPointsAction=V,this.ShowKeyboardMapAction=V,this.ShowMalwareDetectedAction=V,this.ShowOperationsAction=V,this.ShowPermissionsAction=V,this.ShowPropertiesAction=V,this.ShowRunReportAction=V,this.ShowSelectionAction=V,this.ShowVersionHistoryAction=V,this.SignOutAction=V,this.StopSlideShowAction=V,this.SurveyAction=V,this.SwitchPhotoFolderLayoutTypeAction=V,this.SwitchSharingLinkAction=V,this.SwitchViewAction=V,this.SyncAction=V,this.SynchronizeAppViewAction=V,this.LaunchTeamChannelAction=V,this.ToggleAction=V,this.ToggleDebugWindowAction=V,this.ToggleIsLeftNavUserExpandedAction=V,this.ToggleListLayoutAction=V,this.ToggleSelectionModeAction=V,this.TriggerFlowAction=V,this.TriggerFlowByIdAction=V,this.TriggerODBConvertToPdfFlowAction=V,this.TriggerODBRequestSignOffFlowAction=V,this.TriggerSignoffFlowAction=V,this.TriggerExtractFileMetadataFlowAction=V,this.UndoCheckOutAction=V,this.UnPublishAction=V,this.UpdateCaptionAction=V,this.UpdatePermissionsAction=V,this.UploadAction=V,this.UploadTemplateAction=V,this.QuotaBlockAction=V,this.ViewInFolderAction=V,this.ViewItemAction=V,this.ViewOriginalAction=V,this.WorkflowAction=V});function q(e){var t=new(e.injected(H));e.expose(o.e,t),e.exposeFactory(s.n,new c.e(h)),e.exposeFactory(r.u,new c.e(l)),e.exposeFactory(r.o,new c.e(l)),e.expose(i.e,new W),e.exposeFactory(r.n,new c.e(N)),e.exposeFactory(b.e,new c.e(v)),e.exposeFactory(y,new c.e(S.resourceKey)),e.exposeFactory(D.e,new c.e(S.resourceKey))}}}]);