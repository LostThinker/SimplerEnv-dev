import gymnasium as gym
import mani_skill2_real2sim.envs
import warnings

ENVIRONMENTS = [
    "google_robot_pick_coke_can",
    "google_robot_pick_horizontal_coke_can",
    "google_robot_pick_vertical_coke_can",
    "google_robot_pick_standing_coke_can",
    "google_robot_pick_object",
    "google_robot_move_near_v0",
    "google_robot_move_near_v1",
    "google_robot_move_near",
    "google_robot_open_drawer",
    "google_robot_open_top_drawer",
    "google_robot_open_middle_drawer",
    "google_robot_open_bottom_drawer",
    "google_robot_close_drawer",
    "google_robot_close_top_drawer",
    "google_robot_close_middle_drawer",
    "google_robot_close_bottom_drawer",
    "google_robot_place_in_closed_drawer",
    "google_robot_place_in_closed_top_drawer",
    "google_robot_place_in_closed_middle_drawer",
    "google_robot_place_in_closed_bottom_drawer",
    "google_robot_place_apple_in_closed_top_drawer",
    "widowx_spoon_on_towel",
    "widowx_carrot_on_plate",
    "widowx_stack_cube",
    "widowx_put_eggplant_in_basket",
    # "widowx_carrot_on_plate_distractor",
    # "widowx_spoon_on_towel_distractor",
    # "widowx_stack_cube_distractor",
    # "widowx_unseen_on_plate",
    # "widowx_multi_on_plate",
    # "widowx_seq_on_plate",
    # "widowx_comb_on_plate",
    # "widowx_carrot_on_plate_lang_distractor",
    # "widowx_stack_cube_lang_distractor",
    # "widowx_spoon_on_towel_lang_distractor",
    # "widowx_vegetable_on_plate_ambig",
    # "widowx_drink_on_plate_ambig",
    # "widowx_fruit_on_plate_ambig",
    # "widowx_two_plate_ambig",
    # "widowx_two_same_ambig",
    # "widowx_toy_bin_pick",
    # "widowx_fruit_bin_pick",
    # "widowx_vegetable_bin_pick",
    # "widowx_fruit_bin_pick_correction",
    # "widowx_multi_on_plate_set",
    # "widowx_move_near",
    # "widowx_move_to_left_right",
    # "widowx_move_to_left_right_further",
    # "widowx_move_to_left_right_closer",
    # "widowx_multi_set_on_plate",
    # "widowx_multi_spatial_on_plate",
    # "widowx_animals_semantic",
    # "widowx_human_semantic",
    # "widowx_logo_semantic",
    # "widowx_ambig_obj_on_plate",
    # "widowx_ambig_target_on_plate",
    # "widowx_rubiks_on_seen_tg",
    # "widowx_mouse_on_unseen_tg",
    # "widowx_seen_on_unseen_tg",
    # "widowx_move_spatial",
    # "widowx_move_spatial_printer",
    # "widowx_move_spatial_dress",
    "widowx_seen_obj_on_seen_tg",
    "widowx_unseen_obj_on_seen_tg",
    "widowx_unseen_obj_on_unseen_tg",
    "widowx_unseen_obj_on_unseen_tg_hard",
    "widowx_move_near_tg",
    "widowx_move_left_tg",
    "widowx_move_right_tg",
    "widowx_move_front_tg",
    "widowx_move_behind_tg",
    "widowx_move_away_tg",
    "widowx_move_between_tg",
    "widowx_put_sw_obj_tg",
    "widowx_put_ambig_obj_tg",
    "widowx_put_obj_ambig_tg",
    "widowx_put_vege_tg",
    "widowx_put_toy_tg",
    "widowx_put_fruit_tg",
    "widowx_put_obj_tg_semantic",
    "widowx_put_all_in_tray",
    "widowx_put_toy_in_tray",
    "widowx_put_fruit_in_tray",
    "widowx_put_vege_in_tray",
    "widowx_put_in_tray_categ",
    "widowx_put_on_multi_tg",
    "widowx_put_on_multi_tg_occu",
]

