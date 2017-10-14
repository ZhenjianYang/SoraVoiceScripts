from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1103   ._SN',
        MapName             = 'Bose',
        Location            = 'C1103.x',
        MapIndex            = 49,
        MapDefaultBGM       = "ed60030",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Loewe',                                # 9
        'Agate',                                # 10
        'General Morgan',                       # 11
        'Royal Army Officer',                   # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Soldier',                              # 16
        'Soldier',                              # 17
        'Soldier',                              # 18
        'Soldier',                              # 19
        'Soldier',                              # 20
        'Soldier',                              # 21
        'Soldier',                              # 22
        'Afterimage',                           # 23
        'Broken Sword',                         # 24
        'Ancient Dragon Ragnard',               # 25
        '竜',                                   # 26
        'Patrol Ship',                          # 27
        ' ',                                    # 28
        ' ',                                    # 29
        ' ',                                    # 30
        ' ',                                    # 31
        ' ',                                    # 32
        ' ',                                    # 33
        ' ',                                    # 34
        ' ',                                    # 35
        ' ',                                    # 36
        ' ',                                    # 37
        ' ',                                    # 38
        ' ',                                    # 39
        ' ',                                    # 40
        ' ',                                    # 41
        ' ',                                    # 42
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02040 ._CH',             # 00
        'ED6_DT06/CH20053 ._CH',             # 01
        'ED6_DT07/CH02080 ._CH',             # 02
        'ED6_DT07/CH01600 ._CH',             # 03
        'ED6_DT07/CH01640 ._CH',             # 04
        'ED6_DT27/CH04540 ._CH',             # 05
        'ED6_DT27/CH04542 ._CH',             # 06
        'ED6_DT27/CH04548 ._CH',             # 07
        'ED6_DT27/CH04546 ._CH',             # 08
        'ED6_DT07/CH00150 ._CH',             # 09
        'ED6_DT07/CH00151 ._CH',             # 0A
        'ED6_DT07/CH00152 ._CH',             # 0B
        'ED6_DT07/CH00153 ._CH',             # 0C
        'ED6_DT07/CH00154 ._CH',             # 0D
        'ED6_DT06/CH20137 ._CH',             # 0E
        'ED6_DT26/CH20343 ._CH',             # 0F
        'ED6_DT26/CH20345 ._CH',             # 10
        'ED6_DT07/CH00161 ._CH',             # 11
        'ED6_DT26/CH20346 ._CH',             # 12
        'ED6_DT07/CH00321 ._CH',             # 13
        'ED6_DT07/CH00326 ._CH',             # 14
        'ED6_DT26/CH20362 ._CH',             # 15
        'ED6_DT26/CH20340 ._CH',             # 16
        'ED6_DT07/CH00158 ._CH',             # 17
        'ED6_DT07/CH00159 ._CH',             # 18
        'ED6_DT26/CH20207 ._CH',             # 19
        'ED6_DT26/CH20364 ._CH',             # 1A
        'ED6_DT26/CH20363 ._CH',             # 1B
        'ED6_DT26/CH20243 ._CH',             # 1C
        'ED6_DT26/CH20347 ._CH',             # 1D
        'ED6_DT26/CH20348 ._CH',             # 1E
        'ED6_DT27/CH04541 ._CH',             # 1F
        'ED6_DT27/CH04547 ._CH',             # 20
        'ED6_DT27/CH04545 ._CH',             # 21
        'ED6_DT06/CH20138 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT07/CH02040P._CP',             # 00
        'ED6_DT06/CH20053P._CP',             # 01
        'ED6_DT07/CH02080P._CP',             # 02
        'ED6_DT07/CH01600P._CP',             # 03
        'ED6_DT07/CH01640P._CP',             # 04
        'ED6_DT27/CH04540P._CP',             # 05
        'ED6_DT27/CH04542P._CP',             # 06
        'ED6_DT27/CH04548P._CP',             # 07
        'ED6_DT27/CH04546P._CP',             # 08
        'ED6_DT07/CH00150P._CP',             # 09
        'ED6_DT07/CH00151P._CP',             # 0A
        'ED6_DT07/CH00152P._CP',             # 0B
        'ED6_DT07/CH00153P._CP',             # 0C
        'ED6_DT07/CH00154P._CP',             # 0D
        'ED6_DT06/CH20137P._CP',             # 0E
        'ED6_DT26/CH20343P._CP',             # 0F
        'ED6_DT26/CH20345P._CP',             # 10
        'ED6_DT07/CH00161P._CP',             # 11
        'ED6_DT26/CH20346P._CP',             # 12
        'ED6_DT07/CH00321P._CP',             # 13
        'ED6_DT07/CH00326P._CP',             # 14
        'ED6_DT26/CH20362P._CP',             # 15
        'ED6_DT26/CH20340P._CP',             # 16
        'ED6_DT07/CH00158P._CP',             # 17
        'ED6_DT07/CH00159P._CP',             # 18
        'ED6_DT26/CH20207P._CP',             # 19
        'ED6_DT26/CH20364P._CP',             # 1A
        'ED6_DT26/CH20363P._CP',             # 1B
        'ED6_DT26/CH20243P._CP',             # 1C
        'ED6_DT26/CH20347P._CP',             # 1D
        'ED6_DT26/CH20348P._CP',             # 1E
        'ED6_DT27/CH04541P._CP',             # 1F
        'ED6_DT27/CH04547P._CP',             # 20
        'ED6_DT27/CH04545P._CP',             # 21
        'ED6_DT06/CH20138P._CP',             # 22
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_602",          # 00, 0
        "Function_1_66C",          # 01, 1
        "Function_2_67A",          # 02, 2
        "Function_3_C56",          # 03, 3
        "Function_4_CDF",          # 04, 4
        "Function_5_CF4",          # 05, 5
        "Function_6_D17",          # 06, 6
        "Function_7_159C",         # 07, 7
        "Function_8_161D",         # 08, 8
        "Function_9_288D",         # 09, 9
        "Function_10_28A1",        # 0A, 10
        "Function_11_2C9A",        # 0B, 11
        "Function_12_2CCA",        # 0C, 12
        "Function_13_311E",        # 0D, 13
        "Function_14_58B6",        # 0E, 14
        "Function_15_58CD",        # 0F, 15
        "Function_16_5914",        # 10, 16
        "Function_17_5938",        # 11, 17
        "Function_18_5966",        # 12, 18
        "Function_19_5994",        # 13, 19
        "Function_20_59C2",        # 14, 20
        "Function_21_5A79",        # 15, 21
        "Function_22_5B2F",        # 16, 22
        "Function_23_5B4B",        # 17, 23
        "Function_24_5B67",        # 18, 24
        "Function_25_5B83",        # 19, 25
        "Function_26_5BBA",        # 1A, 26
        "Function_27_5C05",        # 1B, 27
        "Function_28_5C50",        # 1C, 28
        "Function_29_5C9B",        # 1D, 29
        "Function_30_5CE6",        # 1E, 30
        "Function_31_5D31",        # 1F, 31
        "Function_32_5D7C",        # 20, 32
        "Function_33_5DC7",        # 21, 33
        "Function_34_5E12",        # 22, 34
        "Function_35_5E5D",        # 23, 35
        "Function_36_5EA8",        # 24, 36
        "Function_37_5F58",        # 25, 37
        "Function_38_6307",        # 26, 38
        "Function_39_66B3",        # 27, 39
        "Function_40_6E02",        # 28, 40
        "Function_41_6E71",        # 29, 41
        "Function_42_8236",        # 2A, 42
        "Function_43_8292",        # 2B, 43
        "Function_44_82EA",        # 2C, 44
        "Function_45_82FF",        # 2D, 45
        "Function_46_831B",        # 2E, 46
        "Function_47_8337",        # 2F, 47
        "Function_48_8353",        # 30, 48
        "Function_49_844C",        # 31, 49
        "Function_50_8490",        # 32, 50
        "Function_51_84D5",        # 33, 51
        "Function_52_8569",        # 34, 52
    )


    def Function_0_602(): pass

    label("Function_0_602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_621")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 41)
    Jump("loc_66B")

    label("loc_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_651")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (107, "loc_639"),
        (SWITCH_DEFAULT, "loc_64E"),
    )


    label("loc_639")

    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_64E")

    label("loc_64E")

    Jump("loc_66B")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66B")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_66B")

    Return()

    # Function_0_602 end

    def Function_1_66C(): pass

    label("Function_1_66C")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_10(0x0, 0x0)
    Return()

    # Function_1_66C end

    def Function_2_67A(): pass

    label("Function_2_67A")


    def lambda_680():
        OP_6D(-2940, 0, 5940, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_680)

    def lambda_698():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_698)

    def lambda_6A8():
        OP_6B(3500, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A8)

    def lambda_6B8():
        OP_6E(262, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6B8)
    SetChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 10)

    def lambda_6D2():
        OP_8E(0xFE, 0xFFFFE386, 0x0, 0x203A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6D2)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 11)

    def lambda_6FC():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6FC)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_711():
        OP_96(0xFE, 0xFFFFF5E2, 0x0, 0x14A0, 0x578, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_711)
    Sleep(300)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_73E():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_73E)
    Sleep(100)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)

    def lambda_7A3():
        OP_99(0xFE, 0x4, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7A3)
    OP_96(0x9, 0xFFFFF268, 0x0, 0x15CC, 0xC8, 0x1388)
    WaitChrThread(0x9, 0x1)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_7D4():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7D4)

    def lambda_7E4():
        OP_96(0xFE, 0xFFFFF8EE, 0x0, 0x13E2, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7E4)
    Sleep(100)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_80F():
        OP_96(0x8, 0x4F6, 0x0, 0x104A, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_80F)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 2)
    Sleep(200)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    WaitChrThread(0x8, 0x0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 5)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 0)

    def lambda_876():
        OP_99(0x8, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_876)

    def lambda_886():
        OP_96(0x8, 0xFFFFFFA6, 0x0, 0x1176, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_886)
    Sleep(100)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_8F4():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_8F4)
    WaitChrThread(0x8, 0x0)
    SetChrSubChip(0x8, 7)
    ClearChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 24)

    def lambda_927():
        OP_99(0xFE, 0x0, 0xE, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_927)
    Sleep(400)
    OP_22(0x1F9, 0x0, 0x64)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_949():
        OP_96(0x8, 0x6E, 0x0, 0x164E, 0xC8, 0x2328)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_949)

    def lambda_967():
        OP_8C(0x8, 225, 0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_967)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)
    Sleep(200)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x9, 0x1)
    OP_7D(0x1, 0x8, 0x0, 0x0)

    def lambda_99B():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_99B)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 6)
    WaitChrThread(0x9, 0x1)

    def lambda_9C4():
        OP_99(0x8, 0x0, 0xA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9C4)
    Sleep(200)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_A24():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_A24)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 4)
    WaitChrThread(0x8, 0x0)
    SetChrSubChip(0x8, 7)
    ClearChrFlags(0x9, 0x2)

    def lambda_A5C():
        OP_8C(0x9, 45, 0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A5C)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 11)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_A7E():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A7E)

    def lambda_A8E():
        OP_96(0x9, 0xFFFFFD58, 0x0, 0x14C8, 0xC8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A8E)
    Sleep(200)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)

    def lambda_AC8():
        OP_96(0x8, 0x13BA, 0x0, 0xF96, 0x258, 0x2328)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_AC8)
    Sleep(200)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)

    def lambda_AF5():
        OP_6D(4240, 0, 3920, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF5)

    def lambda_B0D():
        OP_6C(332000, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B0D)
    WaitChrThread(0x9, 0x1)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x9, 0xF5A, 0x0, 0x4D8, 0x1F4, 0x1770)
    OP_8C(0x9, 0, 0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    TurnDirection(0x8, 0x9, 0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 3)
    Sleep(300)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 10)

    def lambda_B90():
        OP_96(0xFE, 0x1194, 0x0, 0x83E, 0x12C, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B90)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_BB6():
        OP_96(0xFE, 0x12B6, 0x0, 0xBCC, 0x12C, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BB6)
    Sleep(200)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 8)
    WaitChrThread(0x8, 0x1)
    ClearChrFlags(0x8, 0x1000)
    ClearChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x8, 8)
    SetChrChipByIndex(0x9, 14)

    def lambda_C01():

        label("loc_C01")

        OP_9E(0xFE, 0x14, 0x0, 0xFA0, 0x9C4)
        OP_48()
        Jump("loc_C01")

    QueueWorkItem2(0x9, 3, lambda_C01)
    Sleep(100)

    def lambda_C23():

        label("loc_C23")

        OP_9E(0xFE, 0x14, 0x0, 0xFA0, 0x9C4)
        OP_48()
        Jump("loc_C23")

    QueueWorkItem2(0x8, 3, lambda_C23)
    Sleep(500)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Return()

    # Function_2_67A end

    def Function_3_C56(): pass

    label("Function_3_C56")

    SetChrChipByIndex(0x8, 33)
    SetChrSubChip(0x8, 1)

    def lambda_C66():
        OP_9E(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C66)

    def lambda_C80():
        OP_96(0xFE, 0x474, 0x0, 0x104, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C80)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 2)

    def lambda_CB2():
        OP_96(0xFE, 0xF28, 0x0, 0xFFFFFC54, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CB2)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 6)
    Return()

    # Function_3_C56 end

    def Function_4_CDF(): pass

    label("Function_4_CDF")

    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    Return()

    # Function_4_CDF end

    def Function_5_CF4(): pass

    label("Function_5_CF4")

    WaitChrThread(0x9, 0x1)
    Sleep(400)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 0)

    def lambda_D0E():
        OP_8C(0xFE, 110, 400)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_D0E)
    Return()

    # Function_5_CF4 end

    def Function_6_D17(): pass

    label("Function_6_D17")

    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x20)

    def lambda_D2C():
        OP_6D(-1800, 0, 6230, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D2C)

    def lambda_D44():
        OP_67(0, 4450, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D44)

    def lambda_D5C():
        OP_6B(2029, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D5C)
    SetChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 0)

    def lambda_D7B():
        OP_8E(0xFE, 0xFFFFE642, 0x0, 0x1FD6, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D7B)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 3)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_DAF():
        OP_96(0xFE, 0xFFFFF7FE, 0x0, 0x163A, 0x578, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_DAF)
    Sleep(200)

    def lambda_DD2():
        OP_99(0xFE, 0x3, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_DD2)
    Sleep(100)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 2)
    OP_8C(0x8, 332, 0)
    OP_7D(0x0, 0x8, 0x32, 0xC8)

    def lambda_E00():
        OP_96(0xFE, 0xFFFFFB50, 0x0, 0x8C, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E00)
    Sleep(150)
    SetChrFlags(0x9, 0x800)
    OP_22(0x55, 0x0, 0x5A)
    PlayEffect(0x12, 0xFF, 0xFF, -380, -1000, 4830, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x258, 0xBB8, 0x64)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 32)
    SetChrSubChip(0x8, 1)
    OP_8C(0x8, 20, 0)
    Sleep(200)

    def lambda_E93():
        OP_6D(370, 0, 2040, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E93)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 4)
    OP_8C(0x9, 200, 0)

    def lambda_EBC():
        OP_99(0xFE, 0x4, 0xE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_EBC)

    def lambda_ECC():
        OP_96(0xFE, 0xFFFFFB14, 0x0, 0x5A0, 0xC8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ECC)
    OP_43(0x9, 0x0, 0x0, 0x5)
    Sleep(200)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 2)

    def lambda_F00():
        OP_8C(0xFE, 330, 400)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_F00)

    def lambda_F0E():
        OP_96(0xFE, 0x5D2, 0x0, 0xFFFFF6C8, 0x1F4, 0xDAC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F0E)
    Sleep(200)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_F40():
        OP_8C(0xFE, 280, 400)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_F40)

    def lambda_F4E():
        OP_96(0xFE, 0x1108, 0x0, 0xC8, 0x1F4, 0xDAC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F4E)
    WaitChrThread(0x8, 0x1)

    def lambda_F71():
        OP_6D(-2540, 0, 3240, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F71)

    def lambda_F89():
        OP_6B(1930, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F89)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 3)

    def lambda_FB0():
        OP_96(0xFE, 0x64, 0x0, 0x370, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FB0)
    Sleep(150)

    def lambda_FD3():
        OP_99(0xFE, 0x3, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_FD3)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x9, 1000, 500, -500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_44(0x9, 0x0)
    OP_44(0x9, 0x3)
    ClearChrFlags(0x9, 0x800)
    OP_8C(0x9, 110, 0)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)

    def lambda_1051():
        OP_8F(0xFE, 0xFFFFF380, 0x0, 0x816, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1051)

    def lambda_106C():
        OP_9E(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_106C)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    Sleep(100)

    def lambda_109A():
        OP_6D(-4210, 0, 3570, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_109A)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 2)

    def lambda_10BC():
        OP_96(0xFE, 0xFFFFECC8, 0x0, 0xA64, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10BC)

    def lambda_10DA():
        OP_8F(0xFE, 0xFFFFF8F8, 0x0, 0x668, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10DA)
    Sleep(100)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 1)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x9, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 3)
    Sleep(100)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 10)

    def lambda_112C():
        OP_8F(0xFE, 0xFFFFF196, 0x0, 0x8F2, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_112C)
    Sleep(100)

    def lambda_114C():
        OP_99(0xFE, 0xA, 0xE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_114C)
    Sleep(100)

    def lambda_1161():
        OP_6D(-270, 0, 2070, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1161)

    def lambda_1179():
        OP_6B(2029, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1179)
    OP_23(0xD6)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x8, -1000, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_43(0x8, 0x0, 0x0, 0x3)
    Sleep(400)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 0)

    def lambda_11F2():
        OP_8F(0xFE, 0xFFFFFC9A, 0x0, 0x46A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11F2)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 3)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1226():
        OP_96(0xFE, 0xCDA, 0x0, 0xFFFFFC4A, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1226)
    Sleep(200)

    def lambda_1249():
        OP_99(0xFE, 0x3, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1249)
    SetChrChipByIndex(0x8, 32)
    SetChrSubChip(0x8, 14)

    def lambda_1263():
        OP_8F(0xFE, 0x10AE, 0x0, 0x44C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1263)
    WaitChrThread(0x8, 0x1)
    Sleep(100)
    SetChrFlags(0x9, 0x800)
    OP_22(0x55, 0x0, 0x5A)
    PlayEffect(0x12, 0xFF, 0xFF, 4830, -1000, -1240, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x258, 0xBB8, 0x64)
    Sleep(100)

    def lambda_12DD():
        OP_6D(2850, 0, 920, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12DD)

    def lambda_12F5():
        OP_6C(314000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12F5)
    SetChrSubChip(0x8, 15)
    Sleep(30)
    OP_8C(0x8, 200, 0)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 0)

    def lambda_1320():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1320)

    def lambda_1330():
        OP_8F(0xFE, 0xF8C, 0x0, 0x3C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1330)
    Sleep(150)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x9, 1000, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    ClearChrFlags(0x9, 0x800)
    OP_8C(0x9, 60, 0)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 9)

    def lambda_13B1():
        OP_8F(0xFE, 0x10C2, 0x0, 0xFFFFECFA, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13B1)

    def lambda_13CC():
        OP_9E(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_13CC)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x9, 0x2)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 2)

    def lambda_13FA():
        OP_96(0xFE, 0x127A, 0x0, 0x88E, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13FA)
    OP_43(0x8, 0x0, 0x0, 0x4)

    def lambda_141F():
        OP_6D(4240, 0, 3920, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_141F)

    def lambda_1437():
        OP_6C(332000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1437)

    def lambda_1447():
        OP_6B(2130, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1447)

    def lambda_1457():
        OP_67(0, 5080, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1457)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 2)
    OP_8C(0x9, 20, 0)

    def lambda_1480():
        OP_96(0xFE, 0x1194, 0x0, 0x83E, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1480)

    def lambda_149E():
        OP_99(0xFE, 0x2, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_149E)
    Sleep(350)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x8, 0, 800, -1000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_44(0x9, 0x2)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 34)
    SetChrSubChip(0x9, 0)

    def lambda_151A():
        OP_8F(0xFE, 0x131A, 0x0, 0xC08, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_151A)

    def lambda_1535():
        OP_9E(0xFE, 0x3C, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1535)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x2)

    def lambda_1558():
        OP_9E(0xFE, 0xF, 0xFFFFFFF8, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_1558)

    def lambda_1572():
        OP_9E(0xFE, 0xF, 0xFFFFFFF8, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1572)
    OP_43(0x8, 0x0, 0x0, 0x7)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)
    Return()

    # Function_6_D17 end

    def Function_7_159C(): pass

    label("Function_7_159C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_161C")
    PlayEffect(0x3, 0xFF, 0xFF, 4760, 1100, 2720, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x3, 0xFF, 0xFF, 4700, 1200, 2700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Jump("Function_7_159C")

    label("loc_161C")

    Return()

    # Function_7_159C end

    def Function_8_161D(): pass

    label("Function_8_161D")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-17960, 0, -9210, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(2740, 0)
    OP_6C(59000, 0)
    OP_6E(602, 0)
    SetChrFlags(0x8, 0x800)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, -460, 0, 4800, 21)
    ClearChrFlags(0x8, 0x80)
    OP_72(0x0, 0x4)
    OP_CF(0x19, 0x0, "Frame127_FireEmitter")
    OP_A1(0x18, 0x0)
    SetChrPos(0x18, 12660, 0, 13410, 232)
    SetChrFlags(0x18, 0x1)
    ClearChrFlags(0x18, 0x80)
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x249F0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "map\\\\mp015_00.eff")

    def lambda_1721():
        OP_6D(6450, 0, 10810, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1721)

    def lambda_1739():
        OP_67(0, 7880, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1739)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 0x1)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x78)
    Fade(500)
    OP_6D(990, 3620, 6360, 0)
    OP_67(0, 5670, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(356000, 0)
    OP_6E(580, 0)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x37)
    Sleep(1000)
    OP_DC()

    ChrTalk(    #0
        0x8,
        "#121F#5P...\x02",
    )

    CloseMessageWindow()
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 22)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0x4, 0x5DC)
    Sleep(500)
    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x8, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_B0(0x0, 0x1E)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_B0(0x0, 0xF)
    Fade(500)
    OP_6F(0x0, 290)
    OP_70(0x0, 0x12C)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 300)
    OP_70(0x0, 0x15E)
    OP_22(0x122, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0x1E)
    OP_73(0x0)
    OP_B0(0x0, 0xF)

    def lambda_18C9():
        OP_6D(2140, 0, 8390, 3500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_18C9)

    def lambda_18E1():
        OP_67(0, 5940, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18E1)

    def lambda_18F9():
        OP_6B(2290, 3500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_18F9)
    Fade(500)
    OP_23(0x193)
    OP_6F(0x0, 350)
    OP_70(0x0, 0x1B3)
    OP_73(0x0)
    OP_43(0x19, 0x0, 0x0, 0x9)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #1
        0x8,
        "#124FAll right, that should be enough.\x02",
    )

    CloseMessageWindow()
    OP_99(0x8, 0x4, 0x0, 0x5DC)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(750)

    ChrTalk(    #2
        0x8,
        (
            "#121FHmph. We'll need a bit more time to\x01",
            "gather the necessary data.\x02\x03",

            "Of course this is the sort of job he'd\x01",
            "shove off on me...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -15470, 0, 11980, 90)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #3
        0x9,
        "Young Man's Voice",
        "#4PHavin' a bad day?\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1A58():
        OP_6D(-6950, 0, 9120, 2500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A58)

    def lambda_1A70():
        OP_67(0, 5080, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1A70)

    def lambda_1A88():
        OP_6B(3020, 2500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1A88)

    def lambda_1A98():
        OP_6C(332000, 2500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1A98)

    def lambda_1AA8():
        OP_6E(385, 2500)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1AA8)
    Sleep(500)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)

    def lambda_1AC7():
        TurnDirection(0x8, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1AC7)
    OP_8E(0x9, 0xFFFFD1A2, 0x0, 0x2A44, 0x7D0, 0x0)
    WaitChrThread(0x8, 0x1)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x8,
        "#120F#2PI have a guest, it seems.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#051F#6PYou're that red lieutenant from\x01",
            "before, aren't you? You've got that\x01",
            "same golden sword.\x02\x03",

            "Been a while...you bastard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#124F#2PAgate Crosner, the Heavy Blade.\x01",
            "Bracer rank C.\x02\x03",

            "#123FAh, no, you were promoted to\x01",
            "rank B after the coup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "#053F#6PNo surprise that a former member of\x01",
            "the Intelligence Division would already\x01",
            "know that.\x02\x03",

            "#555FYou were always sneakin' around in\x01",
            "the shadows like a rat back then...\x02\x03",

            "Decided to get a bit more showy this\x01",
            "time, huh?\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x9, 14)
    OP_0D()
    Sleep(750)

    ChrTalk(    #8
        0x9,
        (
            "#057F#6PWell, whatever. I ain't interested in arrests\x01",
            "or anything nice like that today.\x02\x03",

            "I'm just gonna slice that smug look\x01",
            "right off your face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#124F#2PConfident, aren't we?\x02\x03",

            "#123FI wouldn't call what happened 'showy,'\x01",
            "personally.\x02\x03",

            "It was certainly nothing compared to\x01",
            "what you saw ten years ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #10
        0x8,
        (
            "#123F#2PI've had a look at the records of every\x01",
            "bracer in this country.\x02\x03",

            "Heh. You and I are very similar in some\x01",
            "ways, Agate Crosner.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)

    ChrTalk(    #11
        0x9,
        (
            "#057F#6P...\x02\x03",

            "#053FHeh... Similar, huh?\x02",
        )
    )

    OP_21()
    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x2B)
    Sleep(500)
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 3)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #12
        0x9,
        (
            "#550F#6P#3SYOU DON'T KNOW SHIT!\x01",
            "SO DON'T! SAY! SHIT!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    LoadEffect(0x3, "map\\\\mp009_00.eff")
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x18, 0x0, 0x0, 0x6)
    WaitChrThread(0x18, 0x0)

    ChrTalk(    #13
        0x8,
        (
            "#124F#4PYou should know from our last encounter\x01",
            "the difference in our abilities.\x02\x03",

            "On top of that, I have a dragon at my\x01",
            "disposal.\x02\x03",

            "#120FSo what could possibly drive you to\x01",
            "engage me alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x9,
        (
            "#057F#6PYou think I give a damn about my\x01",
            "'chances of winning'?\x02\x03",

            "#054FI can't stand you. I'll take any chance\x01",
            "I can get to kick your ass!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#121F#4PUnbelievable. This is the extent of\x01",
            "your power?\x02\x03",

            "I won't even need the dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        "#057F#6PWhat?!\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0x3)
    OP_44(0x8, 0x3)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 6)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)
    OP_96(0x8, 0x15CC, 0x0, 0x16A8, 0x1F4, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)

    def lambda_21E9():
        OP_96(0xFE, 0x13BA, 0x0, 0xF96, 0xC8, 0x3A98)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_21E9)

    def lambda_2207():
        OP_99(0xFE, 0x0, 0x5, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2207)
    Sleep(100)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0x64)
    OP_22(0xD6, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)

    def lambda_2276():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2276)

    def lambda_2290():
        OP_8F(0xFE, 0x1108, 0x0, 0x708, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2290)
    WaitChrThread(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 6)

    def lambda_22BF():
        OP_99(0xFE, 0x0, 0x5, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_22BF)
    Sleep(100)
    PlayEffect(0x3, 0x2, 0x9, 0, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0xBB8, 0x64)

    def lambda_231F():
        OP_8F(0xFE, 0x1252, 0x0, 0xC26, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_231F)

    def lambda_233A():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_233A)

    def lambda_2354():
        OP_8F(0xFE, 0x100E, 0x0, 0x460, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2354)
    WaitChrThread(0x8, 0x2)
    OP_22(0x226, 0x0, 0x64)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 0)

    def lambda_2383():
        OP_99(0xFE, 0x0, 0x4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2383)
    Sleep(100)
    PlayEffect(0x3, 0x3, 0x9, 0, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_7C(0x0, 0x258, 0xBB8, 0x64)

    def lambda_23E3():
        OP_8F(0xFE, 0x1194, 0x0, 0x83E, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23E3)
    Sleep(100)

    def lambda_2403():
        OP_6D(3100, 0, 170, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2403)

    def lambda_241B():
        OP_9E(0xFE, 0x1E, 0x0, 0x4B0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_241B)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 12)
    SetChrSubChip(0x9, 0)

    def lambda_2444():
        OP_96(0x9, 0xC8A, 0x0, 0xFFFFF4CA, 0x1F4, 0x4650)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2444)
    Sleep(100)
    SetChrChipByIndex(0x9, 13)
    SetChrSubChip(0x9, 0)

    def lambda_2471():
        OP_96(0x9, 0xB68, 0x0, 0xFFFFF100, 0xC8, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2471)

    ChrTalk(    #17 op#A op#5
        0x9,
        "#056F#10AGuaaah!\x05\x02",
    )

    Sleep(500)

    def lambda_24AA():
        OP_99(0xFE, 0x4, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_24AA)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_24C8():
        OP_6B(2540, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_24C8)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 7)
    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x8,
        (
            "#121FWe may be similar in some ways,\x01",
            "but there is one crucial difference\x01",
            "between us.\x02\x03",

            "That being the reason we take up\x01",
            "our swords.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        "#057FThe hell are you--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#124FI wield mine to discard my humanity\x01",
            "and walk the path of ruin.\x02\x03",

            "#120FYou only wield yours in a desperate\x01",
            "attempt to fill the emptiness within you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        "#052F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#124FSwinging that lump of iron fills the\x01",
            "void within you.\x02\x03",

            "For a brief moment, your rage lets\x01",
            "you flee from your grief.\x02\x03",

            "#121FBut in the end, you're only deluding\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_26FF():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_26FF)
    Sleep(500)

    ChrTalk(    #23
        0x9,
        "#056F...Shut up...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#123FShould you continue to hide behind\x01",
            "your delusions, you will never move\x01",
            "forward.\x02\x03",

            "As you are now, you are neither fit for\x01",
            "enlightenment nor the path I follow.\x02\x03",

            "You will always remain incomplete.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x3)

    def lambda_2807():
        OP_9E(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2807)
    Sleep(500)
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 3)
    OP_0D()
    Sleep(500)

    ChrTalk(    #25
        0x9,
        "#550F#3SSHUT! THE! HELL! UUUUUUUP!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_A2(0x1A17)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1102   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_8_161D end

    def Function_9_288D(): pass

    label("Function_9_288D")

    OP_71(0x0, 0x20)
    OP_6F(0x0, 385)
    OP_70(0x0, 0x1B3)
    Return()

    # Function_9_288D end

    def Function_10_28A1(): pass

    label("Function_10_28A1")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x800)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 0)

    def lambda_28C9():
        OP_8F(0x9, 0xD0C, 0x0, 0xFFFFF77C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_28C9)

    def lambda_28E4():
        OP_6D(4450, 0, 1950, 1000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_28E4)
    Sleep(200)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 11)

    def lambda_2929():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2929)

    def lambda_2939():
        OP_96(0x9, 0x1022, 0x0, 0x2E4, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2939)
    OP_22(0x1F9, 0x0, 0x64)
    Sleep(200)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_2969():
        OP_96(0x8, 0x1338, 0x0, 0xB54, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2969)
    TurnDirection(0x8, 0x9, 0)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x8, 400)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_299F():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_299F)

    def lambda_29AF():
        OP_96(0x9, 0x1158, 0x0, 0x834, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_29AF)
    Sleep(250)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_2A2F():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A2F)
    WaitChrThread(0x9, 0x1)

    def lambda_2A44():
        OP_99(0xFE, 0x4, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2A44)

    def lambda_2A54():
        TurnDirection(0x9, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2A54)

    def lambda_2A62():
        OP_96(0x9, 0x143C, 0x0, 0xFFFFFD9E, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2A62)
    WaitChrThread(0x9, 0x1)
    Sleep(100)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 24)

    def lambda_2A99():
        OP_99(0xFE, 0x0, 0xE, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2A99)
    Sleep(400)

    def lambda_2AAE():
        OP_96(0x9, 0x1464, 0x0, 0x172, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2AAE)
    OP_22(0x1F9, 0x0, 0x64)
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_2AED():
        OP_96(0x8, 0x7A8, 0x0, 0xFFFFEC50, 0x7D0, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2AED)

    def lambda_2B0B():
        OP_6D(1870, 0, -5050, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B0B)
    Sleep(200)

    def lambda_2B28():
        OP_8C(0x8, 0, 0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2B28)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    TurnDirection(0x9, 0x8, 500)
    Sleep(100)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 23)
    SetChrSubChip(0x9, 19)

    def lambda_2B72():
        OP_99(0xFE, 0x14, 0x17, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B72)
    WaitChrThread(0x9, 0x1)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2B8C():
        OP_6D(1990, 2310, -4890, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B8C)

    def lambda_2BA4():
        OP_96(0x9, 0x87A, 0x0, 0xFFFFF060, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2BA4)
    Sleep(600)

    def lambda_2BC7():
        OP_6D(1870, 0, -5050, 100)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BC7)

    def lambda_2BDF():
        OP_6B(3360, 100)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2BDF)
    SetChrFlags(0x9, 0x800)
    OP_22(0x55, 0x0, 0x5A)

    def lambda_2BF9():
        OP_99(0xFE, 0x18, 0x1A, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2BF9)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)

    def lambda_2C1B():
        OP_96(0x8, 0x2A8, 0x0, 0xFFFFDCD8, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2C1B)
    PlayEffect(0x12, 0xFF, 0xFF, 1960, 0, -5040, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x1F4, 0x7D0, 0x64)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_28A1 end

    def Function_11_2C9A(): pass

    label("Function_11_2C9A")

    Sleep(200)

    def lambda_2CA5():
        OP_8C(0x8, 0, 0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2CA5)
    WaitChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_11_2C9A end

    def Function_12_2CCA(): pass

    label("Function_12_2CCA")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x800)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 0)

    def lambda_2CF2():
        OP_8F(0x9, 0xD0C, 0x0, 0xFFFFF77C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2CF2)

    def lambda_2D0D():
        OP_6D(4450, 0, 1950, 600)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2D0D)

    def lambda_2D25():
        OP_6B(2870, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D25)
    Sleep(200)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 9)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 3)

    def lambda_2D62():
        OP_96(0x9, 0x1022, 0x0, 0x2E4, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2D62)
    Sleep(200)

    def lambda_2D85():
        OP_99(0xFE, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D85)
    OP_22(0x1F9, 0x0, 0x64)
    OP_7D(0x0, 0x8, 0x14, 0x12C)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 2)

    def lambda_2DAC():
        OP_96(0x8, 0x1338, 0x0, 0xB54, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2DAC)
    TurnDirection(0x8, 0x9, 0)
    WaitChrThread(0x9, 0x0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    Sleep(300)
    TurnDirection(0x9, 0x8, 400)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_2DF9():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2DF9)

    def lambda_2E09():
        OP_96(0x9, 0x1158, 0x0, 0x834, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2E09)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 1)

    def lambda_2E31():
        OP_99(0xFE, 0x1, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2E31)
    Sleep(250)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_44(0x9, 0x1)

    def lambda_2E95():
        OP_99(0xFE, 0x4, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2E95)

    def lambda_2EA5():
        TurnDirection(0x9, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2EA5)

    def lambda_2EB3():
        OP_96(0x9, 0x143C, 0x0, 0xFFFFFD9E, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2EB3)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 0)

    def lambda_2EE0():
        OP_99(0xFE, 0x0, 0xE, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2EE0)
    Sleep(400)

    def lambda_2EF5():
        OP_96(0x9, 0x1464, 0x0, 0x172, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2EF5)
    Sleep(200)
    OP_22(0x1F9, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_2F34():
        OP_96(0x8, 0x7A8, 0x0, 0xFFFFEC50, 0x7D0, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F34)

    def lambda_2F52():
        OP_6D(2800, 0, -1440, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F52)

    def lambda_2F6A():
        OP_6B(3370, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F6A)
    OP_43(0x8, 0x0, 0x0, 0xB)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0x9, 0)
    SetChrFlags(0x9, 0x20)
    TurnDirection(0x9, 0x8, 1000)
    ClearChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 23)
    SetChrSubChip(0x9, 19)

    def lambda_2FB0():
        OP_99(0xFE, 0x13, 0x15, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2FB0)
    WaitChrThread(0x9, 0x1)
    Sleep(100)

    def lambda_2FCA():
        OP_99(0xFE, 0x15, 0x17, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2FCA)
    WaitChrThread(0x9, 0x1)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2FE4():
        OP_6D(1990, 2310, -4890, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2FE4)

    def lambda_2FFC():
        OP_96(0x9, 0x87A, 0x0, 0xFFFFF060, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2FFC)
    Sleep(200)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 10)
    Sleep(200)
    OP_7D(0x0, 0x8, 0x1E, 0x12C)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)

    def lambda_3045():
        OP_96(0x8, 0x2A8, 0x0, 0xFFFFDCD8, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3045)
    Sleep(200)

    def lambda_3068():
        OP_6D(1870, 0, -5050, 100)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3068)

    def lambda_3080():
        OP_6B(3360, 100)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3080)
    OP_44(0x9, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x800)
    SetChrChipByIndex(0x9, 23)
    SetChrSubChip(0x9, 24)

    def lambda_30A8():
        OP_99(0xFE, 0x18, 0x1A, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_30A8)
    OP_22(0x55, 0x0, 0x5A)
    PlayEffect(0x12, 0xFF, 0xFF, 1960, -1000, -5040, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x258, 0xBB8, 0xC8)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_2CCA end

    def Function_13_311E(): pass

    label("Function_13_311E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3131")
    Call(0, 52)

    label("loc_3131")

    OP_6D(3100, 0, 170, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3670, 0)
    OP_6C(332000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 4500, 0, 2110, 180)
    SetChrPos(0x9, 2950, 0, -4500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 7)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 3)
    OP_72(0x0, 0x4)
    SetChrPos(0x18, 12660, 0, 13410, 225)
    OP_A1(0x18, 0x0)
    SetChrPos(0x18, 12660, 0, 13410, 232)
    SetChrPos(0x19, 0, 0, 0, 225)
    OP_CF(0x19, 0x0, "Frame127_FireEmitter")
    SetChrFlags(0x18, 0x1)
    ClearChrFlags(0x18, 0x80)
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x249F0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x20)
    OP_6F(0x0, 385)
    OP_70(0x0, 0x1B3)
    LoadEffect(0x0, "battle\\\\mgaria0.eff")
    LoadEffect(0x1, "monster\\ms30703.eff")
    LoadEffect(0x2, "battle\\\\btbomb00.eff")
    LoadEffect(0x3, "map\\\\mp009_00.eff")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #26
        0x9,
        "#550F#3SRAAAAAAAAAAAGH!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_43(0x18, 0x0, 0x0, 0xC)
    WaitChrThread(0x18, 0x0)
    Sleep(1000)

    def lambda_330E():
        OP_6D(1300, 0, -5900, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_330E)

    def lambda_3326():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3326)

    def lambda_333E():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_333E)

    def lambda_334E():
        OP_6C(332000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_334E)

    def lambda_335E():
        OP_6E(262, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_335E)
    OP_99(0x9, 0x1A, 0x1E, 0x3E8)
    WaitChrThread(0x101, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x800)

    ChrTalk(    #27
        0x9,
        "#550FD-Damn you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#124FCareless.\x02\x03",

            "#120FAs the one mercy I can offer you,\x01",
            "I'll end this quickly.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 8)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #29
        0x8,
        "#126FHnnnnnnn...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        "#550FTch!\x02",
    )

    CloseMessageWindow()

    def lambda_3466():
        OP_6D(1910, 0, -4550, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3466)

    def lambda_347E():
        OP_96(0xFE, 0xBEA, 0x0, 0xFFFFF5D8, 0xC8, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_347E)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 7)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x3, "map\\\\mp009_00.eff")

    ChrTalk(    #31
        0x8,
        "#127F#5PHYA...!\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x16, 1380, 0, -6560, 0)
    ClearChrFlags(0x16, 0x80)

    def lambda_3506():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3506)
    OP_82(0x0, 0x0)

    def lambda_351B():
        OP_96(0xFE, 0x1342, 0x0, 0x8C0, 0xC8, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_351B)
    OP_22(0x9B, 0x0, 0x64)
    OP_20(0x0)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x17, 0x0, 0x0, 0x28)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 16)
    SetChrSubChip(0x9, 0)

    def lambda_358E():
        OP_6D(3620, 0, 240, 200)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_358E)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 5)
    WaitChrThread(0x16, 0x1)
    SetChrFlags(0x16, 0x80)
    Sleep(1000)

    def lambda_35BF():

        label("loc_35BF")

        OP_9E(0xFE, 0x14, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_35BF")

    QueueWorkItem2(0x9, 3, lambda_35BF)
    Sleep(500)

    ChrTalk(    #32
        0x9,
        "#056F#5PGuh...\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0x3)
    OP_99(0x9, 0x1, 0x4, 0x3E8)
    OP_22(0x20C, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_99(0x8, 0x5, 0x7, 0x640)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    Sleep(500)

    def lambda_362D():
        TurnDirection(0xFE, 0x9, 300)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_362D)
    Sleep(1000)

    ChrTalk(    #33
        0x8,
        "#121F...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x8, 0, 400)

    def lambda_366F():
        OP_6D(4340, 0, 9850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_366F)

    def lambda_3687():
        OP_67(0, 4770, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3687)

    def lambda_369F():
        OP_6B(4410, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_369F)

    def lambda_36AF():
        OP_6C(359000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_36AF)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #34
        0x8,
        (
            "#124F#2PNow, then. It's almost time.\x02\x03",

            "#120FI should alter the Gospel's control\x01",
            "style while I still have a moment.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #35
        0x9,
        "#5P#40WJust a...damn second...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x9, 400)
    Fade(500)
    OP_6D(3620, 0, 240, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(332000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_1D(0x53)

    def lambda_37C7():

        label("loc_37C7")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_37C7")

    QueueWorkItem2(0x9, 3, lambda_37C7)
    Sleep(500)
    OP_99(0x9, 0x4, 0x1, 0x1F4)
    OP_44(0x9, 0x3)
    Sleep(500)

    def lambda_37FB():

        label("loc_37FB")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_37FB")

    QueueWorkItem2(0x9, 3, lambda_37FB)
    SetChrFlags(0x9, 0x20)
    OP_8C(0x9, 0, 200)
    OP_44(0x9, 0x3)
    ClearChrFlags(0x9, 0x20)
    Sleep(500)

    ChrTalk(    #36
        0x9,
        (
            "#550F#40WI'm not...done yet!\x02\x03",

            "It's not...over...yet!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-26270, 0, 18840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -26050, 0, 19690, 90)
    SetChrPos(0x107, -26220, 0, 18290, 90)
    SetChrPos(0xF8, -27300, 0, 19840, 90)
    SetChrPos(0xF9, -27540, 0, 18220, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #37
        0x101,
        "#1020F#6PThat's...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x107,
        "#065F#6PAGATE!\x02",
    )

    CloseMessageWindow()

    def lambda_392A():
        OP_8E(0xFE, 0xFFFFC7D4, 0x0, 0x3AB6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_392A)
    Sleep(300)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #39
        0x101,
        "#1005F#6PTita!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_71(0x0, 0x4)
    Fade(500)
    OP_6D(3800, 0, -260, 0)
    OP_67(0, 8070, -10000, 0)
    OP_6B(1780, 0)
    OP_6C(237000, 0)
    OP_6E(428, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(    #40
        0x8,
        "#124FYou still cling to that broken lump of iron.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #41
        0x8,
        (
            "#123FAs you wish.\x01",
            "You shall die as broken as your blade.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x107, -8990, 0, 1190, 135)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 17)

    NpcTalk(    #42
        0x107,
        "Girl's Voice",
        "#3P#3SNOOOOOO!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrFlags(0x107, 0x1000)

    def lambda_3AED():
        OP_6B(2000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AED)

    def lambda_3AFD():
        OP_67(0, 7000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AFD)
    OP_8E(0x107, 0xED8, 0x0, 0xFFFFFBA0, 0x1770, 0x0)
    TurnDirection(0x107, 0x8, 400)
    Sleep(500)

    ChrTalk(    #43
        0x9,
        (
            "#550FShortstuff...\x02\x03",

            "The hell...are you doing...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x107,
        (
            "#065F#6PI, um...!\x02\x03",

            "I-I was worried about you, Agate,\x01",
            "so I came here with Estelle and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#3STITA!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    LoadEffect(0x0, "map\\\\mp015_00.eff")
    TurnDirection(0x8, 0x101, 400)
    Fade(250)
    SetChrChipByIndex(0x8, 22)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_22(0xD8, 0x0, 0x64)
    OP_99(0x8, 0x0, 0x4, 0x5DC)
    Sleep(300)

    ChrTalk(    #46
        0x8,
        "#121F#5PYou. Stop them.\x02",
    )

    CloseMessageWindow()
    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x8, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Fade(500)
    OP_72(0x0, 0x4)
    SetChrPos(0x18, 15390, 0, 12100, 255)
    OP_6D(11070, 0, 18710, 0)
    OP_67(0, 7880, -10000, 0)
    OP_6B(3710, 0)
    OP_6C(21000, 0)
    OP_6E(426, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x122, 0x0, 0x64)
    Sleep(1000)

    def lambda_3CDD():
        OP_6D(4220, 3290, 14610, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3CDD)

    def lambda_3CF5():
        OP_67(0, 2730, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3CF5)

    def lambda_3D0D():
        OP_6B(2760, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3D0D)

    def lambda_3D1D():
        OP_6C(56000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3D1D)

    def lambda_3D2D():
        OP_6E(426, 3000)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_3D2D)
    OP_72(0x0, 0x20)
    Fade(500)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 460)
    OP_70(0x0, 0x16D)

    def lambda_3D59():
        OP_8E(0xFE, 0xFFFFEBF6, 0x0, 0x14FA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D59)

    def lambda_3D74():
        OP_8E(0xFE, 0xFFFFEB92, 0x0, 0x19FA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3D74)

    def lambda_3D8F():
        OP_8E(0xFE, 0xFFFFE4F8, 0x0, 0x1270, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3D8F)
    OP_73(0x0)
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x78)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x0, 0x19, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x121, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_6D(3920, 0, 15460, 0)
    OP_67(0, 2610, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(45000, 0)
    OP_6E(532, 0)
    Sleep(300)
    OP_44(0x101, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E7B")
    OP_62(0xF9, 0x0, 2300, 0x28, 0x2B, 0x64, 0x0)
    Jump("loc_3EAF")

    label("loc_3E7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E9D")
    OP_62(0xF9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Jump("loc_3EAF")

    label("loc_3E9D")

    OP_62(0xF9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    label("loc_3EAF")

    OP_43(0xF9, 0x0, 0x0, 0x13)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EDD")
    OP_62(0xF8, 0x0, 2300, 0x28, 0x2B, 0x64, 0x0)
    Jump("loc_3F11")

    label("loc_3EDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EFF")
    OP_62(0xF8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Jump("loc_3F11")

    label("loc_3EFF")

    OP_62(0xF8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    label("loc_3F11")

    OP_43(0xF8, 0x0, 0x0, 0x12)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x101, 0x0, 0x0, 0x11)
    OP_73(0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x20)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x37)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    OP_63(0xF8)
    OP_63(0xF9)
    OP_63(0x101)

    ChrTalk(    #47
        0x101,
        "#1021F#5PAh...!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x0, 0x20)
    OP_6F(0x0, 465)
    OP_70(0x0, 0x1E7)
    Sleep(500)
    OP_22(0x122, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)

    def lambda_3FF3():
        OP_96(0xFE, 0xFFFFC5A4, 0x0, 0x256C, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3FF3)
    Sleep(100)

    def lambda_4016():
        OP_96(0xFE, 0xFFFFCE32, 0x0, 0x2ADA, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4016)
    Sleep(100)

    def lambda_4039():
        OP_96(0xFE, 0xFFFFD152, 0x0, 0x25C6, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4039)
    OP_73(0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x20)
    OP_6F(0x0, 487)
    OP_70(0x0, 0x205)
    Fade(500)
    OP_6D(-5710, 0, 10880, 0)
    OP_67(0, 4380, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(78000, 0)
    OP_6E(599, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40E8")

    ChrTalk(    #48
        0x108,
        "#077F#5PThis is bad!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4165")

    label("loc_40E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_413B")

    ChrTalk(    #49
        0x103,
        (
            "#523F#5PJust when I thought this day couldn't\x01",
            "get any worse!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4165")

    label("loc_413B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4165")

    ChrTalk(    #50
        0x105,
        "#043F#5PWhat do we do?\x02",
    )

    CloseMessageWindow()

    label("loc_4165")

    Sleep(500)
    Fade(500)
    OP_71(0x0, 0x4)
    OP_6D(3800, 0, -260, 0)
    OP_67(0, 8070, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(237000, 0)
    OP_6E(428, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0x8,
        "#121F#5P...\x02",
    )

    CloseMessageWindow()
    OP_99(0x8, 0x4, 0x0, 0x5DC)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 25)
    Sleep(250)
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)
    OP_43(0x8, 0x0, 0x0, 0x10)

    def lambda_41F9():
        OP_6D(3300, 0, -900, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41F9)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(    #52 op#5
        0x107,
        "#065F#6PPlease...\x05\x02",
    )

    ClearChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 17)
    OP_8F(0x107, 0xDCA, 0x0, 0xFFFFF95C, 0x3E8, 0x0)
    OP_56(0x0)
    OP_59()
    OP_63(0x107)
    SetChrFlags(0x107, 0x2)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 18)
    Sleep(500)

    ChrTalk(    #53
        0x107,
        "#068F#6PStay away, please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "#550FYou idiot! You think 'please' will\x01",
            "work on him?!\x02\x03",

            "Just run already!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #55
        0x8,
        (
            "#121FThe granddaughter of Zeiss' Professor Russell,\x01",
            "Tita Russell...\x02\x03",

            "I'd heard you were a child genius, but no\x01",
            "genius would ever behave so recklessly.\x02\x03",

            "#124FIn truth, I'm not fond of harming women\x01",
            "or children.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x8,
        (
            "#120FStill, I'll do what I must.\x02\x03",

            "Now, be a good girl and move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        "#550FYou son...of a bitch!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x107,
        "#062F#6PI... I won't move!\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0x107, 0x0, 0x4, 0x4B0)

    def lambda_44AB():
        OP_6B(1700, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_44AB)
    Sleep(500)

    ChrTalk(    #59
        0x107,
        (
            "#063F#6PI won't!\x01",
            "Agate's always saving me, so...\x02\x03",

            "I have to help him back! I have to...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 4)
    Sleep(50)
    SetChrSubChip(0x107, 5)
    Sleep(50)
    SetChrSubChip(0x107, 6)
    Sleep(50)
    SetChrSubChip(0x107, 5)
    Sleep(50)
    SetChrSubChip(0x107, 4)
    Sleep(50)
    SetChrSubChip(0x107, 7)
    Sleep(50)
    SetChrSubChip(0x107, 8)
    Sleep(50)
    SetChrSubChip(0x107, 7)
    Sleep(50)
    SetChrSubChip(0x107, 4)
    Sleep(50)
    SetChrSubChip(0x107, 5)
    Sleep(50)
    SetChrSubChip(0x107, 6)
    Sleep(50)
    SetChrSubChip(0x107, 5)
    Sleep(50)
    SetChrSubChip(0x107, 4)
    Sleep(500)

    ChrTalk(    #60
        0x107,
        "#561F#6PNo... That's not it. Not just it.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #61
        0x107,
        (
            "#066F#6PHe's blunt, and he always looks annoyed...\x02\x03",

            "He always treats me like a kid and calls\x01",
            "me things like 'shortstuff,' but...\x02\x03",

            "He's really very nice, and he's always\x01",
            "watching out for me!\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x107, 0x4, 0x0, 0x5DC)
    Sleep(300)

    ChrTalk(    #62
        0x107,
        "#062F#6PHe means so much to me... I love him!\x02",
    )

    CloseMessageWindow()
    OP_99(0x107, 0x0, 0x4, 0x7D0)

    def lambda_46E0():
        OP_99(0x107, 0x9, 0x17, 0x7D0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_46E0)
    Sleep(400)
    OP_22(0xD8, 0x0, 0x50)
    OP_22(0x82, 0x0, 0x50)
    WaitChrThread(0x107, 0x2)
    Sleep(300)
    OP_99(0x107, 0x18, 0x1B, 0x7D0)
    Sleep(500)

    ChrTalk(    #63
        0x107,
        "#068F#6P#3SSo I won't move, no matter what!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        "#052FTita...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #65
        0x8,
        (
            "#124FHeh. You're a very brave little girl.\x02\x03",

            "#121FThough I can hardly believe you care\x01",
            "that much for such a blockhead...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrPos(0x1A, -11240, 30000, -11760, 227)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x8, 0x800)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    TurnDirection(0x8, 0x107, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #66
        0x8,
        (
            "#123FIt seems you aren't the only ones who\x01",
            "wish to challenge me, so I'll take my\x01",
            "leave for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x107,
        "#064F#6PEh?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_20(0x3E8)
    Fade(500)
    OP_72(0x0, 0x4)
    SetChrPos(0x18, 12660, 0, 13410, 225)
    OP_6D(780, 0, 12430, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(332000, 0)
    OP_6E(552, 0)
    OP_0D()
    ClearChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    OP_CF(0x1B, 0x0, "Frame143_back_Null1")
    SetChrPos(0x1C, 9190, 0, 5540, 0)
    SetChrPos(0x1D, -230, 0, 4170, 0)
    PlayEffect(0x2, 0xFF, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_72(0x0, 0x20)
    PlayEffect(0x2, 0xFF, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 517)
    OP_70(0x0, 0x21C)
    OP_73(0x0)
    OP_6F(0x0, 125)
    OP_70(0x0, 0xB4)
    Sleep(1500)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x0)

    def lambda_4A3B():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A3B)

    def lambda_4A49():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4A49)

    def lambda_4A57():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4A57)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x37)
    Sleep(500)
    OP_1D(0x74)
    Sleep(500)
    OP_DB()
    Fade(500)
    OP_72(0x1, 0x4)
    OP_A1(0x1A, 0x1)
    SetChrPos(0x1A, -11240, 30000, -11760, 227)
    LoadEffect(0x4, "map\\\\mp021_00.eff")
    OP_6D(-1010, 0, -1490, 0)
    OP_67(0, 22530, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(30000, 0)
    OP_6E(523, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_43(0x1A, 0x1, 0x0, 0x15)

    def lambda_4B02():
        OP_6D(-8560, 0, -7500, 13000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4B02)

    def lambda_4B1A():
        OP_6C(315000, 13000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B1A)

    def lambda_4B2A():
        OP_6B(1890, 13000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B2A)
    Sleep(2000)
    SetMessageWindowPos(100, 75, -1, -1)
    SetChrName("General Morgan")

    AnonymousTalk(    #68 op#A op#5
        (
            "\x07\x00#163F#30AMain guns and portside guns!\x01",
            "Aim for the dragon!\x05\x02",
        )
    )

    Sleep(2000)
    SetChrName("General Morgan")

    AnonymousTalk(    #69 op#A op#5
        (
            "\x07\x00#160F#30AAll hands! Prepare to take the field\x01",
            "immediately upon landing!\x05\x02",
        )
    )

    Sleep(2500)
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(300, 250, -1, -1)
    SetChrName("Soldiers")

    AnonymousTalk(    #70 op#A op#5
        "\x07\x00#5S#30AYes, sir!\x05\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    Sleep(2000)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_4C4F():
        OP_8C(0xFE, 125, 10)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4C4F)
    Sleep(100)

    def lambda_4C62():
        OP_8C(0xFE, 125, 16)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4C62)
    Sleep(100)

    def lambda_4C75():
        OP_8C(0xFE, 125, 20)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4C75)
    Sleep(100)

    def lambda_4C88():
        OP_8C(0xFE, 125, 26)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4C88)
    Sleep(100)

    def lambda_4C9B():
        OP_8C(0xFE, 125, 30)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4C9B)
    Sleep(100)

    def lambda_4CAE():
        OP_8C(0xFE, 125, 39)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4CAE)
    Sleep(85)

    def lambda_4CC1():
        OP_8C(0xFE, 125, 40)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4CC1)
    Sleep(85)

    def lambda_4CD4():
        OP_8C(0xFE, 125, 46)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4CD4)
    Sleep(85)

    def lambda_4CE7():
        OP_8C(0xFE, 125, 50)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4CE7)
    Sleep(85)

    def lambda_4CFA():
        OP_8C(0xFE, 125, 59)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4CFA)
    Sleep(85)

    def lambda_4D0D():
        OP_8C(0xFE, 125, 60)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4D0D)
    Sleep(85)

    def lambda_4D20():
        OP_8C(0xFE, 125, 66)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4D20)
    Sleep(85)

    def lambda_4D33():
        OP_8C(0xFE, 125, 50)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4D33)
    Sleep(85)
    OP_6F(0x1, 1001)
    OP_70(0x1, 0x3FC)

    def lambda_4D54():
        OP_8C(0xFE, 125, 30)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4D54)
    Sleep(85)

    def lambda_4D67():
        OP_8C(0xFE, 125, 20)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4D67)
    Sleep(85)

    def lambda_4D7A():
        OP_8C(0xFE, 125, 14)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4D7A)
    WaitChrThread(0x1A, 0x3)
    Sleep(2000)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_23(0x79)
    OP_23(0xCC)
    OP_6D(4250, 0, 1420, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(332000, 0)
    OP_6E(321, 0)
    OP_6D(3320, 0, 260, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(321000, 0)
    OP_6E(374, 0)
    OP_0D()
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    Sleep(1000)
    OP_DC()

    ChrTalk(    #71
        0x8,
        (
            "#124F#4PHeh. They finally show their faces.\x02\x03",

            "#123FNow we can begin the final experiment.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x8, 0x0, 0x0, 0x14)
    Sleep(600)
    Fade(500)
    OP_B0(0x0, 0xA)
    OP_6D(8460, 2890, 13560, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(42000, 0)
    OP_6E(374, 0)
    OP_0D()
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #72
        0x107,
        "#065F#5PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        "#550F#5PW-Wait, you...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 315, 400)
    Sleep(500)

    ChrTalk(    #74
        0x8,
        (
            "#121F#6PDon't forget, Agate Crosner.\x02\x03",

            "So long as you continue to delude yourself,\x01",
            "you won't amount to anything.\x02\x03",

            "Nor can you protect anything you deem\x01",
            "important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        "#550F#5PTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#2PW-Waaaaait!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, -8130, 0, 9590, 90)
    SetChrPos(0xF8, -9490, 0, 10350, 90)
    SetChrPos(0xF9, -9580, 0, 8320, 90)
    SetChrSubChip(0x9, 4)
    Sleep(100)
    Fade(500)
    OP_6D(-3200, 0, 9770, 0)
    OP_67(0, 9230, -10000, 0)
    OP_6B(2170, 0)
    OP_6C(260000, 0)
    OP_6E(594, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #77
        0x101,
        (
            "#1005F#6PNow look, I stood here and listened to you\x01",
            "run your mouth for what felt like forever!\x02\x03",

            "I am SO not letting you get away after\x01",
            "all that!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    Sleep(500)

    ChrTalk(    #78
        0x8,
        (
            "#124F#2PEstelle Bright.\x01",
            "You, too, should take this to heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        (
            "#121F#2POnce this experiment ends, our plan will\x01",
            "enter its next stage.\x02\x03",

            "If you fail to keep your wits about you,\x01",
            "I guarantee you will come to regret it.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x8, 22)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_22(0xD8, 0x0, 0x64)
    OP_99(0x8, 0x0, 0x4, 0x5DC)
    Sleep(300)
    LoadEffect(0x3, "map\\\\mp015_00.eff")
    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x3, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    Fade(500)
    OP_6D(19800, 0, 12010, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(4290, 0)
    OP_6C(80000, 0)
    OP_6E(431, 0)
    OP_8C(0x8, 0, 0)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 1)
    OP_8C(0x101, 90, 0)
    OP_8C(0xF8, 90, 0)
    OP_8C(0xF9, 90, 0)
    OP_0D()
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 185)
    OP_70(0x0, 0xE1)
    Sleep(1000)
    OP_22(0x195, 0x0, 0x64)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x0)
    LoadEffect(0x0, "monster\\ms30704.eff")
    Fade(500)
    OP_6F(0x0, 225)
    OP_70(0x0, 0xF8)
    OP_B0(0x0, 0xA)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 235)
    OP_70(0x0, 0xF8)
    OP_43(0x18, 0x3, 0x0, 0xE)
    Sleep(500)
    OP_43(0x18, 0x2, 0x0, 0xF)
    Sleep(1000)

    ChrTalk(    #81
        0x101,
        "#1020F#5PHey, wait! What's that supposed to--\x02",
    )

    CloseMessageWindow()
    OP_43(0xA, 0x1, 0x0, 0x19)
    Sleep(400)
    LoadEffect(0x4, "monster\\ms30602b.eff")
    LoadEffect(0x5, "monster\\ms30602a.eff")
    LoadEffect(0x6, "map\\\\mp003_00.eff")
    LoadEffect(0x7, "scraft\\sc003_12.eff")
    Fade(500)
    OP_6D(-370, 0, 3680, 0)
    OP_67(0, 4380, -10000, 0)
    OP_6B(3560, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    Sleep(200)
    OP_43(0x11, 0x1, 0x0, 0x1B)
    Sleep(100)
    OP_43(0xD, 0x1, 0x0, 0x1C)
    Sleep(400)
    OP_43(0x12, 0x1, 0x0, 0x1D)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x1E)
    Sleep(300)
    OP_43(0x13, 0x1, 0x0, 0x1F)
    Sleep(100)
    OP_43(0xF, 0x1, 0x0, 0x20)
    Sleep(400)
    OP_43(0x14, 0x1, 0x0, 0x21)
    Sleep(100)
    OP_43(0x10, 0x1, 0x0, 0x22)
    Sleep(400)
    OP_43(0xC, 0x1, 0x0, 0x23)
    Sleep(100)
    OP_43(0x15, 0x1, 0x0, 0x1A)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #82
        0xA,
        (
            "#162F#4PCurse you, dragon! You will not flee!\x02\x03",

            "All hands, fire! FIRE! BRING IT DOWN!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x15, 0x1)
    Sleep(200)
    Fade(500)
    OP_6D(10720, 30000, 32460, 0)
    OP_67(0, 9320, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(180000, 0)
    OP_6E(306, 0)
    OP_43(0x1A, 0x0, 0x0, 0x26)
    OP_43(0xC, 0x1, 0x0, 0x25)
    OP_43(0x1A, 0x1, 0x0, 0x27)
    OP_43(0x11, 0x1, 0x0, 0x24)
    Sleep(100)
    OP_43(0xD, 0x1, 0x0, 0x24)
    OP_43(0x12, 0x1, 0x0, 0x24)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x25)
    OP_43(0x14, 0x1, 0x0, 0x24)
    Sleep(100)
    OP_43(0xF, 0x1, 0x0, 0x24)
    OP_43(0x13, 0x1, 0x0, 0x24)
    Sleep(100)
    OP_43(0x10, 0x1, 0x0, 0x25)
    OP_43(0x15, 0x1, 0x0, 0x24)
    Sleep(2000)

    ChrTalk(    #83
        0x8,
        (
            "#123F#6PHeh. As if your cannons can do anything\x01",
            "against a legend.\x02\x03",

            "#124FLet us go...Ragnard the Ancient.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_DB()

    def lambda_5678():
        OP_6D(14000, 17250, 12870, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5678)

    def lambda_5690():
        OP_67(0, 8180, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5690)

    def lambda_56A8():
        OP_6B(4220, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_56A8)

    def lambda_56B8():
        OP_6C(200000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_56B8)

    def lambda_56C8():
        OP_6E(426, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_56C8)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 200)
    OP_70(0x0, 0x113)
    OP_44(0x18, 0x3)
    OP_23(0x1F7)
    OP_22(0x195, 0x0, 0x64)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x0)
    OP_43(0x18, 0x3, 0x0, 0xE)

    def lambda_572F():
        OP_6B(4800, 5000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_572F)

    def lambda_573F():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_573F)
    OP_6F(0x0, 545)
    OP_70(0x0, 0x234)
    PlayEffect(0x0, 0xFF, 0x18, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 565)
    OP_70(0x0, 0x249)
    OP_43(0x18, 0x2, 0x0, 0xF)

    def lambda_57BA():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_57BA)
    Sleep(300)
    OP_44(0x18, 0x2)

    def lambda_57DE():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_57DE)
    Sleep(100)

    def lambda_57FE():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_57FE)
    Sleep(100)

    def lambda_581E():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_581E)
    Sleep(100)

    def lambda_583E():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_583E)
    Sleep(100)

    def lambda_585E():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_585E)
    Sleep(100)

    def lambda_587E():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_587E)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_311E end

    def Function_14_58B6(): pass

    label("Function_14_58B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58CC")
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    Jump("Function_14_58B6")

    label("loc_58CC")

    Return()

    # Function_14_58B6 end

    def Function_15_58CD(): pass

    label("Function_15_58CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5913")
    PlayEffect(0x0, 0xFF, 0x18, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1300)
    Jump("Function_15_58CD")

    label("loc_5913")

    Return()

    # Function_15_58CD end

    def Function_16_5914(): pass

    label("Function_16_5914")

    SetChrChipByIndex(0xFE, 25)
    OP_8F(0xFE, 0x1108, 0x0, 0x2C6, 0x2BC, 0x0)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_16_5914 end

    def Function_17_5938(): pass

    label("Function_17_5938")

    SetChrChipByIndex(0xFE, 65535)
    OP_96(0xFE, 0xFFFFDC38, 0x0, 0x20D0, 0x1F4, 0x1388)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_17_5938 end

    def Function_18_5966(): pass

    label("Function_18_5966")

    SetChrChipByIndex(0xFE, 65535)
    OP_96(0xFE, 0xFFFFDC6A, 0x0, 0x2620, 0x1F4, 0x1388)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_18_5966 end

    def Function_19_5994(): pass

    label("Function_19_5994")

    SetChrChipByIndex(0xFE, 65535)
    OP_96(0xFE, 0xFFFFD508, 0x0, 0x2238, 0x1F4, 0x1388)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_19_5994 end

    def Function_20_59C2(): pass

    label("Function_20_59C2")

    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0)
    OP_8C(0xFE, 0, 500)
    SetChrChipByIndex(0xFE, 28)
    SetChrSubChip(0xFE, 1)
    Sleep(100)
    SetChrSubChip(0xFE, 2)
    SetChrFlags(0xFE, 0x4)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_59FF():
        OP_96(0xFE, 0x1FE0, 0x206C, 0x3566, 0x2328, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_59FF)
    WaitChrThread(0x8, 0x3)
    ClearChrFlags(0x8, 0x1)
    OP_8C(0xFE, 90, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_CF(0x8, 0x0, "Frame143_back_Null1")
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x4)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0xFE, 1)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_20_59C2 end

    def Function_21_5A79(): pass

    label("Function_21_5A79")


    def lambda_5A7F():
        OP_8F(0xFE, 0xFFFFD418, 0x0, 0xFFFFD210, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_5A7F)
    Sleep(6000)

    def lambda_5A9F():
        OP_8F(0xFE, 0xFFFFD418, 0x0, 0xFFFFD210, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_5A9F)
    Sleep(3000)

    def lambda_5ABF():
        OP_8F(0xFE, 0xFFFFD418, 0x0, 0xFFFFD210, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_5ABF)
    Sleep(2000)

    def lambda_5ADF():
        OP_8F(0xFE, 0xFFFFD418, 0x0, 0xFFFFD210, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_5ADF)
    PlayEffect(0x4, 0x1, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x1, 0x64)
    Return()

    # Function_21_5A79 end

    def Function_22_5B2F(): pass

    label("Function_22_5B2F")

    OP_8E(0xFE, 0xFFFFE656, 0x0, 0x2CE2, 0x1770, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_22_5B2F end

    def Function_23_5B4B(): pass

    label("Function_23_5B4B")

    OP_8E(0xFE, 0xFFFFDFA8, 0x0, 0x2DF0, 0x1770, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_23_5B4B end

    def Function_24_5B67(): pass

    label("Function_24_5B67")

    OP_8E(0xFE, 0xFFFFE35E, 0x0, 0x26B6, 0x1770, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_24_5B67 end

    def Function_25_5B83(): pass

    label("Function_25_5B83")

    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF6D2, 0x0, 0xA50, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_25_5B83 end

    def Function_26_5BBA(): pass

    label("Function_26_5BBA")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFEB2E, 0x0, 0xFFFFFEDE, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_26_5BBA end

    def Function_27_5C05(): pass

    label("Function_27_5C05")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFEB38, 0x0, 0x11BC, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_27_5C05 end

    def Function_28_5C50(): pass

    label("Function_28_5C50")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFD8A, 0x0, 0xFFFFFA4C, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_28_5C50 end

    def Function_29_5C9B(): pass

    label("Function_29_5C9B")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFC90, 0x0, 0x37A, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_29_5C9B end

    def Function_30_5CE6(): pass

    label("Function_30_5CE6")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFE142, 0x0, 0x139C, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_30_5CE6 end

    def Function_31_5D31(): pass

    label("Function_31_5D31")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF344, 0x0, 0x136, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_31_5D31 end

    def Function_32_5D7C(): pass

    label("Function_32_5D7C")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFE9DA, 0x0, 0xAA0, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_32_5D7C end

    def Function_33_5DC7(): pass

    label("Function_33_5DC7")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF1F0, 0x0, 0xFFFFF880, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_33_5DC7 end

    def Function_34_5E12(): pass

    label("Function_34_5E12")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFDE68, 0x0, 0xAF0, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_34_5E12 end

    def Function_35_5E5D(): pass

    label("Function_35_5E5D")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFE4BC, 0x0, 0x550, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_35_5E5D end

    def Function_36_5EA8(): pass

    label("Function_36_5EA8")

    SetChrChipByIndex(0xFE, 20)

    label("loc_5EAD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F57")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EEE")
    Sleep(500)
    Jump("loc_5F54")

    label("loc_5EEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F03")
    Sleep(600)
    Jump("loc_5F54")

    label("loc_5F03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F18")
    Sleep(700)
    Jump("loc_5F54")

    label("loc_5F18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F2D")
    Sleep(800)
    Jump("loc_5F54")

    label("loc_5F2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F42")
    Sleep(900)
    Jump("loc_5F54")

    label("loc_5F42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F54")
    Sleep(1000)

    label("loc_5F54")

    Jump("loc_5EAD")

    label("loc_5F57")

    Return()

    # Function_36_5EA8 end

    def Function_37_5F58(): pass

    label("Function_37_5F58")

    SetChrChipByIndex(0xFE, 20)

    label("loc_5F5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6306")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FD8")
    PlayEffect(0x6, 0xFF, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("loc_6303")

    label("loc_5FD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6022")
    PlayEffect(0x6, 0xFF, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jump("loc_6303")

    label("loc_6022")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_606C")
    PlayEffect(0x6, 0xFF, 0x1E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Jump("loc_6303")

    label("loc_606C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60B6")
    PlayEffect(0x6, 0xFF, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    Jump("loc_6303")

    label("loc_60B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6100")
    PlayEffect(0x6, 0xFF, 0x20, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("loc_6303")

    label("loc_6100")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_614A")
    PlayEffect(0x6, 0xFF, 0x21, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_6303")

    label("loc_614A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6194")
    PlayEffect(0x6, 0xFF, 0x22, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jump("loc_6303")

    label("loc_6194")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61DE")
    PlayEffect(0x6, 0xFF, 0x23, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Jump("loc_6303")

    label("loc_61DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6228")
    PlayEffect(0x6, 0xFF, 0x24, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    Jump("loc_6303")

    label("loc_6228")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6272")
    PlayEffect(0x6, 0xFF, 0x25, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("loc_6303")

    label("loc_6272")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62BC")
    PlayEffect(0x6, 0xFF, 0x26, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_6303")

    label("loc_62BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6303")
    PlayEffect(0x6, 0xFF, 0x27, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)

    label("loc_6303")

    Jump("loc_5F5D")

    label("loc_6306")

    Return()

    # Function_37_5F58 end

    def Function_38_6307(): pass

    label("Function_38_6307")

    SetChrPos(0x28, -2890, 4570, -13910, 45)

    label("loc_6318")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66B2")
    Sleep(500)
    PlayEffect(0x5, 0xFF, 0x28, 0, 0, 0, -21, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x3E0, 0x0, 0x64)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63B6")
    PlayEffect(0x4, 0xFF, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_66AA")

    label("loc_63B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63FB")
    PlayEffect(0x4, 0xFF, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_66AA")

    label("loc_63FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6440")
    PlayEffect(0x4, 0xFF, 0x1E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_66AA")

    label("loc_6440")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6485")
    PlayEffect(0x4, 0xFF, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_66AA")

    label("loc_6485")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64CA")
    PlayEffect(0x4, 0xFF, 0x20, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_66AA")

    label("loc_64CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_650F")
    PlayEffect(0x4, 0xFF, 0x21, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_66AA")

    label("loc_650F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6554")
    PlayEffect(0x4, 0xFF, 0x22, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_66AA")

    label("loc_6554")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6599")
    PlayEffect(0x4, 0xFF, 0x23, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_66AA")

    label("loc_6599")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65DE")
    PlayEffect(0x4, 0xFF, 0x24, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_66AA")

    label("loc_65DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6623")
    PlayEffect(0x4, 0xFF, 0x25, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_66AA")

    label("loc_6623")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6668")
    PlayEffect(0x4, 0xFF, 0x26, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_66AA")

    label("loc_6668")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66AA")
    PlayEffect(0x4, 0xFF, 0x27, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_66AA")

    Sleep(10000)
    Jump("loc_6318")

    label("loc_66B2")

    Return()

    # Function_38_6307 end

    def Function_39_66B3(): pass

    label("Function_39_66B3")

    SetChrPos(0x1C, -1050, 0, 10880, 0)
    SetChrPos(0x1D, 610, 0, 13410, 0)
    SetChrPos(0x1E, 230, 0, 7550, 0)
    SetChrPos(0x1F, 7300, 0, 7640, 0)
    SetChrPos(0x20, 9270, 0, 5590, 0)
    SetChrPos(0x21, 11970, 0, 7410, 0)
    SetChrPos(0x22, 9780, 0, 8530, 0)
    SetChrPos(0x23, -1300, 0, 16110, 0)
    SetChrPos(0x24, 8280, 0, 5580, 0)
    SetChrPos(0x25, 11320, 0, 4310, 0)
    SetChrPos(0x26, 13890, 0, 5860, 0)
    SetChrPos(0x27, 6890, 0, 9970, 0)

    label("loc_677F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E01")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x7, 0x1, 0xFF, -8950, 6000, -6300, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x7, 0x2, 0xFF, -8950, 6000, -6300, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6887")
    PlayEffect(0x2, 0xFF, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6DF9")

    label("loc_6887")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6906")
    PlayEffect(0x2, 0xFF, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x21, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6DF9")

    label("loc_6906")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6985")
    PlayEffect(0x2, 0xFF, 0x1E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x23, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6DF9")

    label("loc_6985")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A04")
    PlayEffect(0x2, 0xFF, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x25, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6DF9")

    label("loc_6A04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A83")
    PlayEffect(0x2, 0xFF, 0x20, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x27, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6DF9")

    label("loc_6A83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B02")
    PlayEffect(0x2, 0xFF, 0x21, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6DF9")

    label("loc_6B02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B81")
    PlayEffect(0x2, 0xFF, 0x22, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x1E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6DF9")

    label("loc_6B81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C00")
    PlayEffect(0x2, 0xFF, 0x23, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x20, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6DF9")

    label("loc_6C00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C7F")
    PlayEffect(0x2, 0xFF, 0x24, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x22, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6DF9")

    label("loc_6C7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CFE")
    PlayEffect(0x2, 0xFF, 0x25, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x24, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6DF9")

    label("loc_6CFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D7D")
    PlayEffect(0x2, 0xFF, 0x26, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6DF9")

    label("loc_6D7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DF9")
    PlayEffect(0x2, 0xFF, 0x27, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x26, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_6DF9")

    Sleep(2000)
    Jump("loc_677F")

    label("loc_6E01")

    Return()

    # Function_39_66B3 end

    def Function_40_6E02(): pass

    label("Function_40_6E02")

    SetChrPos(0xFE, 3990, 800, -760, 180)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)

    def lambda_6E32():
        OP_96(0xFE, 0x1554, 0xFFFFFE0C, 0xFFFFF8F8, 0xFA0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E32)

    def lambda_6E50():

        label("loc_6E50")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_6E50")

    QueueWorkItem2(0xFE, 2, lambda_6E50)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x2)
    OP_22(0x124, 0x0, 0x50)
    SetChrSubChip(0xFE, 5)
    Return()

    # Function_40_6E02 end

    def Function_41_6E71(): pass

    label("Function_41_6E71")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E84")
    Call(0, 52)

    label("loc_6E84")

    OP_6D(-20380, 0, 2110, 0)
    OP_67(0, 5350, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(257000, 0)
    OP_6E(660, 0)
    SetChrFlags(0x107, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0xF8, 0x80)
    ClearChrFlags(0xF9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xF8, -3000, 0, -4670, 225)
    SetChrPos(0x101, -4070, 0, -3070, 225)
    SetChrPos(0xF9, -2360, 0, -2940, 225)
    SetChrPos(0xA, -5010, 0, -5490, 45)
    SetChrPos(0xB, -5010, 0, -7780, 45)
    OP_72(0x1, 0x4)
    OP_6F(0x1, 200)

    def lambda_6F46():
        OP_6D(-10260, 0, -7880, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F46)

    def lambda_6F5E():
        OP_67(0, 5350, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6F5E)

    def lambda_6F76():
        OP_6C(257000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6F76)
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0x1A, 0x1)
    SetChrPos(0x1A, -11240, 0, -11760, 127)
    SetChrFlags(0x1A, 0x1)
    ClearChrFlags(0x1A, 0x80)
    OP_51(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1500, 0)
    OP_43(0xC, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0xD, 0x1, 0x0, 0x2B)
    Sleep(800)
    FadeToBright(2000, 0)
    OP_43(0xA, 0x3, 0x0, 0x2A)
    Sleep(500)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #84
        0x101,
        (
            "#1020F#2PW-Waaaaaaaaaait!\x01",
            "Why aren't we chasing him?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(-3640, 0, -5570, 0)
    OP_67(0, 4390, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(176000, 0)
    OP_6E(310, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #85
        0x101,
        (
            "#1005F#6PWhat're you doing?!\x02\x03",

            "Does this have something to do with your\x01",
            "stupid bracer grudge?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xA,
        (
            "#160FNot in the slightest.\x02\x03",

            "That monster wasn't even scratched by\x01",
            "rounds from a combat vessel.\x02\x03",

            "What do you intend to do that cannons\x01",
            "cannot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#1026F#6PW-Well...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72D0")

    ChrTalk(    #88
        0x105,
        "#043FGeneral!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "#163FEven to you, Your Highness, I shall not\x01",
            "yield this point.\x02\x03",

            "#160FCourage and recklessness are different things.\x02\x03",

            "Your Highness, I'm sure you saw the damage\x01",
            "to Bose and Ravennue.\x02\x03",

            "This has, in essence, become a war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x105,
        "#049FA war...? Yes... You're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7381")

    label("loc_72D0")


    ChrTalk(    #91
        0xA,
        (
            "#163FCourage and recklessness are different things.\x02\x03",

            "#160FI'm sure you all saw the damage to Bose\x01",
            "and Ravennue.\x02\x03",

            "This has, in essence, become a war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1003F#6PA war...\x02",
    )

    CloseMessageWindow()

    label("loc_7381")


    ChrTalk(    #93
        0xA,
        (
            "#163FLeave the bread to the bakers,\x01",
            "Miss Bright.\x02\x03",

            "If this is a war, the professionals will\x01",
            "handle it.\x02\x03",

            "#161FAnd if you want my advice, you're\x01",
            "better off searching for Ouroboros'\x01",
            "center of command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1005F#6PB-But!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, -10540, 0, -390, 135)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #95
        0x9,
        "Young Man's Voice",
        "#1P...'re kiddin'...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74FC")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_753A")

    label("loc_74FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7523")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_753A")

    label("loc_7523")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_753A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7561")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_759F")

    label("loc_7561")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7588")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_759F")

    label("loc_7588")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_759F")

    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_75C6():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75C6)

    def lambda_75D4():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_75D4)
    Sleep(50)

    def lambda_75E7():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_75E7)

    def lambda_75F5():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_75F5)
    Sleep(50)

    def lambda_7608():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7608)

    def lambda_7616():

        label("loc_7616")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_7616")

    QueueWorkItem2(0x101, 2, lambda_7616)

    def lambda_7627():

        label("loc_7627")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_7627")

    QueueWorkItem2(0xF8, 2, lambda_7627)

    def lambda_7638():

        label("loc_7638")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_7638")

    QueueWorkItem2(0xF9, 2, lambda_7638)

    def lambda_7649():

        label("loc_7649")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_7649")

    QueueWorkItem2(0xA, 2, lambda_7649)

    def lambda_765A():

        label("loc_765A")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_765A")

    QueueWorkItem2(0xB, 2, lambda_765A)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrFlags(0x9, 0x20)
    OP_43(0x9, 0x0, 0x0, 0x30)
    OP_6D(-4720, 0, -5400, 4000)

    ChrTalk(    #96
        0x101,
        "#1004F#6PAgate?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x0)
    SetChrPos(0x107, -11980, 0, 4770, 135)
    ClearChrFlags(0x107, 0x80)

    ChrTalk(    #97
        0x107,
        "#1PA-Agate!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x107, 0xFFFFE944, 0x0, 0xFFFFF100, 0x1388, 0x0)
    TurnDirection(0x107, 0x9, 400)

    def lambda_7715():

        label("loc_7715")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_7715")

    QueueWorkItem2(0x107, 2, lambda_7715)

    ChrTalk(    #98
        0x107,
        (
            "#065F#6PTake it easy, okay?\x01",
            "I just finished patching you up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        "#1286F#4P...\x02",
    )

    CloseMessageWindow()
    OP_44(0xB, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0x2)
    OP_44(0x107, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)
    OP_44(0xA, 0x2)
    OP_44(0xB, 0x2)

    ChrTalk(    #100
        0xA,
        (
            "#160F#6PYou are the Heavy Blade, Agate,\x01",
            "yes?\x02\x03",

            "Cassius tells me you're quite an active\x01",
            "young bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "#1282F#4PDon't care what the old man said.\x02\x03",

            "#1293FGeneral. Listen.\x02\x03",

            "Leave the bread to the bakers...\x01",
            "War to the professionals?\x02\x03",

            "You seriously sayin' that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "#163F#6POf course I'm serious.\x02\x03",

            "#160FUnlike bracers who exist only to protect\x01",
            "private citizens, we must protect the country\x01",
            "as a whole.\x02\x03",

            "We must protect Liberl's soil and those who\x01",
            "live upon it.\x02\x03",

            "The army is the only instrument that ca--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        (
            "#1291F#4PKheh. 'Protect Liberl's soil and those\x01",
            "who live upon it,' huh?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)

    def lambda_79E9():

        label("loc_79E9")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_79E9")

    QueueWorkItem2(0x107, 1, lambda_79E9)

    def lambda_79FA():
        OP_6D(-4580, 0, -6170, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_79FA)

    def lambda_7A12():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7A12)
    OP_92(0x9, 0xA, 0x258, 0x5DC, 0x0)
    OP_44(0x9, 0x1)
    Fade(250)
    OP_6B(3000, 0)

    def lambda_7A42():

        label("loc_7A42")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_7A42")

    QueueWorkItem2(0xB, 2, lambda_7A42)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 30)
    SetChrSubChip(0xA, 6)
    SetChrChipByIndex(0x9, 30)
    SetChrSubChip(0x9, 30)
    OP_0D()
    Sleep(500)

    ChrTalk(    #104
        0x9,
        "#1287F#4P#4SDON'T MAKE ME LAUGH!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #105
        0xA,
        "#163F#6PGrgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1020F#6PWh-Whoaaaa! Agate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x107,
        "#065F#7PAgate, calm down, please!\x02",
    )

    CloseMessageWindow()
    OP_43(0x9, 0x0, 0x0, 0x33)
    Sleep(500)

    ChrTalk(    #108
        0x9,
        (
            "#1287F#4PYou're ALWAYS! ALWAYS! TOO LATE!\x02\x03",

            "You idiots move like slugs!\x01",
            "You just worry about keeping everyone in step!\x02\x03",

            "You can't do SHIT without 'orders'! You can't\x01",
            "even protect the things you say you will!\x02\x03",

            "You can't do it now,\x01",
            "AND YOU DIDN'T DO IT TEN YEARS AGO!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0x0)

    ChrTalk(    #109
        0xA,
        (
            "#161F#6PNgh...!\x02\x03",

            "Are you...? I wonder...\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x9, 0x0, 0x0, 0x33)

    ChrTalk(    #110
        0x9,
        (
            "#1287F#4PWho... Who the hell could leave it to you...?\x02\x03",

            "#1285FThis time...gotta protect...\x02\x03",

            "Gotta...protect Mischa...myself...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0x0)
    Sleep(500)

    def lambda_7D1C():
        OP_6D(-4820, 0, -5480, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D1C)

    def lambda_7D34():
        OP_67(0, 6660, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7D34)

    def lambda_7D4C():
        OP_6B(3010, 1500)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_7D4C)

    def lambda_7D5C():
        OP_6E(280, 1500)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_7D5C)
    SetChrFlags(0x9, 0x800)

    def lambda_7D71():
        OP_94(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7D71)

    def lambda_7D87():
        OP_99(0xFE, 0xA, 0xF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7D87)

    def lambda_7D97():
        OP_94(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7D97)

    def lambda_7DAD():
        OP_99(0xFE, 0x22, 0x27, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7DAD)
    Sleep(500)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #111
        0x107,
        "#065F#5PAGATE!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1020F#5PIs he okay?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xA)
    Sleep(500)

    ChrTalk(    #113
        0xA,
        (
            "#163F#6PHe doesn't seem to have\x01",
            "reopened his wounds.\x02\x03",

            "He's simply exhausted.\x01",
            "Physically and mentally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x107,
        "#063F#5POh, Agate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#1007F#5PHe was making an even bigger\x01",
            "fuss than usual...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xA, 0xF, 0x11, 0x3E8)
    Sleep(500)

    ChrTalk(    #116
        0xA,
        (
            "#160F#6PFor now, he needs rest in his own bed.\x02\x03",

            "His home is in Ravennue.\x01",
            "My ship can take him that far, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1015F#5PAh, thank you.\x02\x03",

            "...\x02\x03",

            "#1004FWait a minute, how do you know Agate's\x01",
            "house is in Ravennue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        (
            "#160F#6PI remembered that I...met him,\x01",
            "once before.\x02\x03",

            "The little boy from that day has\x01",
            "grown quite a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#1026F#5PWhat day?\x02",
    )

    CloseMessageWindow()
    OP_99(0xA, 0x11, 0x13, 0x3E8)
    Sleep(500)

    ChrTalk(    #120
        0xA,
        (
            "#163F#6PIt was immediately after the\x01",
            "Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xA, 0x14, 0x17, 0x3E8)
    Sleep(500)

    ChrTalk(    #121
        0xA,
        (
            "#166F#6PThe day the memorial to his sister and\x01",
            "the other villagers was erected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x107,
        "#065F#5P*gasp*\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 1)), scpexpr(EXPR_END)), "loc_814C")

    ChrTalk(    #123
        0x101,
        "#1020F#5P*gasp*\x02",
    )

    CloseMessageWindow()
    Jump("loc_8166")

    label("loc_814C")


    ChrTalk(    #124
        0x101,
        "#1020F#5PWh-Whaaat?!\x02",
    )

    CloseMessageWindow()

    label("loc_8166")

    FadeToDark(2000, 0, -1)
    OP_0D()
    RemoveParty(0x6, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_818B")
    RemoveParty(0x2, 0xFF)
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_81CD")

    label("loc_818B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81A2")
    RemoveParty(0x3, 0xFF)
    AddParty(0x3, 0xF7, 0xFF)
    Jump("loc_81CD")

    label("loc_81A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81B9")
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xF7, 0xFF)
    Jump("loc_81CD")

    label("loc_81B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81CD")
    RemoveParty(0x7, 0xFF)
    AddParty(0x7, 0xF7, 0xFF)

    label("loc_81CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81E4")
    RemoveParty(0x2, 0xFF)
    AddParty(0x2, 0xF8, 0xFF)
    Jump("loc_8226")

    label("loc_81E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81FB")
    RemoveParty(0x3, 0xFF)
    AddParty(0x3, 0xF8, 0xFF)
    Jump("loc_8226")

    label("loc_81FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8212")
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xF8, 0xFF)
    Jump("loc_8226")

    label("loc_8212")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8226")
    RemoveParty(0x7, 0xFF)
    AddParty(0x7, 0xF8, 0xFF)

    label("loc_8226")

    OP_A2(0x1A83)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1201   ._SN", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_41_6E71 end

    def Function_42_8236(): pass

    label("Function_42_8236")

    OP_43(0xE, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0xF, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0x10, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0x11, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0x12, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0x13, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0x14, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0x15, 0x1, 0x0, 0x2B)
    Return()

    # Function_42_8236 end

    def Function_43_8292(): pass

    label("Function_43_8292")

    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, 6580, 0, -8930, 180)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF88A, 0x0, 0xFFFFB5B4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDF6C, 0x514, 0xFFFFCA90, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_43_8292 end

    def Function_44_82EA(): pass

    label("Function_44_82EA")

    OP_8F(0xFE, 0xFFFFEA34, 0x0, 0xFFFFEF7A, 0xFA0, 0x0)
    Return()

    # Function_44_82EA end

    def Function_45_82FF(): pass

    label("Function_45_82FF")

    OP_8F(0xFE, 0xFFFFF254, 0x0, 0xFFFFEE8A, 0xFA0, 0x0)
    TurnDirection(0xFE, 0xA, 400)
    Return()

    # Function_45_82FF end

    def Function_46_831B(): pass

    label("Function_46_831B")

    OP_8E(0xFE, 0xFFFFF1A0, 0x0, 0xFFFFF4F2, 0xFA0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_46_831B end

    def Function_47_8337(): pass

    label("Function_47_8337")

    OP_8E(0xFE, 0xFFFFF682, 0x0, 0xFFFFF06A, 0xFA0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_47_8337 end

    def Function_48_8353(): pass

    label("Function_48_8353")

    SetChrPos(0xFE, -10540, 0, -390, 135)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 8)

    def lambda_837E():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_837E)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x1)
    Sleep(500)

    def lambda_83A2():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83A2)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x1)
    Sleep(500)

    def lambda_83C6():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83C6)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x1)
    Sleep(500)

    def lambda_83EA():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83EA)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x1)
    Sleep(500)

    def lambda_840E():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_840E)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x1)
    Sleep(500)

    def lambda_8432():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8432)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x1)
    Return()

    # Function_48_8353 end

    def Function_49_844C(): pass

    label("Function_49_844C")


    def lambda_8452():
        OP_99(0xFE, 0x8, 0xF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8452)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x1)
    Sleep(500)

    def lambda_8476():
        OP_99(0xFE, 0x8, 0xF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8476)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x1)
    Return()

    # Function_49_844C end

    def Function_50_8490(): pass

    label("Function_50_8490")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 8)

    def lambda_84AA():

        label("loc_84AA")

        OP_99(0xFE, 0x8, 0xF, 0x3E8)
        OP_48()
        Jump("loc_84AA")

    QueueWorkItem2(0xFE, 1, lambda_84AA)
    OP_8F(0x9, 0xFFFFEAE8, 0x0, 0xFFFFEB9C, 0x3E8, 0x0)
    OP_44(0xFE, 0x1)
    SetChrSubChip(0xFE, 8)
    Return()

    # Function_50_8490 end

    def Function_51_84D5(): pass

    label("Function_51_84D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8568")
    SetChrSubChip(0xA, 7)
    SetChrSubChip(0x9, 31)
    Sleep(100)
    SetChrSubChip(0xA, 8)
    SetChrSubChip(0x9, 32)
    Sleep(100)
    SetChrSubChip(0xA, 9)
    SetChrSubChip(0x9, 33)
    Sleep(100)
    SetChrSubChip(0xA, 7)
    SetChrSubChip(0x9, 31)
    Sleep(100)
    SetChrSubChip(0xA, 8)
    SetChrSubChip(0x9, 32)
    Sleep(100)
    SetChrSubChip(0xA, 9)
    SetChrSubChip(0x9, 33)
    Sleep(100)
    SetChrSubChip(0xA, 7)
    SetChrSubChip(0x9, 31)
    Sleep(100)
    SetChrSubChip(0xA, 8)
    SetChrSubChip(0x9, 32)
    Sleep(100)
    SetChrSubChip(0xA, 9)
    SetChrSubChip(0x9, 33)
    Sleep(500)
    Jump("Function_51_84D5")

    label("loc_8568")

    Return()

    # Function_51_84D5 end

    def Function_52_8569(): pass

    label("Function_52_8569")

    FadeToDark(0, 0, -1)
    OP_6D(-41010, -360, 62470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_861F"),
        (1, "loc_8625"),
        (SWITCH_DEFAULT, "loc_862B"),
    )


    label("loc_861F")

    OP_A2(0x1200)
    Jump("loc_862B")

    label("loc_8625")

    OP_A2(0x1201)
    Jump("loc_862B")

    label("loc_862B")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x6, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_52_8569 end

    SaveToFile()

Try(main)
