from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5400   ._SN',
        MapName             = 'Other',
        Location            = 'C5400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '约修亚',                               # 9
        '约修亚',                               # 10
        '约修亚',                               # 11
        '歼灭天使玲',                           # 12
        '强化猎兵',                             # 13
        '强化猎兵',                             # 14
        '剑帝莱维',                             # 15
        '多伦',                                 # 16
        '吉尔',                                 # 17
        '空贼雷古',                             # 18
        '空贼阿伦',                             # 19
        '空贼莱尔',                             # 20
        '空贼罗尔',                             # 21
        '空贼',                                 # 22
        '空贼',                                 # 23
        '哨兵570（蓝）',                        # 24
        '哨兵235（红）',                        # 25
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
        'ED6_DT07/CH00010 ._CH',             # 00
        'ED6_DT27/CH03001 ._CH',             # 01
        'ED6_DT26/CH20380 ._CH',             # 02
        'ED6_DT27/CH03005 ._CH',             # 03
        'ED6_DT26/CH20235 ._CH',             # 04
        'ED6_DT26/CH20376 ._CH',             # 05
        'ED6_DT27/CH03510 ._CH',             # 06
        'ED6_DT27/CH03000 ._CH',             # 07
        'ED6_DT27/CH04620 ._CH',             # 08
        'ED6_DT27/CH03003 ._CH',             # 09
        'ED6_DT07/CH02040 ._CH',             # 0A
        'ED6_DT27/CH04621 ._CH',             # 0B
        'ED6_DT27/CH04622 ._CH',             # 0C
        'ED6_DT27/CH04623 ._CH',             # 0D
        'ED6_DT26/CH20384 ._CH',             # 0E
        'ED6_DT27/CH04624 ._CH',             # 0F
        'ED6_DT26/CH20237 ._CH',             # 10
        'ED6_DT27/CH04001 ._CH',             # 11
        'ED6_DT26/CH20501 ._CH',             # 12
        'ED6_DT27/CH04002 ._CH',             # 13
        'ED6_DT26/CH20381 ._CH',             # 14
        'ED6_DT27/CH04000 ._CH',             # 15
        'ED6_DT07/CH00343 ._CH',             # 16
        'ED6_DT07/CH00341 ._CH',             # 17
        'ED6_DT07/CH00344 ._CH',             # 18
        'ED6_DT29/CH12570 ._CH',             # 19
        'ED6_DT29/CH12571 ._CH',             # 1A
        'ED6_DT29/CH12350 ._CH',             # 1B
        'ED6_DT29/CH12351 ._CH',             # 1C
        'ED6_DT07/CH02110 ._CH',             # 1D
        'ED6_DT07/CH02120 ._CH',             # 1E
        'ED6_DT07/CH01380 ._CH',             # 1F
        'ED6_DT26/CH20208 ._CH',             # 20
    )

    AddCharChipPat(
        'ED6_DT07/CH00010P._CP',             # 00
        'ED6_DT27/CH03001P._CP',             # 01
        'ED6_DT26/CH20380P._CP',             # 02
        'ED6_DT27/CH03005P._CP',             # 03
        'ED6_DT26/CH20235P._CP',             # 04
        'ED6_DT26/CH20376P._CP',             # 05
        'ED6_DT27/CH03510P._CP',             # 06
        'ED6_DT27/CH03000P._CP',             # 07
        'ED6_DT27/CH04620P._CP',             # 08
        'ED6_DT27/CH03003P._CP',             # 09
        'ED6_DT07/CH02040P._CP',             # 0A
        'ED6_DT27/CH04621P._CP',             # 0B
        'ED6_DT27/CH04622P._CP',             # 0C
        'ED6_DT27/CH04623P._CP',             # 0D
        'ED6_DT26/CH20384P._CP',             # 0E
        'ED6_DT27/CH04624P._CP',             # 0F
        'ED6_DT26/CH20237P._CP',             # 10
        'ED6_DT27/CH04001P._CP',             # 11
        'ED6_DT26/CH20501P._CP',             # 12
        'ED6_DT27/CH04002P._CP',             # 13
        'ED6_DT26/CH20381P._CP',             # 14
        'ED6_DT27/CH04000P._CP',             # 15
        'ED6_DT07/CH00343P._CP',             # 16
        'ED6_DT07/CH00341P._CP',             # 17
        'ED6_DT07/CH00344P._CP',             # 18
        'ED6_DT29/CH12570P._CP',             # 19
        'ED6_DT29/CH12571P._CP',             # 1A
        'ED6_DT29/CH12350P._CP',             # 1B
        'ED6_DT29/CH12351P._CP',             # 1C
        'ED6_DT07/CH02110P._CP',             # 1D
        'ED6_DT07/CH02120P._CP',             # 1E
        'ED6_DT07/CH01380P._CP',             # 1F
        'ED6_DT26/CH20208P._CP',             # 20
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
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
        Unknown3            = 32,
        ChipIndex           = 0x20,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -134110,
        Z                   = 0,
        Y                   = 45880,
        Unknown_0C          = 0,
        Unknown_0E          = 25,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -135340,
        Z                   = 0,
        Y                   = -27900,
        Unknown_0C          = 0,
        Unknown_0E          = 27,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 2850,
        Y                   = 0,
        Z                   = 22850,
        Range               = 5160,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x6112,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )

    DeclEvent(
        X                   = -52950,
        Y                   = 0,
        Z                   = -61000,
        Range               = -51020,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF1730,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = -42980,
        Y                   = -1000,
        Z                   = 75190,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 55,
    )

    DeclEvent(
        X                   = -36920,
        Y                   = -1000,
        Z                   = -67150,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 56,
    )

    DeclEvent(
        X                   = 70070,
        Y                   = -1000,
        Z                   = -234030,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 57,
    )

    DeclEvent(
        X                   = -90500,
        Y                   = 0,
        Z                   = -343710,
        Range               = -85100,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFAC61C,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )


    DeclActor(
        TriggerX            = -131900,
        TriggerZ            = 0,
        TriggerY            = 10590,
        TriggerRange        = 1000,
        ActorX              = -131900,
        ActorZ              = 0,
        ActorY              = 11210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -87000,
        TriggerZ            = 0,
        TriggerY            = -342900,
        TriggerRange        = 1000,
        ActorX              = -87000,
        ActorZ              = 1000,
        ActorY              = -343080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -127350,
        TriggerZ            = 0,
        TriggerY            = -58920,
        TriggerRange        = 1000,
        ActorX              = -126610,
        ActorZ              = 0,
        ActorY              = -58850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 37,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -37010,
        TriggerZ            = 0,
        TriggerY            = -67050,
        TriggerRange        = 1000,
        ActorX              = -37010,
        ActorZ              = 1200,
        ActorY              = -67050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 43,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 61080,
        TriggerZ            = 0,
        TriggerY            = -184550,
        TriggerRange        = 1000,
        ActorX              = 61080,
        ActorZ              = 1000,
        ActorY              = -184550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 61000,
        TriggerZ            = 0,
        TriggerY            = -27060,
        TriggerRange        = 1000,
        ActorX              = 61000,
        ActorZ              = 1000,
        ActorY              = -27060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 52900,
        TriggerZ            = 0,
        TriggerY            = -53160,
        TriggerRange        = 1000,
        ActorX              = 52880,
        ActorZ              = 1000,
        ActorY              = -52540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -79360,
        TriggerZ            = 0,
        TriggerY            = -318070,
        TriggerRange        = 1000,
        ActorX              = -78700,
        ActorZ              = 0,
        ActorY              = -318100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -79400,
        TriggerZ            = 0,
        TriggerY            = -298090,
        TriggerRange        = 1000,
        ActorX              = -78740,
        ActorZ              = 0,
        ActorY              = -298130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -37430,
        TriggerZ            = 0,
        TriggerY            = 73910,
        TriggerRange        = 1000,
        ActorX              = -37430,
        ActorZ              = 1000,
        ActorY              = 73910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 60,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38100,
        TriggerZ            = 0,
        TriggerY            = -71790,
        TriggerRange        = 1000,
        ActorX              = -38100,
        ActorZ              = 1000,
        ActorY              = -71790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 61,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -83920,
        TriggerZ            = 0,
        TriggerY            = -346980,
        TriggerRange        = 1000,
        ActorX              = -83920,
        ActorZ              = 1000,
        ActorY              = -346980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 62,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_63A",          # 00, 0
        "Function_1_6E7",          # 01, 1
        "Function_2_9CA",          # 02, 2
        "Function_3_B47",          # 03, 3
        "Function_4_B4C",          # 04, 4
        "Function_5_BEB",          # 05, 5
        "Function_6_C87",          # 06, 6
        "Function_7_D9E",          # 07, 7
        "Function_8_EB5",          # 08, 8
        "Function_9_101F",         # 09, 9
        "Function_10_1136",        # 0A, 10
        "Function_11_1289",        # 0B, 11
        "Function_12_13A0",        # 0C, 12
        "Function_13_14B0",        # 0D, 13
        "Function_14_207A",        # 0E, 14
        "Function_15_274D",        # 0F, 15
        "Function_16_27D6",        # 10, 16
        "Function_17_288D",        # 11, 17
        "Function_18_2C3C",        # 12, 18
        "Function_19_2D66",        # 13, 19
        "Function_20_2DB0",        # 14, 20
        "Function_21_4DC6",        # 15, 21
        "Function_22_4DDB",        # 16, 22
        "Function_23_542A",        # 17, 23
        "Function_24_65A2",        # 18, 24
        "Function_25_661A",        # 19, 25
        "Function_26_671C",        # 1A, 26
        "Function_27_67D3",        # 1B, 27
        "Function_28_69D1",        # 1C, 28
        "Function_29_6A41",        # 1D, 29
        "Function_30_6A93",        # 1E, 30
        "Function_31_6AE5",        # 1F, 31
        "Function_32_7DDD",        # 20, 32
        "Function_33_7DF9",        # 21, 33
        "Function_34_7E15",        # 22, 34
        "Function_35_7E31",        # 23, 35
        "Function_36_7E4D",        # 24, 36
        "Function_37_7EA9",        # 25, 37
        "Function_38_823E",        # 26, 38
        "Function_39_84E3",        # 27, 39
        "Function_40_8517",        # 28, 40
        "Function_41_8547",        # 29, 41
        "Function_42_8577",        # 2A, 42
        "Function_43_858C",        # 2B, 43
        "Function_44_9100",        # 2C, 44
        "Function_45_918C",        # 2D, 45
        "Function_46_9FB0",        # 2E, 46
        "Function_47_A031",        # 2F, 47
        "Function_48_A075",        # 30, 48
        "Function_49_A0A5",        # 31, 49
        "Function_50_A0E9",        # 32, 50
        "Function_51_A12D",        # 33, 51
        "Function_52_A171",        # 34, 52
        "Function_53_A1A1",        # 35, 53
        "Function_54_A1D1",        # 36, 54
        "Function_55_A1ED",        # 37, 55
        "Function_56_A206",        # 38, 56
        "Function_57_A21F",        # 39, 57
        "Function_58_A238",        # 3A, 58
        "Function_59_A2BF",        # 3B, 59
        "Function_60_A350",        # 3C, 60
        "Function_61_A376",        # 3D, 61
        "Function_62_A39C",        # 3E, 62
    )


    def Function_0_63A(): pass

    label("Function_0_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_654")
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_6E6")

    label("loc_654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_665")
    OP_A3(0x10F1)
    Event(0, 14)
    Jump("loc_6E6")

    label("loc_665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_67F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    Event(0, 20)
    Jump("loc_6E6")

    label("loc_67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_699")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F3)
    Event(0, 22)
    Jump("loc_6E6")

    label("loc_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_6AA")
    OP_A3(0x10F4)
    Event(0, 17)
    Jump("loc_6E6")

    label("loc_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_6C4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F5)
    Event(0, 23)
    Jump("loc_6E6")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x456, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7F), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E6")
    Event(0, 38)

    label("loc_6E6")

    Return()

    # Function_0_63A end

    def Function_1_6E7(): pass

    label("Function_1_6E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_705")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_717")
    OP_6F(0x25, 0)
    Jump("loc_71E")

    label("loc_717")

    OP_6F(0x25, 60)

    label("loc_71E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_730")
    OP_6F(0x26, 0)
    Jump("loc_737")

    label("loc_730")

    OP_6F(0x26, 60)

    label("loc_737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_749")
    OP_6F(0x2B, 0)
    Jump("loc_750")

    label("loc_749")

    OP_6F(0x2B, 60)

    label("loc_750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_762")
    OP_6F(0x2C, 0)
    Jump("loc_769")

    label("loc_762")

    OP_6F(0x2C, 60)

    label("loc_769")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_783")
    OP_64(0x2, 0x1)
    OP_71(0x25, 0x0)
    OP_71(0x25, 0x4)

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_795")
    OP_6F(0x2D, 0)
    Jump("loc_79C")

    label("loc_795")

    OP_6F(0x2D, 60)

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AE")
    OP_6F(0x2E, 0)
    Jump("loc_7B5")

    label("loc_7AE")

    OP_6F(0x2E, 60)

    label("loc_7B5")

    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E1")
    SetChrChipByIndex(0x101, 6)
    SetChrChipByIndex(0x12F, 7)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x12F, 0x1000)

    label("loc_7E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80F")
    SetChrPos(0xB, 70380, 0, -234050, 270)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_72(0x1A, 0x10)

    label("loc_80F")

    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 5)), scpexpr(EXPR_END)), "loc_823")
    OP_65(0x3, 0x1)
    OP_72(0x17, 0x10)

    label("loc_823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_931")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 3)), scpexpr(EXPR_END)), "loc_85B")
    SetChrPos(0xF, -84180, 0, -335080, 270)
    SetChrPos(0x10, -84470, 0, -336340, 270)
    Jump("loc_87D")

    label("loc_85B")

    SetChrPos(0xF, -81860, 0, -334130, 180)
    SetChrPos(0x10, -81190, 0, -335370, 0)

    label("loc_87D")

    SetChrPos(0x11, -82890, 0, -331950, 45)
    SetChrPos(0x14, -81710, 0, -332430, 270)
    SetChrPos(0x15, -81980, 0, -331150, 180)
    SetChrPos(0x13, -81220, 0, -336530, 225)
    SetChrPos(0x12, -81780, 0, -338160, 0)
    SetChrPos(0x16, -82670, 0, -337380, 90)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_65(0x1, 0x1)
    OP_65(0x3, 0x1)
    OP_72(0x17, 0x10)
    OP_72(0x3, 0x10)
    OP_72(0x4, 0x10)
    OP_72(0x5, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x7, 0x10)

    label("loc_931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 3)), scpexpr(EXPR_END)), "loc_951")
    OP_65(0x2, 0x1)
    OP_6F(0x25, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_END)), "loc_951")
    OP_6F(0x25, 60)

    label("loc_951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_969")
    OP_6F(0x3, 50)
    OP_71(0x23, 0x4)
    OP_72(0x24, 0x4)

    label("loc_969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 0)), scpexpr(EXPR_END)), "loc_981")
    OP_6F(0x4, 50)
    OP_71(0x23, 0x4)
    OP_72(0x24, 0x4)

    label("loc_981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 1)), scpexpr(EXPR_END)), "loc_999")
    OP_6F(0x5, 50)
    OP_71(0x23, 0x4)
    OP_72(0x24, 0x4)

    label("loc_999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 2)), scpexpr(EXPR_END)), "loc_9B1")
    OP_6F(0x6, 50)
    OP_71(0x23, 0x4)
    OP_72(0x24, 0x4)

    label("loc_9B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 3)), scpexpr(EXPR_END)), "loc_9C9")
    OP_6F(0x7, 50)
    OP_71(0x23, 0x4)
    OP_72(0x24, 0x4)

    label("loc_9C9")

    Return()

    # Function_1_6E7 end

    def Function_2_9CA(): pass

    label("Function_2_9CA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EF")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_B31")

    label("loc_9EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A08")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_B31")

    label("loc_A08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A21")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_B31")

    label("loc_A21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_B31")

    label("loc_A3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A53")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_B31")

    label("loc_A53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_B31")

    label("loc_A6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A85")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_B31")

    label("loc_A85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_B31")

    label("loc_A9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB7")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_B31")

    label("loc_AB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD0")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_B31")

    label("loc_AD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE9")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_B31")

    label("loc_AE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B02")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_B31")

    label("loc_B02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_B31")

    label("loc_B1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B31")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_B31")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B46")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_B31")

    label("loc_B46")

    Return()

    # Function_2_9CA end

    def Function_3_B47(): pass

    label("Function_3_B47")

    Call(0, 19)
    Return()

    # Function_3_B47 end

    def Function_4_B4C(): pass

    label("Function_4_B4C")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_END)), "loc_B96")

    ChrTalk(    #0
        0xF,
        (
            "#490F哦哦，找到卡了吗！\x02\x03",

            "#191F那就好办了！\x01",
            "赶快逃跑吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE7")

    label("loc_B96")


    ChrTalk(    #1
        0xF,
        (
            "#197F前方区域的第二层……\x01",
            "地方太大都不知道在哪里了。\x02\x03",

            "#199F总之小心前往吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE7")

    TalkEnd(0xF)
    Return()

    # Function_4_B4C end

    def Function_5_BEB(): pass

    label("Function_5_BEB")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_END)), "loc_C3E")

    ChrTalk(    #2
        0x10,
        (
            "#204F……看来似乎\x01",
            "平安返回了呢。\x02\x03",

            "#200F没时间了。\x01",
            "赶快逃出去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C83")

    label("loc_C3E")


    ChrTalk(    #3
        0x10,
        (
            "#204F……刚才有红衣士兵\x01",
            "到这里来巡逻过。\x02\x03",

            "#206F小心别被发现哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C83")

    TalkEnd(0x10)
    Return()

    # Function_5_BEB end

    def Function_6_C87(): pass

    label("Function_6_C87")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x287, 1)"), scpexpr(EXPR_END)), "loc_CF6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\x87\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D30)
    Jump("loc_D5C")

    label("loc_CF6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\x87\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x87\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_D5C")

    Jump("loc_D90")

    label("loc_D5F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D90")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_C87 end

    def Function_7_D9E(): pass

    label("Function_7_D9E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E76")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x26, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_E0D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D31)
    Jump("loc_E73")

    label("loc_E0D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x26, 60)
    OP_70(0x26, 0x0)

    label("loc_E73")

    Jump("loc_EA7")

    label("loc_E76")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_EA7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_D9E end

    def Function_8_EB5(): pass

    label("Function_8_EB5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1EF, 1)"), scpexpr(EXPR_END)), "loc_F24")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\xEF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D3B)
    Jump("loc_F8A")

    label("loc_F24")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "宝箱里装有\x1F\xEF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xEF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2B, 60)
    OP_70(0x2B, 0x0)

    label("loc_F8A")

    Jump("loc_FBE")

    label("loc_F8D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_FBE")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1016")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x44)"), scpexpr(EXPR_END)), "loc_FDD")
    Jump("loc_1016")

    label("loc_FDD")


    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\xEF\x01\x07\x00的食谱。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #14
        "\x1F\xEF\x01\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_1016")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_EB5 end

    def Function_9_101F(): pass

    label("Function_9_101F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_108E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D3C)
    Jump("loc_10F4")

    label("loc_108E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2C, 60)
    OP_70(0x2C, 0x0)

    label("loc_10F4")

    Jump("loc_1128")

    label("loc_10F7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1128")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_101F end

    def Function_10_1136(): pass

    label("Function_10_1136")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2D, 0x1E)
    OP_73(0x2D)
    OP_6F(0x2D, 30)
    AddSepith(0x0, 0x12C)
    AddSepith(0x1, 0x12C)
    AddSepith(0x2, 0x12C)
    AddSepith(0x3, 0x12C)
    AddSepith(0x4, 0x12C)
    AddSepith(0x5, 0x12C)
    AddSepith(0x6, 0x12C)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #18
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×３００\x01",
            "\x07\x02#57I水之耀晶片×３００\x01",
            "\x07\x02#58I火之耀晶片×３００\x01",
            "\x07\x02#59I风之耀晶片×３００\x01",
            "\x07\x02#62I时之耀晶片×３００\x01",
            "\x07\x02#60I空之耀晶片×３００\x01",
            "\x07\x02#61I幻之耀晶片×３００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D4A)
    Jump("loc_1277")

    label("loc_125D")


    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1277")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1136 end

    def Function_11_1289(): pass

    label("Function_11_1289")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1361")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x12A, 1)"), scpexpr(EXPR_END)), "loc_12F8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\x2A\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D4B)
    Jump("loc_135E")

    label("loc_12F8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "宝箱里装有\x1F\x2A\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x2A\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2E, 60)
    OP_70(0x2E, 0x0)

    label("loc_135E")

    Jump("loc_1392")

    label("loc_1361")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1392")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1289 end

    def Function_12_13A0(): pass

    label("Function_12_13A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B9")
    OP_71(0x1, 0x4)
    OP_72(0x0, 0x4)
    Jump("loc_14AF")

    label("loc_13B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 5)), scpexpr(EXPR_END)), "loc_1428")
    OP_64(0x4, 0x1)
    SetChrPos(0xC, 54170, 0, 12070, 270)
    SetChrPos(0xD, 60700, 0, 7800, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xD, 18)
    SetChrSubChip(0xC, 15)
    SetChrSubChip(0xD, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1422")
    OP_22(0x1C3, 0x0, 0x64)
    Jump("loc_1425")

    label("loc_1422")

    OP_23(0x1C3)

    label("loc_1425")

    Jump("loc_14AF")

    label("loc_1428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 3)), scpexpr(EXPR_END)), "loc_143C")
    OP_71(0x1, 0x4)
    OP_72(0x0, 0x4)
    Jump("loc_14AF")

    label("loc_143C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x391, 1)), scpexpr(EXPR_END)), "loc_1474")
    OP_64(0x4, 0x1)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 270)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x48), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F(0x64, 0x0)
    OP_71(0x1, 0x4)
    OP_72(0x0, 0x4)
    Jump("loc_14AF")

    label("loc_1474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_END)), "loc_1499")
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 0)
    OP_71(0x1, 0x4)
    OP_72(0x0, 0x4)
    Jump("loc_14AF")

    label("loc_1499")

    OP_72(0x2, 0x10)
    OP_6F(0x2, 0)
    OP_71(0x1, 0x4)
    OP_72(0x0, 0x4)

    label("loc_14AF")

    Return()

    # Function_12_13A0 end

    def Function_13_14B0(): pass

    label("Function_13_14B0")

    EventBegin(0x0)
    OP_20(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_D6(0x1)
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    OP_31(0xFF, 0xFE, 0x0)
    SetChrPos(0x101, 78890, 0, 5300, 270)
    SetChrPos(0x8, 84600, 0, 5600, 270)
    ClearChrFlags(0x8, 0x80)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(79330, 0, 5940, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(3000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x101,
        "\x07\x00#1003F#5P……这里……是……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(400, 50, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #24
        "\x07\x05#40W………艾丝蒂尔…………\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x5B)
    Sleep(500)

    def lambda_15E2():
        OP_6D(82590, 0, 6280, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15E2)

    def lambda_15FA():
        OP_67(0, 6500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15FA)

    def lambda_1612():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1612)
    TurnDirection(0x101, 0x8, 400)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #25
        0x101,
        "\x07\x00#1020F#6P约修亚！？\x02",
    )

    CloseMessageWindow()

    def lambda_1650():

        label("loc_1650")

        OP_99(0x101, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_1650")

    QueueWorkItem2(0x101, 1, lambda_1650)
    Sleep(1500)
    SetChrChipByIndex(0x101, 1)

    def lambda_166D():

        label("loc_166D")

        OP_99(0x101, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_166D")

    QueueWorkItem2(0x101, 1, lambda_166D)
    Sleep(1500)
    OP_62(0x101, 0x64, 1900, 0x28, 0x2B, 0xFA, 0x0)

    def lambda_1697():

        label("loc_1697")

        OP_99(0x101, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_1697")

    QueueWorkItem2(0x101, 1, lambda_1697)
    Sleep(3000)

    ChrTalk(    #26
        0x101,
        "\x07\x00#1021F#6P为……为什么……？\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #27
        0x8,
        (
            "\x07\x05#2P#40W够了……\x01",
            "……已经够了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    Sleep(500)
    OP_99(0x8, 0x0, 0x9, 0x5DC)
    OP_22(0x82, 0x0, 0x64)
    OP_99(0x8, 0xA, 0xB, 0x5DC)
    Sleep(500)
    OP_44(0x101, 0x1)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x101,
        "\x07\x00#1020F#6P啊啊……！\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #29
        0x8,
        (
            "\x07\x05#2P#40W原本……\x01",
            "#40W我就是个坏掉的人偶……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17B3():
        OP_99(0x8, 0xC, 0x14, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17B3)
    Sleep(500)
    OP_22(0x82, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    ChrTalk(    #30
        0x8,
        "\x07\x05#2P#40W无法恢复成人类……\x02",
    )

    CloseMessageWindow()

    def lambda_17F8():
        OP_6D(83130, 0, 6760, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17F8)
    OP_99(0x8, 0x15, 0x18, 0x5DC)

    def lambda_1819():
        OP_99(0x8, 0x19, 0x25, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1819)
    OP_22(0xB1, 0x0, 0x64)
    Sleep(500)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 20)
    SetChrSubChip(0x101, 32)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    SetChrPos(0x9, 82600, -800, 6180, 0)

    ChrTalk(    #31
        0x9,
        (
            "\x07\x05#5P#40W所以……\x01",
            "#40W……已经够了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #32
        0x101,
        "\x07\x00#1020F#6P……………啊………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x101, 0x800)
    SetChrFlags(0x101, 0x8000)

    def lambda_18D0():
        OP_9E(0xFE, 0x14, 0x0, 0x9C4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18D0)

    def lambda_18EA():

        label("loc_18EA")

        OP_99(0xFE, 0x20, 0x27, 0x5DC)
        OP_48()
        Jump("loc_18EA")

    QueueWorkItem2(0x101, 2, lambda_18EA)
    OP_8F(0x101, 0x13A2E, 0x0, 0x164E, 0x3E8, 0x0)
    OP_44(0x101, 0x2)
    SetChrSubChip(0x101, 32)
    Sleep(500)

    def lambda_191F():
        OP_9E(0xFE, 0x14, 0x0, 0x9C4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_191F)

    def lambda_1939():

        label("loc_1939")

        OP_99(0xFE, 0x20, 0x27, 0x5DC)
        OP_48()
        Jump("loc_1939")

    QueueWorkItem2(0x101, 2, lambda_1939)
    OP_8F(0x101, 0x14064, 0x0, 0x1842, 0x3E8, 0x0)
    OP_44(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    OP_99(0x101, 0x0, 0x5, 0x5DC)
    Sleep(1500)
    Fade(500)

    def lambda_198B():
        OP_6B(2200, 5000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_198B)
    SetChrSubChip(0x8, 38)
    SetChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 82020, 0, 6210, 0)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 20)
    SetChrSubChip(0xA, 21)
    Sleep(200)
    SetChrSubChip(0x101, 6)
    SetChrSubChip(0xA, 22)
    Sleep(200)
    SetChrSubChip(0x101, 7)
    SetChrSubChip(0xA, 23)
    Sleep(1000)
    Sleep(500)
    SetChrPos(0x9, 81500, 0, 5500, 0)

    ChrTalk(    #33
        0x9,
        (
            "\x07\x05#2P#60W谢谢你……\x02\x03",

            "#80W再见了，艾丝蒂尔……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrSubChip(0xA, 24)
    Sleep(1500)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #34
        0x101,
        "\x07\x00#1025F#5P不……不要……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 8)
    SetChrSubChip(0xA, 26)
    Sleep(100)
    SetChrSubChip(0x101, 10)
    SetChrSubChip(0xA, 27)
    Sleep(100)
    SetChrSubChip(0x101, 11)
    Sleep(1000)
    FadeToDark(2000, 0, -1)

    def lambda_1AA2():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AA2)

    ChrTalk(    #35 op#A op#5
        0x101,
        "\x07\x00#1014F#4S#30A#5P不要啊啊啊啊啊！！\x05\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x1F4)
    Sleep(3500)
    OP_0D()
    OP_20(0x3E8)
    OP_21()
    ClearChrFlags(0x101, 0x800)
    ClearChrFlags(0x101, 0x8000)
    OP_44(0x101, 0x2)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x800)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    SetChrPos(0x101, 60300, 500, 15000, 270)
    SetChrPos(0xB, 60720, 0, 13200, 0)
    ClearChrFlags(0xB, 0x80)
    OP_6D(60440, 0, 15530, 0)
    OP_67(0, 8510, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(32000, 0)
    OP_6E(288, 0)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_1B97():
        OP_99(0x101, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B97)
    WaitChrThread(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 5)
    Sleep(500)

    ChrTalk(    #36
        0x101,
        "#1020F#5P………啊…………………\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0xB,
        (
            "\x07\x00#264F#4P吓死我了……\x02\x03",

            "艾丝蒂尔，不要紧吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 7)
    Sleep(500)

    ChrTalk(    #38
        0x101,
        (
            "#1026F#5P玲……\x02\x03",

            "#1025F太、太好了……\x01",
            "……是梦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        (
            "\x07\x00#260F#4P嘻嘻……\x01",
            "做了恶梦吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 4)
    Sleep(500)

    ChrTalk(    #40
        0x101,
        (
            "#1007F嗯……最糟糕的梦……\x02\x03",

            "都是碰上了那种人偶\x01",
            "才会做这么奇怪的梦——\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x23B, 0x0, 0x3C)

    def lambda_1D15():
        OP_96(0xFE, 0xE9D4, 0x2BC, 0x3BD8, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D15)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1)
    OP_8C(0x101, 180, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 3)
    WaitChrThread(0x101, 0x1)
    ClearChrFlags(0x101, 0x800)
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #41
        0x101,
        (
            "#1020F#5P……慢、慢着！\x02\x03",

            "为什么玲\x01",
            "会在这种地方啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xB,
        (
            "\x07\x00#261F#4P呜呵呵……\x01",
            "你吓一跳的节奏都晚半拍。\x02\x03",

            "艾丝蒂尔真是的，\x01",
            "还是那么没紧张感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1019F#5P我就是没紧张感，不好意思呀。\x02\x03",

            "#1004F……那，这里……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(500)
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 90, 400)
    Sleep(500)

    ChrTalk(    #44
        0xB,
        (
            "\x07\x00#263F#4P玲在这里\x01",
            "并不是什么奇怪的事。\x02\x03",

            "#269F因为这里是\x01",
            "我们的新据点嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #45
        0x101,
        "#1002F#5P新据点……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xB,
        (
            "\x07\x00#1305F#4P嘻嘻……\x01",
            "去看看那个窗口如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1002F#5P………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_1F44():

        label("loc_1F44")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_1F44")

    QueueWorkItem2(0xB, 2, lambda_1F44)
    OP_8F(0x101, 0xE84E, 0x2BC, 0x3642, 0x5DC, 0x0)
    OP_96(0x101, 0xE93E, 0x0, 0x3516, 0xC8, 0xBB8)

    def lambda_1F80():
        OP_6D(62950, 0, 12460, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F80)

    def lambda_1F98():
        OP_67(0, 4220, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F98)

    def lambda_1FB0():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FB0)

    def lambda_1FC0():
        OP_6C(57000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1FC0)

    def lambda_1FD0():
        OP_6E(288, 3000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1FD0)
    OP_8E(0x101, 0xE9FC, 0x0, 0x2D78, 0x7D0, 0x0)

    def lambda_1FF4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1FF4)
    OP_8E(0x101, 0xF032, 0x0, 0x2C1A, 0x7D0, 0x0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #48
        0x101,
        "#1020F#4S什…什么…！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5414   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_14B0 end

    def Function_14_207A(): pass

    label("Function_14_207A")

    EventBegin(0x0)
    SetChrPos(0x101, 61490, 0, 11290, 90)
    SetChrPos(0xB, 61300, 0, 12390, 90)
    ClearChrFlags(0xB, 0x80)
    OP_6D(62950, 0, 12460, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(57000, 0)
    OP_6E(288, 0)
    OP_6D(63980, 0, 13140, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(57000, 0)
    OP_6E(288, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #49
        0x101,
        "#1020F#6P…………………（惊讶）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        (
            "#263F#6P『红色方舟』古罗力亚斯……\x02\x03",

            "光凭这一艘飞船，\x01",
            "就可能超越一个国家的军队哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)
    Sleep(400)

    ChrTalk(    #51
        0xB,
        (
            "#1306F#5P嘻嘻，相当\x01",
            "有趣的玩具对吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #52
        0x101,
        (
            "#1020F#4P你、你们……\x02\x03",

            "拿出这样的东西想干什么……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x5A)
    Sleep(1000)
    SetMessageWindowPos(320, 60, -1, -1)
    SetChrName("男性的声音")

    AnonymousTalk(    #53
        "\x07\x05呀，看来醒了呢。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 270, 600)
    Sleep(500)
    OP_8C(0x101, 180, 600)
    Sleep(500)
    OP_8C(0x101, 270, 600)
    Sleep(500)
    SetChrName("男性的声音")

    AnonymousTalk(    #54
        (
            "\x07\x05欢迎，艾丝蒂尔。\x01",
            "睡得还好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("男性的声音")

    AnonymousTalk(    #55
        (
            "\x07\x05被带到这种地方来，\x01",
            "想必你内心相当混乱吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("男性的声音")

    AnonymousTalk(    #56
        (
            "\x07\x05不过，我们并不\x01",
            "打算加害于你。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("男性的声音")

    AnonymousTalk(    #57
        "\x07\x05请你大可以放心。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #58
        0x101,
        "#1002F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("男性的声音")

    AnonymousTalk(    #59
        (
            "\x07\x05如何，你不想\x01",
            "好好地谈一次吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("男性的声音")

    AnonymousTalk(    #60
        (
            "\x07\x05关于结社的事、我们的目的，\x01",
            "以及那位共同的朋友……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("男性的声音")

    AnonymousTalk(    #61
        (
            "\x07\x05你的种种的疑问\x01",
            "应该都能得到解答哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #62
        0x101,
        (
            "#1022F#5P……好吧。\x02\x03",

            "就让我好好发问吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("男性的声音")

    AnonymousTalk(    #63
        "\x07\x05好，稍等。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("男性的声音")

    AnonymousTalk(    #64
        (
            "\x07\x05玲，给艾丝蒂尔\x01",
            "带个路吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #65
        0xB,
        "#261F#5P嘻嘻，明白了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x5A)
    Sleep(1000)
    OP_8C(0xB, 225, 400)

    def lambda_24E5():
        OP_6D(61750, 0, 11850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24E5)
    OP_8E(0xB, 0xE8A8, 0x0, 0x2B34, 0x5DC, 0x0)
    OP_8C(0xB, 90, 400)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #66
        0xB,
        (
            "#260F#6P那么，艾丝蒂尔。\x01",
            "去『圣堂』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1002F#2P『圣堂』……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "#263F#6P是这艘战舰最上层的\x01",
            "一个很棒的房间哦。\x02\x03",

            "『教授』在那里等着你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1002F#2P…………………………………\x02\x03",

            "#1022F……明白了。\x01",
            "你带路吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xB,
        (
            "#1305F#6P嘻嘻，不用\x01",
            "那么紧张啦。\x02\x03",

            "或许对艾丝蒂尔来说\x01",
            "也一定不会是什么坏事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1015F#2P哦……什么意思？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xB,
        (
            "#261F#6P好戏在后头呢。\x02\x03",

            "#265F好了，跟玲走吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x2E, 0xFF, 0xFF)
    SetChrChipByIndex(0x101, 6)
    SetChrChipByIndex(0x12F, 7)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x12F, 0x1000)
    SetChrFlags(0xB, 0x80)
    OP_6D(59560, 0, 11060, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 59560, 0, 11060, 270)
    SetChrPos(0x1, 59560, 0, 11060, 270)
    OP_69(0x0, 0x0)
    OP_A2(0x1C1B)
    OP_3F(0x3FA, 1)
    OP_3F(0x3FB, 1)
    OP_3F(0x3FC, 1)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_14_207A end

    def Function_15_274D(): pass

    label("Function_15_274D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_275A")
    Return()

    label("loc_275A")

    EventBegin(0x1)
    TurnDirection(0x101, 0x12F, 400)

    NpcTalk(    #73
        0x101,
        "歼灭天使玲",
        (
            "#263F艾丝蒂尔。\x01",
            "『圣堂』不是这边。\x02\x03",

            "#260F要去走廊另一端\x01",
            "搭乘升降梯哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_15_274D end

    def Function_16_27D6(): pass

    label("Function_16_27D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27E3")
    Return()

    label("loc_27E3")

    EventBegin(0x1)
    TurnDirection(0x101, 0x12F, 400)

    NpcTalk(    #74
        0x101,
        "歼灭天使玲",
        (
            "#265F艾丝蒂尔。\x01",
            "『圣堂』不是这边。\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(-38720, 0, -65209, 2000)

    NpcTalk(    #75
        0x101,
        "歼灭天使玲",
        (
            "#2P看，就在那里\x01",
            "搭乘升降梯哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_69(0x101, 0x0)
    OP_0D()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_16_27D6 end

    def Function_17_288D(): pass

    label("Function_17_288D")

    EventBegin(0x0)
    SetChrPos(0x101, 73290, 0, -234130, 270)
    SetChrPos(0x12F, 74790, 0, -234130, 270)
    OP_6D(72090, 0, -232990, 0)
    OP_67(0, 7540, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x1A, 0x10)
    OP_72(0x1A, 0x20)
    OP_6F(0x1A, 0)
    OP_70(0x1A, 0xF)
    OP_73(0x1A)

    def lambda_2923():
        OP_6D(67800, 0, -233840, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2923)

    def lambda_293B():
        OP_90(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_293B)
    Sleep(100)

    def lambda_295B():
        OP_90(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12F, 1, lambda_295B)
    WaitChrThread(0x12F, 0x1)
    OP_6F(0x1A, 15)
    OP_70(0x1A, 0x0)
    TurnDirection(0x101, 0x12F, 400)
    Sleep(500)

    NpcTalk(    #76
        0x101,
        "歼灭天使玲",
        (
            "#263F#6P嘻嘻……\x01",
            "这里就是教授所在的『圣堂』哦。\x02\x03",

            "#260F这前面\x01",
            "艾丝蒂尔一个人去就好了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #77
        0x12F,
        "艾丝蒂尔",
        "#1015F#2P……对了，玲。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #78
        0x101,
        "歼灭天使玲",
        "#260F#6P什么事？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #79
        0x12F,
        "艾丝蒂尔",
        (
            "#1002F#2P在研究所，操纵约修亚的\x01",
            "人偶的是玲对吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #80
        0x101,
        "歼灭天使玲",
        (
            "#265F#6P嗯嗯，是啊。\x02\x03",

            "#261F是『教授』拜托我做的，\x01",
            "相当有趣对吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #81
        0x12F,
        "艾丝蒂尔",
        (
            "#1007F#2P唉……\x02\x03",

            "#1003F……看来你也是\x01",
            "『结社』的受害者啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0x101,
        "歼灭天使玲",
        "#264F#6P咦……？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #83
        0x12F,
        "艾丝蒂尔",
        (
            "#1007F#2P……算了，现在先不管。\x02\x03",

            "#1006F那么我过去了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0x101,
        "玲",
        "#261F#6P嘻嘻，慢走。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(67790, 0, -234130, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    RemoveParty(0x2E, 0xFF)
    SetChrPos(0x101, 67790, 0, -234130, 270)
    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0xB, 70380, 0, -234050, 270)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_69(0x101, 0x0)
    OP_69(0x0, 0x0)
    OP_72(0x1A, 0x10)
    OP_A2(0x1C1C)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_17_288D end

    def Function_18_2C3C(): pass

    label("Function_18_2C3C")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 61000, 0, -185610, 0)
    OP_6D(61240, 0, -185600, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_20(0xBB8)

    def lambda_2C9D():
        OP_6D(60980, 500, -184400, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C9D)

    def lambda_2CB5():
        OP_67(0, 5000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CB5)

    def lambda_2CCD():
        OP_6B(3120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2CCD)

    def lambda_2CDD():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2CDD)
    WaitChrThread(0x101, 0x0)
    OP_21()
    Sleep(300)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x10E)
    OP_22(0x132, 0x0, 0x64)
    Sleep(500)
    OP_1D(0x79)
    OP_1F(0x46, 0x64)
    OP_73(0x2)

    def lambda_2D1B():
        OP_8E(0xFE, 0xEDA8, 0x0, 0xFFFD3EEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D1B)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/C5401   ._SN", 125, 0, 0)
    IdleLoop()
    OP_64(0x4, 0x1)
    OP_A2(0x1C89)
    Sleep(500)
    EventEnd(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_2C3C end

    def Function_19_2D66(): pass

    label("Function_19_2D66")

    TalkBegin(0xB)

    ChrTalk(    #85
        0xB,
        (
            "#1306F沿着走廊前进，\x01",
            "马上就到『圣堂』了。\x02\x03",

            "『教授』在等你哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_19_2D66 end

    def Function_20_2DB0(): pass

    label("Function_20_2DB0")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrPos(0xC, 6240, 0, 4990, 270)
    ClearChrFlags(0xC, 0x80)
    OP_6D(6850, 0, 5420, 0)
    OP_67(0, 5820, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(56000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    SetChrPos(0x101, 55870, 200, 13910, 0)
    ClearChrFlags(0x101, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 9)
    OP_6D(57200, 0, 14960, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(56000, 0)
    OP_6E(296, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #86
        0x101,
        (
            "#1003F#6P（进入『结社』\x01",
            "就能再见到约修亚……）\x02\x03",

            "（这种可能性\x01",
            " 倒是的确相当的高……）\x02\x03",

            "#1016F（而且，也不一定\x01",
            "真的要加入吧……？）\x02\x03",

            "（假装成为同伴之后\x01",
            "探听内情也是可以……）\x02\x03",

            "#1025F（以我的演技来说虽然困难，\x01",
            "但是总比被关在这里好……）\x02\x03",

            "（………………………………）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)

    def lambda_2F9E():
        OP_6D(58030, 0, 14730, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F9E)
    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0x101, 56790, 0, 14000, 90)
    OP_0D()
    Sleep(1000)

    def lambda_2FD2():
        OP_6D(62030, 0, 11840, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2FD2)
    OP_8E(0x101, 0xE272, 0x0, 0x2BD4, 0x7D0, 0x0)
    OP_8E(0x101, 0xF03C, 0x0, 0x2B34, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(300)

    ChrTalk(    #87
        0x101,
        (
            "#1010F#6P（可是……\x01",
            "总觉得有点不太对……）\x02\x03",

            "#1002F（这……\x01",
            "并不是我的作风。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xE, 50890, 0, 10990, 90)
    ClearChrFlags(0xE, 0x80)

    NpcTalk(    #88
        0xE,
        "青年的声音",
        "#2P……打扰了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_30DB():
        OP_6D(59440, 0, 11670, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30DB)
    OP_22(0x6D, 0x0, 0x64)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x101, 0x1)

    def lambda_3104():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3104)

    def lambda_3116():
        OP_8E(0xFE, 0xDDFE, 0x0, 0x2AE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3116)
    Sleep(500)

    def lambda_3136():
        OP_6D(60440, 0, 11670, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3136)
    Sleep(500)

    ChrTalk(    #89
        0x101,
        (
            "#1020F啊……\x02\x03",

            "#1002F………………………………\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xE, 0x1)

    ChrTalk(    #90
        0xE,
        (
            "#123F#6P呵……不用那么戒备。\x02\x03",

            "只要不再做出刚才那种\x01",
            "不经大脑思考的行为，\x01",
            "我们就不会加害于你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1022F不好意思啊，我做事就是不经大脑。\x02\x03",

            "#1019F什么嘛，你们\x01",
            "不是到外面去了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        (
            "#124F#6P我只是负责留守。\x02\x03",

            "出去的是教授\x01",
            "和其它的『执行者』们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1002F……你到底想怎样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xE,
        (
            "#121F#6P想知道的话\x01",
            "就接受教授的邀请如何？\x02\x03",

            "这样就能得知你想了解的一切吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#1003F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xE,
        (
            "#123F#6P呵呵……\x02\x03",

            "已经有了答案，\x01",
            "却还在迷惘中吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#1026F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xE,
        (
            "#124F#6P以我个人的意见看来，\x01",
            "你到底还是\x01",
            "不太适合『结社』。\x02\x03",

            "无论是能力，还是性格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1019F呜……\x02\x03",

            "说得好直白，\x01",
            "也太打击别人的自尊心了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xE,
        (
            "#121F#6P嗯，关于能力方面，\x01",
            "倒是还潜藏着一些可能性吧。\x02\x03",

            "但是，说到性格……\x02\x03",

            "#124F以『结社』的标准来衡量，\x01",
            "你的阴暗面实在太少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1026F阴暗面……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xE,
        (
            "#120F#6P从属于『结社』的人\x01",
            "必定都背负着某种黑暗的过去。\x02\x03",

            "我，教授，其他的执行者……\x02\x03",

            "#124F当然，还有约修亚也是。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #103
        0x101,
        (
            "#1003F………………………………\x02\x03",

            "#1010F对了，『剑帝』……\x02\x03",

            "#1002F你和约修亚\x01",
            "到底是什么关系？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xE,
        "#121F#6P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1002F约修亚一直\x01",
            "十分介意洛伦斯少尉的事。\x02\x03",

            "虽然未曾谋面，\x01",
            "却好像知道对方是谁……\x02\x03",

            "似乎在竭尽全力\x01",
            "调查他的真实身份。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xE,
        (
            "#121F#6P呼……这也难怪。\x02\x03",

            "#124F他的一部分记忆\x01",
            "被教授封印了。\x02\x03",

            "从离开『结社』的一刹起\x01",
            "就被暗示了，\x01",
            "根本无法想起任何具体的情报。\x02\x03",

            "#120F就算记得自己在『结社』\x01",
            "做了怎样的事情\x01",
            "但也想不起来相关人员的名字……\x02\x03",

            "必须要面对这样的一种困境。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#1020F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xE,
        (
            "#124F小时候的记忆也是一样……\x02\x03",

            "就算他还记得卡琳，\x01",
            "恐怕对我的记忆也变得模糊了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1003F是吗……所以才……\x02\x03",

            "#1015F对了，『卡琳』这个名字，\x01",
            "我好像在哪里听过？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xE,
        "#121F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_37F0():
        OP_6D(62560, 0, 12000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37F0)

    def lambda_3808():

        label("loc_3808")

        TurnDirection(0x101, 0xE, 400)
        OP_48()
        Jump("loc_3808")

    QueueWorkItem2(0x101, 2, lambda_3808)
    OP_8F(0xE, 0xF078, 0x0, 0x2F1C, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x2)
    Sleep(1000)

    ChrTalk(    #111
        0xE,
        (
            "#129F#5P──卡琳·阿斯特雷。\x02\x03",

            "我的青梅竹马，\x01",
            "也就是约修亚的亲姐姐。\x02\x03",

            "１０年前死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1020F#3S#4P！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xE,
        (
            "#122F#5P你拿的口琴\x01",
            "原本是卡琳的东西。\x02\x03",

            "作为遗物，\x01",
            "交给约修亚保管……\x02\x03",

            "#125F之后他又将它交给了你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#1020F#4P约修亚……\x01",
            "原来有姐姐啊……\x02\x03",

            "#1003F…………………………………\x02\x03",

            "那个……为什么……\x02\x03",

            "#1026F卡琳……\x01",
            "约修亚的姐姐会死呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(    #115
        0xE,
        (
            "#123F#5P……如果告诉你的话，\x01",
            "也许你会受到很大的刺激。\x02\x03",

            "而且也会了解到约修亚和我们\x01",
            "所背负的黑暗。\x02\x03",

            "你有这个心理准备吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1003F#4P……………………………\x02\x03",

            "#1010F……嗯，请告诉我吧。\x02\x03",

            "#1025F虽然不知道是否\x01",
            "真的做好了心理准备……\x02\x03",

            "可是我……\x01",
            "无论如何都想知道\x01",
            "约修亚曾经发生过的事情。\x02\x03",

            "这就是我目前的心境。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xE,
        "#124F#5P……好吧。\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_8C(0xE, 90, 300)
    WaitChrThread(0x101, 0x1)
    OP_21()
    Sleep(500)
    OP_1D(0x72)
    Sleep(500)

    def lambda_3B10():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B10)
    Sleep(1000)

    ChrTalk(    #118
        0xE,
        (
            "#129F#5P那是在１０年前……\x02\x03",

            "我们所居住的哈梅尔村\x01",
            "还记载在地图上的时候。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_AD(0x240083, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetChrName("")

    AnonymousTalk(    #119
        (
            "\x07\x0C哈梅尔是个小村子……\x02\x03",

            "小孩子也很少，\x01",
            "所以我们常常在一起玩。\x02\x03",

            "我梦想有一天能成为游击士\x01",
            "空闲的时候就会练剑……\x02\x03",

            "对此，卡琳和小约修亚\x01",
            "每天都司空见惯了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_AD(0x240084, 0x0, 0x0, 0x64)
    Sleep(3000)

    AnonymousTalk(    #120
        (
            "\x07\x0C……练习结束之后，\x01",
            "我和约修亚会倾听\x01",
            "卡琳吹奏口琴的旋律。\x02\x03",

            "卡琳会吹很多首曲子，\x01",
            "但我们最喜欢的还是\x01",
            "曾经一度流行的『星之所在』。\x02\x03",

            "我们一直深信着\x02\x03",

            "这样的日子将会持续到永远……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    Sleep(500)

    AnonymousTalk(    #121
        (
            "\x07\x0C但是，有一天，一群手持\x01",
            "                王国制导力枪的黑衣人\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240085, 0x0, 0x0, 0x64)
    Sleep(3000)

    AnonymousTalk(    #122
        (
            "\x07\x0C向村子发动了袭击……\x02\x03",

            "他们包围了村子之后，\x01",
            "开始对村民们进行残酷的折磨、虐杀。\x02\x03",

            "从老人到婴儿，没有一个人可以幸免。\x02\x03",

            "被直接杀死的人也许还算是幸运，\x02\x03",

            "……女人们的命运就更加悲惨。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_AD(0x240086, 0x0, 0x0, 0x64)
    Sleep(3000)

    AnonymousTalk(    #123
        (
            "\x07\x0C我们──就在那地狱中开始拼命逃跑。\x02\x03",

            "听着亲人和朋友们的临终哀嚎，\x01",
            "在『快逃！』的声音的催促下，\x01",
            "拼尽全力向村外逃去。\x02\x03",

            "之后，终于逃到了村外，\x01",
            "我为了吸引追兵的注意力留下断后，\x02\x03",

            "让卡琳和约修亚先走，\x01",
            "并向他们保证随后就会追上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    Sleep(500)

    AnonymousTalk(    #124
        (
            "\x07\x0C但是……\x01",
            "袭击者们的布局超乎想象的周全。\x02\x03",

            "竟特意留下了负责截杀逃跑村民的人在外待命。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x2F0, 0x264, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x2EF, 0x263, 0xFFFFFF, 0x0, "C_VIS112._CH")
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0xFF38, 0x0, 0x300, 0x200, 0x0, 0x0, 0x1FF, 0x1FF, 0xFFFFFF, 0x0, "C_VIS138._CH")
    OP_C5(0x2, 0x0, 0x0, 0x2C8, 0x264, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x2C7, 0x263, 0xFFFFFF, 0x1, "C_VIS139._CH")
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C6(0x0, 0x0, -100000, 0, 3000)
    Sleep(1000)
    OP_C6(0x1, 0x3, -1, 500, 0)
    OP_C6(0x1, 0x0, 100000, 0, 2000)
    Sleep(3000)
    FadeToDark(3000, 16777215, -1)
    OP_C6(0x1, 0x3, 16777215, 2000, 0)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C6(0x2, 0x3, 16777215, 2000, 0)
    Sleep(2000)
    OP_0D()
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)

    AnonymousTalk(    #125
        (
            "\x07\x0C当我赶上他们的时候，那里出奇地安静。\x02\x03",

            "一具喉咙被打穿的男人尸体……\x02\x03",

            "手中握着枪发呆的约修亚……\x02\x03",

            "从肩膀到背后都被劈开，\x01",
            "但仍然紧紧抱着约修亚的卡琳……\x02\x03",

            "卡琳……在我赶到时还有一口气。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240088, 0x0, 0x0, 0x64)
    Sleep(3000)

    AnonymousTalk(    #126
        (
            "\x07\x0C不知为何，卡琳她……\x01",
            "脸上竟浮现出平静而满足的表情。\x02\x03",

            "她将心爱的口琴托付给约修亚，\x01",
            "并请求我照顾约修亚……\x02\x03",

            "然后──静静地离开了人世。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #127
        0x101,
        (
            "#1020F#4P…………………………………\x02\x03",

            "……为……什么……\x02\x03",

            "为什么……会有这种事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xE,
        (
            "#129F#5P帝国军在这之后\x01",
            "开始侵略利贝尔。\x02\x03",

            "手持王国制造的导力枪的\x01",
            "袭击者在国境附近引起的\x01",
            "惨剧……\x02\x03",

            "这无疑是发动侵略战争\x01",
            "的最佳借口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1026F#4P……怎么会……\x02\x03",

            "真的是利贝尔的士兵……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xE,
        (
            "#128F#5P被军队保护的我们\x01",
            "最初是这样被告知的。\x02\x03",

            "#129F然而数月后……\x01",
            "战争以帝国军的败退而结束时，\x01",
            "我们却收到了截然相反的说明。\x02\x03",

            "袭击村子的人们\x01",
            "是猎兵团的野盗。\x02\x03",

            "并且威胁我们\x01",
            "绝对不许说出袭击的事……\x02\x03",

            "军队向外界宣布发生了山崩，\x01",
            "将通往哈梅尔的道路完全封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        (
            "#1020F#4P等、等一下！？\x02\x03",

            "为什么要特意\x01",
            "撒这种谎？\x02\x03",

            "那简直就是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xE,
        (
            "#125F#5P哼哼……\x02\x03",

            "#122F这一切都是帝国内的主战派\x01",
            "为了侵略利贝尔\x01",
            "而精心策划的剧本。\x02\x03",

            "到战争末期，此事已经无法掩盖，\x01",
            "帝国政府也开始惊慌失措了。\x02\x03",

            "只得假惺惺地提出停战，\x01",
            "并决定借着将主谋者们悉数处刑\x01",
            "来抹消这个事件。\x02\x03",

            "#129F这就是──\x01",
            "『哈梅尔的悲剧』的真相。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        "#1020F#4P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xE,
        (
            "#129F#5P在这些日子中……\x01",
            "约修亚的心完全坏掉了。\x02\x03",

            "姐姐的死，亲人的死，邻居的死，\x01",
            "初次夺走他人的生命的冲击，\x01",
            "还有这充满欺瞒的世界……\x02\x03",

            "这一切，足够让\x01",
            "一个六岁孩子的心灵彻底崩溃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1003F#4P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xE,
        (
            "#128F#5P之后发生的事情，\x01",
            "大概约修亚都已经告诉你了吧。\x02\x03",

            "心灵破碎的约修亚，\x01",
            "对除口琴以外的一切事情都失去了兴趣，\x01",
            "日渐消瘦衰弱。\x02\x03",

            "就在此时，怀斯曼出现在了\x01",
            "约修亚和我的面前……\x02\x03",

            "我把约修亚托付给他，\x01",
            "自己投身加入了『噬身之蛇』。\x02\x03",

            "#129F而两年后……\x02\x03",

            "被教授改造之后的约修亚也\x01",
            "走上了与我同样的道路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#1027F#4P………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 180, 400)
    Sleep(500)

    ChrTalk(    #138
        0xE,
        (
            "#123F#5P──这就是黑暗。\x01",
            "艾丝蒂尔·布莱特。\x02\x03",

            "你和约修亚之间\x01",
            "有着怎样的隔阂……\x02\x03",

            "现在终于可以理解了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1003F#4P………………………………\x02\x03",

            "#1010F……嗯。\x02\x03",

            "我觉得，终于明白\x01",
            "约修亚失踪的真正理由了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xE,
        "#126F#5P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1006F#4P──我现在可以明确拒绝\x01",
            "教授的邀请了。\x02\x03",

            "我绝对不会\x01",
            "进入『噬身之蛇』的。\x02\x03",

            "不管是喜欢还是讨厌『结社』\x01",
            "这都无所谓……\x02\x03",

            "只要我还在追寻约修亚\x01",
            "就绝对不会加入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xE,
        "#120F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1015F#4P虽然很对不起\x01",
            "特地邀请我的玲……\x02\x03",

            "#1016F不过只要道歉，她应该会原谅我吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xE,
        (
            "#124F#5P哼……奇怪的小姑娘。\x02\x03",

            "#123F听了刚才的话\x01",
            "反而打消了迷惘。\x02\x03",

            "看来，只把你当作是『剑圣』的女儿\x01",
            "似乎有些小看你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1016F#4P是、是吗？\x01",
            "虽然不是很了解……\x02\x03",

            "#1006F倒是你，\x01",
            "并不只是约修亚\x01",
            "从前的朋友那么简单吧。\x02\x03",

            "对他来说，你可以算是哥哥吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xE,
        "#121F#5P……………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 90, 400)
    Sleep(500)

    ChrTalk(    #147
        0xE,
        (
            "#125F#5P为了避免误会，我要先声明，\x01",
            "我和那家伙的兄弟情份\x01",
            "在１０年前就已经结束了。\x02\x03",

            "对现在的我来说，那家伙\x01",
            "不过是个应该排除的危险分子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#1020F#4P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xE,
        (
            "#128F#5P教授似乎以\x01",
            "放任约修亚为乐……\x02\x03",

            "但我的想法却与教授不同。\x02\x03",

            "#129F在不久的将来，\x01",
            "我会亲手收拾他的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #150
        0x101,
        (
            "#1005F#4P慢、慢着！\x01",
            "为什么要这样啊！？\x02\x03",

            "卡琳……\x01",
            "约修亚的姐姐\x01",
            "不是把他托付给你吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xE,
        (
            "#129F#5P我有我自己选择的道路。\x02\x03",

            "谁阻我路，就是我的敌人，\x01",
            "无论是谁，我也都会斩杀。\x02\x03",

            "#128F即便是违背\x01",
            "卡琳的遗愿，也在所不惜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#1026F#4P怎么会……\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_43(0xE, 0x1, 0x0, 0x15)
    Sleep(4000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 90, 400)
    Sleep(1000)

    ChrTalk(    #153
        0x101,
        "#1020F啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5414   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_2DB0 end

    def Function_21_4DC6(): pass

    label("Function_21_4DC6")

    OP_22(0x133, 0x0, 0x2D)
    Sleep(4000)
    OP_22(0x133, 0x0, 0x2D)
    Sleep(4000)
    Return()

    # Function_21_4DC6 end

    def Function_22_4DDB(): pass

    label("Function_22_4DDB")

    EventBegin(0x0)
    SetChrPos(0x101, 61500, 0, 11060, 90)
    SetChrPos(0xE, 61560, 0, 12060, 90)
    ClearChrFlags(0xE, 0x80)
    OP_6D(62560, 0, 12000, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(56000, 0)
    OP_6E(296, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #154
        0x101,
        "#1020F#6P那个是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xE,
        (
            "#125F#5P是教授和其他的执行者。\x02\x03",

            "计划的第三阶段\x01",
            "终于要实行了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)
    Sleep(500)

    ChrTalk(    #156
        0x101,
        "#1002F#4P第、第三阶段是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(    #157
        0xE,
        (
            "#123F#5P呼……\x01",
            "你没有必要知道这些。\x02\x03",

            "#124F事成之后，你应该也\x01",
            "可以回到父亲的身边吧。\x02\x03",

            "在那之前\x01",
            "乖乖待在这里就好。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 270, 400)
    Sleep(500)

    def lambda_4F6D():
        OP_6D(60160, 0, 11740, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F6D)

    def lambda_4F85():
        OP_8F(0xFE, 0xDA52, 0x0, 0x2B16, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4F85)
    Sleep(200)
    OP_8C(0x101, 270, 400)
    Sleep(1000)

    ChrTalk(    #158
        0x101,
        "#1005F#2P慢、慢着！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #159
        0xE,
        (
            "#122F#8P话先说在前头……\x01",
            "可别想逃跑哦。\x02\x03",

            "#125F这里距离地面的高度是８０００亚矩。\x01",
            "你根本没有任何逃跑的机会。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_504C():
        OP_6D(57590, 0, 11310, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_504C)
    OP_8E(0xE, 0xC6AC, 0x0, 0x2B16, 0x7D0, 0x0)

    def lambda_5078():
        OP_8E(0xFE, 0xC15C, 0x0, 0x2AC6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5078)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    WaitChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    WaitChrThread(0x101, 0x1)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(1000)
    OP_6D(62560, 0, 12000, 2000)
    Sleep(500)

    ChrTalk(    #160
        0x101,
        (
            "#1002F#5P……………………………………\x02\x03",

            "#1007F叫我别想逃跑吗。\x02\x03",

            "越是这么说就越想试试看，\x01",
            "这应该算是人之常情吧。\x02\x03",

            "#1006F幸好教授和玲他们\x01",
            "好像都出去了……\x02\x03",

            "好……就这么决定了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5180():
        OP_6D(58740, 0, 11420, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5180)
    OP_8E(0x101, 0xD066, 0x0, 0x2A76, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)
    OP_8C(0x101, 270, 400)
    OP_8C(0x101, 180, 400)
    Sleep(500)
    OP_8C(0x101, 270, 400)
    Sleep(1000)
    OP_8C(0x101, 45, 400)
    OP_8E(0x101, 0xDF02, 0x0, 0x31F6, 0xBB8, 0x0)
    OP_8E(0x101, 0xDFF2, 0x0, 0x3778, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0x101, 45, 400)
    Sleep(500)
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8E(0x101, 0xDF84, 0x0, 0x297C, 0xBB8, 0x0)
    OP_8C(0x101, 270, 400)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 90, 600)
    Sleep(500)

    def lambda_526B():
        OP_6D(62560, 0, 12000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_526B)
    OP_8E(0x101, 0xF03C, 0x0, 0x2A9E, 0x1388, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #161
        0x101,
        (
            "#1002F#6P……………………………\x02\x03",

            "虽然…一旦掌握不好时机就会有性命危险，\x01",
            "但如果能够抓住这次机会……\x02\x03",

            "#1015F为了让他们放松警惕，\x01",
            "先老老实实地待上两个小时……\x02\x03",

            "#1006F……嗯！\x01",
            "看来值得一试呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8C(0x101, 270, 400)
    Sleep(500)

    def lambda_5374():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5374)
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 4)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #162
        0x101,
        (
            "#1007F#5P……原来这是\x01",
            "姐姐的珍贵遗物啊。\x02\x03",

            "#1027F#5P约修亚那笨蛋……\x01",
            "这种东西怎么可以轻易交给别人呀！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/C5400   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_22_4DDB end

    def Function_23_542A(): pass

    label("Function_23_542A")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0xD, 6240, 0, 4990, 270)
    SetChrPos(0xC, 4270, 0, 26120, 315)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xD, 32)
    SetChrChipByIndex(0xC, 32)
    OP_6D(4660, 0, 23820, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(44000, 0)
    OP_6E(265, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x8, 0x10)
    OP_72(0x8, 0x20)
    OP_22(0x6D, 0x0, 0x64)
    OP_6F(0x8, 0)
    OP_70(0x8, 0xF)
    OP_73(0x8)
    Sleep(1000)
    SetChrChipByIndex(0xC, 32)

    def lambda_54DE():
        OP_8E(0xFE, 0xF78, 0x0, 0x1694, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_54DE)

    def lambda_54F9():
        OP_6D(5620, 0, 5560, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54F9)

    def lambda_5511():
        OP_6C(66000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5511)
    Sleep(2000)
    OP_6F(0x8, 15)
    OP_70(0x8, 0x0)
    OP_71(0x8, 0x10)
    WaitChrThread(0x0, 0x1)
    SetChrChipByIndex(0xC, 32)
    SetChrSubChip(0xC, 0)
    Sleep(100)
    OP_8C(0xC, 90, 400)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    NpcTalk(    #163
        0xC,
        "强化猎兵",
        "#6P换班的时间到了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #164
        0xC,
        "强化猎兵",
        "#6P小丫头的情况怎样？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #165
        0xD,
        "强化猎兵",
        "#5P哈哈，很安分呢。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #166
        0xD,
        "强化猎兵",
        (
            "#5P就算是游击士，\x01",
            "到底还是小孩子。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #167
        0xD,
        "强化猎兵",
        "#5P恐怕正在床上发抖呢。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #168
        0xC,
        "强化猎兵",
        (
            "#6P哼……\x01",
            "居然要留下来看守这个小东西。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #169
        0xC,
        "强化猎兵",
        (
            "#6P真是够无聊的。\x01",
            "我也想参加启动作战啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #170
        0xD,
        "强化猎兵",
        (
            "#5P别发牢骚啦。\x01",
            "这是莱恩哈特大人的命令嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_1F(0x50, 0x3E8)
    OP_22(0xD6, 0x1, 0x46)
    Sleep(500)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(    #171
        0xD,
        "强化猎兵",
        "#5P……嗯？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #172
        0xC,
        "强化猎兵",
        "#6P什么，这声音是？\x02",
    )

    CloseMessageWindow()

    def lambda_573C():
        OP_6D(7090, 0, 5430, 1000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_573C)
    OP_8C(0xD, 90, 400)
    Sleep(500)
    OP_22(0x72, 0x0, 0x64)
    Sleep(1500)

    NpcTalk(    #173
        0xD,
        "强化猎兵",
        (
            "#6P喂！\x01",
            "你到底在干什么！？\x02",
        )
    )

    CloseMessageWindow()
    OP_23(0xD6)
    OP_22(0x134, 0x0, 0x64)
    Sleep(1000)
    OP_1F(0x64, 0x3E8)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #174
        0xC,
        "强化猎兵",
        "#6P喂，难不成……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #175
        0xD,
        "强化猎兵",
        "#6P逃走了吗！？\x02",
    )

    CloseMessageWindow()
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_72(0xA, 0x10)
    OP_72(0xA, 0x20)
    OP_22(0x6D, 0x0, 0x64)
    OP_6F(0xA, 0)
    OP_70(0xA, 0xF)
    OP_73(0xA)
    SetChrChipByIndex(0xD, 11)

    def lambda_584B():
        OP_8E(0xFE, 0x2134, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_584B)
    Sleep(100)
    SetChrChipByIndex(0xC, 11)

    def lambda_5870():
        OP_8E(0xFE, 0x2134, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5870)
    WaitChrThread(0xD, 0x1)
    SetChrFlags(0xD, 0x80)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    Fade(1000)
    OP_6D(52360, 0, 12450, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(56000, 0)
    OP_6E(281, 0)
    LoadEffect(0x1, "scraft\\\\sc000_11.eff")
    OP_71(0xA, 0x10)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_22(0x1C3, 0x0, 0x64)
    OP_0D()

    def lambda_590D():
        OP_6D(58180, 0, 12600, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_590D)
    OP_43(0xD, 0x1, 0x0, 0x1D)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0x1E)
    WaitChrThread(0xC, 0x1)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)

    NpcTalk(    #176
        0xC,
        "强化猎兵",
        "#6P啊，糟糕……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #177
        0xD,
        "强化猎兵",
        (
            "#6P怎、怎么会！？\x01",
            "她以为这里是哪里啊！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #178
        0xD,
        "强化猎兵",
        "#6P那丫头，难道想自杀吗！？\x02",
    )

    CloseMessageWindow()

    def lambda_59F7():
        OP_6D(61920, 0, 11630, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59F7)
    SetChrChipByIndex(0xD, 11)

    def lambda_5A14():
        OP_8E(0xFE, 0xF032, 0x0, 0x28F0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5A14)
    Sleep(300)
    SetChrChipByIndex(0xC, 11)

    def lambda_5A39():
        OP_8E(0xFE, 0xEC4A, 0x0, 0x2CE2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5A39)
    WaitChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 8)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 8)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    NpcTalk(    #179
        0xD,
        "强化猎兵",
        "#6P…………………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #180
        0xD,
        "强化猎兵",
        "#6P不行，可能掉下去了……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #181
        0xC,
        "强化猎兵",
        "#6P喂喂，饶了我吧……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #182
        0xC,
        "强化猎兵",
        (
            "#6P该怎么对莱恩哈特大人\x01",
            "交代才好？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #183
        0xC,
        "强化猎兵",
        (
            "#6P那个臭小鬼……\x01",
            "居然给我惹出这种麻烦！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_20(0x3E8)
    OP_21()
    SetChrPos(0x101, 63690, 2000, 11810, 270)

    ChrTalk(    #184
        0x101,
        "#6P你说谁～是臭小鬼？\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_1D(0x71)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 14)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 63500, 500, 11810, 270)
    ClearChrFlags(0x101, 0x80)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x1000)
    OP_99(0x101, 0x0, 0x2, 0x9C4)
    SetChrFlags(0x101, 0x800)

    def lambda_5C17():
        OP_99(0xFE, 0x3, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C17)
    OP_8F(0x101, 0xF1D6, 0xFFFFFF38, 0x2E22, 0x2EE0, 0x0)
    PlayEffect(0x1, 0x0, 0xC, 0, 800, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    OP_43(0xC, 0x0, 0x0, 0x1C)

    NpcTalk(    #185 op#A op#5
        0xC,
        "强化猎兵",
        "#15A#5P呜哇！\x05\x02",
    )


    def lambda_5CA9():
        OP_6D(59720, 0, 11940, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5CA9)
    WaitChrThread(0x101, 0x2)

    def lambda_5CC6():

        label("loc_5CC6")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_5CC6")

    QueueWorkItem2(0x101, 3, lambda_5CC6)

    def lambda_5CD7():
        OP_96(0xFE, 0xEE02, 0x0, 0x2E7C, 0x9C4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CD7)
    Sleep(100)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)

    def lambda_5D0E():

        label("loc_5D0E")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5D0E")

    QueueWorkItem2(0xD, 3, lambda_5D0E)

    def lambda_5D1F():
        OP_96(0xFE, 0xE7FE, 0x0, 0x1E96, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_5D1F)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 14)

    def lambda_5D51():
        OP_99(0xFE, 0x5, 0x6, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D51)
    WaitChrThread(0x101, 0x2)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x800)
    WaitChrThread(0xD, 0x2)
    Sleep(500)
    WaitChrThread(0xC, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_5D88():
        OP_6D(59670, 0, 10950, 1000)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_5D88)

    def lambda_5DA0():
        OP_6E(298, 1000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5DA0)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    LoadEffect(0x2, "map\\\\mp003_00.eff")
    LoadEffect(0x3, "monster\\\\msc0310.eff")
    WaitChrThread(0xC, 0x0)
    WaitChrThread(0xC, 0x1)
    OP_44(0x101, 0x3)

    NpcTalk(    #186
        0xD,
        "强化猎兵",
        "#4P你、你！？\x02",
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)
    TurnDirection(0x101, 0xD, 500)
    Sleep(500)

    ChrTalk(    #187
        0x101,
        "#1005F#5P太天真了，大叔！\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0xD, 0x0, 0x0, 0x18)
    OP_43(0xD, 0x1, 0x0, 0x19)

    def lambda_5E6D():
        OP_6D(58930, 0, 12880, 600)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_5E6D)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x101, 0x4)

    def lambda_5E8F():
        OP_96(0xFE, 0xE8A8, 0x1F4, 0x3B4C, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5E8F)
    WaitChrThread(0x101, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)

    def lambda_5EBC():
        OP_6D(55620, 0, 9400, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_5EBC)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_5ED9():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5ED9)

    def lambda_5EE7():
        OP_96(0xFE, 0xDAF2, 0xC8, 0x36BA, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5EE7)
    Sleep(50)
    OP_43(0xD, 0x0, 0x0, 0x1A)
    OP_43(0xD, 0x1, 0x0, 0x1B)
    WaitChrThread(0x101, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_5F2C():
        OP_8C(0xFE, 225, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F2C)

    def lambda_5F3A():
        OP_96(0xFE, 0xD0CA, 0x0, 0x285A, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5F3A)
    WaitChrThread(0x101, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_44(0xD, 0x3)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 17)

    def lambda_5F70():
        OP_6D(59460, 0, 8740, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_5F70)
    OP_97(0x101, 0xD7DC, 0x24CC, 0xFFFE7960, 0x2EE0, 0x1)

    def lambda_5F9D():
        OP_8C(0xFE, 90, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F9D)

    def lambda_5FAB():
        OP_96(0xFE, 0xE1A0, 0x0, 0x1EA0, 0xC8, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5FAB)
    Sleep(100)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 0)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_5FDD():
        OP_99(0x101, 0x1, 0xC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5FDD)
    OP_44(0xD, 0x0)
    OP_44(0xD, 0x1)
    Sleep(400)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0x0, 0xD, 0, 700, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)

    def lambda_6045():
        OP_6D(61000, 0, 8620, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6045)

    def lambda_605D():
        OP_6B(2810, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_605D)
    OP_44(0xD, 0x3)
    OP_8C(0xD, 270, 0)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x2)
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x1000)

    def lambda_6091():
        OP_8F(0xFE, 0xF03C, 0x5DC, 0x1F0E, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6091)
    SetChrChipByIndex(0xD, 13)
    SetChrSubChip(0xD, 7)
    WaitChrThread(0xD, 0x1)
    OP_7C(0x64, 0x32, 0x1388, 0x3E8)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    def lambda_60DA():
        OP_8F(0xD, 0xF03C, 0x0, 0x1F0E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_60DA)
    Sleep(100)

    def lambda_60FA():
        OP_8F(0xD, 0xF03C, 0x0, 0x1F0E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_60FA)
    Sleep(100)

    def lambda_611A():
        OP_8F(0xD, 0xF03C, 0x0, 0x1F0E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_611A)
    WaitChrThread(0xD, 0x1)
    ClearChrFlags(0xD, 0x20)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 15)
    SetChrSubChip(0xD, 0)
    OP_99(0xD, 0x0, 0x2, 0x5DC)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #188
        0xD,
        "强化猎兵",
        "#5P呜哇，呼呼……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    Sleep(500)
    OP_8E(0x101, 0xE92A, 0x0, 0x1F67, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #189
        0x101,
        (
            "#1028F#6P哼哼。\x01",
            "可别小看游击士哦。\x02\x03",

            "而且你们太没礼貌了吧？\x01",
            "竟然称呼少女为臭小鬼。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #190
        0xD,
        "强化猎兵",
        "#5P真、真是看走眼了……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #191
        0xD,
        "强化猎兵",
        "#5P我可没有那么说啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#1004F#6P哦，是吗？\x02\x03",

            "#1006F算了，大叔你也是同罪。\x01",
            "暂且做个替罪羊吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 19)
    OP_0D()
    Sleep(300)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x101, 0x20)

    def lambda_62D8():
        OP_99(0x101, 0x0, 0xC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_62D8)
    Sleep(500)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0x32, 0x1388, 0x3E8)
    PlayEffect(0x1, 0x0, 0xD, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_6338():
        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_6338)
    WaitChrThread(0x101, 0x0)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)

    NpcTalk(    #193 op#5
        0xD,
        "强化猎兵",
        "#5P……嗯～…………\x05\x02",
    )

    Sleep(1500)
    Fade(500)
    OP_22(0x20C, 0x0, 0x64)
    SetChrPos(0xD, 60700, 0, 7800, 270)
    ClearChrFlags(0xD, 0x1)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 18)
    SetChrSubChip(0xD, 15)
    OP_0D()
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xD, 0x40)
    Sleep(1500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #194
        0x101,
        "#1007F#6P那～么……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(500)

    ChrTalk(    #195
        0x101,
        (
            "#1006F#5P增援大概很快就会来了，\x01",
            "还是赶快逃跑吧。\x02\x03",

            "必须想个脱逃的办法才行……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 16)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #196
        0x101,
        (
            "#1027F#5P（我不会放弃的……）\x02\x03",

            "（一定要再次见到约修亚……\x01",
            "  ……和那个笨蛋重逢……）\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(500)

    ChrTalk(    #197
        0x101,
        "#1005F#5P#3S（我绝对不会放弃！）\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x1000)
    OP_6D(59690, 0, 8039, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_A2(0x1C1D)
    OP_28(0x99, 0x4, 0x2)
    OP_28(0x99, 0x4, 0x8)
    OP_28(0x99, 0x1, 0x1)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_23_542A end

    def Function_24_65A2(): pass

    label("Function_24_65A2")

    PlayEffect(0x3, 0x1, 0xD, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x3, 0x1, 0xD, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_82(0x1, 0x2)
    Return()

    # Function_24_65A2 end

    def Function_25_661A(): pass

    label("Function_25_661A")

    Sleep(300)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 60520, 0, 10840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 60910, 0, 12450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 60540, 500, 14400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 61770, 800, 15340, 90, 90, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Return()

    # Function_25_661A end

    def Function_26_671C(): pass

    label("Function_26_671C")

    Sleep(100)
    PlayEffect(0x3, 0x1, 0xD, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x3, 0x1, 0xD, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x3, 0x1, 0xD, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_82(0x1, 0x2)
    Return()

    # Function_26_671C end

    def Function_27_67D3(): pass

    label("Function_27_67D3")

    Sleep(300)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 59540, 500, 15040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 57490, 1000, 16020, 0, 90, 90, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 56080, 800, 15120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 55920, 200, 13920, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 53370, 0, 12980, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 53800, 0, 10980, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 52880, 0, 8770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 52810, 0, 8230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Return()

    # Function_27_67D3 end

    def Function_28_69D1(): pass

    label("Function_28_69D1")

    SetChrChipByIndex(0xC, 13)
    SetChrSubChip(0xC, 0)

    def lambda_69E1():
        OP_96(0xFE, 0xE010, 0x0, 0x2E40, 0x7D0, 0x2710)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_69E1)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x1)
    SetChrChipByIndex(0xC, 18)
    SetChrSubChip(0xC, 11)
    OP_96(0xC, 0xD96C, 0x0, 0x2F30, 0x3E8, 0x1F40)
    OP_96(0xC, 0xD39A, 0x0, 0x2F26, 0x12C, 0x1770)
    Return()

    # Function_28_69D1 end

    def Function_29_6A41(): pass

    label("Function_29_6A41")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 49790, 0, 10830, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_6A68():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6A68)
    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0xD5E8, 0x0, 0x27BA, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_29_6A41 end

    def Function_30_6A93(): pass

    label("Function_30_6A93")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 49790, 0, 10830, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_6ABA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6ABA)
    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0xD5E8, 0x0, 0x2E22, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_30_6A93 end

    def Function_31_6AE5(): pass

    label("Function_31_6AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6AF2")
    Return()

    label("loc_6AF2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B17")
    Call(0, 58)
    Call(0, 59)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_6B17")

    Fade(1000)
    OP_4A(0xF, 0)
    OP_4A(0x10, 0)
    OP_4A(0x11, 0)
    OP_4A(0x14, 0)
    OP_4A(0x15, 0)
    OP_4A(0x12, 0)
    OP_4A(0x13, 0)
    OP_4A(0x16, 0)
    SetChrPos(0x15, -81520, 0, -331440, 225)
    OP_6D(-87930, 0, -344320, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(57000, 0)
    OP_6E(343, 0)
    SetChrPos(0x10B, -88230, 0, -342500, 0)
    SetChrPos(0x102, -87830, 0, -343500, 0)
    SetChrPos(0x101, -89410, 0, -343500, 0)
    SetChrPos(0xF9, -88810, 0, -344500, 0)
    Sleep(500)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x10B, 0x1, 0x0, 0x20)

    def lambda_6BFC():
        OP_6D(-82340, 0, -335690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6BFC)

    def lambda_6C14():
        OP_67(0, 6000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6C14)

    def lambda_6C2C():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C2C)

    def lambda_6C3C():
        OP_6C(57000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_6C3C)

    def lambda_6C4C():
        OP_6E(343, 2000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_6C4C)
    OP_43(0x101, 0x1, 0x0, 0x22)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0x21)
    Sleep(400)
    OP_43(0xF9, 0x1, 0x0, 0x23)
    WaitChrThread(0x10B, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #198
        0x10B,
        "#415F#4S#6P各位！\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_6D68():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6D68)
    Sleep(50)

    def lambda_6D7B():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6D7B)
    Sleep(50)

    def lambda_6D8E():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6D8E)
    Sleep(50)

    def lambda_6DA1():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6DA1)
    Sleep(50)

    def lambda_6DB4():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6DB4)
    Sleep(50)

    def lambda_6DC7():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6DC7)
    Sleep(50)

    def lambda_6DDA():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6DDA)
    Sleep(50)

    def lambda_6DED():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6DED)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #199
        0x10,
        "#201F#5P什…什么…！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xF,
        (
            "#192F#5P乔丝特……\x01",
            "还有这小子！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E41():
        OP_67(0, 5660, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6E41)

    def lambda_6E59():
        OP_6D(-84260, 0, -335810, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E59)

    def lambda_6E71():
        OP_8E(0xFE, 0xFFFEB60A, 0x0, 0xFFFADE2C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6E71)
    Sleep(500)

    def lambda_6E91():
        OP_8E(0xFE, 0xFFFEB790, 0x0, 0xFFFAE318, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_6E91)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #201
        0x11,
        "#5P小、小姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x12,
        "怎、怎么会在这里！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x10B,
        (
            "#415F#6P太、太好了……\x01",
            "大家都平安无事吧……\x02\x03",

            "现在就来救你们，等等哦！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0xF, 0x0)

    ChrTalk(    #204
        0x10,
        (
            "#203F#5P救、救我们……\x02\x03",

            "#201F……喂，约修亚！\x01",
            "到底怎么回事啊！？\x02\x03",

            "为什么连你们\x01",
            "都来到这个浮游都市了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        "#1042F#6P嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #206
        "\x07\x05向空贼们简单地说明了之前的经过。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #207
        0xF,
        (
            "#490F#5P原来如此……\x01",
            "还有这种事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x10,
        (
            "#204F#5P我说啊，乔丝特……\x02\x03",

            "#206F我们可是为了掩护你逃走\x01",
            "才会被捕的，你难道不知道吗？\x02\x03",

            "可你现在却又……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x10B,
        (
            "#214F#6P别、别自作主张了！\x02\x03",

            "我才不想抛下大家，\x01",
            "自己一个人得救！\x02\x03",

            "与其这样的话，\x01",
            "我宁可和哥哥们一起被关在这里！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x10,
        (
            "#201F#5P笨蛋，你是女人吧！\x02\x03",

            "总该稍微担心一下\x01",
            "自己的人身安全啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x10B,
        (
            "#216F#6P这、这么说太狡猾了！\x02\x03",

            "#215F吉尔哥你\x01",
            "总是在这种时候\x01",
            "才把我当女人对待！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71F1")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_722F")

    label("loc_71F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7218")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_722F")

    label("loc_7218")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_722F")

    Sleep(1000)

    ChrTalk(    #212
        0x101,
        (
            "#1016F#6P（这、这个……\x01",
            "兄妹之间的感情真好啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72A6")

    ChrTalk(    #213
        0x107,
        (
            "#067F#6P（嘿嘿……\x01",
            "稍微有点羡慕呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741A")

    label("loc_72A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72E3")

    ChrTalk(    #214
        0x105,
        (
            "#1168F#6P（呵呵……\x01",
            "稍微有点羡慕啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741A")

    label("loc_72E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_732A")

    ChrTalk(    #215
        0x109,
        (
            "#1061F#6P（哈哈……\x01",
            "真是令人莞尔的兄妹吵架啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741A")

    label("loc_732A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7370")

    ChrTalk(    #216
        0x103,
        (
            "#027F#6P（呵呵……\x01",
            "真是令人莞尔的兄妹吵架啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741A")

    label("loc_7370")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73B4")

    ChrTalk(    #217
        0x104,
        (
            "#031F#6P（呼……\x01",
            "真是感情深厚的一对兄妹啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741A")

    label("loc_73B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73E5")

    ChrTalk(    #218
        0x106,
        "#556F#6P（嘿………是啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_741A")

    label("loc_73E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_741A")

    ChrTalk(    #219
        0x108,
        (
            "#071F#6P（哈哈……\x01",
            "感情真好呀。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_741A")


    ChrTalk(    #220
        0xF,
        (
            "#192F#5P喂喂，别在这种地方\x01",
            "吵架啊。\x02\x03",

            "#199F你们两个真是……\x01",
            "都什么时候了还耍小孩子脾气！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x10B,
        "#215F#6P多伦哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x10,
        "#207F#2P可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xF,
        (
            "#198F#5P既然来了，那也没办法了。\x01",
            "只能一起逃出去了吧。\x02\x03",

            "#199F那么，小子……\x01",
            "你要怎样把我们从这里弄出去？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_751C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_751C)
    Sleep(50)

    def lambda_752F():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_752F)
    Sleep(500)

    ChrTalk(    #224
        0x102,
        (
            "#1035F#6P……这个嘛。\x02\x03",

            "#1042F看来这个能量障壁\x01",
            "已经完全被锁上了。\x02\x03",

            "要解除保护，\x01",
            "说实话，确实很难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x10,
        "#204F#5P……原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x10B,
        "#216F#5P怎，怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x101,
        (
            "#1015F#5P嗯～那么\x01",
            "不能用暴力弄开吗？\x02\x03",

            "比如使用炸弹之类的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)

    ChrTalk(    #228
        0x102,
        (
            "#1043F#4P不行，这个能量障壁\x01",
            "不是普通炸弹能伤得了的。\x02\x03",

            "就算可以炸开，强大的爆破力\x01",
            "可能也会危及到吉尔他们。\x02\x03",

            "#1042F现在也只能去\x01",
            "找一张最新密码卡来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x101,
        "#1004F#5P密码卡？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x10B,
        (
            "#415F#5P用、用那个\x01",
            "就能解除这个障壁吗！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_770C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_770C)
    Sleep(100)

    def lambda_771F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_771F)

    def lambda_772D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_772D)
    OP_6D(-84260, 0, -340520, 2000)

    ChrTalk(    #231
        0x102,
        (
            "#1040F#5P只要有那张密码卡，应该\x01",
            "就能通过终端解除障壁。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7788():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7788)
    Sleep(100)

    def lambda_779B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_779B)
    OP_6D(-84260, 0, -335810, 1500)

    ChrTalk(    #232
        0x102,
        (
            "#1042F#4P我以前潜入时用的那张\x01",
            "大概已经无法再使用了，\x01",
            "所以需要找到最新的卡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x10B,
        "#212F#5P原、原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x101,
        (
            "#1015F#5P那么，最新的密码卡\x01",
            "放在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x102,
        (
            "#1035F#4P──前方区域的第二层。\x02\x03",

            "#1042F应该被保管在以前\x01",
            "囚禁你的房间周边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        "#1002F#5P是吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78EC")

    ChrTalk(    #237
        0x107,
        (
            "#062F#6P看来赶快去\x01",
            "调查为好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A37")

    label("loc_78EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7923")

    ChrTalk(    #238
        0x105,
        (
            "#1162F#6P看来赶快去\x01",
            "调查为好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A37")

    label("loc_7923")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7958")

    ChrTalk(    #239
        0x109,
        (
            "#1060F#6P那么，赶快\x01",
            "去调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A37")

    label("loc_7958")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7990")

    ChrTalk(    #240
        0x103,
        (
            "#027F#6P既然如此\x01",
            "就赶快去调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A37")

    label("loc_7990")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79CA")

    ChrTalk(    #241
        0x104,
        (
            "#035F#6P呼，那就需要\x01",
            "赶快去调查了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A37")

    label("loc_79CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A02")

    ChrTalk(    #242
        0x106,
        (
            "#051F#6P既然如此\x01",
            "就赶快去调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A37")

    label("loc_7A02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A37")

    ChrTalk(    #243
        0x108,
        (
            "#070F#6P既然如此\x01",
            "就赶快去调查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A37")


    def lambda_7A3D():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_7A3D)
    Sleep(50)

    def lambda_7A50():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A50)
    Sleep(50)

    def lambda_7A63():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_7A63)
    Sleep(50)

    def lambda_7A76():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A76)
    WaitChrThread(0x10B, 0x1)
    Sleep(500)

    ChrTalk(    #244
        0x10B,
        (
            "#214F#6P吉尔哥！多伦哥！\x01",
            "还有大家！\x02\x03",

            "委屈你们\x01",
            "再耐心等等吧！\x02\x03",

            "我们会马上找到密码卡\x01",
            "回来的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x10,
        "#203F#5P唉……没办法了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xF,
        (
            "#198F#5P小子……\x01",
            "还有游击士的小姑娘。\x02\x03",

            "#490F麻烦你们了，\x01",
            "可别让那个冒失鬼乱来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x102,
        "#1040F#6P啊啊，交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        (
            "#1006F#6P嗯，我们会\x01",
            "管好她的，放心吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 400)
    Sleep(300)

    ChrTalk(    #249
        0x10B,
        (
            "#210F#2P哼，哼……\x02\x03",

            "你明明比我还莽撞无脑很多，\x01",
            "竟然还敢说那种话啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 400)

    ChrTalk(    #250
        0x101,
        "#1019F#6P你，你说什么～？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)

    ChrTalk(    #251
        0x102,
        (
            "#1052F#2P好了好了，适可而止。\x02\x03",

            "#1042F──那么，\x01",
            "马上返回出口附近吧。\x02\x03",

            "要去前方区域第２层\x01",
            "需要使用反方向\x01",
            "的升降梯呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x102, 400)

    ChrTalk(    #252
        0x10B,
        "#212F#5P知、知道了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #253
        0x101,
        "#1006F#5P那么，去吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-87640, 0, -336030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87640, 0, -336030, 180)
    SetChrPos(0x1, -87640, 0, -336030, 180)
    SetChrPos(0x2, -87640, 0, -336030, 180)
    SetChrPos(0x3, -87640, 0, -336030, 180)
    SetChrPos(0xF, -84180, 0, -335080, 270)
    OP_8C(0xF, 270, 0)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    OP_4B(0x11, 255)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    OP_4B(0x12, 255)
    OP_4B(0x13, 255)
    OP_4B(0x16, 255)
    OP_0D()
    OP_A2(0x2223)
    OP_28(0x9E, 0x1, 0x20)
    OP_28(0x9E, 0x1, 0x40)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_31_6AE5 end

    def Function_32_7DDD(): pass

    label("Function_32_7DDD")

    OP_8E(0xFE, 0xFFFEB146, 0x0, 0xFFFADD14, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_32_7DDD end

    def Function_33_7DF9(): pass

    label("Function_33_7DF9")

    OP_8E(0xFE, 0xFFFEAFC0, 0x0, 0xFFFAD8AA, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_33_7DF9 end

    def Function_34_7E15(): pass

    label("Function_34_7E15")

    OP_8E(0xFE, 0xFFFEACD2, 0x0, 0xFFFADDDC, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_34_7E15 end

    def Function_35_7E31(): pass

    label("Function_35_7E31")

    OP_8E(0xFE, 0xFFFEA926, 0x0, 0xFFFAD828, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_35_7E31 end

    def Function_36_7E4D(): pass

    label("Function_36_7E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_END)), "loc_7E5B")
    Call(0, 45)
    Jump("loc_7EA5")

    label("loc_7E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7E75")
    Call(0, 45)
    Jump("loc_7EA5")

    label("loc_7E75")


    AnonymousTalk(    #254
        (
            "\x07\x05终端被锁定了。\x01",
            "似乎需要密码卡。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_7EA5")

    TalkEnd(0xFF)
    Return()

    # Function_36_7E4D end

    def Function_37_7EA9(): pass

    label("Function_37_7EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8204")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ED6")
    Call(0, 58)
    Call(0, 59)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_7ED6")

    Fade(1000)
    OP_6D(-127570, 0, -60040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, -127670, 0, -58950, 90)
    SetChrPos(0x101, -126930, 0, -59970, 0)
    SetChrPos(0x10B, -128550, 0, -59930, 45)
    SetChrPos(0xF9, -127840, 0, -61020, 0)
    OP_0D()
    OP_6F(0x25, 0)
    OP_70(0x25, 0x3C)
    OP_22(0x2B, 0x0, 0x64)
    OP_73(0x25)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #255
        "\x07\x00得到了\x1F\x10\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x410, 1)

    ChrTalk(    #256
        0x10B,
        "#213F#6P难道那就是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x101,
        (
            "#1004F#4P刚刚说的\x01",
            "最新的密码卡？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 400)
    Sleep(300)

    ChrTalk(    #258
        0x102,
        (
            "#1040F#5P嗯……没错。\x02\x03",

            "通过这个，牢房中的终端\x01",
            "就能解除障壁哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x101,
        "#1018F#4P太好了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x10B,
        "#415F#6P太好了……这下就……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80C1")

    ChrTalk(    #261
        0x107,
        (
            "#067F嘿嘿……那么，\x01",
            "赶快返回牢房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F6")

    label("loc_80C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80F7")

    ChrTalk(    #262
        0x105,
        (
            "#1168F呵呵……\x01",
            "赶快返回牢房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F6")

    label("loc_80F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_812B")

    ChrTalk(    #263
        0x109,
        (
            "#1061F那么，马上\x01",
            "返回牢房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F6")

    label("loc_812B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8160")

    ChrTalk(    #264
        0x103,
        (
            "#021F呵呵……\x01",
            "赶快返回牢房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F6")

    label("loc_8160")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8195")

    ChrTalk(    #265
        0x104,
        (
            "#031F呼，那么尽快\x01",
            "返回牢房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F6")

    label("loc_8195")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81C6")

    ChrTalk(    #266
        0x106,
        (
            "#051F好～马上\x01",
            "返回牢房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F6")

    label("loc_81C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81F6")

    ChrTalk(    #267
        0x108,
        (
            "#070F好……\x01",
            "马上返回牢房吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F6")

    OP_A2(0x2225)
    OP_28(0x9E, 0x1, 0x80)
    EventEnd(0x0)
    Jump("loc_823D")

    label("loc_8204")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #268
        "\x07\x05宝箱里什么也没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_823D")

    Return()

    # Function_37_7EA9 end

    def Function_38_823E(): pass

    label("Function_38_823E")

    EventBegin(0x0)
    FadeToBright(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_825E")
    Call(0, 58)
    Call(0, 59)

    label("loc_825E")

    OP_6D(-42070, 0, 75240, 0)
    OP_67(0, 7490, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -42880, 0, 76490, 180)
    SetChrPos(0x102, -42880, 0, 76490, 180)
    SetChrPos(0x10B, -42880, 0, 76490, 180)
    SetChrPos(0xF9, -42880, 0, 76490, 180)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x12, 0x10)
    OP_72(0x12, 0x20)
    OP_6F(0x12, 0)
    OP_70(0x12, 0xF)
    OP_73(0x12)
    Sleep(300)

    def lambda_8319():
        OP_6D(-42610, 0, 71440, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8319)

    def lambda_8331():
        OP_67(0, 6710, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8331)
    OP_43(0x101, 0x0, 0x0, 0x27)
    Sleep(700)
    OP_43(0x102, 0x0, 0x0, 0x28)
    Sleep(600)
    OP_43(0x10B, 0x0, 0x0, 0x29)
    Sleep(600)
    OP_43(0xF9, 0x0, 0x0, 0x2A)
    Sleep(1000)
    OP_71(0x12, 0x10)
    OP_6F(0x12, 15)
    OP_70(0x12, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF9, 0x0)
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #269
        0x101,
        (
            "#1015F#6P嗯，这一带的确是\x01",
            "我当初被监禁的区域呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x102,
        (
            "#1035F#5P嗯，是前方区域的第２层。\x02\x03",

            "#1040F也是用来向猎兵们\x01",
            "传达作战方案的会议室。\x02\x03",

            "最新的密码卡\x01",
            "应该被保管在这附近。  \x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #271
        0x10B,
        (
            "#212F#5P那、那么\x01",
            "赶快调查看看吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 400)

    ChrTalk(    #272
        0x101,
        (
            "#1007F#6P好好，知道啦。\x02\x03",

            "#1006F总之先把房间\x01",
            "一个个都调查一遍吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22B2)
    EventEnd(0x0)
    Return()

    # Function_38_823E end

    def Function_39_84E3(): pass

    label("Function_39_84E3")

    OP_8E(0xFE, 0xFFFF575E, 0x0, 0x10F68, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_39_84E3 end

    def Function_40_8517(): pass

    label("Function_40_8517")

    OP_8E(0xFE, 0xFFFF5740, 0x0, 0x11E22, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF53C6, 0x0, 0x1140E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_40_8517 end

    def Function_41_8547(): pass

    label("Function_41_8547")

    OP_8E(0xFE, 0xFFFF5740, 0x0, 0x11E22, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5C54, 0x0, 0x11512, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_41_8547 end

    def Function_42_8577(): pass

    label("Function_42_8577")

    OP_8E(0xFE, 0xFFFF5858, 0x0, 0x11904, 0x7D0, 0x0)
    Return()

    # Function_42_8577 end

    def Function_43_858C(): pass

    label("Function_43_858C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9063")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85BD")
    Call(0, 58)
    Call(0, 59)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_85BD")

    Fade(1000)
    OP_6D(-37810, 0, -66450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -37980, 0, -67260, 90)
    SetChrPos(0x102, -38640, 0, -66330, 90)
    SetChrPos(0x10B, -39140, 0, -67430, 90)
    SetChrPos(0xF9, -39800, 0, -66450, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #273
        0x101,
        "#1004F#6P咦，这个升降梯是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x102,
        (
            "#1042F#5P是在『圣堂』和『引擎室』\x01",
            "之间用来移动的升降梯。\x02\x03",

            "由于要进行声纹模式的认证，\x01",
            "所以只有『执行者』以上的人才能使用。\x02\x03",

            "#1035F看来只有放弃这里了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #275
        0x101,
        "#1007F#4P是吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x102, 400)
    Sleep(300)

    ChrTalk(    #276
        0x10B,
        (
            "#213F#6P……对了，\x01",
            "声纹模式是什么？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10B, 400)
    Sleep(300)

    ChrTalk(    #277
        0x102,
        (
            "#1040F#5P每个人的声音频率\x01",
            "都是不同的。\x02\x03",

            "由机械对声音进行识别，\x01",
            "借此来判别是否有资格……\x02\x03",

            "似乎就是这样的装置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x10B,
        "#414F#6P原、原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x101,
        (
            "#1016F#4P好像懂了，\x01",
            "又好像不懂……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_892F")

    ChrTalk(    #280
        0x107,
        (
            "#561F#6P不过，真是高超的技术啊……\x02\x03",

            "#063F……对了，约修亚哥哥。\x02\x03",

            "这艘飞船和人形兵器\x01",
            "究竟都是谁制造的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x102,
        (
            "#1035F#5P这个啊……\x02\x03",

            "#1042F听说是\x01",
            "『蛇之使徒』之一的\x01",
            "诺华提斯博士…\x02\x03",

            "结社使用的导力机械，\x01",
            "全都是由那个博士所率领的\x01",
            "『十三工房』开发出来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F55")

    label("loc_892F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A37")

    ChrTalk(    #282
        0x105,
        (
            "#1167F#6P真的是很高超的技术……\x02\x03",

            "#1162F……对了，约修亚。\x02\x03",

            "这艘飞船和人形兵器\x01",
            "究竟都是谁制造的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x102,
        (
            "#1035F#5P这个啊……\x02\x03",

            "#1042F听说是\x01",
            "『蛇之使徒』之一的\x01",
            "诺华提斯博士…\x02\x03",

            "结社使用的导力机械，\x01",
            "全都是由那个博士所率领的\x01",
            "『十三工房』开发出来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F55")

    label("loc_8A37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B3D")

    ChrTalk(    #284
        0x109,
        (
            "#1068F#6P真是高超的技术啊……\x02\x03",

            "#1063F……对了，约修亚。\x02\x03",

            "这艘飞船和人形兵器\x01",
            "究竟都是谁制造的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x102,
        (
            "#1035F#5P这个啊……\x02\x03",

            "#1042F听说是\x01",
            "『蛇之使徒』之一的\x01",
            "诺华提斯博士…\x02\x03",

            "结社使用的导力机械，\x01",
            "全都是由那个博士所率领的\x01",
            "『十三工房』开发出来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F55")

    label("loc_8B3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C41")

    ChrTalk(    #286
        0x103,
        (
            "#025F#6P真是高超的技术啊……\x02\x03",

            "#022F……对了，约修亚。\x02\x03",

            "这艘飞船和人形兵器\x01",
            "究竟都是谁制造的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x102,
        (
            "#1035F#5P这个啊……\x02\x03",

            "#1042F听说是\x01",
            "『蛇之使徒』之一的\x01",
            "诺华提斯博士…\x02\x03",

            "结社使用的导力机械，\x01",
            "全都是由那个博士所率领的\x01",
            "『十三工房』开发出来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F55")

    label("loc_8C41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D41")

    ChrTalk(    #288
        0x104,
        (
            "#035F#6P真是高超的技术啊。\x02\x03",

            "#030F……对了约修亚。\x02\x03",

            "这艘飞船和人形兵器\x01",
            "究竟都是谁制造的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x102,
        (
            "#1035F#5P这个啊……\x02\x03",

            "#1042F听说是\x01",
            "『蛇之使徒』之一的\x01",
            "诺华提斯博士…\x02\x03",

            "结社使用的导力机械，\x01",
            "全都是由那个博士所率领的\x01",
            "『十三工房』开发出来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F55")

    label("loc_8D41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E54")

    ChrTalk(    #290
        0x106,
        (
            "#551F#6P真是的，到处都是一些\x01",
            "古怪的小玩意……\x02\x03",

            "#555F……喂，约修亚。\x02\x03",

            "这艘飞船和人形兵器\x01",
            "究竟都是谁制造的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x102,
        (
            "#1035F#5P这个啊……\x02\x03",

            "#1042F听说是\x01",
            "『蛇之使徒』之一的\x01",
            "诺华提斯博士…\x02\x03",

            "结社使用的导力机械，\x01",
            "全都是由那个博士所率领的\x01",
            "『十三工房』开发出来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F55")

    label("loc_8E54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F55")

    ChrTalk(    #292
        0x108,
        (
            "#074F#6P相当了不起的技术呢。\x02\x03",

            "#072F……对了，约修亚。\x02\x03",

            "这艘飞船和人形兵器\x01",
            "究竟都是谁制造的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x102,
        (
            "#1035F#5P这个啊……\x02\x03",

            "#1042F听说是\x01",
            "『蛇之使徒』之一的\x01",
            "诺华提斯博士…\x02\x03",

            "结社使用的导力机械，\x01",
            "全都是由那个博士所率领的\x01",
            "『十三工房』开发出来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F55")


    ChrTalk(    #294
        0x10B,
        "#212F#6P『十三工房』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        (
            "#1007F#4P嗯……\x01",
            "虽然不知道是个怎样的人……\x02\x03",

            "#1019F但感觉他好像比拉赛尔博士\x01",
            "还要更加疯狂的样子呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 400)
    Sleep(300)

    ChrTalk(    #296
        0x102,
        (
            "#1043F#5P疯狂吗……\x01",
            "老实说，是个神秘莫测的人哦。\x02\x03",

            "#1035F……不过包括教授在内，\x01",
            "『蛇之使徒』全体人员也都是这样。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2226)
    EventEnd(0x0)
    Jump("loc_90B4")

    label("loc_9063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90B4")
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #297
        "\x07\x05升降机的门牢牢地关着\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_90B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90FF")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #298
        "\x07\x05升降机的门牢牢地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_90FF")

    Return()

    # Function_43_858C end

    def Function_44_9100(): pass

    label("Function_44_9100")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x410), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_910D")
    Return()

    label("loc_910D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_918B")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x151E4), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x159B4), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x539E4), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x53FC0), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_918A")
    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(200)
    Call(0, 45)
    Jump("loc_918B")

    label("loc_918A")

    Return()

    label("loc_918B")

    Return()

    # Function_44_9100 end

    def Function_45_918C(): pass

    label("Function_45_918C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91A3")
    Call(0, 58)
    Call(0, 59)

    label("loc_91A3")

    Fade(1000)
    OP_6D(-86740, 0, -342830, 0)
    OP_67(0, 7350, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -88010, 0, -343970, 90)
    SetChrPos(0x102, -87600, 0, -343010, 90)
    SetChrPos(0x10B, -88360, 0, -342220, 90)
    SetChrPos(0xF9, -88850, 0, -343260, 90)
    OP_0D()
    Sleep(500)
    FadeToBright(0, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_929E")
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_71(0x23, 0x4)
    Sleep(100)
    OP_72(0x24, 0x4)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #299
        "\x07\x05──认证完毕。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_929E")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #300
        (
            "\x07\x05请选择想解除锁定的\x01",
            "障壁号码。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #301
        "\x18\x07\x05输入想解除的障壁号码\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【１号】\x01",      # 0
            "【２号】\x01",      # 1
            "【３号】\x01",      # 2
            "【４号】\x01",      # 3
            "【５号】\x01",      # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_9395"),
        (2, "loc_9540"),
        (3, "loc_96EB"),
        (4, "loc_9896"),
        (0, "loc_9A41"),
        (SWITCH_DEFAULT, "loc_9FAF"),
    )


    label("loc_9395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9478")
    OP_6D(-83240, 0, -320400, 3000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x4)
    Sleep(500)
    OP_6F(0x4, 35)
    OP_70(0x4, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x2228)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_953D")

    label("loc_9478")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #302
        (
            "\x07\x05２号的锁定\x01",
            "已经被解除。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    TalkEnd(0xFF)

    label("loc_953D")

    Jump("loc_9FAF")

    label("loc_9540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9623")
    OP_6D(-83240, 0, -309340, 3000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x5)
    Sleep(500)
    OP_6F(0x5, 35)
    OP_70(0x5, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x5)
    OP_A2(0x2229)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_96E8")

    label("loc_9623")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #303
        (
            "\x07\x05３号的锁定\x01",
            "已经被解除。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    TalkEnd(0xFF)

    label("loc_96E8")

    Jump("loc_9FAF")

    label("loc_96EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97CE")
    OP_6D(-83240, 0, -299470, 3000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x6)
    Sleep(500)
    OP_6F(0x6, 35)
    OP_70(0x6, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x6)
    OP_A2(0x222A)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_9893")

    label("loc_97CE")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #304
        (
            "\x07\x05４号的锁定\x01",
            "已经被解除。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    TalkEnd(0xFF)

    label("loc_9893")

    Jump("loc_9FAF")

    label("loc_9896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9979")
    OP_A2(0x222B)
    OP_6D(-83240, 0, -289000, 3000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x7)
    Sleep(500)
    OP_6F(0x7, 35)
    OP_70(0x7, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x7)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_9A3E")

    label("loc_9979")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #305
        (
            "\x07\x05５号的锁定\x01",
            "已经被解除。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    TalkEnd(0xFF)

    label("loc_9A3E")

    Jump("loc_9FAF")

    label("loc_9A41")

    SetMessageWindowPos(-1, -1, -1, -1)
    OP_6D(-81410, 0, -332940, 2000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x3)
    Sleep(500)
    OP_6F(0x3, 35)
    OP_70(0x3, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x3)
    OP_4A(0xF, 0)

    def lambda_9AA0():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9AA0)
    Sleep(20)
    OP_4A(0x10, 0)

    def lambda_9AB7():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9AB7)
    Sleep(80)
    OP_4A(0x11, 0)

    def lambda_9ACE():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9ACE)
    Sleep(10)
    OP_4A(0x14, 0)

    def lambda_9AE5():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9AE5)
    Sleep(10)
    OP_4A(0x15, 0)

    def lambda_9AFC():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9AFC)
    Sleep(70)
    OP_4A(0x12, 0)

    def lambda_9B13():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9B13)
    Sleep(20)
    OP_4A(0x13, 0)

    def lambda_9B2A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9B2A)
    Sleep(15)
    OP_4A(0x16, 0)
    OP_8C(0x16, 270, 400)

    ChrTalk(    #306
        0x13,
        "#2P哦哦……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x14,
        "#5P得、得救了……！\x02",
    )

    CloseMessageWindow()

    def lambda_9B74():
        OP_6D(-86260, 0, -337310, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9B74)

    def lambda_9B8C():
        OP_67(0, 4660, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9B8C)

    def lambda_9BA4():
        OP_6B(3450, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_9BA4)

    def lambda_9BB4():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_9BB4)
    OP_43(0x10, 0x1, 0x0, 0x30)
    Sleep(500)
    OP_43(0xF, 0x1, 0x0, 0x2F)
    Sleep(600)
    OP_43(0x102, 0x2, 0x0, 0x2E)
    OP_43(0x16, 0x1, 0x0, 0x31)
    Sleep(700)
    OP_43(0x12, 0x1, 0x0, 0x32)
    Sleep(300)
    OP_43(0x13, 0x1, 0x0, 0x33)
    OP_43(0x14, 0x1, 0x0, 0x34)
    Sleep(400)
    OP_43(0x11, 0x1, 0x0, 0x35)
    Sleep(600)
    OP_43(0x15, 0x1, 0x0, 0x36)
    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #308
        0x10B,
        "#415F#6P吉尔哥、多伦哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x10,
        "#200F#5P乔丝特……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xF,
        (
            "#490F#5P嘿嘿……\x02\x03",

            "看来也欠了你们一次\x01",
            "很大的人情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x102,
        "#1040F#4P哪里，彼此彼此啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x101,
        (
            "#1006F#4P是啊是啊，之前逃脱的时候\x01",
            "可是多亏有你们的帮忙。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAC, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D57")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9D95")

    label("loc_9D57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D7E")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9D95")

    label("loc_9D7E")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_9D95")

    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10B, 180, 400)

    ChrTalk(    #313
        0x101,
        "#1005F糟糕……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x102,
        (
            "#1035F#4P看来我们的动向\x01",
            "完全都在他们的掌握之中……\x02\x03",

            "#1042F各位，赶快逃跑吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x10B,
        "#210F#5P嗯、嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x10,
        (
            "#201F#5P好……\x01",
            "马上逃跑吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 45, 400)
    OP_8C(0x14, 225, 400)

    ChrTalk(    #317
        0xF,
        "#196F#6P小子们，别拖拉！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(150, 80, -1, -1)
    SetChrName("空贼们")

    AnonymousTalk(    #318
        "\x07\x00#5S遵命！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5702   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_9FAF")

    label("loc_9FAF")

    Return()

    # Function_45_918C end

    def Function_46_9FB0(): pass

    label("Function_46_9FB0")


    def lambda_9FB6():
        OP_8E(0xFE, 0xFFFEA926, 0x0, 0xFFFAD134, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_9FB6)
    Sleep(300)

    def lambda_9FD6():
        OP_8E(0xFE, 0xFFFEAAF2, 0x0, 0xFFFACBDA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9FD6)
    Sleep(300)

    def lambda_9FF6():
        OP_8E(0xFE, 0xFFFEA3FE, 0x0, 0xFFFAC8F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_9FF6)
    Sleep(300)

    def lambda_A016():
        OP_8E(0xFE, 0xFFFEA80E, 0x0, 0xFFFAC63A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A016)
    WaitChrThread(0x10B, 0x1)
    Return()

    # Function_46_9FB0 end

    def Function_47_A031(): pass

    label("Function_47_A031")

    OP_8E(0xFE, 0xFFFEB89E, 0x0, 0xFFFADF62, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEB074, 0x0, 0xFFFADF62, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEA6B0, 0x0, 0xFFFAD6DE, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_47_A031 end

    def Function_48_A075(): pass

    label("Function_48_A075")

    OP_8E(0xFE, 0xFFFEB074, 0x0, 0xFFFADF62, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEAC3C, 0x0, 0xFFFAD63E, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_48_A075 end

    def Function_49_A0A5(): pass

    label("Function_49_A0A5")

    OP_8E(0xFE, 0xFFFEB89E, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEB074, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEA548, 0x0, 0xFFFADC24, 0xFA0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_49_A0A5 end

    def Function_50_A0E9(): pass

    label("Function_50_A0E9")

    OP_8E(0xFE, 0xFFFEB89E, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEB074, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEA7BE, 0x0, 0xFFFAE188, 0xFA0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_50_A0E9 end

    def Function_51_A12D(): pass

    label("Function_51_A12D")

    OP_8E(0xFE, 0xFFFEB89E, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEB074, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEAA16, 0x0, 0xFFFADD5A, 0xFA0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_51_A12D end

    def Function_52_A171(): pass

    label("Function_52_A171")

    OP_8E(0xFE, 0xFFFEB89E, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEAE1C, 0x0, 0xFFFADB7A, 0xFA0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_52_A171 end

    def Function_53_A1A1(): pass

    label("Function_53_A1A1")

    OP_8E(0xFE, 0xFFFEB916, 0x0, 0xFFFAE3D6, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEB36C, 0x0, 0xFFFADE18, 0xFA0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_53_A1A1 end

    def Function_54_A1D1(): pass

    label("Function_54_A1D1")

    OP_8E(0xFE, 0xFFFEB682, 0x0, 0xFFFAE37C, 0xFA0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_54_A1D1 end

    def Function_55_A1ED(): pass

    label("Function_55_A1ED")

    OP_A3(0x1C81)
    OP_A2(0x1C82)
    OP_A3(0x1C83)
    OP_A3(0x1C84)
    OP_A3(0x1C85)
    OP_A3(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_55_A1ED end

    def Function_56_A206(): pass

    label("Function_56_A206")

    OP_A3(0x1C81)
    OP_A3(0x1C82)
    OP_A2(0x1C83)
    OP_A3(0x1C84)
    OP_A3(0x1C85)
    OP_A3(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_56_A206 end

    def Function_57_A21F(): pass

    label("Function_57_A21F")

    OP_A3(0x1C81)
    OP_A3(0x1C82)
    OP_A3(0x1C83)
    OP_A2(0x1C84)
    OP_A3(0x1C85)
    OP_A3(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_57_A21F end

    def Function_58_A238(): pass

    label("Function_58_A238")

    FadeToDark(0, 0, -1)
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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A2B2"),
        (1, "loc_A2B8"),
        (SWITCH_DEFAULT, "loc_A2BE"),
    )


    label("loc_A2B2")

    OP_A2(0x1200)
    Jump("loc_A2BE")

    label("loc_A2B8")

    OP_A2(0x1201)
    Jump("loc_A2BE")

    label("loc_A2BE")

    Return()

    # Function_58_A238 end

    def Function_59_A2BF(): pass

    label("Function_59_A2BF")

    FadeToDark(0, 0, -1)
    OP_6D(-107890, 0, -346700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xA, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_59_A2BF end

    def Function_60_A350(): pass

    label("Function_60_A350")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x24012F, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_60_A350 end

    def Function_61_A376(): pass

    label("Function_61_A376")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240130, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_61_A376 end

    def Function_62_A39C(): pass

    label("Function_62_A39C")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240136, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_62_A39C end

    SaveToFile()

Try(main)