ENVIRONMENT_MAP = {
    "google_robot_pick_coke_can": ("GraspSingleOpenedCokeCanInScene-v0", {}),
    "google_robot_pick_horizontal_coke_can": (
        "GraspSingleOpenedCokeCanInScene-v0",
        {"lr_switch": True},
    ),
    "google_robot_pick_vertical_coke_can": (
        "GraspSingleOpenedCokeCanInScene-v0",
        {"laid_vertically": True},
    ),
    "google_robot_pick_standing_coke_can": (
        "GraspSingleOpenedCokeCanInScene-v0",
        {"upright": True},
    ),
    "google_robot_pick_object": ("GraspSingleRandomObjectInScene-v0", {}),
    "google_robot_move_near": ("MoveNearGoogleBakedTexInScene-v1", {}),
    "google_robot_move_near_v0": ("MoveNearGoogleBakedTexInScene-v0", {}),
    "google_robot_move_near_v1": ("MoveNearGoogleBakedTexInScene-v1", {}),
    "google_robot_open_drawer": ("OpenDrawerCustomInScene-v0", {}),
    "google_robot_open_top_drawer": ("OpenTopDrawerCustomInScene-v0", {}),
    "google_robot_open_middle_drawer": ("OpenMiddleDrawerCustomInScene-v0", {}),
    "google_robot_open_bottom_drawer": ("OpenBottomDrawerCustomInScene-v0", {}),
    "google_robot_close_drawer": ("CloseDrawerCustomInScene-v0", {}),
    "google_robot_close_top_drawer": ("CloseTopDrawerCustomInScene-v0", {}),
    "google_robot_close_middle_drawer": ("CloseMiddleDrawerCustomInScene-v0", {}),
    "google_robot_close_bottom_drawer": ("CloseBottomDrawerCustomInScene-v0", {}),
    "google_robot_place_in_closed_drawer": ("PlaceIntoClosedDrawerCustomInScene-v0", {}),
    "google_robot_place_in_closed_top_drawer": ("PlaceIntoClosedTopDrawerCustomInScene-v0", {}),
    "google_robot_place_in_closed_middle_drawer": ("PlaceIntoClosedMiddleDrawerCustomInScene-v0", {}),
    "google_robot_place_in_closed_bottom_drawer": ("PlaceIntoClosedBottomDrawerCustomInScene-v0", {}),
    "google_robot_place_apple_in_closed_top_drawer": (
        "PlaceIntoClosedTopDrawerCustomInScene-v0",
        {"model_ids": "baked_apple_v2"}
    ),
    "widowx_spoon_on_towel": ("PutSpoonOnTableClothInScene-v0", {}),
    "widowx_carrot_on_plate": ("PutCarrotOnPlateInScene-v0", {}),
    "widowx_stack_cube": ("StackGreenCubeOnYellowCubeBakedTexInScene-v0", {}),
    "widowx_put_eggplant_in_basket": ("PutEggplantInBasketScene-v0", {}),
}

