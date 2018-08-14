from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1500   ._SN',
        MapName             = 'Bose',
        Location            = 'C1500.x',
        MapIndex            = 61,
        MapDefaultBGM       = "ed60125",
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
        '魔兽',                                 # 9
        '古怪的魔兽',                           # 10
        '古罗尼山道·关所方向',                 # 11
        '西柏斯街道方向',                       # 12
        '目标角色',                             # 13
        '目标用照相机',                         # 14
        '',                                     # 15
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
        'ED6_DT09/CH10200 ._CH',             # 00
        'ED6_DT29/CH14370 ._CH',             # 01
        'ED6_DT26/CH20700 ._CH',             # 02
        'ED6_DT26/CH20701 ._CH',             # 03
        'ED6_DT26/CH20702 ._CH',             # 04
        'ED6_DT26/CH20703 ._CH',             # 05
        'ED6_DT26/CH20704 ._CH',             # 06
        'ED6_DT26/CH20705 ._CH',             # 07
        'ED6_DT29/CH14371 ._CH',             # 08
        'ED6_DT29/CH14372 ._CH',             # 09
        'ED6_DT29/CH14373 ._CH',             # 0A
        'ED6_DT26/CH20709 ._CH',             # 0B
        'ED6_DT29/CH14373 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT09/CH10200P._CP',             # 00
        'ED6_DT29/CH14370P._CP',             # 01
        'ED6_DT26/CH20700P._CP',             # 02
        'ED6_DT26/CH20701P._CP',             # 03
        'ED6_DT26/CH20702P._CP',             # 04
        'ED6_DT26/CH20703P._CP',             # 05
        'ED6_DT26/CH20704P._CP',             # 06
        'ED6_DT26/CH20705P._CP',             # 07
        'ED6_DT29/CH14371P._CP',             # 08
        'ED6_DT29/CH14372P._CP',             # 09
        'ED6_DT29/CH14373P._CP',             # 0A
        'ED6_DT26/CH20709P._CP',             # 0B
        'ED6_DT29/CH14373P._CP',             # 0C
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -140810,
        Z                   = 6010,
        Y                   = -31010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -119390,
        Z                   = -60,
        Y                   = 180920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
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
        NpcIndex            = 0x1EE,
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


    DeclEvent(
        X                   = -155740,
        Y                   = 3980,
        Z                   = 128479,
        Range               = -152500,
        Unknown_10          = 0xFFFFF8B2,
        Unknown_14          = 0x1FB58,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )


    DeclActor(
        TriggerX            = -153280,
        TriggerZ            = 4000,
        TriggerY            = 97180,
        TriggerRange        = 1500,
        ActorX              = -153280,
        ActorZ              = 4500,
        ActorY              = 97180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -144990,
        TriggerZ            = 1960,
        TriggerY            = 163750,
        TriggerRange        = 1500,
        ActorX              = -144990,
        ActorZ              = 2460,
        ActorY              = 163750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 33,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -156650,
        TriggerZ            = 2000,
        TriggerY            = 117940,
        TriggerRange        = 1500,
        ActorX              = -156650,
        ActorZ              = 2500,
        ActorY              = 117940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -123200,
        TriggerZ            = 4070,
        TriggerY            = 93650,
        TriggerRange        = 1500,
        ActorX              = -123200,
        ActorZ              = 4570,
        ActorY              = 93650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 35,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -152490,
        TriggerZ            = 2050,
        TriggerY            = 139950,
        TriggerRange        = 1500,
        ActorX              = -152490,
        ActorZ              = 2550,
        ActorY              = 139950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2A6",          # 00, 0
        "Function_1_35B",          # 01, 1
        "Function_2_4C0",          # 02, 2
        "Function_3_63D",          # 03, 3
        "Function_4_6B5",          # 04, 4
        "Function_5_24E1",         # 05, 5
        "Function_6_2554",         # 06, 6
        "Function_7_2592",         # 07, 7
        "Function_8_261D",         # 08, 8
        "Function_9_26A0",         # 09, 9
        "Function_10_26FD",        # 0A, 10
        "Function_11_29E7",        # 0B, 11
        "Function_12_2A48",        # 0C, 12
        "Function_13_2AD3",        # 0D, 13
        "Function_14_2B54",        # 0E, 14
        "Function_15_2B74",        # 0F, 15
        "Function_16_2BA0",        # 10, 16
        "Function_17_2C4B",        # 11, 17
        "Function_18_2C80",        # 12, 18
        "Function_19_2CB2",        # 13, 19
        "Function_20_3070",        # 14, 20
        "Function_21_30A5",        # 15, 21
        "Function_22_35B3",        # 16, 22
        "Function_23_3613",        # 17, 23
        "Function_24_38C7",        # 18, 24
        "Function_25_4867",        # 19, 25
        "Function_26_489C",        # 1A, 26
        "Function_27_48DA",        # 1B, 27
        "Function_28_4A05",        # 1C, 28
        "Function_29_4AA6",        # 1D, 29
        "Function_30_4ABD",        # 1E, 30
        "Function_31_4AE7",        # 1F, 31
        "Function_32_4B22",        # 20, 32
        "Function_33_4BD9",        # 21, 33
        "Function_34_4C8A",        # 22, 34
        "Function_35_4D41",        # 23, 35
        "Function_36_4DFC",        # 24, 36
    )


    def Function_0_2A6(): pass

    label("Function_0_2A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 5)), scpexpr(EXPR_END)), "loc_2D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -152740, 4000, 101020, 32)

    label("loc_2D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A")
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_30E")
    OP_A3(0x2506)
    OP_A2(0x3)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 24)
    Jump("loc_35A")

    label("loc_30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_330")
    OP_A3(0x2505)
    OP_A2(0x2)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 23)
    Jump("loc_35A")

    label("loc_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_349")
    OP_A3(0x2504)
    OP_A2(0x1)
    SetMapFlags(0x10000000)
    Event(0, 10)
    Jump("loc_35A")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_35A")

    Return()

    # Function_0_2A6 end

    def Function_1_35B(): pass

    label("Function_1_35B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_37D")
    OP_A3(0x2)
    OP_B1("C1500_2")
    OP_71(0x5, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    Jump("loc_3D8")

    label("loc_37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B4")
    OP_A3(0x1)
    OP_B1("C1500_1")
    OP_71(0x7, 0x0)
    ExitThread()
    OP_71(0x407, 0x0)
    ExitThread()
    OP_71(0x8, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()
    Jump("loc_3D8")

    label("loc_3B4")

    OP_A3(0x3)
    OP_B1("C1500_0")
    OP_71(0x7, 0x0)
    ExitThread()
    OP_71(0x407, 0x0)
    ExitThread()
    OP_71(0x8, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()

    label("loc_3D8")

    OP_11(0xFF, 0xFF, 0xFF, 0x9470, 0x1FBD0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40D")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_B2(0x0, 0x0, 0x80)

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_END)), "loc_418")
    OP_64(0x0, 0x1)

    label("loc_418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_END)), "loc_423")
    OP_64(0x1, 0x1)

    label("loc_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_END)), "loc_42E")
    OP_64(0x2, 0x1)

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_END)), "loc_439")
    OP_64(0x3, 0x1)

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_END)), "loc_444")
    OP_64(0x4, 0x1)

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 6)), scpexpr(EXPR_END)), "loc_450")
    OP_B2(0x0, 0x0, 0x80)

    label("loc_450")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BF")
    OP_71(0x0, 0x0)
    ExitThread()
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x200, 0x0)
    ExitThread()
    OP_71(0x1, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x201, 0x0)
    ExitThread()
    OP_71(0x2, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x202, 0x0)
    ExitThread()
    OP_71(0x3, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x203, 0x0)
    ExitThread()
    OP_71(0x4, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x204, 0x0)
    ExitThread()
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x1A6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BF")

    Return()

    # Function_1_35B end

    def Function_2_4C0(): pass

    label("Function_2_4C0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E5")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_627")

    label("loc_4E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_627")

    label("loc_4FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_517")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_627")

    label("loc_517")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_530")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_627")

    label("loc_530")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_549")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_627")

    label("loc_549")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_562")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_627")

    label("loc_562")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_627")

    label("loc_57B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_594")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_627")

    label("loc_594")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_627")

    label("loc_5AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C6")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_627")

    label("loc_5C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DF")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_627")

    label("loc_5DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_627")

    label("loc_5F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_611")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_627")

    label("loc_611")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_627")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_627")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_627")

    label("loc_63C")

    Return()

    # Function_2_4C0 end

    def Function_3_63D(): pass

    label("Function_3_63D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_690")

    def lambda_64D():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_64D)

    ChrTalk(    #0
        0xFE,
        (
            "（哆哆嗦嗦）\x01",
            "请快点啊……！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xFE, 0x2)
    Jump("loc_6B1")

    label("loc_690")


    ChrTalk(    #1
        0xFE,
        "麻、麻烦快一点……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_6B1")

    TalkEnd(0xFE)
    Return()

    # Function_3_63D end

    def Function_4_6B5(): pass

    label("Function_4_6B5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_11(0xFF, 0xFF, 0xFF, 0x9470, 0x1FBD0, 0x0)
    OP_6D(-144160, 5720, -27100, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6C(344000, 0)
    OP_6B(3000, 0)
    OP_6E(262, 0)
    OP_6A(0x14E)
    OP_C4(0x0, 0x40)
    SetChrPos(0x14E, -144160, 5920, -28200, 315)

    def lambda_733():
        OP_8E(0xFE, 0xFFFDE20C, 0x17C0, 0xFFFFB834, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_733)
    FadeToBright(2000, 0)

    def lambda_757():
        OP_6B(3160, 11000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_757)

    def lambda_767():
        OP_6E(352, 11000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_767)

    def lambda_777():
        OP_6C(314000, 11000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_777)
    OP_0D()

    ChrTalk(    #2 op#A
        0x14E,
        "#1717F#3S#15A波利～！#2S\x02",
    )

    OP_7C(0x96, 0x96, 0xBB8, 0x12C)
    Sleep(2000)
    OP_56(0x0)

    ChrTalk(    #3 op#A
        0x14E,
        "#1717F#3S#15A波利啊～！#2S\x02",
    )

    OP_7C(0x96, 0x96, 0xBB8, 0x12C)
    Sleep(2000)
    OP_56(0x0)
    Sleep(1500)

    ChrTalk(    #4
        0x14E,
        (
            "#1716F真是的，\x01",
            "到底跑到哪里去了……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    WaitChrThread(0x14E, 0x1)
    Sleep(300)
    Fade(1000)
    OP_6A(0xFF)
    OP_6D(-139330, 6050, -17610, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(314000, 0)
    OP_6E(337, 0)
    OP_0D()
    OP_8C(0x14E, 0, 400)
    Sleep(1000)
    OP_8C(0x14E, 90, 400)
    Sleep(500)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #5
        0x14E,
        (
            "#1714F这里……是什么地方……？\x02\x03",

            "#1713F（从、从没来过\x01",
            "  这么远的地方……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(2000)
    OP_63(0x14E)
    Sleep(500)

    ChrTalk(    #6
        0x14E,
        (
            "#1713F……我是不是\x01",
            "迷路了呢……\x02\x03",

            "…………………………\x02\x03",

            "#1901F我必须\x01",
            "振作起来才行啊。\x02\x03",

            "要担当起\x01",
            "照顾大家的责任才行啊……！\x02",
        )
    )

    Jump("loc_9DC")

    label("loc_9DC")

    CloseMessageWindow()
    OP_59()
    OP_8C(0x14E, 315, 400)
    Sleep(800)

    ChrTalk(    #7
        0x14E,
        "#1713F……得快点把波利找到。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(-138740, 6080, -18380, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_6A(0x14E)

    def lambda_A63():
        OP_6C(270000, 12000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_A63)

    def lambda_A73():
        OP_8E(0xFE, 0xFFFDBEBC, 0x1770, 0xFFFFD6AC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_A73)
    Sleep(2000)

    ChrTalk(    #8
        0x14E,
        (
            "#1713F我竟然相信世上会有什么幸福之石，\x01",
            "还把波利带到\x01",
            "这么远的地方……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #9
        0x14E,
        "#1713F……都是我的错。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14E, 0x1)

    ChrTalk(    #10
        0x14E,
        "#1901F……都是我不好……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(2000)
    OP_63(0x14E)
    Sleep(500)
    OP_9E(0x14E, 0xF, 0x0, 0x12C, 0xBB8)

    ChrTalk(    #11
        0x14E,
        "#1901F#60W………………呜……\x02",
    )

    CloseMessageWindow()
    OP_6A(0xFF)
    SetChrFlags(0x14E, 0x40)

    def lambda_B98():
        OP_6D(-151340, 5820, -7880, 1500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_B98)

    def lambda_BB0():
        OP_67(0, 4040, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_BB0)

    def lambda_BC8():
        OP_6C(282000, 1500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_BC8)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrPos(0x10, -159140, 6000, -400, 142)
    OP_43(0x10, 0x2, 0x0, 0xB)
    WaitChrThread(0x15, 0x0)
    Sleep(500)
    OP_43(0x14E, 0x2, 0x0, 0xC)
    Sleep(2000)

    def lambda_C10():
        OP_6D(-149730, 5950, -12330, 5000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_C10)

    def lambda_C28():
        OP_6C(257000, 5000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C28)
    WaitChrThread(0x10, 0x2)
    SetChrFlags(0x10, 0x80)
    WaitChrThread(0x15, 0x0)

    ChrTalk(    #12
        0x14E,
        "#1716F呼……\x02",
    )

    CloseMessageWindow()

    def lambda_C60():
        OP_6D(-149230, 5980, -10480, 3000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_C60)

    def lambda_C78():
        OP_6C(269000, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C78)
    OP_44(0x14E, 0x3)

    def lambda_C8C():
        OP_8E(0xFE, 0xFFFDAFE4, 0x1734, 0xFFFFD2D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_C8C)
    WaitChrThread(0x14E, 0x1)

    def lambda_CAC():
        OP_8E(0xFE, 0xFFFDBE9E, 0x175C, 0xFFFFD7EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_CAC)
    WaitChrThread(0x14E, 0x1)
    Sleep(300)
    OP_8C(0x14E, 135, 350)
    Sleep(800)
    WaitChrThread(0x15, 0x0)

    ChrTalk(    #13
        0x14E,
        (
            "#1713F#6P……得快点把波利找到。\x02\x03",

            "#1712F万一她被魔兽\x01",
            "袭击了的话……！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x0)
    Sleep(400)
    OP_8C(0x14E, 315, 600)
    OP_63(0x14E)

    ChrTalk(    #14
        0x14E,
        "#1717F#6P得、得赶快找到她才行……！！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x0)

    def lambda_DA4():
        OP_8E(0xFE, 0xFFFD86B8, 0x177A, 0xDD4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_DA4)
    Sleep(2000)
    Fade(1000)
    OP_44(0x14E, 0x1)
    OP_6D(-160450, 3980, 38710, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -159720, 4059, 27990, 0)

    def lambda_E1B():
        OP_8E(0xFE, 0xFFFD8F64, 0xF78, 0x9970, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_E1B)
    OP_0D()
    WaitChrThread(0x14E, 0x1)
    OP_43(0x14E, 0x2, 0x0, 0xE)

    ChrTalk(    #15
        0x14E,
        "#1717F#3S#5P波利！波利～！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    CloseMessageWindow()
    WaitChrThread(0x14E, 0x2)
    WaitChrThread(0x14E, 0x2)

    def lambda_E88():
        OP_8E(0xFE, 0xFFFD85DC, 0xF82, 0xBEA0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_E88)
    Sleep(1200)
    Fade(1000)
    OP_44(0x14E, 0x1)
    OP_6D(-135440, 1980, 56260, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -142940, 2029, 64879, 135)

    def lambda_EFF():
        OP_8E(0xFE, 0xFFFDF15C, 0x7A8, 0xDBC4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_EFF)
    OP_0D()
    WaitChrThread(0x14E, 0x1)
    OP_43(0x14E, 0x2, 0x0, 0xF)

    ChrTalk(    #16
        0x14E,
        (
            "#1717F#3S#5P……波利，你在哪儿～！？\x01",
            "拜托，快出来～！！#2S\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    CloseMessageWindow()
    WaitChrThread(0x14E, 0x2)

    def lambda_F84():
        OP_8E(0xFE, 0xFFFDD4CE, 0x7D0, 0xB734, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_F84)
    Sleep(1800)
    Fade(1000)
    OP_44(0x14E, 0x1)
    OP_6D(-150400, 6340, 8980, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -164560, 5990, 4120, 90)

    def lambda_FFB():
        OP_8E(0xFE, 0xFFFDB480, 0x1798, 0x2314, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_FFB)
    OP_0D()
    WaitChrThread(0x14E, 0x1)
    OP_63(0x14E)
    Sleep(500)

    ChrTalk(    #17
        0x14E,
        "#1716F#12P呼、呼……\x02",
    )

    CloseMessageWindow()

    def lambda_1045():
        OP_6D(-149400, 6280, 9140, 2000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1045)

    def lambda_105D():
        OP_67(0, 4560, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_105D)

    def lambda_1075():
        OP_6C(224000, 2000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1075)

    def lambda_1085():
        OP_6B(2560, 2000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_1085)

    def lambda_1095():
        OP_8E(0xFE, 0xFFFDB868, 0x175C, 0x23B4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1095)

    def lambda_10B0():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_10B0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x14E, 0x1)

    ChrTalk(    #18
        0x14E,
        (
            "#1901F#12P…………波利……\x01",
            "……求求你……\x02\x03",

            "#1901F……赶快出来吧……\x02\x03",

            "是我……不好，\x01",
            "求、求你了……波利……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_1160():
        OP_6D(-148400, 6280, 9140, 2000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1160)

    def lambda_1178():
        OP_8E(0xFE, 0xFFFDBB88, 0x175C, 0x23B4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1178)
    WaitChrThread(0x14E, 0x1)
    Fade(100)
    SetChrChipByIndex(0x14E, 4)
    SetChrSubChip(0x14E, 0)
    SetChrFlags(0x14E, 0x2)
    SetChrFlags(0x14E, 0x800)
    SetChrFlags(0x14E, 0x20)
    SetChrFlags(0x14E, 0x4)

    def lambda_11BB():
        OP_99(0xFE, 0x0, 0x4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_11BB)

    def lambda_11CB():
        OP_8F(0xFE, 0xFFFDBC50, 0x16EE, 0x23B4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_11CB)

    ChrTalk(    #19 op#A op#5
        0x14E,
        "#1902F#3S#4P#10A#12P啊呜……！\x05\x02",
    )

    OP_22(0x8E, 0x0, 0x28)
    OP_22(0xD1, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    CloseMessageWindow()
    Sleep(1000)

    def lambda_1232():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_1232)

    ChrTalk(    #20
        0x14E,
        "#1901F#12P呜…………\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(800)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrSubChip(0x14E, 5)
    Sleep(1000)

    ChrTalk(    #21
        0x14E,
        (
            "#1901F#12P………………\x02\x03",

            "#1901F（不能哭……\x01",
            "  不能…………）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1500)

    def lambda_12DB():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_12DB)

    def lambda_12F5():
        OP_99(0xFE, 0x6, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_12F5)

    ChrTalk(    #22
        0x14E,
        (
            "#1901F#12P……呜……嗯……\x01",
            "…………呜……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    def lambda_1340():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0x2EE)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_1340)
    OP_43(0x14E, 0x0, 0x0, 0x8)
    StopSound(0x64, 0xC350, 0xFA0)
    Sleep(2000)

    def lambda_1373():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_1373)
    Sleep(2000)
    OP_44(0x14E, 0x3)
    Sleep(1000)
    StopSound(0x3DB8, 0xEA60, 0xBB8)
    Sleep(4000)
    SetChrPos(0x11, -143440, 4000, 20700, 200)

    NpcTalk(    #23
        0x11,
        "声音",
        (
            "啊，现在这个季节\x01",
            "果然还是有些冷哦。\x02",
        )
    )

    Jump("loc_13F1")

    label("loc_13F1")

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1000, 0x2, 0x7, 0x96, 0x1)
    Sleep(1000)
    OP_63(0x14E)
    Fade(200)
    SetChrChipByIndex(0x14E, 65535)
    SetChrSubChip(0x14E, 0)
    SetChrPos(0x14E, -148400, 5970, 9140, 90)
    ClearChrFlags(0x14E, 0x2)
    ClearChrFlags(0x14E, 0x800)
    ClearChrFlags(0x14E, 0x20)
    ClearChrFlags(0x14E, 0x4)
    OP_95(0x14E, 0x0, 0x0, 0x0, 0x190, 0xFA0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x0)

    def lambda_147E():
        OP_6D(-147340, 6140, 10920, 5000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_147E)

    def lambda_1496():
        OP_6C(234000, 5000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1496)

    def lambda_14A6():
        OP_6B(2980, 5000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_14A6)

    def lambda_14B6():
        OP_67(0, 3760, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_14B6)

    def lambda_14CE():
        OP_6E(264, 5000)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_14CE)

    def lambda_14DE():
        OP_8E(0xFE, 0xFFFDBFD4, 0x17C0, 0x16D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_14DE)
    WaitChrThread(0x14E, 0x1)

    def lambda_14FE():
        OP_8E(0xFE, 0xFFFDC308, 0x1798, 0x17E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_14FE)
    WaitChrThread(0x14E, 0x1)
    OP_63(0x14E)
    OP_8C(0x14E, 0, 500)
    SetChrFlags(0x11, 0x800)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    OP_4A(0x11, 255)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_1545():
        OP_8E(0xFE, 0xFFFDC650, 0x175C, 0x2ECC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1545)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    WaitChrThread(0x15, 0x0)
    OP_8C(0x11, 90, 280)
    Sleep(800)
    SetChrName("玛丽")

    ChrTalk(    #24
        0x14E,
        "#1714F#2P……………………！！？\x02",
    )

    Jump("loc_15B1")

    label("loc_15B1")

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 3)

    def lambda_15C7():
        OP_9E(0xFE, 0x14, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_15C7)
    Sleep(300)
    WaitChrThread(0x11, 0x3)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Sleep(300)
    SetChrName("古怪的魔兽")

    ChrTalk(    #25
        0x11,
        (
            "呼…………\x01",
            "还是再睡个回笼觉吧……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1638():
        OP_6D(-149100, 6060, 7000, 2500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1638)

    def lambda_1650():
        OP_6C(210000, 2500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1650)
    OP_8C(0x11, 225, 600)
    Sleep(500)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_1676():
        OP_8E(0xFE, 0xFFFDBA98, 0x175C, 0x2314, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1676)
    Sleep(1000)
    SetChrFlags(0x14E, 0x4)

    def lambda_169B():
        OP_8E(0xFE, 0xFFFDC6AA, 0x17AC, 0x196E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_169B)
    WaitChrThread(0x14E, 0x1)

    def lambda_16BB():
        OP_8E(0xFE, 0xFFFDC6C8, 0x17AC, 0x2788, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_16BB)
    WaitChrThread(0x14E, 0x1)
    ClearChrFlags(0x14E, 0x4)
    OP_8C(0x14E, 260, 500)

    def lambda_16E7():

        label("loc_16E7")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_16E7")

    QueueWorkItem2(0x14E, 3, lambda_16E7)

    ChrTalk(    #26
        0x14E,
        "#1714F你、你是？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #27
        0x11,
        "#2P…………哎？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 80, 500)
    Sleep(500)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2300, 0x2, 0x7, 0xC8, 0x1)
    Sleep(200)
    OP_95(0x11, 0x0, 0x190, 0x0, 0x190, 0x1388)
    Sleep(1000)
    OP_63(0x11)

    def lambda_177C():
        OP_6D(-146880, 6090, 5530, 1500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_177C)

    def lambda_1794():
        OP_67(0, 3480, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1794)

    def lambda_17AC():
        OP_6C(180000, 1500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_17AC)
    OP_8C(0x11, 180, 600)
    OP_22(0x81, 0x0, 0x64)
    ClearChrFlags(0x11, 0x800)

    def lambda_17CD():
        OP_8E(0xFE, 0xFFFDC09C, 0x178E, 0x1892, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_17CD)
    WaitChrThread(0x11, 0x1)

    def lambda_17ED():
        OP_9E(0xFE, 0xF, 0x0, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_17ED)
    OP_44(0x14E, 0x3)
    WaitChrThread(0x15, 0x0)

    ChrTalk(    #28
        0x11,
        (
            "#3S#2P怎、怎、怎、怎么了啊，真是的！\x01",
            "别吓唬人啊～！#2S\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_44(0x11, 0x0)
    Sleep(300)

    ChrTalk(    #29
        0x11,
        (
            "#2P差、差点让我\x01",
            "心脏都停止跳动了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1890():
        OP_6D(-147360, 5980, 3220, 2000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1890)

    def lambda_18A8():
        OP_67(0, 2920, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_18A8)

    def lambda_18C0():
        OP_6B(3070, 2000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_18C0)

    def lambda_18D0():
        OP_6C(180000, 2000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_18D0)

    def lambda_18E0():
        OP_8E(0xFE, 0xFFFDC02E, 0x173E, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_18E0)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 180, 400)
    WaitChrThread(0x15, 0x0)

    ChrTalk(    #30
        0x14E,
        "#1714F#6P…………哇。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2300, 0x28, 0x2B, 0x64, 0x2)
    TurnDirection(0x11, 0x14E, 600)
    Sleep(500)

    ChrTalk(    #31
        0x11,
        (
            "#11P……什、什么？\x02\x03",

            "我脸上\x01",
            "有什么东西吗？？\x02",
        )
    )

    Jump("loc_198B")

    label("loc_198B")

    CloseMessageWindow()
    WaitChrThread(0x11, 0x3)

    ChrTalk(    #32
        0x14E,
        (
            "#1903F#6P噗……#3S啊哈哈哈哈！\x01",
            "好奇怪～！#2S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x14E,
        "#1903F#6P#3S啊哈哈哈哈哈哈哈哈哈哈！#2S\x02",
    )

    OP_7C(0x64, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x11, 0x0, 2300, 0x28, 0x2B, 0x64, 0x2)
    Sleep(1000)

    ChrTalk(    #34
        0x11,
        (
            "#11P#40W什……#200W\x01",
            "#20W笑得太夸张啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x14E,
        (
            "#1718F#6P呵呵呵……\x01",
            "你在这里干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        "#11P我、我吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        (
            "#11P啊～……\x01",
            "最近好像发生了不少事，\x01",
            "所以我就藏起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x14E,
        "#1714F#6P不少事，是什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x11,
        (
            "#11P比如古罗力亚斯啊，辉之环啊，\x01",
            "……这些东西你没听说过吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x14E,
        "#1900F#6P？？不太清楚……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_1B87():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1B87)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-144710, 2210, 47660, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(280000, 0)
    OP_6E(325, 0)
    SetChrPos(0x14E, -140720, 2020, 46040, 45)
    SetChrPos(0x11, -142140, 2000, 47480, 45)
    SetChrFlags(0x11, 0x800)
    SoundLoad(16)

    def lambda_1C0E():
        OP_8E(0xFE, 0xFFFDE5A4, 0x7F8, 0xC030, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1C0E)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_1C33():
        OP_8E(0xFE, 0xFFFDDE60, 0x7D0, 0xC5A8, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C33)
    OP_43(0x14E, 0x3, 0x0, 0x9)
    FadeToBright(2000, 0)

    def lambda_1C5E():
        OP_6D(-140810, 2070, 50260, 4500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1C5E)

    def lambda_1C76():
        OP_6C(267000, 4500)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_1C76)
    WaitChrThread(0x15, 0x0)
    Fade(1000)
    OP_6D(-141100, 2029, 49930, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(267000, 0)
    OP_6E(250, 0)
    OP_0D()
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    TurnDirection(0x14E, 0x11, 500)
    Sleep(100)
    TurnDirection(0x11, 0x14E, 500)
    Sleep(500)

    ChrTalk(    #41
        0x14E,
        "#1710F唔～你还是个孩子呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        (
            "#2P是啊。\x01",
            "才３２０岁左右呢～。\x02",
        )
    )

    Jump("loc_1D4D")

    label("loc_1D4D")

    CloseMessageWindow()

    ChrTalk(    #43
        0x14E,
        "#1714F咦～怎么会～！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "#2P这很普通啦，很普通。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x14E,
        (
            "#1714F是、是吗？\x02\x03",

            "#1900F嗯～\x01",
            "感觉好像有点奇怪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x11,
        "#2P不说这个了，肚子好饿～。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 45, 400)
    Sleep(800)
    OP_8C(0x11, 180, 400)
    Sleep(800)

    ChrTalk(    #47
        0x11,
        (
            "#2P有没有哪里\x01",
            "开着蒲公英呢～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x14E,
        "#1714F你喜欢蒲公英？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 145, 400)
    Sleep(400)

    ChrTalk(    #49
        0x11,
        (
            "#2P我还喜欢向日葵。\x02\x03",

            "有太阳的味道哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x14E,
        "#1900F嗯～……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #51
        0x14E,
        "#1718F啊，对了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 235, 400)
    Sleep(300)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(1000)
    OP_63(0x14E)
    Sleep(500)
    TurnDirection(0x14E, 0x11, 400)
    Sleep(100)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)

    ChrTalk(    #52
        0x14E,
        (
            "#1711F铛铛～！\x01",
            "玛丽特制三明治！\x02\x03",

            "虽然没放蒲公英和向日葵，\x01",
            "不过用了院子里采来的油菜花哦。\x02\x03",

            "#1718F一定会有太阳的味道的！\x02\x03",

            "来，张嘴～……\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 3)
    Sleep(250)

    def lambda_2008():
        OP_6D(-141090, 2050, 50180, 1000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2008)

    def lambda_2020():
        OP_6B(2940, 1000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2020)

    def lambda_2030():
        OP_8F(0xFE, 0xFFFDE248, 0x7D0, 0xC1D4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2030)
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x15, 0x0)
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_205F():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x258, 0xFA0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_205F)
    WaitChrThread(0x14E, 0x1)
    Sleep(300)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 7)
    Sleep(300)
    OP_22(0x10, 0x0, 0x64)
    OP_9E(0x11, 0x0, 0x14, 0x3E8, 0x3E8)
    Sleep(1000)

    ChrTalk(    #53
        0x14E,
        "#1710F怎样，好吃吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        "#2P嗯咕嗯咕……\x02",
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2300, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x11)

    ChrTalk(    #55
        0x11,
        "#2P……好、好好吃！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x14E,
        (
            "#1719F这是我做的哦。\x02\x03",

            "嘿嘿，厉害吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        (
            "#2P厉、厉害！\x01",
            "刮目相看了！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x11,
        "#2P……还想要一个。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x14E,
        (
            "#1714F哎～还要一个？\x01",
            "我的份都没了啦～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x11,
        "#2P那要一半。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x14E,
        (
            "#1710F唔～……好吧。\x02\x03",

            "#1711F来，一半！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x11, 0x0, 2200, 0x8, 0x9, 0xC8, 0x5)
    Sleep(2000)
    OP_63(0x11)
    OP_43(0x11, 0x3, 0x0, 0x5)
    Sleep(2000)

    def lambda_2260():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2260)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0x15, 0x1)
    Sleep(1000)
    OP_6D(-153950, 2009, 119810, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(251000, 0)
    OP_6E(262, 0)
    StopSound(0x3DB8, 0x15F90, 0x0)

    def lambda_22CF():
        OP_6C(280000, 10000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_22CF)
    SetChrPos(0x14E, -155900, 2040, 132380, 156)
    SetChrPos(0x11, -155900, 2040, 132380, 156)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_43(0x14E, 0x3, 0x0, 0x6)
    OP_43(0x14E, 0x2, 0x0, 0x7)
    Sleep(500)
    OP_43(0x11, 0x3, 0x0, 0x6)
    WaitChrThread(0x14E, 0x3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x14E, 0x2)
    OP_44(0x15, 0x3)
    Sleep(1000)
    OP_6D(-155120, 2000, 120200, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(298000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -156480, 2009, 118340, 250)
    SetChrPos(0x11, -149000, 2040, 120990, 250)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_23BA():
        OP_8F(0xFE, 0xFFFDB0A2, 0x7BC, 0x1D5F6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_23BA)
    Sleep(1500)

    def lambda_23DA():
        OP_8C(0xFE, 70, 400)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_23DA)
    WaitChrThread(0x14E, 0x2)
    Sleep(300)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(1000)
    OP_63(0x14E)
    Sleep(500)

    def lambda_2411():
        OP_8C(0xFE, 250, 500)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_2411)
    WaitChrThread(0x14E, 0x2)
    Sleep(500)

    def lambda_2429():
        OP_8F(0xFE, 0xFFFDA738, 0x7E4, 0x1D254, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2429)
    Sleep(1000)

    def lambda_2449():
        OP_8C(0xFE, 70, 700)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_2449)
    WaitChrThread(0x14E, 0x2)
    OP_44(0x11, 0x1)
    OP_62(0x11, 0x0, 2200, 0x10, 0x13, 0xC8, 0x1)
    Sleep(1000)
    OP_9E(0x11, 0x14, 0x0, 0x3E8, 0x7D0)
    Sleep(1000)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    OP_95(0x14E, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    OP_95(0x14E, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 1)
    IdleLoop()
    Return()

    # Function_4_6B5 end

    def Function_5_24E1(): pass

    label("Function_5_24E1")

    Fade(250)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 3)
    Sleep(250)
    Sleep(500)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2505():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x258, 0xFA0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2505)
    WaitChrThread(0x14E, 0x1)
    Sleep(300)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 7)
    Sleep(300)
    OP_22(0x10, 0x0, 0x64)
    OP_9E(0x11, 0x0, 0x14, 0x3E8, 0x3E8)
    Sleep(1000)
    Return()

    # Function_5_24E1 end

    def Function_6_2554(): pass

    label("Function_6_2554")

    OP_8F(0xFE, 0xFFFDAEF4, 0x7C6, 0x1D740, 0x1388, 0x0)
    OP_97(0xFE, 0xFFFDA6CA, 0x1D33A, 0x57E40, 0x1388, 0x1)
    OP_8F(0xFE, 0xFFFDBE26, 0xECE, 0x1B346, 0x1388, 0x0)
    Return()

    # Function_6_2554 end

    def Function_7_2592(): pass

    label("Function_7_2592")

    Sleep(500)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(400)
    OP_62(0x11, 0x0, 2500, 0x26, 0x27, 0xC8, 0x2)
    Sleep(2000)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(400)
    OP_62(0x11, 0x0, 2500, 0x26, 0x27, 0xC8, 0x2)
    Sleep(2000)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(400)
    OP_62(0x11, 0x0, 2500, 0x26, 0x27, 0xC8, 0x2)
    Return()

    # Function_7_2592 end

    def Function_8_261D(): pass

    label("Function_8_261D")

    OP_22(0x1C3, 0x1, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x5A)
    Sleep(4000)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_23(0x1C3)
    Return()

    # Function_8_261D end

    def Function_9_26A0(): pass

    label("Function_9_26A0")

    Sleep(1200)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(800)
    OP_62(0x11, 0x0, 2300, 0x26, 0x27, 0xC8, 0x2)
    Sleep(1600)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(800)
    OP_62(0x11, 0x0, 2300, 0x26, 0x27, 0xC8, 0x2)
    Return()

    # Function_9_26A0 end

    def Function_10_26FD(): pass

    label("Function_10_26FD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_6D(-152660, 4800, 102120, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(248000, 0)
    OP_6E(282, 0)
    SetChrPos(0x14E, -151400, 4040, 103280, 202)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    OP_4A(0x11, 255)
    SetChrPos(0x11, -152740, 4000, 101020, 32)

    def lambda_2781():
        OP_6B(2740, 5000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2781)

    def lambda_2791():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2791)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(1000)
    OP_62(0x11, 0x0, 2200, 0x26, 0x27, 0xC8, 0x2)
    Sleep(1000)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xC8, 0x3)
    Sleep(1000)
    OP_62(0x11, 0x0, 2200, 0x26, 0x27, 0xC8, 0x3)
    OP_0D()
    WaitChrThread(0x15, 0x1)
    OP_63(0x14E)
    OP_63(0x11)
    OP_43(0x14E, 0x3, 0x0, 0x12)
    Sleep(2000)
    OP_9E(0x11, 0x14, 0x0, 0x3E8, 0x7D0)
    Sleep(1000)
    OP_8C(0x11, 350, 400)
    Sleep(800)
    OP_8C(0x11, 100, 400)
    Sleep(800)

    ChrTalk(    #62
        0x11,
        "#5P变、变冷了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x14E,
        (
            "#1900F#12P是、是吗……？\x02\x03",

            "#1714F啊，明白了！\x01",
            "你怕冷！\x02",
        )
    )

    Jump("loc_28B9")

    label("loc_28B9")

    CloseMessageWindow()
    OP_8C(0x11, 32, 400)
    Sleep(400)

    ChrTalk(    #64
        0x11,
        (
            "#5P没、没那回事哦。\x02\x03",

            "这、这点程度无所谓啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x14E,
        (
            "#1710F#12P呵呵，稍等一下。\x01",
            "我这就拾些柴来。\x02\x03",

            "#1718F点起火来，\x01",
            "一定就暖和了。\x02\x03",

            "…………对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x11,
        (
            "#5P明、明白了。\x02\x03",

            "麻烦快一点……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    ClearChrFlags(0x14E, 0x40)
    ClearChrFlags(0x11, 0x40)
    OP_4B(0x11, 255)
    OP_A3(0x2F1B)
    OP_A3(0x2F1C)
    OP_A3(0x2F1D)
    OP_A3(0x2F1E)
    OP_A3(0x2F1F)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_A2(0x2F25)
    EventEnd(0x0)
    Return()

    # Function_10_26FD end

    def Function_11_29E7(): pass

    label("Function_11_29E7")


    def lambda_29ED():
        OP_8F(0xFE, 0xFFFDB700, 0x1798, 0xFFFFE7C8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_29ED)
    WaitChrThread(0x10, 0x1)

    def lambda_2A0D():
        OP_8F(0xFE, 0xFFFDC86C, 0x175C, 0xFFFFCC0C, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2A0D)
    WaitChrThread(0x10, 0x1)

    def lambda_2A2D():
        OP_8F(0xFE, 0xFFFDD938, 0x17D4, 0xFFFFC284, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2A2D)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_11_29E7 end

    def Function_12_2A48(): pass

    label("Function_12_2A48")

    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0x78, 0x1)
    Sleep(1000)
    OP_63(0x14E)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x0)

    def lambda_2A7F():
        OP_8E(0xFE, 0xFFFDAF6C, 0x1734, 0xFFFFD29C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2A7F)
    WaitChrThread(0x14E, 0x1)

    def lambda_2A9F():
        OP_8E(0xFE, 0xFFFDAC88, 0x1734, 0xFFFFD4E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2A9F)
    WaitChrThread(0x14E, 0x1)

    def lambda_2ABF():

        label("loc_2ABF")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_2ABF")

    QueueWorkItem2(0x14E, 3, lambda_2ABF)
    Sleep(500)
    OP_63(0x14E)
    Return()

    # Function_12_2A48 end

    def Function_13_2AD3(): pass

    label("Function_13_2AD3")


    def lambda_2AD9():
        OP_8E(0xFE, 0xFFFDB1D8, 0x17FC, 0xFFFFEE44, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2AD9)
    WaitChrThread(0x14E, 0x1)

    def lambda_2AF9():
        OP_8E(0xFE, 0xFFFD907C, 0x175C, 0xFFFFFD44, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2AF9)
    WaitChrThread(0x14E, 0x1)

    def lambda_2B19():
        OP_8E(0xFE, 0xFFFD9C84, 0x177A, 0x1CAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2B19)
    WaitChrThread(0x14E, 0x1)

    def lambda_2B39():
        OP_8E(0xFE, 0xFFFDB480, 0x1798, 0x2314, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2B39)
    WaitChrThread(0x14E, 0x1)
    Return()

    # Function_13_2AD3 end

    def Function_14_2B54(): pass

    label("Function_14_2B54")

    OP_8C(0x14E, 315, 500)
    Sleep(600)
    OP_8C(0x14E, 90, 500)
    Sleep(600)
    OP_8C(0x14E, 0, 500)
    Return()

    # Function_14_2B54 end

    def Function_15_2B74(): pass

    label("Function_15_2B74")

    OP_8C(0x14E, 90, 500)
    Sleep(600)
    OP_8C(0x14E, 270, 500)
    Sleep(600)
    OP_8C(0x14E, 15, 500)
    Sleep(600)
    OP_8C(0x14E, 225, 500)
    Return()

    # Function_15_2B74 end

    def Function_16_2BA0(): pass

    label("Function_16_2BA0")


    def lambda_2BA6():
        OP_6D(-158840, 6000, -40, 3900)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2BA6)

    def lambda_2BBE():
        OP_67(0, 5700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2BBE)

    def lambda_2BD6():
        OP_6C(166000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2BD6)

    def lambda_2BE6():
        OP_6B(2580, 4000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_2BE6)
    WaitChrThread(0x15, 0x1)

    def lambda_2BFB():
        OP_6D(-150400, 6340, 8980, 3000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2BFB)

    def lambda_2C13():
        OP_67(0, 4560, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2C13)

    def lambda_2C2B():
        OP_6C(224000, 2000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2C2B)

    def lambda_2C3B():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_2C3B)
    WaitChrThread(0x15, 0x0)
    Return()

    # Function_16_2BA0 end

    def Function_17_2C4B(): pass

    label("Function_17_2C4B")

    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_2C5B():
        OP_8F(0xFE, 0xFFFDB6A6, 0x17AC, 0x21A2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C5B)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Return()

    # Function_17_2C4B end

    def Function_18_2C80(): pass

    label("Function_18_2C80")

    OP_22(0x1C3, 0x0, 0x64)
    Sleep(2500)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_23(0x1C3)
    Return()

    # Function_18_2C80 end

    def Function_19_2CB2(): pass

    label("Function_19_2CB2")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_6D(-154790, 2070, 128600, 0)
    OP_67(0, 4570, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(297000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -153300, 2110, 126400, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    OP_4A(0x11, 255)
    SetChrPos(0x11, -151220, 1980, 119660, 0)

    def lambda_2D34():
        OP_8E(0xFE, 0xFFFDA36E, 0x74E, 0x1FA72, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2D34)
    FadeToBright(2000, 0)
    Sleep(1500)
    OP_43(0x11, 0x3, 0x0, 0x14)
    WaitChrThread(0x14E, 0x1)
    OP_62(0x14E, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)
    Sleep(500)
    OP_63(0x14E)
    OP_8C(0x14E, 180, 400)
    Sleep(500)

    ChrTalk(    #67
        0x14E,
        "#1714F哎呀呀？你怎么跟来了？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x3)

    ChrTalk(    #68
        0x11,
        "因、因为天色变暗了嘛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        "一、一个人好危险……\x02",
    )

    CloseMessageWindow()

    def lambda_2E01():
        OP_8E(0xFE, 0xFFFDA878, 0x802, 0x1F0FE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2E01)
    WaitChrThread(0x14E, 0x1)
    OP_22(0xD1, 0x0, 0x64)

    def lambda_2E26():
        OP_9E(0x11, 0x14, 0x0, 0x7D0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_2E26)

    ChrTalk(    #70
        0x14E,
        "#1719F#2P抱～……！！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14E, 0x2)
    Sleep(500)

    def lambda_2E6C():
        OP_8F(0xFE, 0xFFFDA63E, 0x7E4, 0x1F5F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2E6C)
    WaitChrThread(0x14E, 0x1)
    Sleep(300)

    ChrTalk(    #71
        0x14E,
        "#1710F#2P……怎样？有精神了吗？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_2ECC():
        OP_8E(0xFE, 0xFFFDA7BA, 0x7ED, 0x1F1C6, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2ECC)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Sleep(300)

    def lambda_2EFB():
        OP_9E(0x14E, 0xA, 0x0, 0x7D0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2EFB)

    ChrTalk(    #72
        0x14E,
        (
            "#1903F#2P哇，好痒！\x02\x03",

            "呵呵，不仅软绵绵的，\x01",
            "还散发着香气……\x02\x03",

            "#1714F（……咦？这个香味……）\x02\x03",

            "（感觉好像\x01",
            "  似曾相识……）\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x14E, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_2FC2():
        OP_8F(0xFE, 0xFFFDA9CC, 0x83E, 0x1EDC0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2FC2)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Sleep(300)

    ChrTalk(    #73
        0x11,
        (
            "一起找柴火吧。\x02\x03",

            "这样比较暖和。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x14E,
        "#1718F#2P嗯，就这么办吧！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    ClearChrFlags(0x11, 0x1)
    AddParty(0x4F, 0xFF, 0xFF)
    SetChrPos(0x150, -153140, 2110, 126400, 0)
    OP_A2(0x2F26)
    OP_B2(0x0, 0x0, 0x80)
    EventEnd(0x0)
    Return()

    # Function_19_2CB2 end

    def Function_20_3070(): pass

    label("Function_20_3070")

    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_3080():
        OP_8E(0xFE, 0xFFFDA9CC, 0x83E, 0x1EDC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3080)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Return()

    # Function_20_3070 end

    def Function_21_30A5(): pass

    label("Function_21_30A5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-165040, 6000, 3720, 0)
    OP_67(0, 7260, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(284000, 0)
    OP_6E(280, 0)
    SoundLoad(270)
    SetChrPos(0x14E, -162570, 6010, 3090, 280)
    RemoveParty(0x4F, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8)
    SetChrFlags(0x11, 0x1)
    SetChrPos(0x11, -166680, 5990, 6400, 140)
    OP_4A(0x11, 255)
    SetChrPos(0x14, -163760, 6800, 3390, 0)
    OP_72(0x7, 0x0)
    ExitThread()
    OP_72(0x407, 0x0)
    ExitThread()
    LoadEffect(0x0, "map\\\\bigfire.eff")
    LoadEffect(0x1, "monster\\\\ms30703.eff")

    def lambda_3176():
        OP_6D(-166920, 5980, 4190, 4000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_3176)

    def lambda_318E():
        OP_67(0, 4720, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_318E)

    def lambda_31A6():
        OP_6B(2660, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_31A6)

    def lambda_31B6():
        OP_6E(262, 4000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_31B6)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x14E, 0x3, 0x0, 0x16)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x14E, 0x3)

    ChrTalk(    #75
        0x14E,
        (
            "#1718F#5P这样就好了。\x02\x03",

            "#1900F……啊，火怎么办呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x11,
        (
            "#2P没问题。\x01",
            "请退后一点！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 320, 500)
    Sleep(200)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)

    def lambda_3277():
        OP_6D(-167740, 5970, 4630, 1300)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3277)

    def lambda_328F():
        OP_6B(2560, 1300)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_328F)

    def lambda_329F():
        OP_6C(257000, 1300)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_329F)

    def lambda_32AF():
        OP_8E(0xFE, 0xFFFD75D8, 0x1766, 0xFDB, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_32AF)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 100, 500)
    WaitChrThread(0x15, 0x0)
    Sleep(300)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_32EA():
        OP_8E(0xFE, 0xFFFD772C, 0x1766, 0x16BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_32EA)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x11, 3)
    SetChrSubChip(0x11, 0)
    Sleep(800)
    SetChrPos(0x14, -163760, 6800, 3390, 0)

    def lambda_333E():

        label("loc_333E")

        OP_7C(0x32, 0x32, 0xBB8, 0x3E8)
        OP_48()
        Jump("loc_333E")

    QueueWorkItem2(0x14, 3, lambda_333E)
    OP_22(0x26D, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x11, 500, 1040, 500, 0, -30, 0, 500, 500, 500, 0x14, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x0, 0x1, 0xFF, -163760, 6100, 3390, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_71(0x7, 0x0)
    ExitThread()
    OP_71(0x407, 0x0)
    ExitThread()
    OP_72(0x8, 0x0)
    ExitThread()
    OP_72(0x408, 0x0)
    ExitThread()
    Sleep(1000)
    OP_44(0x14, 0x3)
    OP_22(0x10E, 0x1, 0x5A)
    Sleep(1500)
    Fade(500)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    Sleep(800)

    ChrTalk(    #77
        0x14E,
        (
            "#1714F#5P哇，好厉害！\x01",
            "你还会吐火啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        (
            "#2P只要练习练习，\x01",
            "谁都能学会啦～。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 340, 500)
    Sleep(400)

    ChrTalk(    #79
        0x14E,
        "#1712F哎～你骗人！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 160, 600)
    Sleep(400)

    ChrTalk(    #80
        0x11,
        "#2P不骗你啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x11,
        (
            "#2P我也是\x01",
            "最近才学会的～。\x02",
        )
    )

    Jump("loc_34E3")

    label("loc_34E3")

    CloseMessageWindow()

    ChrTalk(    #82
        0x14E,
        (
            "#1714F是、是吗？\x02\x03",

            "#1900F我、我也能行吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x11,
        "#2P练习个３２０年就会了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)
    Sleep(300)

    ChrTalk(    #84
        0x14E,
        "#1717F那、那怎么可能～！！\x02",
    )

    CloseMessageWindow()

    def lambda_358B():
        OP_6B(2660, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_358B)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 1)
    IdleLoop()
    Return()

    # Function_21_30A5 end

    def Function_22_35B3(): pass

    label("Function_22_35B3")


    def lambda_35B9():

        label("loc_35B9")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_35B9")

    QueueWorkItem2(0x14E, 2, lambda_35B9)

    def lambda_35CA():
        OP_8F(0xFE, 0xFFFD808C, 0x1770, 0x1130, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_35CA)
    WaitChrThread(0x14E, 0x1)
    Sleep(600)

    def lambda_35EF():
        OP_8F(0xFE, 0xFFFD7B50, 0x1770, 0xE88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_35EF)
    WaitChrThread(0x14E, 0x1)
    OP_44(0x14E, 0x2)
    Sleep(300)
    Return()

    # Function_22_35B3 end

    def Function_23_3613(): pass

    label("Function_23_3613")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-155620, 6060, 2700, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(3680, 0)
    OP_6C(286000, 0)
    OP_6E(424, 0)
    SetChrFlags(0x14E, 0x4)
    SetChrPos(0x14E, -164800, 5820, 5800, 150)
    SetChrFlags(0x14E, 0x2)
    SetChrChipByIndex(0x14E, 5)
    SetChrSubChip(0x14E, 0)

    def lambda_3687():

        label("loc_3687")

        OP_99(0xFE, 0x0, 0x7, 0x1F4)
        OP_48()
        Jump("loc_3687")

    QueueWorkItem2(0x14E, 2, lambda_3687)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x800)
    SetChrPos(0x11, -165320, 6020, 5520, 150)
    OP_4A(0x11, 255)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)

    def lambda_36CD():

        label("loc_36CD")

        OP_99(0xFE, 0x0, 0x7, 0x1F4)
        OP_48()
        Jump("loc_36CD")

    QueueWorkItem2(0x11, 2, lambda_36CD)
    OP_72(0x5, 0x0)
    ExitThread()
    OP_72(0x405, 0x0)
    ExitThread()

    def lambda_36EC():
        OP_6D(-165320, 6020, 5520, 9000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_36EC)

    def lambda_3704():
        OP_6B(3180, 9000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3704)
    FadeToBright(4000, 0)
    WaitChrThread(0x15, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(-165320, 6420, 5520, 0)
    OP_67(0, 4600, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(286000, 0)
    OP_6E(250, 0)
    Sleep(2000)

    def lambda_376E():
        OP_6B(2660, 15000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_376E)

    ChrTalk(    #85
        0x14E,
        "#1719F#60W嗯…………\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    ChrTalk(    #86
        0x14E,
        (
            "#1719F#60W好软……\x01",
            "……还有这个香味……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)

    ChrTalk(    #87
        0x14E,
        (
            "#1719F#60W…………果然，\x01",
            "……我是知道的……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_44(0x14E, 0x2)
    Fade(500)
    SetChrChipByIndex(0x14E, 11)
    SetChrSubChip(0x14E, 0)
    OP_0D()
    OP_99(0x14E, 0x0, 0x3, 0x3E8)
    Sleep(300)

    ChrTalk(    #88
        0x14E,
        "#1719F#60W……是什么呢…………？\x02",
    )

    CloseMessageWindow()
    FadeToDark(4000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #89
        "\x07\x00\x18…………好温暖…………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_20(0xBB8)
    OP_21()
    OP_A2(0x2506)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 1)
    IdleLoop()
    Return()

    # Function_23_3613 end

    def Function_24_38C7(): pass

    label("Function_24_38C7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-165320, 6420, 5520, 0)
    OP_67(0, 4600, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(286000, 0)
    OP_6E(250, 0)
    StopSound(0x64, 0xEA60, 0x0)
    SetChrFlags(0x14E, 0x4)
    SetChrPos(0x14E, -164800, 5820, 5800, 150)
    SetChrFlags(0x14E, 0x2)
    SetChrChipByIndex(0x14E, 5)
    SetChrSubChip(0x14E, 0)

    def lambda_3948():

        label("loc_3948")

        OP_99(0xFE, 0x0, 0x7, 0x1F4)
        OP_48()
        Jump("loc_3948")

    QueueWorkItem2(0x14E, 2, lambda_3948)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x11, 0x1)
    OP_72(0x7, 0x0)
    ExitThread()
    OP_72(0x407, 0x0)
    ExitThread()
    LoadEffect(0x2, "map\\mp087_00.eff")
    FadeToBright(2000, 0)
    OP_0D()
    OP_9E(0x14E, 0xA, 0x0, 0x12C, 0xBB8)
    OP_44(0x14E, 0x2)
    Sleep(300)

    ChrTalk(    #90
        0x14E,
        "#1716F#12P哈嚏……！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    OP_44(0x14E, 0x2)
    Fade(1000)
    SetChrChipByIndex(0x14E, 6)
    SetChrSubChip(0x14E, 0)
    OP_0D()

    ChrTalk(    #91
        0x14E,
        "#1713F#12P嗯、嗯嗯…………？\x02",
    )

    CloseMessageWindow()

    def lambda_3A1F():
        OP_99(0xFE, 0x0, 0x4, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_3A1F)
    WaitChrThread(0x14E, 0x2)

    def lambda_3A34():
        OP_99(0xFE, 0x4, 0x3, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_3A34)
    WaitChrThread(0x14E, 0x2)

    def lambda_3A49():
        OP_99(0xFE, 0x3, 0x4, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_3A49)
    WaitChrThread(0x14E, 0x2)

    def lambda_3A5E():
        OP_99(0xFE, 0x4, 0x2, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_3A5E)
    WaitChrThread(0x14E, 0x2)
    Sleep(200)
    Fade(500)
    SetChrSubChip(0x14E, 5)
    OP_0D()

    ChrTalk(    #92
        0x14E,
        "#1714F#12P…………啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_3AAA():
        OP_67(0, 5260, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3AAA)

    def lambda_3AC2():
        OP_6B(2860, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3AC2)

    def lambda_3AD2():
        OP_6E(316, 4000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3AD2)
    Sleep(500)
    SetChrSubChip(0x14E, 7)
    Sleep(1000)
    SetChrSubChip(0x14E, 5)
    Sleep(150)
    SetChrSubChip(0x14E, 6)
    Sleep(1350)
    OP_22(0x8F, 0x0, 0x64)
    Fade(300)
    SetChrChipByIndex(0x14E, 65535)
    SetChrSubChip(0x14E, 0)
    ClearChrFlags(0x14E, 0x4)
    ClearChrFlags(0x14E, 0x2)
    SetChrPos(0x14E, -164800, 6020, 5800, 150)
    Sleep(500)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(2000)
    OP_63(0x14E)
    WaitChrThread(0x15, 0x0)

    def lambda_3B58():
        OP_6D(-164300, 5990, 6610, 4000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3B58)
    OP_8C(0x14E, 65, 400)

    def lambda_3B77():
        OP_8E(0xFE, 0xFFFD84EC, 0x175C, 0x1824, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_3B77)
    WaitChrThread(0x14E, 0x1)
    Sleep(500)
    OP_8C(0x14E, 320, 400)
    Sleep(1000)
    OP_8C(0x14E, 150, 400)
    Sleep(1000)

    def lambda_3BB4():
        OP_6D(-161920, 6020, 3830, 4000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3BB4)

    def lambda_3BCC():
        OP_8E(0xFE, 0xFFFD8BB8, 0x1784, 0xDD4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_3BCC)
    WaitChrThread(0x14E, 0x1)
    Sleep(500)
    OP_8C(0x14E, 220, 400)
    Sleep(1000)
    OP_8C(0x14E, 65, 400)
    Sleep(1000)

    ChrTalk(    #93
        0x14E,
        "#1714F#5P…………不在了……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 285, 400)
    Sleep(1000)

    ChrTalk(    #94
        0x14E,
        (
            "#1713F#5P………………\x02\x03",

            "#1713F结束了啊……\x02",
        )
    )

    CloseMessageWindow()
    StopSound(0x64, 0x1ADB0, 0xFA0)
    Sleep(1000)
    OP_22(0x1C2, 0x0, 0x64)
    Sleep(4000)
    OP_8C(0x14E, 45, 400)
    Sleep(1000)

    ChrTalk(    #95
        0x14E,
        "#1713F#5P…………回去吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_3CCD():
        OP_8E(0xFE, 0xFFFDA71A, 0x1784, 0x218E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_3CCD)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_24(0x1C2, 0x5A)
    Sleep(200)
    OP_24(0x1C2, 0x50)
    Sleep(200)
    OP_24(0x1C2, 0x46)
    Sleep(200)
    OP_24(0x1C2, 0x3C)
    Sleep(200)
    OP_24(0x1C2, 0x32)
    Sleep(200)
    OP_24(0x1C2, 0x28)
    Sleep(200)
    OP_24(0x1C2, 0x1E)
    Sleep(200)
    OP_24(0x1C2, 0x14)
    OP_0D()
    OP_23(0x1C2)
    OP_44(0x14E, 0x1)
    Sleep(1500)
    OP_1D(0x7D)
    ClearMapFlags(0x10)
    OP_6D(-135320, 2410, 61200, 0)
    OP_67(0, 6590, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(191000, 0)
    OP_6E(311, 0)

    def lambda_3D8B():
        OP_6D(-141720, 2410, 61000, 10000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3D8B)
    SetChrPos(0x14E, -136060, 1970, 57120, 0)

    def lambda_3DB4():
        OP_8E(0xFE, 0xFFFDD064, 0x794, 0x111D4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_3DB4)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x15, 0x0)
    OP_6D(-146820, 4000, 90050, 0)
    OP_67(0, 7770, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(261000, 0)
    OP_6E(305, 0)

    def lambda_3E2A():
        OP_6D(-143670, 4000, 94700, 10000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3E2A)
    OP_44(0x14E, 0x1)
    SetChrPos(0x14E, -141620, 4019, 89840, 330)

    def lambda_3E57():
        OP_8E(0xFE, 0xFFFDC7A4, 0xF96, 0x16698, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_3E57)
    FadeToBright(2000, 0)
    WaitChrThread(0x14E, 0x1)

    def lambda_3E80():
        OP_8E(0xFE, 0xFFFDCC04, 0x10A4, 0x17444, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_3E80)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x15, 0x0)
    PlayEffect(0x2, 0xFF, 0xFF, -146100, -5000, 68530, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -133390, -5000, 66740, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -143890, -5000, 73350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -138880, -5000, 73210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -137110, -5000, 70530, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -134110, -5000, 68170, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -133040, -5000, 66590, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -133050, -5000, 70070, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -139440, -5000, 76200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -136720, -5000, 75940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0x14E, 0x1)
    Sleep(1500)
    StopSound(0x64, 0x186A0, 0x0)
    OP_6D(-140240, 2480, 64239, 0)
    OP_67(0, 5060, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(294000, 0)
    OP_6E(330, 0)
    SetChrPos(0x14E, -140100, 2000, 64180, 5)

    def lambda_4125():
        OP_6D(-144130, 2650, 72560, 6500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_4125)

    def lambda_413D():
        OP_6B(2460, 6500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_413D)

    def lambda_414D():
        OP_6E(316, 6500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_414D)

    def lambda_415D():
        OP_67(0, 4019, -10000, 6500)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_415D)

    def lambda_4175():
        OP_6C(298000, 6500)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_4175)

    def lambda_4185():
        OP_8E(0xFE, 0xFFFDD49C, 0x82A, 0x10F18, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4185)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x14E, 0x3, 0x0, 0x1E)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x14E, 0x1)
    Sleep(500)

    ChrTalk(    #96
        0x14E,
        "#1713F………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_41E4():
        OP_6D(-145110, 2720, 74470, 8000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_41E4)
    SetChrFlags(0x14E, 0x4)

    def lambda_4201():
        OP_8E(0xFE, 0xFFFDD2B2, 0x82A, 0x118A0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4201)
    WaitChrThread(0x14E, 0x1)

    def lambda_4221():
        OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_4221)
    Sleep(500)

    def lambda_4240():
        OP_8E(0xFE, 0xFFFDD15E, 0x91A, 0x11D14, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4240)
    WaitChrThread(0x14E, 0x1)

    def lambda_4260():
        OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_4260)
    Sleep(500)

    def lambda_427F():
        OP_8E(0xFE, 0xFFFDD104, 0xAD2, 0x120DE, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_427F)
    WaitChrThread(0x14E, 0x1)

    def lambda_429F():
        OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_429F)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_44(0x14E, 0x1)
    SetChrFlags(0x14E, 0x20)
    OP_22(0x58, 0x0, 0x64)
    Sleep(200)

    def lambda_42DF():
        OP_6D(-143820, 2650, 74500, 300)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_42DF)

    def lambda_42F7():
        OP_67(0, 3430, -10000, 300)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_42F7)

    def lambda_430F():
        OP_D0(1000, 300)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_430F)

    def lambda_431F():

        label("loc_431F")

        OP_9E(0xFE, 0x32, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_431F")

    QueueWorkItem2(0x14E, 3, lambda_431F)

    def lambda_433C():
        OP_8F(0xFE, 0xFFFDD366, 0xAD2, 0x1216A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_433C)
    OP_20(0x0)

    def lambda_435C():
        OP_7C(0x64, 0x64, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_435C)

    ChrTalk(    #97 op#A
        0x14E,
        "#6P#3S#5A啊…………！\x02",
    )

    OP_22(0x14D, 0x0, 0x46)
    OP_22(0x16D, 0x0, 0x64)
    Sleep(800)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_43A9():
        OP_6D(-143820, 1500, 74500, 1000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_43A9)

    def lambda_43C1():
        OP_D0(5000, 1000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_43C1)
    Fade(250)
    SetChrPos(0x14E, -143100, 2670, 73950, 354)
    ClearChrFlags(0x14E, 0x100)
    SetChrFlags(0x14E, 0x800)
    ClearChrFlags(0x14E, 0x1)
    OP_D1(334, 35000, 300000, 0, 0)
    SetChrFlags(0x14E, 0x4)
    SetChrFlags(0x14E, 0x20)

    def lambda_4413():
        OP_96(0x14E, 0xFFFDD938, 0xFFFFF254, 0x12264, 0x12C, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4413)

    def lambda_4431():
        OP_D1(254, 35000, 300000, -45000, 1000)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_4431)

    def lambda_444B():
        OP_8C(0x14E, 270, 200)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_444B)
    OP_22(0xBD, 0x0, 0x64)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    LoadEffect(0x3, "map\\mp253_01.eff")
    LoadEffect(0x4, "map\\mp253_04.eff")
    SoundLoad(128)
    SoundLoad(612)
    SoundLoad(215)
    OP_44(0x14E, 0xFF)
    SetChrFlags(0x14E, 0x100)
    ClearChrFlags(0x14E, 0x800)
    SetChrFlags(0x14E, 0x20)
    SetChrFlags(0x14E, 0x1000)
    SetChrPos(0x14E, -87660, 5200, -1140, 90)
    SetChrFlags(0x14E, 0x2)
    SetChrChipByIndex(0x14E, 7)
    SetChrSubChip(0x14E, 0)

    def lambda_44E4():

        label("loc_44E4")

        OP_99(0xFE, 0x0, 0x3, 0xBB8)
        OP_48()
        Jump("loc_44E4")

    QueueWorkItem2(0x14E, 2, lambda_44E4)
    OP_72(0x8, 0x0)
    ExitThread()
    OP_72(0x408, 0x0)
    ExitThread()
    OP_6D(-87660, -800, -1140, 0)
    OP_67(0, 3860, -10000, 0)
    OP_6B(750, 0)
    OP_6C(270000, 0)
    OP_6E(946, 0)
    OP_D0(0, 0)
    OP_22(0x85, 0x1, 0x3C)

    def lambda_454E():

        label("loc_454E")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_454E")

    QueueWorkItem2(0x10, 3, lambda_454E)
    OP_43(0x14E, 0x0, 0x0, 0x1C)
    StopSound(0x64, 0xAAB4, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)
    WaitChrThread(0x14E, 0x0)
    WaitChrThread(0x15, 0x0)
    Sleep(2000)

    def lambda_459B():
        OP_6B(650, 16000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_459B)
    OP_C4(0x0, 0x800)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #98
        "\x07\x0C\x18#60W#3S老师…………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #99
        "\x07\x0C\x18#60W#3S……对不起……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_77(0xB4, 0xB4, 0xB4, 0x0, 0x3E8)
    Sleep(1000)
    SetChrPos(0x11, -87120, 2500, 1760, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x11, 0x20)
    ClearChrFlags(0x11, 0x8)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x11, 255)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)

    def lambda_4685():

        label("loc_4685")

        OP_99(0x11, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_4685")

    QueueWorkItem2(0x10, 2, lambda_4685)
    OP_43(0x11, 0x3, 0x0, 0x1F)
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x3, 0x0, 0x11, 0, 0, 0, 0, 2800, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0x80, 0x0, 0x64)
    OP_97(0x11, 0xFFFEA994, 0xFFFFFB8C, 0x57E40, 0xDAC, 0x1)
    OP_97(0x11, 0xFFFEA994, 0xFFFFFB8C, 0x2BF20, 0xDAC, 0x1)
    WaitChrThread(0x11, 0x3)
    OP_8C(0x11, 45, 400)
    Sleep(500)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    OP_22(0x264, 0x0, 0x64)
    OP_22(0xD7, 0x0, 0x64)
    OP_23(0x146)
    Fade(500)
    PlayEffect(0x4, 0x1, 0x11, 0, 0, 0, -500, 5000, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_51(0x11, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x11, 45, 0)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)

    def lambda_4786():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_4786)
    OP_43(0x11, 0x0, 0x0, 0x1D)

    def lambda_479F():

        label("loc_479F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_479F")

    QueueWorkItem2(0x11, 2, lambda_479F)
    OP_82(0x0, 0x2)
    Sleep(1000)
    OP_82(0x1, 0x2)
    Sleep(2000)

    def lambda_47C2():

        label("loc_47C2")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_47C2")

    QueueWorkItem2(0x11, 2, lambda_47C2)

    def lambda_47D5():
        OP_8F(0xFE, 0xFFFEA9F8, 0xFFFFF448, 0xFFFFF614, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_47D5)
    WaitChrThread(0x11, 0x1)

    def lambda_47F5():
        OP_8F(0xFE, 0xFFFEBDE4, 0x76C, 0x19B4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_47F5)
    Sleep(200)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x14E, 0x8)

    def lambda_481F():
        OP_8F(0xFE, 0xFFFEBDE4, 0x9C4, 0x19B4, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_481F)
    WaitChrThread(0x11, 0x1)
    OP_43(0x14E, 0x0, 0x0, 0x19)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x11, 0x1)
    SetMapFlags(0x100000)
    ClearChrFlags(0x14E, 0x8)
    OP_A2(0x2506)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_38C7 end

    def Function_25_4867(): pass

    label("Function_25_4867")

    OP_24(0x85, 0x32)
    Sleep(300)
    OP_24(0x85, 0x28)
    Sleep(300)
    OP_24(0x85, 0x1E)
    Sleep(300)
    OP_24(0x85, 0x14)
    Sleep(300)
    OP_24(0x85, 0xA)
    Sleep(300)
    OP_24(0x85, 0x0)
    OP_23(0x85)
    Return()

    # Function_25_4867 end

    def Function_26_489C(): pass

    label("Function_26_489C")

    OP_24(0x120, 0x3C)
    Sleep(150)
    OP_24(0x120, 0x32)
    Sleep(150)
    OP_24(0x120, 0x28)
    Sleep(150)
    OP_24(0x120, 0x1E)
    Sleep(150)
    OP_24(0x120, 0x14)
    Sleep(150)
    OP_24(0x120, 0xA)
    Sleep(150)
    OP_24(0x120, 0x0)
    OP_23(0x120)
    Return()

    # Function_26_489C end

    def Function_27_48DA(): pass

    label("Function_27_48DA")


    def lambda_48E0():
        OP_8F(0xFE, 0xFFFEA610, 0xFFFFEA84, 0xFFFFF9FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48E0)
    Sleep(700)

    def lambda_4900():
        OP_8C(0xFE, 135, 100)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4900)

    def lambda_490E():
        OP_8F(0xFE, 0xFFFEA610, 0xFFFFEA84, 0xFFFFF9FC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_490E)
    Sleep(600)

    def lambda_492E():
        OP_8C(0xFE, 90, 100)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_492E)

    def lambda_493C():
        OP_8F(0xFE, 0xFFFEA610, 0xFFFFEA84, 0xFFFFF9FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_493C)
    Sleep(500)

    def lambda_495C():
        OP_8F(0xFE, 0xFFFEA610, 0xFFFFEA84, 0xFFFFF9FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_495C)
    WaitChrThread(0xFE, 0x1)

    def lambda_497C():
        OP_8C(0xFE, 45, 100)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_497C)

    def lambda_498A():
        OP_8F(0xFE, 0xFFFEA9F8, 0xFFFFF31C, 0xFFFFF420, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_498A)
    Sleep(200)

    def lambda_49AA():
        OP_8F(0xFE, 0xFFFEA9F8, 0xFFFFF31C, 0xFFFFF420, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49AA)
    Sleep(300)

    def lambda_49CA():
        OP_8F(0xFE, 0xFFFEA9F8, 0xFFFFF31C, 0xFFFFF420, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49CA)
    Sleep(300)

    def lambda_49EA():
        OP_8F(0xFE, 0xFFFEA9F8, 0xFFFFF31C, 0xFFFFF420, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49EA)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_27_48DA end

    def Function_28_4A05(): pass

    label("Function_28_4A05")


    def lambda_4A0B():
        OP_8F(0xFE, 0xFFFEA994, 0xFFFFF830, 0xFFFFFB8C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4A0B)
    Sleep(500)

    def lambda_4A2B():
        OP_8F(0xFE, 0xFFFEA994, 0xFFFFF830, 0xFFFFFB8C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4A2B)
    Sleep(500)

    def lambda_4A4B():
        OP_8F(0xFE, 0xFFFEA994, 0xFFFFF830, 0xFFFFFB8C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4A4B)
    Sleep(400)

    def lambda_4A6B():
        OP_8F(0xFE, 0xFFFEA994, 0xFFFFF830, 0xFFFFFB8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4A6B)
    Sleep(400)

    def lambda_4A8B():
        OP_8F(0xFE, 0xFFFEA994, 0xFFFFF830, 0xFFFFFB8C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_4A8B)
    WaitChrThread(0x14E, 0x1)
    Return()

    # Function_28_4A05 end

    def Function_29_4AA6(): pass

    label("Function_29_4AA6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4ABC")
    OP_22(0x120, 0x0, 0x46)
    Sleep(1400)
    Jump("Function_29_4AA6")

    label("loc_4ABC")

    Return()

    # Function_29_4AA6 end

    def Function_30_4ABD(): pass

    label("Function_30_4ABD")

    OP_22(0x1C3, 0x1, 0x14)
    Sleep(500)
    OP_24(0x1C3, 0x28)
    Sleep(500)
    OP_24(0x1C3, 0x3C)
    Sleep(500)
    OP_24(0x1C3, 0x50)
    Sleep(500)
    OP_24(0x1C3, 0x64)
    Return()

    # Function_30_4ABD end

    def Function_31_4AE7(): pass

    label("Function_31_4AE7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B21")
    OP_51(0x11, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_PUSH_LONG, 0x898), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B19")
    OP_51(0x11, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x898), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B21")

    label("loc_4B19")

    Sleep(10)
    Jump("Function_31_4AE7")

    label("loc_4B21")

    Return()

    # Function_31_4AE7 end

    def Function_32_4B22(): pass

    label("Function_32_4B22")


    ChrTalk(    #100
        0x14E,
        "#1711F发现柴火～！\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #101
        "\x07\x05捡起柴火。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2F1B)
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BD5")

    ChrTalk(    #102
        0x14E,
        "#1710F嗯，这些差不多了吧？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)

    label("loc_4BD5")

    TalkEnd(0xFF)
    Return()

    # Function_32_4B22 end

    def Function_33_4BD9(): pass

    label("Function_33_4BD9")

    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #103
        "\x07\x05捡起柴火。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #104
        0x14E,
        "#1718F嘿咻！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F1C)
    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C86")

    ChrTalk(    #105
        0x14E,
        "#1710F嗯，这些差不多了吧？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)

    label("loc_4C86")

    TalkEnd(0xFF)
    Return()

    # Function_33_4BD9 end

    def Function_34_4C8A(): pass

    label("Function_34_4C8A")


    ChrTalk(    #106
        0x14E,
        "#1718F嗯，找到了！\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #107
        "\x07\x05捡起柴火。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2F1D)
    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D3D")

    ChrTalk(    #108
        0x14E,
        "#1710F嗯，这些差不多了吧？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)

    label("loc_4D3D")

    TalkEnd(0xFF)
    Return()

    # Function_34_4C8A end

    def Function_35_4D41(): pass

    label("Function_35_4D41")


    ChrTalk(    #109
        0x14E,
        "#1714F咦，这里也有……\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #110
        "\x07\x05捡起柴火。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2F1E)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DF8")

    ChrTalk(    #111
        0x14E,
        "#1710F嗯，这些差不多了吧？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)

    label("loc_4DF8")

    TalkEnd(0xFF)
    Return()

    # Function_35_4D41 end

    def Function_36_4DFC(): pass

    label("Function_36_4DFC")


    ChrTalk(    #112
        0x14E,
        "#1711F有了有了！\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #113
        "\x07\x05捡起柴火。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2F1F)
    OP_64(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EAD")

    ChrTalk(    #114
        0x14E,
        "#1710F嗯，这些差不多了吧？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)

    label("loc_4EAD")

    TalkEnd(0xFF)
    Return()

    # Function_36_4DFC end

    SaveToFile()

Try(main)
