from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2210   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        'Flora',                                # 9
        'Dominique',                            # 10
        'Viego',                                # 11
        'Provost Guardsman',                    # 12
        'Dario',                                # 13
        'Solomon',                              # 14
        'Mayor Norman',                         # 15
        'Secretary Dels',                       # 16
        'Belden',                               # 17
        'カップ',                               # 18
        'カップ',                               # 19
        'ポット',                               # 20
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
        'ED6_DT06/CH20020 ._CH',             # 00
        'ED6_DT07/CH02540 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
        'ED6_DT07/CH01280 ._CH',             # 03
        'ED6_DT07/CH01300 ._CH',             # 04
        'ED6_DT07/CH01560 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01200 ._CH',             # 07
        'ED6_DT07/CH01140 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT06/CH20020P._CP',             # 00
        'ED6_DT07/CH02540P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
        'ED6_DT07/CH01280P._CP',             # 03
        'ED6_DT07/CH01300P._CP',             # 04
        'ED6_DT07/CH01560P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01200P._CP',             # 07
        'ED6_DT07/CH01140P._CP',             # 08
    )

    DeclNpc(
        X                   = 34540,
        Z                   = 0,
        Y                   = 27220,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -63810,
        Z                   = 0,
        Y                   = 34870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 33500,
        Z                   = 0,
        Y                   = 24400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 2620,
        Z                   = 0,
        Y                   = 3200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 67820,
        Z                   = -30,
        Y                   = -5200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 0,
        Y                   = 2100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -64500,
        Z                   = 0,
        Y                   = 33170,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -7500,
        Z                   = 0,
        Y                   = 33230,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 36150,
        Z                   = 0,
        Y                   = 34260,
        Direction           = 193,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 35510,
        Z                   = 750,
        Y                   = 27280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638400,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35450,
        Z                   = 750,
        Y                   = 26890,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638400,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35490,
        Z                   = 750,
        Y                   = 26520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703936,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -475,
        TriggerZ            = 0,
        TriggerY            = 3173,
        TriggerRange        = 800,
        ActorX              = -475,
        ActorZ              = 800,
        ActorY              = 3173,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -63800,
        TriggerZ            = 0,
        TriggerY            = 50790,
        TriggerRange        = 900,
        ActorX              = -63800,
        ActorZ              = -300,
        ActorY              = 50790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -62370,
        TriggerZ            = 0,
        TriggerY            = -43110,
        TriggerRange        = 500,
        ActorX              = -62370,
        ActorZ              = 2000,
        ActorY              = -43110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -59500,
        TriggerZ            = 250,
        TriggerY            = -36760,
        TriggerRange        = 800,
        ActorX              = -59500,
        ActorZ              = 1250,
        ActorY              = -36760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_302",          # 00, 0
        "Function_1_402",          # 01, 1
        "Function_2_43E",          # 02, 2
        "Function_3_5BB",          # 03, 3
        "Function_4_698",          # 04, 4
        "Function_5_B2D",          # 05, 5
        "Function_6_1229",         # 06, 6
        "Function_7_1874",         # 07, 7
        "Function_8_1EC1",         # 08, 8
        "Function_9_2257",         # 09, 9
        "Function_10_2553",        # 0A, 10
        "Function_11_2FBF",        # 0B, 11
        "Function_12_364F",        # 0C, 12
        "Function_13_3D97",        # 0D, 13
        "Function_14_4641",        # 0E, 14
        "Function_15_46E5",        # 0F, 15
        "Function_16_46EF",        # 10, 16
        "Function_17_46F9",        # 11, 17
    )


    def Function_0_302(): pass

    label("Function_0_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3B8")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, 33760, 0, 25890, 270)
    SetChrPos(0x8, -4550, 0, -4059, 95)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, 67400, 0, 32619, 270)
    Jump("loc_3B5")

    label("loc_365")

    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4070, 0, 35300, 270)
    SetChrPos(0x9, -1900, 0, 4450, 90)
    SetChrPos(0xF, -61820, 0, 30050, 355)
    SetChrPos(0x8, -2750, 0, 42770, 342)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_3B5")

    Jump("loc_401")

    label("loc_3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_3D3")
    SetChrPos(0x8, 35530, 0, 34250, 180)
    Jump("loc_401")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_3DD")
    Jump("loc_401")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FA")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_401")

    label("loc_3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_401")

    label("loc_401")

    Return()

    # Function_0_302 end

    def Function_1_402(): pass

    label("Function_1_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_42C")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)

    label("loc_42C")

    OP_72(0x10, 0x10)
    OP_72(0x10, 0x8)
    OP_6F(0x10, 360)
    Return()

    # Function_1_402 end

    def Function_2_43E(): pass

    label("Function_2_43E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_463")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5A5")

    label("loc_463")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5A5")

    label("loc_47C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_495")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5A5")

    label("loc_495")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AE")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5A5")

    label("loc_4AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C7")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5A5")

    label("loc_4C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E0")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5A5")

    label("loc_4E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F9")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5A5")

    label("loc_4F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_512")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5A5")

    label("loc_512")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5A5")

    label("loc_52B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_544")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5A5")

    label("loc_544")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5A5")

    label("loc_55D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_576")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5A5")

    label("loc_576")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58F")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5A5")

    label("loc_58F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A5")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5A5")

    label("loc_5BA")

    Return()

    # Function_2_43E end

    def Function_3_5BB(): pass

    label("Function_3_5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_635")

    label("loc_5C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_632")
    OP_8E(0xFE, 0xFFFFEE6C, 0x0, 0xFFFFEAA2, 0x3E8, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_8C(0xFE, 90, 400)
    Sleep(3500)
    OP_8E(0xFE, 0xFFFFEE6C, 0x0, 0xFFFFF204, 0x3E8, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(4500)
    Jump("loc_5C2")

    label("loc_632")

    Jump("loc_697")

    label("loc_635")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_63F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_697")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_694")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68A")
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)

    label("loc_68A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_694")

    Jump("loc_63F")

    label("loc_697")

    Return()

    # Function_3_5BB end

    def Function_4_698(): pass

    label("Function_4_698")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_7FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_74E")

    ChrTalk(    #0
        0xFE,
        (
            "Man, the grub they serve here is too good.\x01",
            "Meal time is like heaven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "If I end up getting posted here permanently,\x01",
            "I'm just gonna get fatter and fatter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FC")

    label("loc_74E")

    OP_A2(0x3)

    ChrTalk(    #2
        0xFE,
        (
            "Hmm, a wonderful smell wafted\x01",
            "over from the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "The cook's meals here are absolutely amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Thanks to that, my belt's starting\x01",
            "to get reeeeal tight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FC")

    Jump("loc_B29")

    label("loc_7FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_8F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_863")

    ChrTalk(    #5
        0xFE,
        "To keep a monster in your own house...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "Some people are crazy, I tell ya.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F6")

    label("loc_863")

    OP_A2(0x3)

    ChrTalk(    #7
        0xFE,
        (
            "There's a secret monster-holding room on\x01",
            "the second floor of the mansion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "...Did you see it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "Some people are crazy, I tell ya.\x02",
    )

    CloseMessageWindow()

    label("loc_8F6")

    Jump("loc_B29")

    label("loc_8F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_995")

    ChrTalk(    #10
        0xFE,
        (
            "To try and go after art like this,\x01",
            "you'd have to be either an idiot\x01",
            "or a genius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "Normal thieves know their place, after all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A3A")

    label("loc_995")

    OP_A2(0x3)

    ChrTalk(    #12
        0xFE,
        (
            "One of the maids told me something\x01",
            "real interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "A bit ago this candelabrum was stolen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "What an incredible thi--er, I mean, TERRIBLE\x01",
            "criminal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3A")

    Jump("loc_B29")

    label("loc_A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_B29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A99")

    ChrTalk(    #15
        0xFE,
        "S-So, don't loiter around here too much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "I'm pretty nervous too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B29")

    label("loc_A99")

    OP_A2(0x3)

    ChrTalk(    #17
        0xFE,
        (
            "This candelabrum is currently under\x01",
            "the watchful eye of the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Please don't get too close.\x01",
            "It is a very expensive object.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B29")

    TalkEnd(0xFE)
    Return()

    # Function_4_698 end

    def Function_5_B2D(): pass

    label("Function_5_B2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_CC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C04")

    ChrTalk(    #19
        0xFE,
        (
            "This is an oven that uses firewood.\x01",
            "Lately all the cooking's been done\x01",
            "with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I made it 'cause I wanted some real flames to cook\x01",
            "with, but I didn't expect it to be this useful.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_CC3")

    label("loc_C04")


    ChrTalk(    #21
        0xFE,
        (
            "This is an oven that uses firewood.\x01",
            "Lately all the cooking's been done\x01",
            "with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Well, not much I can do about the fact that\x01",
            "my repertoire gets a bit smaller 'cause of it,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC3")

    Jump("loc_1225")

    label("loc_CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_DF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D85")

    ChrTalk(    #23
        0xFE,
        "Dario, the butler, came back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Having a friend who also served the Dalmore\x01",
            "family for many years is reassuring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "I owe the new mayor already for hirin' him.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_DF1")

    label("loc_D85")


    ChrTalk(    #26
        0xFE,
        "That Dario guy came back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "It's reassuring having someone else\x01",
            "who served the Dalmore family back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF1")

    Jump("loc_1225")

    label("loc_DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_F29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E8A")

    ChrTalk(    #28
        0xFE,
        "All right, I should start getting ready for lunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I've got a great meal planned tonight\x01",
            "for the soldiers. One of my best!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F26")

    label("loc_E8A")

    OP_A2(0x2)

    ChrTalk(    #30
        0xFE,
        (
            "Today's menu is chicken teriyaki with\x01",
            "a twist of orange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "It's a special dish of mine, using Eastern\x01",
            "cooking techniques with my own take on it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F26")

    Jump("loc_1225")

    label("loc_F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_F97")

    ChrTalk(    #32
        0xFE,
        "I've been really worried about Dario...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "He was acting odd after the mayor\x01",
            "got arrested...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1225")

    label("loc_F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_109D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_100C")

    ChrTalk(    #34
        0xFE,
        "The soldiers eat plenty and never complain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "Well, it means it's work cooking for 'em.\x02",
    )

    CloseMessageWindow()
    Jump("loc_109A")

    label("loc_100C")

    OP_A2(0x2)

    ChrTalk(    #36
        0xFE,
        (
            "Right now I'm making the food for\x01",
            "the servants and the soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Me and this mansion go way back.\x01",
            "I'll serve here until the end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109A")

    Jump("loc_1225")

    label("loc_109D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1225")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1158")

    ChrTalk(    #38
        0xFE,
        (
            "Say what you like about 'em, I've served\x01",
            "the Dalmore family for years, and I'll\x01",
            "serve here for many more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "It's a terrible shame that\x01",
            "their family line's ended.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1225")

    label("loc_1158")

    OP_A2(0x2)

    ChrTalk(    #40
        0xFE,
        (
            "Mayor Dalmore may have done terrible\x01",
            "things, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Me and the butler Dario have served\x01",
            "the Dalmore family most of our lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "It's a bit painful to know the\x01",
            "family line's come to an end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1225")

    TalkEnd(0xFE)
    Return()

    # Function_5_B2D end

    def Function_6_1229(): pass

    label("Function_6_1229")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_12B4")

    ChrTalk(    #43
        0xFE,
        (
            "Without the light of orbments\x01",
            "this candlestick is pitiable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Just like us, who wore the\x01",
            "orbal culture like a suit...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1870")

    label("loc_12B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_140A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1395")

    ChrTalk(    #45
        0xFE,
        "Dario seems to have entirely recovered.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "For a while there, the way he talked\x01",
            "had become quite creepy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "One way or another, it's nice having someone\x01",
            "who's familiar with the mansion around.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1407")

    label("loc_1395")


    ChrTalk(    #48
        0xFE,
        "Dario seems to have entirely recovered.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "For a while there, the way he talked\x01",
            "had become quite creepy...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1407")

    Jump("loc_1870")

    label("loc_140A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1502")

    ChrTalk(    #50
        0xFE,
        (
            "I'll be tailoring my future job plans based\x01",
            "on the outcome of the election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "If Norman wins, I'll go into the tourism industry,\x01",
            "and if Portos wins, I'll look for work at the\x01",
            "harbor bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "Heehee, a perfect re-employment plan.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1870")

    label("loc_1502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1561")

    ChrTalk(    #53
        0xFE,
        (
            "Sounds like there was a commotion out\x01",
            "there earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "Did something happen?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1870")

    label("loc_1561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_171E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1606")

    ChrTalk(    #55
        0xFE,
        (
            "After the incident with the previous mayor,\x01",
            "the butler Dario became kinda weird.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Seems like Dalmore's arrest\x01",
            "was a real shock to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171B")

    label("loc_1606")

    OP_A2(0x1)

    ChrTalk(    #57
        0xFE,
        (
            "Lately, I haven't seen Dario around.\x01",
            "He used to be the butler here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "But to be honest, he got kinda weird\x01",
            "after the mayor was arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "'There's another me!' he kept saying.\x01",
            "It was totally crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Mayor Dalmore's arrest must have\x01",
            "been a real shock to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171B")

    Jump("loc_1870")

    label("loc_171E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1870")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_17C6")

    ChrTalk(    #61
        0xFE,
        (
            "Everything's just carrying on as normal while\x01",
            "the army's managing the place, but what do\x01",
            "I do later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "I should look for a job now, not later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1870")

    label("loc_17C6")

    OP_A2(0x1)

    ChrTalk(    #63
        0xFE,
        (
            "Everything's just carrying on as normal while\x01",
            "the army's managing the place, but what do\x01",
            "I do later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "I wonder if the servants are\x01",
            "all going to end up fired.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1870")

    TalkEnd(0xFE)
    Return()

    # Function_6_1229 end

    def Function_7_1874(): pass

    label("Function_7_1874")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_18E5")

    ChrTalk(    #65
        0xFE,
        (
            "I can't use the vacuum, so\x01",
            "cleaning's gotten very hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "Phew! This mansion is really big.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EBD")

    label("loc_18E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19DE")

    ChrTalk(    #67
        0xFE,
        "Ah, welcome. Welcome to the mayoral mansion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "All of the servants here got hired\x01",
            "by the new mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "It's hard to do housework when\x01",
            "you can't use orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "If we all work together, I think\x01",
            "we can overcome this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1A5F")

    label("loc_19DE")


    ChrTalk(    #71
        0xFE,
        (
            "We all, aaaaaaall of us got hired\x01",
            "together by the new mayor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Dario's returned, too, so everything's\x01",
            "back to normal. ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A5F")

    Jump("loc_1EBD")

    label("loc_1A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1B46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AC6")

    ChrTalk(    #73
        0xFE,
        "I want to work at this mansion, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "I guess it's not going to happen.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B43")

    label("loc_1AC6")

    OP_A2(0x0)

    ChrTalk(    #75
        0xFE,
        (
            "Oh, Dominique, now you're off\x01",
            "searching for a new job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "With even you doing that,\x01",
            "I'm starting to worry a bit...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B43")

    Jump("loc_1EBD")

    label("loc_1B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1C98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BAA")

    ChrTalk(    #77
        0xFE,
        (
            "I haven't seen the butler, Dario,\x01",
            "around lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "I wonder what happened.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C95")

    label("loc_1BAA")

    OP_A2(0x0)

    ChrTalk(    #79
        0xFE,
        (
            "I was talking to Dominique about this\x01",
            "while we were cleaning, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "I haven't seen the butler, Dario,\x01",
            "around lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "After the thing with mayor Dalmore,\x01",
            "he seemed off somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "I wonder what happened to Dario.\x02",
    )

    CloseMessageWindow()

    label("loc_1C95")

    Jump("loc_1EBD")

    label("loc_1C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D04")

    ChrTalk(    #83
        0xFE,
        "La, lala～la... ♪ Loo lolo loo～... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "The soldiers are quite handsome too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D62")

    label("loc_1D04")

    OP_A2(0x0)

    ChrTalk(    #85
        0xFE,
        "La, lala～la... ♪ Loo lolo loo～... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "I'm making tea to serve to the soldiers.\x02",
    )

    CloseMessageWindow()

    label("loc_1D62")

    Jump("loc_1EBD")

    label("loc_1D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1EBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E09")

    ChrTalk(    #87
        0xFE,
        (
            "I wasn't sure how things would turn out\x01",
            "when the lord was arrested, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Seems like we'll be able to carry on\x01",
            "like normal for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EBD")

    label("loc_1E09")

    OP_A2(0x0)

    ChrTalk(    #89
        0xFE,
        (
            "For now, the Royal Army is running\x01",
            "the mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "In the interim, we servants are being\x01",
            "employed the same as before..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "Heehee, I'm glad the army people are\x01",
            "so nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EBD")

    TalkEnd(0xFE)
    Return()

    # Function_7_1874 end

    def Function_8_1EC1(): pass

    label("Function_8_1EC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_209E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2027")

    ChrTalk(    #92
        0xFE,
        (
            "To think such emergency situations\x01",
            "would occur over and over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "Really, what is happening to the world?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Thinking about it, there was much hard\x01",
            "to understand about the previous mayor's\x01",
            "case, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "...No, I shall say no more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "The truth is that the previous mayor had faults.\x01",
            "Crimes must be recognized as such.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_209B")

    label("loc_2027")


    ChrTalk(    #97
        0xFE,
        (
            "To think such emergency situations\x01",
            "would occur over and over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "What is happening to the world, I wonder.\x02",
    )

    CloseMessageWindow()

    label("loc_209B")

    Jump("loc_2253")

    label("loc_209E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2253")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21BE")

    ChrTalk(    #99
        0xFE,
        "I have long served that Dalmore family...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "I have returned to manage the mayoral\x01",
            "house after the new mayor was good\x01",
            "enough to speak to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I shall serve loyally and faithfully\x01",
            "as if born anew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Should you have any business here,\x01",
            "please speak to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2253")

    label("loc_21BE")


    ChrTalk(    #103
        0xFE,
        (
            "I have returned to serve as a manager\x01",
            "for the mayoral mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Together with old comrades I am reflecting\x01",
            "on the happiness of having work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2253")

    TalkEnd(0xFE)
    Return()

    # Function_8_1EC1 end

    def Function_9_2257(): pass

    label("Function_9_2257")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_23BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2342")

    ChrTalk(    #105
        0xFE,
        (
            "I met with the mayor and requested\x01",
            "urgent aid for Manoria, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Seems like even the City of Ruan\x01",
            "is in a bad situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "Mayor Norman's severe expression speaks\x01",
            "volumes about how bad things are.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_23BA")

    label("loc_2342")


    ChrTalk(    #108
        0xFE,
        (
            "I asked for aid for the village, but it\x01",
            "seems Ruan is also in a tough spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "Mayor Norman looked really tired.\x02",
    )

    CloseMessageWindow()

    label("loc_23BA")

    Jump("loc_254F")

    label("loc_23BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_254F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A8")

    ChrTalk(    #110
        0xFE,
        (
            "I've come to petition the City of Ruan as\x01",
            "a representative of Manoria Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "We'll need to ask for support in terms\x01",
            "of food and fuel very soon, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "Now then, time to go greet\x01",
            "the new mayor.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_254F")

    label("loc_24A8")


    ChrTalk(    #113
        0xFE,
        (
            "I've come to petition the City of Ruan as\x01",
            "a representative of Manoria Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "We'll need to ask for support in terms\x01",
            "of food and fuel very soon, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_254F")

    TalkEnd(0xFE)
    Return()

    # Function_9_2257 end

    def Function_10_2553(): pass

    label("Function_10_2553")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2ADC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25DB")
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #115
        0xFE,
        "Ohh, you all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "I just received a report about\x01",
            "the academy moments ago.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2646")

    label("loc_25DB")


    ChrTalk(    #117
        0xFE,
        "Ohh... So you're the bracers I heard of?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "I just received a report about\x01",
            "the academy moments ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2646")


    ChrTalk(    #119
        0x101,
        "#1011FHuh, you sure do hear fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x102,
        "#1040FDid Jean update you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "Yes, a messenger from the guild came...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Oh, that reminds me, I haven't\x01",
            "properly introduced myself yet.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_27E9")

    ChrTalk(    #123
        0xFE,
        (
            "After all, I'm in a bit of a different\x01",
            "position than when we last met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        "#1000FOh, yeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I'm Norman, recently elected\x01",
            "to the post of mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "I hope to continue our cooperation in the future.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2853")

    label("loc_27E9")


    ChrTalk(    #127
        0xFE,
        (
            "I'm called Norman, recently elected\x01",
            "to the post of mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "A pleasure to make your acquaintance.\x02",
    )

    CloseMessageWindow()

    label("loc_2853")


    ChrTalk(    #129
        0x101,
        "#1000FNo, the pleasure is ours.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x102,
        "#1040FCongratulation on your election.\x02",
    )

    CloseMessageWindow()
    Call(0, 11)
    Jump("loc_2AD9")

    label("loc_28AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2927")

    ChrTalk(    #131
        0xFE,
        "We're dedicated to weathering this crisis.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "We hope this situation will be\x01",
            "resolved as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD9")

    label("loc_2927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A15")

    ChrTalk(    #133
        0xFE,
        "I just received a report about the academy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "I'm sorry to hear about the janitor,\x01",
            "but it seems things were resolved\x01",
            "safely in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "As a representative of the citizenry,\x01",
            "allow me to offer my thanks as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_2AD9")

    label("loc_2A15")


    ChrTalk(    #136
        0xFE,
        "I just received a report about the academy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Such a criminal occupation of a school is\x01",
            "an unbelievable act of violence in a time\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "The culprits should be punished severely.\x02",
    )

    CloseMessageWindow()

    label("loc_2AD9")

    Jump("loc_2FBB")

    label("loc_2ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2FBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E9E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D66")
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #139
        0xFE,
        "Ohh, you are..\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "I believe I owe you for your help with\x01",
            "the hotel case during the election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1016FAhh, that case.\x02\x03",

            "That was a memorable one, huh? Not often\x01",
            "a mere door commits such a heinous act.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #142
        0x102,
        "#1048FHuh? Just what kind of case were you on...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #143
        0xFE,
        "Oh... How embarrassing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "Anyway, allow me to introduce myself again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "After all, I'm in a bit of a different\x01",
            "position than when we last met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        "#1011FOh, yeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I'm Norman, recently elected\x01",
            "to the post of mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "I hope to continue our cooperation in the future.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E46")

    label("loc_2D66")


    ChrTalk(    #149
        0xFE,
        "Hmm... So you're bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "I know this isn't our first meeting,\x01",
            "but allow me to introduce myself\x01",
            "regardless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "I'm Norman, recently elected to the post\x01",
            "of mayor. I hope to continue our cooperation\x01",
            "in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E46")


    ChrTalk(    #152
        0x101,
        "#1000FNo, the pleasure is ours.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x102,
        "#1040FCongratulation on your election.\x02",
    )

    CloseMessageWindow()
    Call(0, 11)
    Jump("loc_2FBB")

    label("loc_2E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2F21")

    ChrTalk(    #154
        0xFE,
        "We're dedicated to weathering this crisis.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "I'm counting on you to help resolve this\x01",
            "issue as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FBB")

    label("loc_2F21")


    ChrTalk(    #156
        0xFE,
        (
            "Anyway, the present issue is stabilizing\x01",
            "the lives of the citizenry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "Right now I'm consulting with people\x01",
            "that might be able to help with that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FBB")

    TalkEnd(0xFE)
    Return()

    # Function_10_2553 end

    def Function_11_2FBF(): pass

    label("Function_11_2FBF")

    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #158
        0xFE,
        "Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "Still, I can't afford to sit back and enjoy\x01",
            "my victory in this situation.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3089")

    ChrTalk(    #160
        0x106,
        (
            "#552FYeah, seriously.\x02\x03",

            "Talk about a disaster right after you\x01",
            "get into office.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3158")

    label("loc_3089")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30EE")

    ChrTalk(    #161
        0x103,
        (
            "#025FYes, I imagine.\x02\x03",

            "Having to deal with this mess right\x01",
            "after your election.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3158")

    label("loc_30EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3158")

    ChrTalk(    #162
        0x108,
        (
            "#074FIndeed.\x02\x03",

            "This is quite a situation to fall in\x01",
            "your lap right after being elected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3158")


    ChrTalk(    #163
        0xFE,
        (
            "To be totally frank with you,\x01",
            "there's not a whole lot I can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "While the original chaos has settled,\x01",
            "the orbments still haven't been\x01",
            "restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "In this situation, there's little I can do aside\x01",
            "from providing on-the-spot aid to the citizenry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x102,
        (
            "#1043FHowever, I believe that's the best\x01",
            "response at the moment.\x02\x03",

            "Unfortunately, resolving the broader\x01",
            "situation may still take time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3398")

    ChrTalk(    #167
        0x108,
        (
            "#072FCertainly, this isn't the kind of\x01",
            "thing that's solved in a day.\x02\x03",

            "Careful planning will be needed in preparation\x01",
            "for this being a long-term issue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x108, 400)
    Jump("loc_34D5")

    label("loc_3398")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3444")

    ChrTalk(    #168
        0x103,
        (
            "#022FWell, this isn't a case that\x01",
            "can be solved in a day.\x02\x03",

            "A long-lasting plan is needed to prepare\x01",
            "in case this turns into a long-term issue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_34D5")

    label("loc_3444")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34D5")

    ChrTalk(    #169
        0x106,
        (
            "#050FThis is definitely a case that\x01",
            "can't be solved in a day.\x02\x03",

            "We have to think of a good plan\x01",
            "if it's gonna drag out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    label("loc_34D5")


    ChrTalk(    #170
        0xFE,
        "You think so, too, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "It is a bit nerve-racking to have this as\x01",
            "my first job as the new mayor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "I shall take it as a sign of the Goddess'\x01",
            "faith in me and hold on somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "I'm counting on you to help resolve this\x01",
            "issue as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "#1006FGot it. You do your best too, Mayor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x102,
        "#1040FWe shall serve to the best of our abilities.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    OP_A2(0x20BC)
    Return()

    # Function_11_2FBF end

    def Function_12_364F(): pass

    label("Function_12_364F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3D93")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3916")

    ChrTalk(    #176
        0xFE,
        "Ah, bracers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "U-Umm... Thanks very much for the other day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1000FAhhh, you're the victim from the hotel case.\x02\x03",

            "How's the head?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "Much better, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "So, what's your business today\x01",
            "at the manor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#1000FWe don't really have any,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x102,
        (
            "#1040FPlease, don't mind us. We just\x01",
            "came to observe the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "Patrolling inside the town, then?\x01",
            "Ever hard at work, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "Well, should anything happen,\x01",
            "I'll be here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "I've been appointed the mayor's secretary,\x01",
            "so if there's anything I can do, let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1000FOh, yeah? Congrats.\x02\x03",

            "Well, then, we'll be sure to contact you\x01",
            "if anything comes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "Yes, please don't hesitate.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x20BD)
    Jump("loc_3D93")

    label("loc_3916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3998")

    ChrTalk(    #188
        0xFE,
        "I'll do what I can as a servant of the city.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "Should you have some business,\x01",
            "don't hesitate to bring it to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D93")

    label("loc_3998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3B4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC3")

    ChrTalk(    #190
        0xFE,
        (
            "We just received a report about\x01",
            "the academy moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "Both the mayor and I are relieved\x01",
            "to hear it was resolved safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "For now our priority is to prepare\x01",
            "to dispense public information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "Anyway, we need to distribute information\x01",
            "to assuage the citizenry.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3B48")

    label("loc_3AC3")


    ChrTalk(    #194
        0xFE,
        (
            "We just received a report about\x01",
            "the academy moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "Both the mayor and I are relieved\x01",
            "to hear it was resolved safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B48")

    Jump("loc_3D93")

    label("loc_3B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CCE")

    ChrTalk(    #196
        0xFE,
        (
            "Phew! Finally finished handling the\x01",
            "current issues from the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "For a bit there, when they were shoving their\x01",
            "way in, I wasn't sure what I was going to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "Still, resolution of the orbment problem\x01",
            "isn't something we have a date on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "Anyway, we've got our hands full just\x01",
            "trying to keep things running so that\x01",
            "the citizens can go about their lives.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3D93")

    label("loc_3CCE")


    ChrTalk(    #200
        0xFE,
        (
            "We don't even have a date on when the\x01",
            "orbment problem will be resolved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "Anyway, we've got our hands full just\x01",
            "trying to keep things running so that\x01",
            "the citizens can go about their lives.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D93")

    TalkEnd(0xFE)
    Return()

    # Function_12_364F end

    def Function_13_3D97(): pass

    label("Function_13_3D97")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_463D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42C5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ECF")
    TurnDirection(0xFE, 0x106, 0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #202
        0xFE,
        "Oh, Agate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x106,
        (
            "#051FHey, it's been a while.\x02\x03",

            "Looks like you're doin' well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "Haha, yeah, thanks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "My dad ended up becomin' mayor,\x01",
            "so I'm helpin' out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "Given the sit, even just doing whatever\x01",
            "needs to be done is a lot of work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_401C")

    label("loc_3ECF")


    ChrTalk(    #207
        0xFE,
        "Oh, you guys...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F36")

    ChrTalk(    #208
        0x101,
        "#1000FAh, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x103,
        "#021FHaha, you look well.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F71")

    label("loc_3F36")


    ChrTalk(    #210
        0x101,
        (
            "#1000FAh, it's been a while.\x02\x03",

            "How are you? Been well?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F71")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #211
        0xFE,
        "Haha, yeah, thanks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "My dad ended up becomin' mayor,\x01",
            "so I'm helping out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "Given the sit, even just doing whatever\x01",
            "needs to be done is a lot of work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_401C")


    ChrTalk(    #214
        0x101,
        "#1011FWhoa, so you're seriously working, huh.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #215
        0xFE,
        "Well, it's still basically just a part-time job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "But no point in worryin' about it.\x01",
            "I'll just keep workin' like I am.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4174")

    ChrTalk(    #217
        0x106,
        (
            "#051FIf you're ready to do that,\x01",
            "you'll do fine.\x02\x03",

            "...Keep it up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #218
        0xFE,
        "Y-Yeah. Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "Best to you, too, Agate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_42BC")

    label("loc_4174")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_421C")

    ChrTalk(    #220
        0x103,
        (
            "#020FMmm, if you're that ready,\x01",
            "you'll be fine.\x02\x03",

            "Well, then, keep it up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #221
        0xFE,
        "Y-Yeah, I'll do my best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "Well, you guys be careful too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_42BC")

    label("loc_421C")


    ChrTalk(    #223
        0x101,
        (
            "#1006FIf you're that decided,\x01",
            "you'll be just fine.\x02\x03",

            "Well, then, good luck with the work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        "Y-Yeah, I'll do my best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        "Well, you guys be careful too.\x02",
    )

    CloseMessageWindow()

    label("loc_42BC")

    OP_A2(0xB)
    OP_A2(0x20BE)
    Jump("loc_463D")

    label("loc_42C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_43AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4352")

    ChrTalk(    #226
        0xFE,
        (
            "Anyway, I'm gonna do my best,\x01",
            "slow but sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "It's a rough time, I know, but you\x01",
            "guys take care too, Agate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43A8")

    label("loc_4352")


    ChrTalk(    #228
        0xFE,
        (
            "Anyway, I'm gonna do my best,\x01",
            "slow but sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        "Well, you guys be careful too.\x02",
    )

    CloseMessageWindow()

    label("loc_43A8")

    Jump("loc_463D")

    label("loc_43AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_4513")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_447D")

    ChrTalk(    #230
        0xFE,
        (
            "I heard about the incident at the\x01",
            "academy from the apprentice bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "A hostage case at a time like this?\x01",
            "Aidios, give us a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        "I wonder what those maniacs were thinkin'.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_4510")

    label("loc_447D")


    ChrTalk(    #233
        0xFE,
        (
            "A hostage case at a time like this?\x01",
            "Aidios, give us a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "It's totally unforgivable at a time when\x01",
            "we should all be workin' together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4510")

    Jump("loc_463D")

    label("loc_4513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45DA")

    ChrTalk(    #235
        0xFE,
        (
            "My dad seems like he's got it\x01",
            "pretty rough too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "Dealing with everyone yammerin' at him,\x01",
            "securing foodstuffs and medicine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        "Seriously, talk about a mountain of problems.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_463D")

    label("loc_45DA")


    ChrTalk(    #238
        0xFE,
        (
            "My dad seems like he's got it\x01",
            "pretty rough too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        "I wonder why he even wanted to be mayor.\x02",
    )

    CloseMessageWindow()

    label("loc_463D")

    TalkEnd(0xFE)
    Return()

    # Function_13_3D97 end

    def Function_14_4641(): pass

    label("Function_14_4641")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #240
        (
            "\x07\x05[Sapphire Glim] Priceless orbal art given to the Dalmore\x01",
            "family in honor of their dedication to the City of Ruan.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_4641 end

    def Function_15_46E5(): pass

    label("Function_15_46E5")

    NewScene("ED6_DT21/T2210   ._SN", 123, 1, 0)
    IdleLoop()
    Return()

    # Function_15_46E5 end

    def Function_16_46EF(): pass

    label("Function_16_46EF")

    NewScene("ED6_DT21/T2210   ._SN", 121, 1, 0)
    IdleLoop()
    Return()

    # Function_16_46EF end

    def Function_17_46F9(): pass

    label("Function_17_46F9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #241
        "\x07\x05There is a control device for the drawbridge here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_46F9 end

    SaveToFile()

Try(main)