# DISTRACTOR_ENVIRONMENT_MAP = {
#     "widowx_carrot_on_plate_distractor": ("PutCarrotOnPlateInSceneDistract-v0", {}),
#     "widowx_spoon_on_towel_distractor": ("PutSpoonOnTableClothInSceneDistract-v0", {}),
#     "widowx_stack_cube_distractor": ("StackGreenCubeOnYellowCubeInSceneDistract-v0", {}),
# }
#
# UNSEEN_OBJ_ENV_MAP = {
#     "widowx_unseen_on_plate": ("PutUnseenObjOnPlateInScene-v0", {})
# }
#
# MULTI_OBJ_ENV_MAP = {
#     "widowx_multi_on_plate": ("PutOnPlateInSceneMulti-v0", {}),
#     "widowx_multi_on_plate_set": ("PutOnPlateInSceneMulti-v1", {}),
#     "widowx_seq_on_plate": ("PutOnPlateInSceneSequence-v0", {}),
#     "widowx_comb_on_plate": ("PutOnPlateInSceneComb-v0", {}),
#     "widowx_toy_bin_pick": ("PutToyOnBinInSceneMulti-v0", {}),
#     "widowx_fruit_bin_pick": ("PutFruitOnBinInSceneMulti-v0", {}),
#     "widowx_vegetable_bin_pick": ("PutVegetableOnBinInSceneMulti-v0", {}),
#     "widowx_multi_set_on_plate": ("PutOnMultiInSceneBridgeEnv-v0", {}),
#     "widowx_multi_spatial_on_plate": ("PutOnMultiInSceneBridgeEnvSpatial-v0", {}),
#
# }
#
# # with language distractor
# LANGUAGE_DISTRACTOR_ENVIRONMENT_MAP = {
#     "widowx_carrot_on_plate_lang_distractor": ("PutCarrotOnPlateInSceneLangDistract-v0", {}),
#     "widowx_spoon_on_towel_lang_distractor": ("PutSpoonOnTableClothInSceneLangDistract-v0", {}),
#     "widowx_stack_cube_lang_distractor": ("StackGreenCubeOnYellowCubeInSceneLangDistract-v0", {}),
# }
#
# AMBIGUATE_ENV_MAP = {
#     "widowx_vegetable_on_plate_ambig": ("PutVegetableOnPlateInScene-v0", {}),
#     "widowx_drink_on_plate_ambig": ("PutDrinkOnPlateInScene-v0", {}),
#     "widowx_fruit_on_plate_ambig": ("PutFruitOnPlateInScene-v0", {}),
#     "widowx_two_plate_ambig": ("PutOnTwoPlateInScene-v0", {}),
#     "widowx_two_same_ambig": ("PutSameTwoOnPlateInScene-v0", {}),
#     "widowx_animals_semantic": ("PutOnMultiInSceneBridgeEnvSemantic-v0", {}),
#     "widowx_human_semantic": ("PutOnMultiInSceneBridgeEnvSemantic-v1", {}),
#     "widowx_logo_semantic": ("PutOnMultiInSceneBridgeEnvSemantic-v2", {}),
#     "widowx_ambig_obj_on_plate": ("PutOnAmbigObjInSceneBridgeEnv-v0", {}),
#     "widowx_ambig_target_on_plate": ("PutOnAmbigTargetInSceneBridgeEnv-v0", {}),
# }
#
# CORRECTION_ENV_MAP = {
#     "widowx_fruit_bin_pick_correction": ("PutFruitOnBinInSceneCorrection-v0", {})
# }
#
# MOVE_TO_ENV_MAP = {
#     "widowx_move_near": ("MoveNearBridgeInScene-v0", {}),
#     "widowx_move_to_left_right": ("MoveToLeftRightBridgeInScene-v0", {}),
#     "widowx_move_to_left_right_further": ("MoveToLeftRightFurtherBridgeInScene-v0", {}),
#     "widowx_move_to_left_right_closer": ("MoveToLeftRightCloserBridgeInScene-v0", {}),
# }
#
# ABSTRACT_ENV_MAP = {
#     "widowx_rubiks_on_seen_tg": ("PutUnseenObjOnSeenTgRubiks-v0", {}),
#     "widowx_mouse_on_unseen_tg": ("PutUnseenObjOnUnseenTgMouse-v0", {}),
#     "widowx_seen_on_unseen_tg": ("PutSeenObjOnUnseenTg-v0", {}),
#     "widowx_move_spatial": ("MoveUnseenObjSpatial-v0", {}),
#     "widowx_move_spatial_printer": ("MoveUnseenObjSpatialPrinter-v0", {}),
#     "widowx_move_spatial_dress": ("MoveUnseenObjSpatialDress-v0", {}),
#
# }

