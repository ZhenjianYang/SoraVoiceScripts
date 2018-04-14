from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5511   ._SN',
        MapName             = 'Other',
        Location            = 'C5511.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
        Flags               = 0,
        EntryFunctionIndex  = 14,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C5511   ._SN',
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
        ' ',                                    # 9
        ' ',                                    # 10
        ' ',                                    # 11
        ' ',                                    # 12
        ' ',                                    # 13
        ' ',                                    # 14
        ' ',                                    # 15
        ' ',                                    # 16
        '猎兵',                                 # 17
        '卡露娜',                               # 18
        '库拉茨',                               # 19
        '菲莉斯管理员',                         # 20
        '维修师罗伯特',                         # 21
        ' ',                                    # 22
        '',                                     # 23
        '',                                     # 24
        '',                                     # 25
        '',                                     # 26
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
        'ED6_DT29/CH12240 ._CH',             # 00
        'ED6_DT29/CH12241 ._CH',             # 01
        'ED6_DT29/CH12370 ._CH',             # 02
        'ED6_DT29/CH12371 ._CH',             # 03
        'ED6_DT29/CH12210 ._CH',             # 04
        'ED6_DT29/CH12211 ._CH',             # 05
        'ED6_DT29/CH12270 ._CH',             # 06
        'ED6_DT29/CH12271 ._CH',             # 07
        'ED6_DT27/CH03630 ._CH',             # 08
        'ED6_DT27/CH03640 ._CH',             # 09
        'ED6_DT07/CH00261 ._CH',             # 0A
        'ED6_DT27/CH03900 ._CH',             # 0B
        'ED6_DT07/CH01450 ._CH',             # 0C
        'ED6_DT27/CH04000 ._CH',             # 0D
        'ED6_DT27/CH04001 ._CH',             # 0E
        'ED6_DT07/CH00420 ._CH',             # 0F
        'ED6_DT07/CH00421 ._CH',             # 10
        'ED6_DT27/CH04632 ._CH',             # 11
        'ED6_DT27/CH03820 ._CH',             # 12
        'ED6_DT27/CH04821 ._CH',             # 13
        'ED6_DT27/CH04640 ._CH',             # 14
        'ED6_DT27/CH04641 ._CH',             # 15
        'ED6_DT27/CH04630 ._CH',             # 16
        'ED6_DT27/CH04634 ._CH',             # 17
        'ED6_DT27/CH04631 ._CH',             # 18
        'ED6_DT26/CH20200 ._CH',             # 19
        'ED6_DT26/CH20201 ._CH',             # 1A
        'ED6_DT26/CH20202 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT29/CH12240P._CP',             # 00
        'ED6_DT29/CH12241P._CP',             # 01
        'ED6_DT29/CH12370P._CP',             # 02
        'ED6_DT29/CH12371P._CP',             # 03
        'ED6_DT29/CH12210P._CP',             # 04
        'ED6_DT29/CH12211P._CP',             # 05
        'ED6_DT29/CH12270P._CP',             # 06
        'ED6_DT29/CH12271P._CP',             # 07
        'ED6_DT27/CH03630P._CP',             # 08
        'ED6_DT27/CH03640P._CP',             # 09
        'ED6_DT07/CH00261P._CP',             # 0A
        'ED6_DT27/CH03900P._CP',             # 0B
        'ED6_DT07/CH01450P._CP',             # 0C
        'ED6_DT27/CH04000P._CP',             # 0D
        'ED6_DT27/CH04001P._CP',             # 0E
        'ED6_DT07/CH00420P._CP',             # 0F
        'ED6_DT07/CH00421P._CP',             # 10
        'ED6_DT27/CH04632P._CP',             # 11
        'ED6_DT27/CH03820P._CP',             # 12
        'ED6_DT27/CH04821P._CP',             # 13
        'ED6_DT27/CH04640P._CP',             # 14
        'ED6_DT27/CH04641P._CP',             # 15
        'ED6_DT27/CH04630P._CP',             # 16
        'ED6_DT27/CH04634P._CP',             # 17
        'ED6_DT27/CH04631P._CP',             # 18
        'ED6_DT26/CH20200P._CP',             # 19
        'ED6_DT26/CH20201P._CP',             # 1A
        'ED6_DT26/CH20202P._CP',             # 1B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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


    DeclMonster(
        X                   = 580,
        Z                   = 0,
        Y                   = -79030,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2350,
        Z                   = 0,
        Y                   = 18010,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 122670,
        Z                   = 0,
        Y                   = 56060,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 122370,
        Z                   = 0,
        Y                   = -65990,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -1900,
        TriggerZ            = -500,
        TriggerY            = -56200,
        TriggerRange        = 1000,
        ActorX              = -1900,
        ActorZ              = 1000,
        ActorY              = -56200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2470,
        TriggerZ            = 0,
        TriggerY            = -60170,
        TriggerRange        = 1000,
        ActorX              = 2470,
        ActorZ              = 0,
        ActorY              = -60170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1930,
        TriggerZ            = 0,
        TriggerY            = -30370,
        TriggerRange        = 1000,
        ActorX              = -1930,
        ActorZ              = 0,
        ActorY              = -30370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1960,
        TriggerZ            = 0,
        TriggerY            = -26130,
        TriggerRange        = 1500,
        ActorX              = -1960,
        ActorZ              = 1500,
        ActorY              = -26130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1870,
        TriggerZ            = 0,
        TriggerY            = -33850,
        TriggerRange        = 1500,
        ActorX              = -1870,
        ActorZ              = 1500,
        ActorY              = -33850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5920,
        TriggerZ            = 0,
        TriggerY            = -28120,
        TriggerRange        = 1500,
        ActorX              = -5920,
        ActorZ              = 1500,
        ActorY              = -28120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5990,
        TriggerZ            = 0,
        TriggerY            = -32009,
        TriggerRange        = 1500,
        ActorX              = -5990,
        ActorZ              = 1500,
        ActorY              = -32009,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1920,
        TriggerZ            = 0,
        TriggerY            = -28070,
        TriggerRange        = 1500,
        ActorX              = 1920,
        ActorZ              = 1500,
        ActorY              = -28070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1900,
        TriggerZ            = 0,
        TriggerY            = -32030,
        TriggerRange        = 1500,
        ActorX              = 1900,
        ActorZ              = 1500,
        ActorY              = -32030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 74740,
        TriggerZ            = 0,
        TriggerY            = 102630,
        TriggerRange        = 1000,
        ActorX              = 74740,
        ActorZ              = 1000,
        ActorY              = 102630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -80430,
        TriggerZ            = 0,
        TriggerY            = 17900,
        TriggerRange        = 1000,
        ActorX              = -80430,
        ActorZ              = 1000,
        ActorY              = 17900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = -28920,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 1000,
        ActorY              = -28920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2000,
        TriggerZ            = 0,
        TriggerY            = -28000,
        TriggerRange        = 1000,
        ActorX              = -2000,
        ActorZ              = 1200,
        ActorY              = -28000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_58E",          # 00, 0
        "Function_1_59F",          # 01, 1
        "Function_2_6E6",          # 02, 2
        "Function_3_6EA",          # 03, 3
        "Function_4_700",          # 04, 4
        "Function_5_701",          # 05, 5
        "Function_6_702",          # 06, 6
        "Function_7_718",          # 07, 7
        "Function_8_719",          # 08, 8
        "Function_9_71A",          # 09, 9
        "Function_10_723",         # 0A, 10
        "Function_11_105C",        # 0B, 11
        "Function_12_20A9",        # 0C, 12
        "Function_13_22B9",        # 0D, 13
        "Function_14_26C2",        # 0E, 14
        "Function_15_2CF6",        # 0F, 15
        "Function_16_3150",        # 10, 16
    )


    def Function_0_58E(): pass

    label("Function_0_58E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59E")
    Event(0, 9)

    label("loc_59E")

    Return()

    # Function_0_58E end

    def Function_1_59F(): pass

    label("Function_1_59F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D7")
    OP_6F(0x2, 30)
    OP_6F(0x3, 30)
    OP_6F(0x4, 30)
    OP_6F(0x5, 30)
    OP_79(0xA, 0x2)
    OP_79(0xC, 0x2)
    OP_79(0x20, 0x2)
    OP_79(0x21, 0x2)
    OP_7B()
    Jump("loc_5F3")

    label("loc_5D7")

    OP_6F(0x2, 15)
    OP_6F(0x3, 15)
    OP_6F(0x4, 15)
    OP_6F(0x5, 15)

    label("loc_5F3")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)
    OP_64(0x8, 0x1)
    OP_72(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_64E")
    OP_64(0xC, 0x1)
    OP_7A(0xA, 0x2)
    OP_7A(0xC, 0x2)
    OP_7A(0x20, 0x2)
    OP_7A(0x21, 0x2)
    OP_7B()
    OP_6F(0x2E, 1)
    OP_6F(0xB, 29)
    OP_71(0xB, 0x2)
    Jump("loc_64E")

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_660")
    OP_6F(0x2F, 0)
    Jump("loc_667")

    label("loc_660")

    OP_6F(0x2F, 60)

    label("loc_667")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D2")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 74740, 1000, 102630, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_72(0x7, 0x20)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x0)
    Jump("loc_6E5")

    label("loc_6D2")

    OP_72(0x7, 0x20)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x0)

    label("loc_6E5")

    Return()

    # Function_1_59F end

    def Function_2_6E6(): pass

    label("Function_2_6E6")

    TalkEnd(0xFF)
    Return()

    # Function_2_6E6 end

    def Function_3_6EA(): pass

    label("Function_3_6EA")

    TalkBegin(0xFF)

    AnonymousTalk(    #0
        "开始\x02",
    )

    CloseMessageWindow()
    OP_43(0x8, 0x0, 0x0, 0x4)
    TalkEnd(0xFF)
    Return()

    # Function_3_6EA end

    def Function_4_700(): pass

    label("Function_4_700")

    Return()

    # Function_4_700 end

    def Function_5_701(): pass

    label("Function_5_701")

    Return()

    # Function_5_701 end

    def Function_6_702(): pass

    label("Function_6_702")

    TalkBegin(0xFF)

    AnonymousTalk(    #1
        "开始\x02",
    )

    CloseMessageWindow()
    OP_43(0x8, 0x0, 0x0, 0x7)
    TalkEnd(0xFF)
    Return()

    # Function_6_702 end

    def Function_7_718(): pass

    label("Function_7_718")

    Return()

    # Function_7_718 end

    def Function_8_719(): pass

    label("Function_8_719")

    Return()

    # Function_8_719 end

    def Function_9_71A(): pass

    label("Function_9_71A")

    Call(0, 10)
    Call(0, 11)
    Return()

    # Function_9_71A end

    def Function_10_723(): pass

    label("Function_10_723")

    EventBegin(0x0)
    OP_6D(71250, 0, -31120, 0)
    OP_67(0, 7140, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 70500, 0, -30340, 0)
    SetChrPos(0x10A, 72480, 0, -30340, 0)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 22)
    SetChrPos(0x10, 71440, 2000, -19470, 178)
    ClearChrFlags(0x10, 0x80)
    OP_20(0x5DC)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #2
        0x10,
        "男人的声音",
        "呵呵，终于来了啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x56)
    Sleep(500)

    def lambda_84F():
        OP_6D(71640, 1000, -22120, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84F)

    def lambda_867():
        OP_67(0, 5140, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_867)

    def lambda_87F():
        OP_6C(57000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_87F)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #3
        0x101,
        "#1P#1005F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10A,
        "#1P#812F总算出现了……！\x02",
    )

    CloseMessageWindow()

    def lambda_8D3():
        OP_6B(3700, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8D3)
    SetChrChipByIndex(0x101, 13)

    def lambda_8E8():
        OP_94(0x0, 0x101, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8E8)
    Sleep(200)
    SetChrChipByIndex(0x10A, 15)

    def lambda_908():
        OP_94(0x0, 0x10A, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_908)
    WaitChrThread(0x101, 0x0)
    SetChrChipByIndex(0x101, 13)
    WaitChrThread(0x10A, 0x0)
    SetChrChipByIndex(0x10A, 15)

    ChrTalk(    #5
        0x10,
        (
            "#5P来得正好。\x01",
            "欢迎光临我们的新据点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        "#5P装置还有趣吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#6P#1007F嗯～托你的福呢。\x02\x03",

            "#1002F话说回来，克鲁茨前辈他们\x01",
            "好像在那个门的另一边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        (
            "#816F#4P不想吃苦头的话\x01",
            "最好快放了他们哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#5P呵，两个小丫头\x01",
            "还挺嚣张的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#5P不知这里是死路一条，\x01",
            "竟然毫不在乎地就跑了进来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#6P#1006F哼，这么说的话\x01",
            "你们也是一样吧。\x02\x03",

            "虽然不知道你们有什么目的，\x01",
            "不过你们已经是瓮中之鳖了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        "#5P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10A,
        (
            "#816F#4P协会的支援很快就会过来。\x02\x03",

            "这样一来，你们\x01",
            "可是没有胜算的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#5P哼……\x01",
            "宿舍的通讯器已经完全被破坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        "#5P你要怎么跟他们联络？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#6P#1015F唔，嗯……\x02\x03",

            "（有没有什么虚张声势的好方法……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x18\x07\x05要如何虚张声势？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【已经升起狼烟联络了】\x01",              # 0
            "【不需要联络】\x01",                      # 1
            "【预定有其它的训练志愿者会来】\x01",      # 2
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
        (0, "loc_C5B"),
        (1, "loc_D3F"),
        (2, "loc_E55"),
        (SWITCH_DEFAULT, "loc_F87"),
    )


    label("loc_C5B")


    ChrTalk(    #18
        0x101,
        (
            "#6P#1009F……我们已经升起狼烟\x01",
            "联络山下了。\x02\x03",

            "这是紧急时候的联络手段。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10A,
        "#1317F#4P艾、艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#5P哈哈哈！\x01",
            "好可爱的借口！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "#5P我刚刚才上过屋顶，\x01",
            "可没看到那种东西哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#6P#1019F呜……\x01",
            "（好像太简单了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F87")

    label("loc_D3F")

    OP_2B(0x7E, 0x2)

    ChrTalk(    #23
        0x101,
        (
            "#6P#1006F哼，根本就\x01",
            "不需要联络。\x02\x03",

            "没有收到定时联络，\x01",
            "协会应该就会知道\x01",
            "我们这边发生了异状。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        "#5P什么……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #25
        0x10A,
        (
            "#814F#4P的确，今天早上\x01",
            "应该已经注意到了异状才对……\x02\x03",

            "#811F嗯，支援或许快要到了吧㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#5P……可恶。\x01",
            "最后的关头看来太大意了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F87")

    label("loc_E55")


    ChrTalk(    #27
        0x101,
        (
            "#6P#1002F……今天刚好\x01",
            "有其它的训练志愿者会来。\x02\x03",

            "而且人数相当多，\x01",
            "你们这些人根本不算什么！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10A,
        "#1317F#4P艾、艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#5P呵……\x01",
            "你倒告诉了我一件好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "#5P那么，就在峡谷入口\x01",
            "设下埋伏吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#5P如果他们没有戒备的话，\x01",
            "速攻就能够全部歼灭了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#6P#1019F呜……\x01",
            "（没办法虚张声势了吗。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F87")


    ChrTalk(    #33
        0x10,
        (
            "#5P算了。\x01",
            "总之你们太碍眼了。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x1FD, 0x0, 0x64)
    SetChrChipByIndex(0x10, 17)
    OP_99(0x10, 0x0, 0x5, 0x7D0)
    Sleep(500)

    ChrTalk(    #34
        0x10,
        "#5P赶快让我统统都收拾掉吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#6P#1005F正合我意！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10A,
        "#815F#4P现在就决一胜负吧！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10, 0xFF)
    Battle(0x395, 0x0, 0x0, 0x0, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_10_723 end

    def Function_11_105C(): pass

    label("Function_11_105C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x0)
    OP_44(0x10, 0x0)
    OP_6D(72290, 1500, -21120, 0)
    SetChrPos(0x101, 70540, 1500, -21200, 78)
    SetChrChipByIndex(0x101, 13)
    SetChrPos(0x10A, 73110, 1000, -22200, 17)
    SetChrChipByIndex(0x10A, 15)
    SetChrPos(0x10, 73240, 2000, -19780, 225)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 23)
    SetChrSubChip(0x10, 3)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #37
        0x10,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1006F#6P呼呼……赢、赢了……\x02\x03",

            "#1015F不、不过这个反应……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10A,
        (
            "#1317F嗯、嗯……\x01",
            "艾丝蒂尔也发现了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x11, 71420, 2000, -15600, 180)
    SetChrPos(0x12, 71420, 2000, -15600, 180)

    NpcTalk(    #40
        0x11,
        "女人的声音",
        (
            "#2P呵呵……\x01",
            "好像完全被骗了呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    NpcTalk(    #41
        0x12,
        "男人的声音",
        (
            "#2P哈哈哈。\x01",
            "完全上当了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x7D0)

    def lambda_122F():
        OP_6D(72300, 2000, -18490, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_122F)

    def lambda_1247():
        OP_6B(3600, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1247)
    OP_8C(0x101, 3, 1000)
    Sleep(100)
    OP_8C(0x10A, 3, 1000)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    SetChrPos(0x11, 71480, 2000, -12880, 180)
    SetChrPos(0x12, 71480, 2000, -11880, 180)
    OP_22(0x6D, 0x0, 0x64)
    OP_72(0xD, 0x10)
    OP_6F(0xD, 0)
    OP_70(0xD, 0x1D)
    OP_73(0xD)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    def lambda_12BB():
        OP_8E(0x11, 0x11AE4, 0x7D0, 0xFFFFB8FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12BB)

    def lambda_12D6():
        OP_8E(0x12, 0x11738, 0x7D0, 0xFFFFC34C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_12D6)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #42
        0x101,
        "#1020F#6P啊！\x02",
    )


    def lambda_1308():
        OP_8E(0x12, 0x11698, 0x7D0, 0xFFFFB9CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1308)
    WaitChrThread(0x11, 0x1)
    CloseMessageWindow()

    ChrTalk(    #43
        0x10A,
        "#812F#4P增、增援！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)
    TurnDirection(0x12, 0x101, 400)

    NpcTalk(    #44
        0x11,
        "女猎兵",
        "#5P哈哈，不是啦。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #45
        0x11,
        "女猎兵",
        (
            "#5P虽然口气没变，\x01",
            "但你们也该明白了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1015F#6P这个大姐口气……\x02\x03",

            "#1004F……难、难道是！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #47
        0x10A,
        "#1317F#3S#4P卡、卡露娜前辈！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    NpcTalk(    #48
        0x11,
        "女猎兵",
        "#5P答对了。\x02",
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x11, 25)
    OP_0D()
    OP_1D(0x1)
    Sleep(500)

    ChrTalk(    #49
        0x11,
        (
            "#1201F#5P亚妮拉丝、艾丝蒂尔。\x01",
            "实在是好久不见了呢。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x101,
        (
            "#1020F#6P好久不见……\x01",
            "#1005F到底怎么回事？\x02\x03",

            "那、那这位是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10A,
        "#815F库拉茨前辈！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #52
        0x12,
        "猎兵",
        "#5P对啦！\x02",
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x12, 27)
    OP_0D()
    Sleep(500)

    ChrTalk(    #53
        0x12,
        (
            "#1191F#5P哟，你们两位\x01",
            "辛苦啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1015F#6P辛、辛苦……\x02\x03",

            "……难道这是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        "呵呵，就是这么回事。\x02",
    )

    CloseMessageWindow()
    OP_99(0x10, 0x3, 0x0, 0x5DC)
    Sleep(500)
    OP_22(0xD5, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x10, 26)
    OP_0D()
    OP_8C(0x101, 78, 500)

    NpcTalk(    #56
        0x10,
        "克鲁茨",
        (
            "#1211F艾丝蒂尔、亚妮拉丝。\x01",
            "最终的训练，辛苦你们啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#1004F#6P最、最终训练……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10A,
        (
            "#1317F这、这么说……\x02\x03",

            "从昨天的袭击开始，\x01",
            "一切都是在演戏吗！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #59
        0x10,
        "克鲁茨",
        (
            "#1210F呵呵，这是本训练场\x01",
            "的惯例。\x02\x03",

            "最终训练的用意是欺骗训练人员，\x01",
            "让他们体验到危机的状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#1019F#6P什、什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x12,
        (
            "#1190F#5P而我们就是为了帮忙，\x01",
            "特地从利贝尔赶过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x11,
        (
            "#1201F#5P呵呵……\x01",
            "真是相当有趣哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10A,
        (
            "#1316F呜～……\x02\x03",

            "#812F前辈们真是的，\x01",
            "太欺负人啦～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1009F#6P就、就是呀！\x02\x03",

            "我们还以为\x01",
            "真的碰到危机了呢！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #65
        0x10,
        "克鲁茨",
        (
            "#1213F嗯，这就是这次训练的目的。\x02\x03",

            "#1212F顺带提醒你们……\x01",
            "真正的猎兵可没这么天真哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1003F#6P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10A,
        "#813F呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x11,
        (
            "#1200F#5P在利贝尔，\x01",
            "使用猎兵团是被禁止的，\x01",
            "因此不太容易想象得到……\x02\x03",

            "但在其它国家的话，游击士协会\x01",
            "和猎兵团的较量可是家常便饭的事。\x02\x03",

            "#1202F自然而然，游击士们大多\x01",
            "也会对危机的状况有所戒备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x12,
        (
            "#1192F#5P所以，我们希望利贝尔的游击士\x01",
            "也能体验一次危机的状况。\x02\x03",

            "就当这是一种父母心的表现吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1007F#6P唉……真狡猾。\x02\x03",

            "#1019F被这么一说，\x01",
            "想抱怨也没有办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10A,
        "#812F嗯嗯，真狡猾啊。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x13, 71480, 2000, -12880, 180)

    NpcTalk(    #72
        0x13,
        "女性的声音",
        (
            "#2P哎呀哎呀。\x01",
            "已经结束了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x12, 500)

    def lambda_1A29():
        OP_6D(71800, 2000, -18000, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A29)
    ClearChrFlags(0x13, 0x80)
    OP_8E(0x13, 0x116F2, 0x7D0, 0xFFFFC464, 0x7D0, 0x0)
    OP_8E(0x13, 0x111FC, 0x7D0, 0xFFFFB88E, 0x7D0, 0x0)

    ChrTalk(    #73
        0x101,
        "#1004F#6P啊，管理员小姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10A,
        (
            "#812F唔～管理员小姐\x01",
            "也是共犯吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x13,
        "#5P哎呀，别说成共犯那么难听嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x13,
        (
            "#5P因为要演戏，\x01",
            "我也是拚命在背台词的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x13,
        "#5P嘻嘻，很逼真的演技吧㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1019F#6P嗯嗯～\x01",
            "完全被你骗了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x14, 71310, 0, -31680, 358)

    NpcTalk(    #79
        0x14,
        "男人的声音",
        (
            "#1P哈哈哈。\x01",
            "你们两个都辛苦了！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)

    def lambda_1B8E():
        OP_94(0x0, 0xFE, 0x0, 0x1C84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1B8E)

    def lambda_1BA4():
        OP_6D(72580, 1500, -21110, 2500)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_1BA4)

    def lambda_1BBC():

        label("loc_1BBC")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_1BBC")

    QueueWorkItem2(0x101, 1, lambda_1BBC)

    def lambda_1BCD():

        label("loc_1BCD")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_1BCD")

    QueueWorkItem2(0x10A, 1, lambda_1BCD)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x14, 0x3)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)

    ChrTalk(    #80
        0x10A,
        "#2P#815F啊～大骗子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#1007F#5P结果，\x01",
            "全部的人都是共犯啊。\x02\x03",

            "#1004F啊，这么说的话，\x01",
            "宿舍的通讯器……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x14,
        "嗯，那是报废零件。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x14,
        (
            "真正的通讯器被保管在\x01",
            "其它地方，不必担心啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x14,
        (
            "其实我本来预定要当人质，\x01",
            "就这样一直躲藏到最后的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x14,
        (
            "不过因为你们想知道\x01",
            "怎么样运用新导力器，\x01",
            "我才会在那个时机出现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x10A,
        (
            "#2P#1316F真是的……\x01",
            "大家准备得都太周到了啦。\x02\x03",

            "#1314F但是，结果算是\x01",
            "我们上了当吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1007F#5P嗯～虽然不甘心但确实如此。\x02\x03",

            "#1025F冷静下来思考的话，\x01",
            "的确还有很多不自然的地方……\x02\x03",

            "我们的修练毕竟还是不够啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #88
        0x10,
        "克鲁茨",
        "#1211F呵呵，别这么沮丧嘛。\x02",
    )

    CloseMessageWindow()

    def lambda_1E1D():

        label("loc_1E1D")

        TurnDirection(0xFE, 0x10, 500)
        OP_48()
        Jump("loc_1E1D")

    QueueWorkItem2(0x101, 1, lambda_1E1D)

    def lambda_1E2E():

        label("loc_1E2E")

        TurnDirection(0xFE, 0x10, 500)
        OP_48()
        Jump("loc_1E2E")

    QueueWorkItem2(0x10A, 1, lambda_1E2E)
    OP_6D(72500, 1750, -20000, 800)

    NpcTalk(    #89
        0x10,
        "克鲁茨",
        (
            "#1213F库拉茨也说了，\x01",
            "此次与其说是测试你们的实力，\x01",
            "不如说是希望你们能体验危机的状况。\x02\x03",

            "从这个意义上来说，演习是相当成功的。\x02\x03",

            "#1210F那么接下来……\x01",
            "亚妮拉丝·艾尔菲德。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10A,
        "#814F啊，是。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #91
        0x10,
        "克鲁茨",
        "#1210F艾丝蒂尔·布莱特。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1002F#6P……是！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #93
        0x10,
        "克鲁茨",
        (
            "#1210F至此，本训练场的\x01",
            "综合强化训练全部结束了。\x02\x03",

            "这３周，真的是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1004F#6P这、这么说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10A,
        "#1310F明天就可以……？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #96
        0x10,
        "克鲁茨",
        (
            "#1211F我已经帮你们订了\x01",
            "往利贝尔的定期船票。\x02\x03",

            "今晚什么也不会发生了，\x01",
            "你们两人都好好休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x13,
        "#5P嘻嘻。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x13,
        (
            "#5P作为庆功宴和送别会，\x01",
            "今晚可要大吃一顿哦㈱\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_3F(0x416, 1)
    NewScene("ED6_DT21/C5600   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_105C end

    def Function_12_20A9(): pass

    label("Function_12_20A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20FA")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #99
        "\x07\x05导力好像停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_22B8")

    label("loc_20FA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #100
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_229D")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 74740, 1000, 102630, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x32)
    OP_73(0x7)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 74740, 1000, 102630, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 74740, 1000, 102630, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x7, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_229D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B7")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_22B7")

    Return()

    label("loc_22B8")

    Return()

    # Function_12_20A9 end

    def Function_13_22B9(): pass

    label("Function_13_22B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2328")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -81450, 0, 18230, 90)
    SetChrPos(0x10A, -81380, 0, 17370, 90)
    OP_6D(-80680, 0, 18040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    label("loc_2328")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2400")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x416, 1)"), scpexpr(EXPR_END)), "loc_2397")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #101
        "\x07\x00得到了\x1F\x16\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1145)
    Jump("loc_23FD")

    label("loc_2397")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #102
        (
            "宝箱里装有\x1F\x16\x04\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x16\x04\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2F, 60)
    OP_70(0x2F, 0x0)

    label("loc_23FD")

    Jump("loc_2431")

    label("loc_2400")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #103
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2431")

    Sleep(30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B9")
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #104
        0x101,
        "#1015F#1P这是什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10A,
        (
            "#818F#4P嗯～好像是什么装置呢。\x02\x03",

            "而且还能看见\x01",
            "导力器装置的开关……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)
    Sleep(500)

    ChrTalk(    #106
        0x10A,
        (
            "#810F#4P嗯，总之\x01",
            "还是先拿着比较好吧？\x02\x03",

            "这里是训练设施，\x01",
            "说不定能用来解除哪里的机关。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #107
        0x101,
        (
            "#1011F#1P的确有这个可能呢。\x02\x03",

            "#1015F自从来到这里之后，\x01",
            "像是机关门啦，漆黑的房间啦等等的\x01",
            "也都碰到过了不少……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10A,
        (
            "#1310F#4P有备无患，对吧。\x02\x03",

            "那么，继续前进吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1006F#1P嗯，走吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #110
        (
            "\x07\x05※得到『#15I使用事件道具』。\x01",
            "  在游戏途中，某些场面要直接使用\x01",
            "  这些关键道具来继续向前推进。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #111
        (
            "\x07\x05※利用使用事件道具时，\x01",
            "  从Camp画面选择[Items]页\x01",
            "  直接单击想使用的道具名。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_A2(0x1065)
    EventEnd(0x0)

    label("loc_26B9")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_22B9 end

    def Function_14_26C2(): pass

    label("Function_14_26C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x416), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26CF")
    Return()

    label("loc_26CF")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_2765")
    TalkBegin(0xFF)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #112
        (
            "\x07\x05认证组件已经启动了……\x01",
            "但好像没什么特别的反应。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_2CF0")

    label("loc_2765")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A72")
    EventBegin(0x0)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #113
        "\x07\x05认证组件已经启动了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    SetChrPos(0x15, -1980, 0, -27750, 201)

    def lambda_27D7():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27D7)

    def lambda_27E5():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_27E5)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #114
        0x101,
        "#1004F啊……！？\x02",
    )

    CloseMessageWindow()
    OP_6D(-1890, 0, -32890, 1000)
    OP_64(0xC, 0x1)
    OP_6F(0x2, 30)
    OP_70(0x2, 0xF)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x2)
    SetChrPos(0x15, -5940, 0, -29460, 201)

    def lambda_2861():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2861)

    def lambda_286F():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_286F)
    OP_7A(0xA, 0x2)
    OP_7B()
    Sleep(400)
    OP_6F(0x3, 30)
    OP_70(0x3, 0xF)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x3)
    SetChrPos(0x15, -5900, 0, -37010, 225)

    def lambda_28AE():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28AE)

    def lambda_28BC():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_28BC)
    OP_7A(0x20, 0x2)
    OP_7B()
    Sleep(400)
    OP_6F(0x5, 30)
    OP_70(0x5, 0xF)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x5)
    SetChrPos(0x15, 1660, 0, -36980, 45)

    def lambda_28FB():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28FB)

    def lambda_2909():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2909)
    OP_7A(0x21, 0x2)
    OP_7B()
    Sleep(400)
    OP_6F(0x4, 30)
    OP_70(0x4, 0xF)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x4)
    SetChrPos(0x15, 1670, 0, -29260, 45)

    def lambda_2948():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2948)

    def lambda_2956():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2956)
    OP_7A(0xC, 0x2)
    OP_7B()
    Sleep(1000)
    OP_22(0x73, 0x0, 0x64)
    OP_6F(0xB, 0)
    OP_70(0xB, 0x1D)
    OP_73(0xB)
    SetChrPos(0x15, -1980, 0, -27750, 201)

    def lambda_2995():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2995)

    def lambda_29A3():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_29A3)
    OP_22(0x9D, 0x0, 0x64)
    OP_6F(0x2E, 1)
    OP_70(0x2E, 0x1)
    OP_73(0x2E)
    OP_71(0xB, 0x2)
    OP_A2(0x1067)
    Sleep(1000)
    Fade(1000)
    OP_69(0x0, 0x0)
    OP_0D()

    ChrTalk(    #115
        0x101,
        (
            "#1008F啊哈哈……\x01",
            "真、真的打开了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #116
        0x10A,
        (
            "#811F嘿嘿，正义必胜！对吧。\x02\x03",

            "#816F好，艾丝蒂尔。\x01",
            "接下来也谨慎地前进吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #117
        0x101,
        "#1006F嗯！\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_2CF0")

    label("loc_2A72")

    TalkBegin(0xFF)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #118
        (
            "\x07\x05认证组件已经启动了……\x01",
            "但这个地方好像没什么特别的反应。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2B21")

    ChrTalk(    #119
        0x10A,
        (
            "#814F艾丝蒂尔。\x01",
            "好像不是这里哦。\x02\x03",

            "先往前走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x0)
    Jump("loc_2CED")

    label("loc_2B21")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B67")

    ChrTalk(    #120
        0x10A,
        (
            "#812F嗯～这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CEA")

    label("loc_2B67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA1")

    ChrTalk(    #121
        0x10A,
        (
            "#813F嗯～这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CEA")

    label("loc_2BA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD9")

    ChrTalk(    #122
        0x10A,
        (
            "#814F这里好像\x01",
            "没什么可用的东西吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CEA")

    label("loc_2BD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C13")

    ChrTalk(    #123
        0x10A,
        (
            "#817F嗯～这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CEA")

    label("loc_2C13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C4D")

    ChrTalk(    #124
        0x10A,
        (
            "#818F嗯～这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CEA")

    label("loc_2C4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C7F")

    ChrTalk(    #125
        0x10A,
        (
            "#819F嗯～看来\x01",
            "没找对地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CEA")

    label("loc_2C7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB6")

    ChrTalk(    #126
        0x10A,
        (
            "#1315F这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CEA")

    label("loc_2CB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CEA")

    ChrTalk(    #127
        0x10A,
        (
            "#1316F这里好像\x01",
            "没什么可用的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CEA")

    OP_A2(0x0)

    label("loc_2CED")

    TalkEnd(0xFF)

    label("loc_2CF0")

    ClearMapFlags(0x80)
    Return()

    # Function_14_26C2 end

    def Function_15_2CF6(): pass

    label("Function_15_2CF6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #128
        (
            "\x07\x05好像是门锁机关，\x01",
            "但没看到什么拉杆。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_314C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9D")

    ChrTalk(    #129
        0x10A,
        (
            "#813F说不定，在某处\x01",
            "会有控制这个的装置。\x02\x03",

            "#1316F只好返回通道\x01",
            "去寻找了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF9")

    label("loc_2D9D")


    ChrTalk(    #130
        0x10A,
        (
            "#812F刚才捡到的装置，\x01",
            "是不是应该用在这里呢。\x02\x03",

            "#812F对了，艾丝蒂尔。\x01",
            "我们就稍微试试吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF9")

    Jump("loc_314C")

    label("loc_2DFC")

    EventBegin(0x0)

    ChrTalk(    #131
        0x101,
        (
            "#1002F对了，亚妮拉丝……\x01",
            "这个装置……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x10A,
        (
            "#812F嗯，好像是控制\x01",
            "门锁的机械呢。\x02\x03",

            "如果能启动这个的话，\x01",
            "我想门就会打开了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1007F不过很可惜，\x01",
            "我们不知道启动的方法呢。\x02\x03",

            "#1003F这里也找不到\x01",
            "和那时候大门一样的拉杆……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F52")

    ChrTalk(    #134
        0x10A,
        (
            "#813F说不定，在某处\x01",
            "可能有东西能解除这个。\x02\x03",

            "#812F艾丝蒂尔。\x01",
            "回去找找看吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1006F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_314A")

    label("loc_2F52")


    ChrTalk(    #136
        0x10A,
        (
            "#813F说不定，在某处\x01",
            "可能有东西能解除这个。\x02\x03",

            "#812F艾丝蒂尔。\x01",
            "回去找找看……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #137
        0x10A,
        "#814F啊，对了！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #138
        0x101,
        "#1004F想起什么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #139
        0x10A,
        (
            "#812F艾丝蒂尔。\x01",
            "还记得刚才捡到的装置吗？\x02\x03",

            "你想想，就是在楼梯那里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        "#1011F啊，那个古怪的机械？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x10A,
        (
            "#810F嗯，说不定\x01",
            "要使用那个……\x02\x03",

            "……怎么样，不试试看吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1015F嗯、嗯……\x02\x03",

            "嗯，试试也好，\x01",
            "不过应该没这么顺利吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #143
        (
            "\x07\x05※利用使用事件道具时，\x01",
            "  从Camp画面选择[Items]页\x01",
            "  直接单击想使用的道具名。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_A2(0x1)

    label("loc_314A")

    EventEnd(0x1)

    label("loc_314C")

    TalkEnd(0xFF)
    Return()

    # Function_15_2CF6 end

    def Function_16_3150(): pass

    label("Function_16_3150")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #144
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_16_3150 end

    SaveToFile()

Try(main)