V0_1_ENV_MAP = {
    "widowx_seen_obj_on_seen_tg": ("PutSeenObjOnSeenTg-v0", {}),
    "widowx_unseen_obj_on_seen_tg": ("PutUnseenObjOnSeenTg-v0", {}),
    "widowx_unseen_obj_on_unseen_tg": ("PutUnseenObjOnUnseenTg-v0", {}),
    "widowx_unseen_obj_on_unseen_tg_hard": ("PutUnseenObjOnUnseenTgHard-v0", {}),
    "widowx_move_near_tg": ("MoveObjNearTarget-v0", {}),
    "widowx_move_left_tg": ("MoveObjToLeftOfTarget-v0", {}),
    "widowx_move_right_tg": ("MoveObjToRightOfTarget-v0", {}),
    "widowx_move_front_tg": ("MoveObjInFrontOfTarget-v0", {}),
    "widowx_move_behind_tg": ("MoveObjBehindTarget-v0", {}),
    "widowx_move_away_tg": ("MoveObjAwayFromTarget-v0", {}),
    "widowx_move_between_tg": ("MoveObjBetweenTargets-v0", {}),
    "widowx_put_sw_obj_tg": ("PutObjSomeWhereOnTarget-v0", {}),
    "widowx_put_ambig_obj_tg": ("PutAmbigObjOnTarget-v0", {}),
    "widowx_put_obj_ambig_tg": ("PutObjOnAmbigTarget-v0", {}),
    "widowx_put_vege_tg": ("PutVegeObjOnTarget-v0", {}),
    "widowx_put_toy_tg": ("PutToyObjOnTarget-v0", {}),
    "widowx_put_fruit_tg": ("PutFruitObjOnTarget-v0", {}),
    "widowx_put_obj_tg_semantic": ("PutObjOnTargetSemantic-v0", {}),
    "widowx_put_all_in_tray": ("PutAllInTrayMulti-v0", {}),
    "widowx_put_toy_in_tray": ("PutToyInTrayMulti-v0", {}),
    "widowx_put_fruit_in_tray": ("PutFruitInTrayMulti-v0", {}),
    "widowx_put_vege_in_tray": ("PutVegeInTrayMulti-v0", {}),
    "widowx_put_in_tray_categ": ("PutObjInTrayCategorize-v0", {}),
    "widowx_put_on_multi_tg": ("PutObjectOnTargetMulti-v0", {}),
    "widowx_put_on_multi_tg_occu": ("PutObjectOnOccuTargetMulti-v0", {}),
}

# ENVIRONMENT_MAP.update(DISTRACTOR_ENVIRONMENT_MAP)
# ENVIRONMENT_MAP.update(UNSEEN_OBJ_ENV_MAP)
# ENVIRONMENT_MAP.update(MULTI_OBJ_ENV_MAP)
# ENVIRONMENT_MAP.update(LANGUAGE_DISTRACTOR_ENVIRONMENT_MAP)
# ENVIRONMENT_MAP.update(AMBIGUATE_ENV_MAP)
# ENVIRONMENT_MAP.update(CORRECTION_ENV_MAP)
# ENVIRONMENT_MAP.update(MOVE_TO_ENV_MAP)
# ENVIRONMENT_MAP.update(ABSTRACT_ENV_MAP)
ENVIRONMENT_MAP.update(V0_1_ENV_MAP)


def make(task_name, **kwargs):
    """Creates simulated eval environment from task name."""
    assert task_name in ENVIRONMENTS, f"Task {task_name} is not supported. Environments: \n {ENVIRONMENTS}"
    env_name, env_kwargs = ENVIRONMENT_MAP[task_name]

    env_kwargs["obs_mode"] = "rgbd",
    env_kwargs["prepackaged_config"] = True

    for key, value in kwargs.items():
        if key in env_kwargs:
            warnings.warn(f"default value [{env_kwargs[key]}] for Key {key} changes to value [{value}]")
        env_kwargs[key] = value

    env = gym.make(env_name, **env_kwargs)
    return env
