from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4121   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Elnan',                                # 9
        'Zin',                                  # 10
        'Aina',                                 # 11
        'Kurt',                                 # 12
        'Cassius',                              # 13
        'Fisher',                               # 14
        'Lloyd',                                # 15
        'Mover',                                # 16
        'Percy',                                # 17
        'Target Camera',                        # 18
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
        'ED6_DT07/CH02580 ._CH',             # 00
        'ED6_DT07/CH00070 ._CH',             # 01
        'ED6_DT07/CH02710 ._CH',             # 02
        'ED6_DT07/CH01620 ._CH',             # 03
        'ED6_DT07/CH01200 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH01450 ._CH',             # 06
        'ED6_DT07/CH01460 ._CH',             # 07
        'ED6_DT07/CH00071 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02580P._CP',             # 00
        'ED6_DT07/CH00070P._CP',             # 01
        'ED6_DT07/CH02710P._CP',             # 02
        'ED6_DT07/CH01620P._CP',             # 03
        'ED6_DT07/CH01200P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH01450P._CP',             # 06
        'ED6_DT07/CH01460P._CP',             # 07
        'ED6_DT07/CH00071P._CP',             # 08
    )

    DeclNpc(
        X                   = -4460,
        Z                   = 0,
        Y                   = 960,
        Direction           = 90,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        X                   = 26440,
        Z                   = 0,
        Y                   = 59870,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 32080,
        Z                   = 0,
        Y                   = 63600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 32080,
        Z                   = 0,
        Y                   = 61480,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 33280,
        Z                   = 0,
        Y                   = 63470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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


    DeclActor(
        TriggerX            = -3480,
        TriggerZ            = 0,
        TriggerY            = -450,
        TriggerRange        = 800,
        ActorX              = -4480,
        ActorZ              = 1500,
        ActorY              = -550,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28140,
        TriggerZ            = 0,
        TriggerY            = 61240,
        TriggerRange        = 800,
        ActorX              = 27820,
        ActorZ              = 1500,
        ActorY              = 62520,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4970,
        TriggerZ            = 0,
        TriggerY            = -1040,
        TriggerRange        = 1400,
        ActorX              = 4970,
        ActorZ              = 2000,
        ActorY              = -1040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3370,
        TriggerZ            = 0,
        TriggerY            = 40,
        TriggerRange        = 1400,
        ActorX              = -3370,
        ActorZ              = 1600,
        ActorY              = 40,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2C2",          # 00, 0
        "Function_1_3C8",          # 01, 1
        "Function_2_466",          # 02, 2
        "Function_3_5E3",          # 03, 3
        "Function_4_5E8",          # 04, 4
        "Function_5_5E9",          # 05, 5
        "Function_6_65E",          # 06, 6
        "Function_7_A27",          # 07, 7
        "Function_8_2198",         # 08, 8
        "Function_9_2220",         # 09, 9
        "Function_10_2281",        # 0A, 10
        "Function_11_259F",        # 0B, 11
        "Function_12_28C9",        # 0C, 12
        "Function_13_2AF3",        # 0D, 13
        "Function_14_2C07",        # 0E, 14
        "Function_15_31FB",        # 0F, 15
        "Function_16_3D06",        # 10, 16
        "Function_17_3D89",        # 11, 17
        "Function_18_5B15",        # 12, 18
        "Function_19_5BB9",        # 13, 19
    )


    def Function_0_2C2(): pass

    label("Function_0_2C2")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380")
    OP_10(0x6, 0x0)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_2F3")
    Jump("loc_380")

    label("loc_2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_355")
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 5)), scpexpr(EXPR_END)), "loc_31A")
    SetChrPos(0x13, -5880, 0, -3660, 270)
    Jump("loc_32B")

    label("loc_31A")

    SetChrPos(0x13, -5600, 0, 100, 270)

    label("loc_32B")

    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x17, 34270, 0, 56020, 90)
    SetChrPos(0x16, 32080, 0, 63600, 90)
    Jump("loc_380")

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_35F")
    Jump("loc_380")

    label("loc_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_380")
    OP_65(0x0, 0x1)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -4480, 0, -550, 90)

    label("loc_380")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3A8")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)

    label("loc_3A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_3C7")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_3C7")

    Return()

    # Function_0_2C2 end

    def Function_1_3C8(): pass

    label("Function_1_3C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E0")
    OP_B1("t4121_n")
    Jump("loc_3E9")

    label("loc_3E0")

    OP_B1("t4121_y")

    label("loc_3E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_401")
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()

    label("loc_401")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465")
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_465")

    Return()

    # Function_1_3C8 end

    def Function_2_466(): pass

    label("Function_2_466")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5CD")

    label("loc_48B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A4")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5CD")

    label("loc_4A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BD")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5CD")

    label("loc_4BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D6")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5CD")

    label("loc_4D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EF")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5CD")

    label("loc_4EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_508")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5CD")

    label("loc_508")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_521")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5CD")

    label("loc_521")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53A")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5CD")

    label("loc_53A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_553")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5CD")

    label("loc_553")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56C")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5CD")

    label("loc_56C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_585")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5CD")

    label("loc_585")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59E")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5CD")

    label("loc_59E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B7")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5CD")

    label("loc_5B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CD")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5CD")

    label("loc_5E2")

    Return()

    # Function_2_466 end

    def Function_3_5E3(): pass

    label("Function_3_5E3")

    Call(0, 7)
    Return()

    # Function_3_5E3 end

    def Function_4_5E8(): pass

    label("Function_4_5E8")

    Return()

    # Function_4_5E8 end

    def Function_5_5E9(): pass

    label("Function_5_5E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65D")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05There are no requests on the board.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #1
        0x103,
        "#1642FBah...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_65D")

    Return()

    # Function_5_5E9 end

    def Function_6_65E(): pass

    label("Function_6_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6B8")

    ChrTalk(    #2
        0x103,
        (
            "#1646FOne day, I'll be able to handle this much, too...\x02\x03",

            "Just you watch...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A23")

    label("loc_6B8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x05◆ Requests ◆\x01",
            "6:02 Changing Road Lamps (in front of Grancel)  K\x01",
            "6:14 Royal Avenue Monster Extermination         K\x01",
            "6:17 Parcel Delivery (Gurune Gate)              K\x01",
            "7:44 Elize Highway Safety Check                 K\x01",
            "9:32 Help With Moving (Neighbors?)              S\x01",
            "9:33 Medicinal Herb Procurement                 K\x01",
            "9:55 Traveler Escort (Sanktheim to Capital)     K\x01",
            "10:02 Lost Property Search (Calvardian Embassy)   K\x01",
            "10:28 Parcel Delivery (Grancel + Erbe Villa)    S\x01",
            "10:32 Fix Roof (West Block House)               K\x01",
            "10:58 Oversee Dangerous Goods Transport (Port)  K\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #4
        0x103,
        (
            "#1646F(Wow...)\x02\x03",

            "(It never stops amazing me just how much\x01",
            "work Kurt can burn through.)\x02\x03",

            "#1642F(What's something like changing road lamps\x01",
            "even doing on here?)\x02\x03",

            "#1645FHe sure knows how to take on the dull\x01",
            "stuff... *sigh*\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 0)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)
    OP_A2(0x5)

    label("loc_A23")

    TalkEnd(0xFF)
    Return()

    # Function_6_65E end

    def Function_7_A27(): pass

    label("Function_7_A27")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_A34")
    Jump("loc_2194")

    label("loc_A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_157A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 5)), scpexpr(EXPR_END)), "loc_C30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 6)), scpexpr(EXPR_END)), "loc_B2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_ABF")
    OP_8C(0x13, 270, 0)

    ChrTalk(    #5
        0x13,
        (
            "#840FThese books are out of their proper order.\x02\x03",

            "I'm going to have to sort that out right away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2C")

    label("loc_ABF")

    OP_8C(0x13, 270, 0)

    ChrTalk(    #6
        0x13,
        (
            "#842F...Oh?\x02\x03",

            "93.6... 95.2... 93.4...\x02\x03",

            "#843FThese books are out of order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        "#1643F(Oops...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B2C")

    Jump("loc_C2D")

    label("loc_B2F")

    OP_8C(0x13, 270, 0)

    ChrTalk(    #8
        0x13,
        "#841FThere. All done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        "#1643FWhat were you doing?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x103, 500)
    Sleep(300)

    ChrTalk(    #10
        0x13,
        (
            "#840FOh, just some light cleaning.\x02\x03",

            "There are always so many people shuffling\x01",
            "in and out of here that dust starts to build\x01",
            "up very easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x103,
        "#1645F(Unbelievable...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F56)

    label("loc_C2D")

    Jump("loc_1577")

    label("loc_C30")

    OP_8C(0x13, 270, 0)
    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x103, -5560, 0, -1440, 0)
    SetChrPos(0x151, -4440, 0, -1480, 315)
    OP_6D(-5600, 0, 100, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x13, 0)
    Sleep(500)

    ChrTalk(    #12
        0x13,
        (
            "#841F#2P...Haha. Yes, you're right.\x02\x03",

            "Yes. I'm in contact with Lugran, too...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x13, 0x103, 500)
    Sleep(300)

    ChrTalk(    #13
        0x13,
        "#840F#2PAh, Scherazard. You came at the perfect time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x103,
        "\x07\x00#1643FI did?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #15
        0x13,
        (
            "#840F#2PIt's Scherazard.\x02\x03",

            "...Yes, I'll put her on.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x103, 500)
    Sleep(300)

    ChrTalk(    #16
        0x13,
        "#840F#2PIt's Cassius.\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_DF8():
        OP_8F(0xFE, 0xFFFFEA20, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_DF8)
    Sleep(300)

    def lambda_E18():
        OP_8E(0xFE, 0xFFFFEA20, 0x0, 0x64, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E18)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 270, 500)
    Sleep(300)

    ChrTalk(    #17
        0x103,
        "#1640F#4PU-Umm... Hello.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -6760, 0, -40, 0)
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Cassius")

    AnonymousTalk(    #18
        "\x07\x05Hello, Schera.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #19
        (
            "\x07\x05How are you doing? I hear you're working hard\x01",
            "over there in Grancel.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #20
        0x103,
        (
            "#1640F#4PI-I'm fine, thank you! \x02\x03",

            "Umm... Are you still in Rolent? I'm actually going\x01",
            "to become a se--\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Cassius")

    AnonymousTalk(    #21
        (
            "\x07\x05Actually, no. I've ended up coming to Calvard,\x01",
            "I'm afraid. I doubt I'll be able to return to\x01",
            "Liberl for some time, either.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #22
        (
            "\x07\x05I've left everything in the hands of the other\x01",
            "veteran bracers for the time being, so things\x01",
            "should be fine even without me, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #23
        0x103,
        (
            "#1640F#4P...\x02\x03",

            "#1645F...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Cassius")

    AnonymousTalk(    #24
        "\x07\x05Schera? Are you still there?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #25
        0x103,
        (
            "#1640F#4PY-Yes... Sorry. I'm still here.\x02\x03",

            "#1641FIf you spend too long away on work, though,\x01",
            "Estelle's going to be really mad at you.\x02\x03",

            "I'd probably try and get that job wrapped up\x01",
            "as soon as possible, unless you WANT to face\x01",
            "her wrath.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Cassius")

    AnonymousTalk(    #26
        "\x07\x05Yeah...and hell hath no fury like an angry Estelle.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #27
        (
            "\x07\x05Oh! There was one more thing I wanted to ask of\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #28
        0x103,
        (
            "#1643F#4PReally...?\x02\x03",

            "#1640FO-Of me?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Cassius")

    AnonymousTalk(    #29
        (
            "\x07\x05Next time you swing by Rolent, you might be in\x01",
            "for a little surprise...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #30
        (
            "\x07\x05...but, well, I'm guessing I'm going to be away for\x01",
            "a while, angry daughter or no, so if you could look\x01",
            "after things at home, it'd help.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #31
        0x103,
        "#1642F#4PHmm? S-Sure...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Cassius")

    AnonymousTalk(    #32
        (
            "\x07\x05...Oops. I think I'm about out of time. Could you\x01",
            "put Kurt on the line again for me?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #33
        0x103,
        "#1643F#4POh... Okay. Bye.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x14, 0x80)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0x103, 0, 400)
    Sleep(200)

    def lambda_1418():
        OP_8F(0xFE, 0xFFFFEA48, 0x0, 0xFFFFFA60, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1418)
    Sleep(300)

    def lambda_1438():
        OP_8E(0xFE, 0xFFFFEA20, 0x0, 0x64, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1438)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #34
        0x13,
        (
            "#840F#2PYes... Yes...\x02\x03",

            "Leave everything to me. I'll have the job wrapped\x01",
            "up within the next few days.\x02\x03",

            "Oh, and as for the documents I sent you...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_1512():

        label("loc_1512")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_1512")

    QueueWorkItem2(0x151, 2, lambda_1512)
    Sleep(1000)
    OP_63(0x103)
    OP_43(0x103, 0x3, 0x0, 0x8)
    Sleep(2000)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x151, 0x2)
    OP_43(0x151, 0x3, 0x0, 0x9)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2F55)
    OP_A2(0x2507)
    NewScene("ED6_DT21/T4100   ._SN", 103, 0, 0)
    IdleLoop()

    label("loc_1577")

    Jump("loc_2194")

    label("loc_157A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1584")
    Jump("loc_2194")

    label("loc_1584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2194")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 1)), scpexpr(EXPR_END)), "loc_187C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 2)), scpexpr(EXPR_END)), "loc_16CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_161A")

    ChrTalk(    #35
        0x13,
        (
            "#840FYou don't need to worry about taking on any other\x01",
            "work for now, Scherazard.\x02\x03",

            "Just focus on the task at hand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CB")

    label("loc_161A")


    ChrTalk(    #36
        0x13,
        (
            "#840FCome and let me know as soon as you've\x01",
            "finished that job, Scherazard.\x02\x03",

            "Until then, you don't need to worry about\x01",
            "taking on any other work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x103,
        "#1645FFine, fine...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_16CB")

    Jump("loc_1879")

    label("loc_16CE")

    OP_8C(0x13, 90, 0)

    ChrTalk(    #38
        0x151,
        (
            "#1653FBut here's what I'M wondering.\x02\x03",

            "Are you not the one putting the details\x01",
            "of these wanted monsters on the board\x01",
            "to begin with?\x02\x03",

            "#1650FIs there really any point in doing that if\x01",
            "you're just going to defeat them yourself?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x13, 0x151, 500)
    Sleep(300)

    ChrTalk(    #39
        0x13,
        (
            "#845FP-Perhaps not...but such are the rules of\x01",
            "this organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        "#1645F...Look at this guy. Such a stickler.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F52)

    label("loc_1879")

    Jump("loc_2194")

    label("loc_187C")

    OP_8C(0x13, 90, 0)

    ChrTalk(    #41
        0x151,
        (
            "#1650FThank you very much again for agreeing to take\x01",
            "my request.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x151, 500)
    Sleep(300)

    ChrTalk(    #42
        0x13,
        (
            "#840FOh, not at all. I should be apologizing that\x01",
            "there were no bracers here to take it when\x01",
            "you first arrived.\x02\x03",

            "Speaking of, I should have introduced myself\x01",
            "sooner. My name is Kurt Nardin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x151,
        (
            "#1650FIt's a pleasure to meet you, Mr. Nardin.\x02\x03",

            "#1651FMy name is Aina, and I--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x103,
        (
            "#1645FYou can save the long introductions for later.\x01",
            "You're fine as just 'the client.'\x02\x03",

            "#1640FBy the way, Kurt, can I have the key to get\x01",
            "into the sewers for a while?\x02\x03",

            "I'll go take care of that monster under the\x01",
            "west block while I'm out.\x02\x03",

            "Shouldn't take long at all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x103, 500)
    Sleep(300)

    ChrTalk(    #45
        0x13,
        (
            "#843F...I was under the impression you were in the\x01",
            "middle of escorting this young lady around the\x01",
            "city?\x02\x03",

            "I also seem to recall saying that you should\x01",
            "disregard all of the other jobs on the board\x01",
            "until that was done.\x02\x03",

            "#840FI sincerely hope you weren't ready to take a\x01",
            "civilian on a monster extermination request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x103,
        (
            "#1642FCrap...\x02\x03",

            "#1645FN-No! I wouldn't dream of it... I was just thinking\x01",
            "I might drop by the sewers on my way back after\x01",
            "finishing this job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x13,
        (
            "#843F...\x02\x03",

            "#843FI've explained this several times to you before,\x01",
            "Scherazard.\x02\x03",

            "A bracer's worth is not defined by their \x01",
            "strength in battle.\x02\x03",

            "#842FIt's defined by their ability to help others.\x01",
            "If that strength isn't being used for the good\x01",
            "of the community, it serves no purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        "#1646FBah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x13,
        (
            "#843FI feel as though I'm repeating myself here,\x01",
            "Scherazard, but--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#1645FOkay, okay! I get it.\x02\x03",

            "You want me to focus on helping people and\x01",
            "not just getting stronger. I hear you.\x02\x03",

            "...Though that's easy for you to say when you're\x01",
            "super strong already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x151,
        "#1653FOh? Is he?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(300)

    ChrTalk(    #52
        0x103,
        (
            "#1645FHe sure is.\x02\x03",

            "There was one time a while back where he just\x01",
            "walked past a wanted monster and beat it just\x01",
            "like that. A single strike.\x02\x03",

            "He didn't even change the speed he was walking.\x01",
            "Just...done.\x02\x03",

            "It was insane! I couldn't believe my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x13,
        (
            "#843FAhh, I remember that one.\x02\x03",

            "#840FI wouldn't have done that if not for the fact\x01",
            "I'd arranged to meet with someone soon after.\x02\x03",

            "If more time had been available to me, I would\x01",
            "have fought it using more ordinary tactics.\x02\x03",

            "One shouldn't fight carelessly just because his\x01",
            "or her foe is a simple monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x103,
        "#1645F(Not as insane as how stubborn he is, though.)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F51)

    label("loc_2194")

    TalkEnd(0x13)
    Return()

    # Function_7_A27 end

    def Function_8_2198(): pass

    label("Function_8_2198")

    OP_8C(0x103, 180, 400)

    def lambda_21A5():
        OP_8E(0xFE, 0xFFFFE9E4, 0x0, 0xFFFFF5C4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21A5)
    WaitChrThread(0x103, 0x1)

    def lambda_21C5():
        OP_8E(0xFE, 0xFFFFED7C, 0x0, 0xFFFFF2B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21C5)
    WaitChrThread(0x103, 0x1)

    def lambda_21E5():
        OP_8E(0xFE, 0xFFFFFD58, 0x0, 0xFFFFF2B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21E5)
    WaitChrThread(0x103, 0x1)

    def lambda_2205():
        OP_8E(0xFE, 0xFFFFFD58, 0xFFFFFE0C, 0xFFFFE3B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2205)
    WaitChrThread(0x103, 0x1)
    Return()

    # Function_8_2198 end

    def Function_9_2220(): pass

    label("Function_9_2220")


    def lambda_2226():
        OP_8E(0xFE, 0xFFFFEEA8, 0x0, 0xFFFFF2B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2226)
    WaitChrThread(0x151, 0x1)

    def lambda_2246():
        OP_8E(0xFE, 0xFFFFFD58, 0x0, 0xFFFFF2B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2246)
    WaitChrThread(0x151, 0x1)

    def lambda_2266():
        OP_8E(0xFE, 0xFFFFFD58, 0xFFFFFE0C, 0xFFFFE3B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2266)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_9_2220 end

    def Function_10_2281(): pass

    label("Function_10_2281")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_228E")
    Jump("loc_259B")

    label("loc_228E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_2429")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2314")

    ChrTalk(    #55
        0xFE,
        (
            "From today, this shall be our guild's new base\x01",
            "of operations!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "I am filled with excitement at the prospect.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2426")

    label("loc_2314")


    ChrTalk(    #57
        0xFE,
        (
            "The capital is absolutely the perfect place to be\x01",
            "our guild's new base of operations in my humble\x01",
            "opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "The port itself is ideal for fishing, while the\x01",
            "landing port gives us easy access to other spots\x01",
            "throughout the country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "What more could we ask for?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2426")

    Jump("loc_259B")

    label("loc_2429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2433")
    Jump("loc_259B")

    label("loc_2433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_259B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_24B1")

    ChrTalk(    #60
        0xFE,
        (
            "I once had a house in the outskirts of Grancel,\x01",
            "but no longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "From today, I shall be living here!\x02",
    )

    CloseMessageWindow()
    Jump("loc_259B")

    label("loc_24B1")


    ChrTalk(    #62
        0xFE,
        (
            "It's time for our Fisherman's Guild to finally\x01",
            "establish a presence here in the capital itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "I had to sell my house to make this a reality...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "...but no matter!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "All I need to do is live here in this building.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_259B")

    TalkEnd(0xFE)
    Return()

    # Function_10_2281 end

    def Function_11_259F(): pass

    label("Function_11_259F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_25AC")
    Jump("loc_28C5")

    label("loc_25AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_2711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_262D")
    OP_8C(0xFE, 90, 0)

    ChrTalk(    #66
        0xFE,
        "Yes! Our leader will explain all of that to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "It's all common sense stuff, so not to worry!\x02",
    )

    CloseMessageWindow()
    Jump("loc_270E")

    label("loc_262D")

    OP_8C(0xFE, 90, 0)

    ChrTalk(    #68
        0xFE,
        "So you're interested in joining, are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "But of course! You'd be MORE than welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "You will have to undertake a simple test before\x01",
            "you can actually become a member, and then\x01",
            "poof! You're one of us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_270E")

    Jump("loc_28C5")

    label("loc_2711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_271B")
    Jump("loc_28C5")

    label("loc_271B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_28C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27CC")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #71
        0xFE,
        (
            "I need to get all this work here finished and go \x01",
            "and have a look!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "N-No... I need to be calm. Fishing is all about\x01",
            "being cautious and patient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C5")

    label("loc_27CC")


    ChrTalk(    #73
        0xFE,
        (
            "Did you hear the news about the Masters\x01",
            "of Valleria Lake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "Apparently, they've made their way out of the lake\x01",
            "and have made the Grancel area their new feeding \x01",
            "ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I-I need to get all this work here finished and\x01",
            "go take a look!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_28C5")

    TalkEnd(0xFE)
    Return()

    # Function_11_259F end

    def Function_12_28C9(): pass

    label("Function_12_28C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_28D6")
    Jump("loc_2AEF")

    label("loc_28D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_2A07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2941")

    ChrTalk(    #76
        0xFE,
        "There're some really strange people in the world.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "These guys are proof of that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_2941")


    ChrTalk(    #78
        0xFE,
        (
            "This is easily the longest amount of time I've had\x01",
            "to spend handling fishing gear--and nothing but it,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "I've been doing this job for a while now,\x01",
            "but today's felt like no other.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2A04")

    Jump("loc_2AEF")

    label("loc_2A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2A11")
    Jump("loc_2AEF")

    label("loc_2A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2AEF")
    OP_8C(0xFE, 270, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2AA9")
    OP_4A(0x16, 255)
    TurnDirection(0x16, 0xFE, 500)
    Sleep(300)

    ChrTalk(    #80
        0x16,
        "Be careful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x16,
        "Those break really easily!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x16, 500)
    Sleep(300)

    ChrTalk(    #82
        0xFE,
        "Wh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "O-Okay... I will...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x16, 270, 500)
    OP_4B(0x16, 255)
    Jump("loc_2AEF")

    label("loc_2AA9")


    ChrTalk(    #84
        0xFE,
        "Am I okay leaving these here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "These, uh, rod thingies...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2AEF")

    TalkEnd(0xFE)
    Return()

    # Function_12_28C9 end

    def Function_13_2AF3(): pass

    label("Function_13_2AF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_2B00")
    Jump("loc_2C03")

    label("loc_2B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_2BF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2B8C")

    ChrTalk(    #86
        0xFE,
        "Oh... I do have one question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "Are there any rules and regulations that need to\x01",
            "be followed as part of the guild?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BEF")

    label("loc_2B8C")


    ChrTalk(    #88
        0xFE,
        "Yes, I am...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "I do feel uncertain whether I'm good enough\x01",
            "at fishing to be a member...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2BEF")

    Jump("loc_2C03")

    label("loc_2BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2BFC")
    Jump("loc_2C03")

    label("loc_2BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2C03")

    label("loc_2C03")

    TalkEnd(0xFE)
    Return()

    # Function_13_2AF3 end

    def Function_14_2C07(): pass

    label("Function_14_2C07")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -4600, 0, 560, 90)
    SetChrPos(0x11, -2320, 0, 450, 270)
    OP_6D(4390, -250, 910, 0)
    OP_67(0, 7460, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(315000, 0)
    OP_6E(328, 0)
    Sleep(500)

    def lambda_2C9B():
        OP_6D(-4830, -250, 1680, 3500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2C9B)
    OP_1D(0xE)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    Fade(500)
    OP_6D(-5060, 0, 2040, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(315000, 0)
    OP_6E(338, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #90
        0x10,
        (
            "#760F#5PI see...\x02\x03",

            "I sort of expected it would only be a matter of\x01",
            "time before you returned to the Republic...\x01",
            "Your mind is made up, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x11,
        (
            "#070F'Fraid so. I've made the guys over there take\x01",
            "care of everything without me long enough.\x02\x03",

            "Call it an A-Rank bracer's duty to his peers and\x01",
            "society, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x10,
        (
            "#760F#5PWell, I suppose when you put it that way...\x02\x03",

            "I can't deny that I would like you to stay here\x01",
            "a while longer, but if that is your decision,\x01",
            "I'll have to respect it.\x02\x03",

            "So, when are you planning on returning there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x11,
        (
            "#070FWell, I was planning on heading back right away,\x01",
            "but then something came up.\x02\x03",

            "Ambassador Cochrane over at the embassy invited\x01",
            "me on a little trip, you see. So I'm not going\x01",
            "back just yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x10,
        (
            "#760F#5P...She did?\x02\x03",

            "I wonder what made her want to do that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x11,
        (
            "#070FWell, by the sounds of it, it's not really me\x01",
            "she's after, it's Kilika.\x02\x03",

            "I'm just needed there, too, for some reason or\x01",
            "another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x10,
        (
            "#760F#5PThat makes me even less sure what she might want\x01",
            "you for, though...\x02\x03",

            "Well, either way, have fun, I suppose.\x02\x03",

            "Hopefully it'll make for a nice final memory in\x01",
            "Liberl before you head back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x11,
        (
            "#070FHaha. Here's hoping.\x02\x03",

            "I dunno what to expect either, but it can't hurt\x01",
            "to go along.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2C07 end

    def Function_15_31FB(): pass

    label("Function_15_31FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -4600, 0, 560, 90)
    SetChrPos(0x11, -2320, 0, 450, 270)
    OP_71(0x403, 0x0)
    ExitThread()
    OP_6D(4390, -250, 910, 0)
    OP_67(0, 7460, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(338, 0)
    OP_1D(0xE)
    Sleep(500)

    def lambda_329D():
        OP_6D(-4830, -250, 1680, 3500)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_329D)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x19, 0x0)
    Fade(1000)
    OP_6D(-5060, 0, 2040, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(315000, 0)
    OP_6E(338, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #98
        0x10,
        (
            "#764F#5PI see...\x02\x03",

            "#760FI sort of expected it would only be a matter\x01",
            "of time before you returned to the Republic...\x01",
            "Your mind is made up, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x11,
        (
            "#573F#12P'Fraid so. I've made the guys over there take\x01",
            "care of everything without me long enough.\x02\x03",

            "#070FCall it an A-rank bracer's duty to his peers and\x01",
            "society, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10,
        (
            "#764F#5PWell, I suppose when you put it that way...\x02\x03",

            "I do wish you could stay here a while longer,\x01",
            "but if that is your decision, I'll respect it.\x02\x03",

            "#760FSo when are you planning on returning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        (
            "#074F#12PWell, there's no point in lingering here any\x01",
            "longer than I have to now that I've made up\x01",
            "my mind to leave...\x02\x03",

            "#070F...so, honestly, I was thinking about tomorrow.\x02\x03",

            "Think I could ask you to arrange a ticket\x01",
            "to Calvard for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x10,
        (
            "#763F#5PWell, certainly...\x02\x03",

            "#760FAre you not planning to go and visit Kilika first,\x01",
            "though? I would have thought you'd want to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x11,
        (
            "#075F#12PThat WAS part of the original plan...\x02\x03",

            "...but she wouldn't have any of it.\x01",
            "Surprise, surprise.\x02\x03",

            "#072FHer stance was, 'If you're going to waste time\x01",
            "coming to see me, use it to go back to Calvard\x01",
            "earlier and get some work done.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10,
        (
            "#761F#5PHaha... Very well, then.\x02\x03",

            "#760FThat doesn't sound like a position you'll be able\x01",
            "to talk her out of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x11,
        (
            "#573F#12PIt's no big deal, though.\x02\x03",

            "#070FI mean, it's not like we'll never see\x01",
            "each other again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x10,
        (
            "#760F#5PI suppose that's very true.\x02\x03",

            "#761FI'm not sure there's anything in Zemuria\x01",
            "that could keep you two apart forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x11,
        "#071F#12PHaha. It feels like that to me sometimes, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10,
        (
            "#761F#5PHaha...\x02\x03",

            "#760FWell, regardless, I won't keep you any longer.\x02\x03",

            "So that's one ticket to Calvard for tomorrow,\x01",
            "coming right up!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x1, 0x64)
    Sleep(800)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #109
        0x10,
        "#763F#5PSorry. Let me just get this.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 225, 400)

    def lambda_3A5B():
        OP_6D(-5400, 0, 1800, 1200)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3A5B)
    OP_8E(0x10, 0xFFFFEA20, 0x0, 0x0, 0x5DC, 0x0)
    OP_8C(0x10, 270, 400)
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_23(0xC3)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(    #110
        0x10,
        (
            "#760F#11PYes, this is the Grancel branch of the\x01",
            "Bracer Guild.\x02\x03",

            "#764F...Ah, yes.\x02\x03",

            "#763FYes...\x02\x03",

            "#760FHe's here as we speak, actually.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3B8C():
        OP_6D(-5060, 0, 2040, 1000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3B8C)
    OP_8C(0x10, 90, 400)
    Sleep(500)

    ChrTalk(    #111
        0x10,
        "#760F#5PZin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x11,
        "#073F#12PSomething up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x10,
        (
            "#760F#5PIt's Ambassador Cochrane at the Calvardian\x01",
            "embassy.\x02\x03",

            "#761FShe'd like to invite you on a hot springs trip...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(100)

    ChrTalk(    #114
        0x11,
        "#073F#11P#4SWHAT?!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    def lambda_3CA6():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3CA6)
    FadeToDark(2000, 0, -1)

    def lambda_3CC0():

        label("loc_3CC0")

        TurnDirection(0xFE, 0x11, 500)
        OP_48()
        Jump("loc_3CC0")

    QueueWorkItem2(0x10, 2, lambda_3CC0)
    OP_43(0x11, 0x3, 0x0, 0x10)
    Sleep(500)

    def lambda_3CDD():
        OP_8F(0xFE, 0xFFFFEA20, 0x0, 0x4D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3CDD)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_31FB end

    def Function_16_3D06(): pass

    label("Function_16_3D06")

    OP_8C(0x11, 180, 500)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 0)

    def lambda_3D1D():
        OP_8E(0xFE, 0xFFFFF6F0, 0x0, 0xFFFFF3E4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3D1D)
    WaitChrThread(0x11, 0x1)

    def lambda_3D3D():
        OP_8E(0xFE, 0xFFFFEE08, 0x0, 0xFFFFF3E4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3D3D)
    WaitChrThread(0x11, 0x1)

    def lambda_3D5D():
        OP_8E(0xFE, 0xFFFFEA20, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3D5D)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    OP_8C(0x11, 270, 500)
    Return()

    # Function_16_3D06 end

    def Function_17_3D89(): pass

    label("Function_17_3D89")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #115 op#5
        "\x07\x00#150WGrancel City, 1197...#20W\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetChrName("")

    AnonymousTalk(    #116
        (
            "\x07\x00Five years had passed since the Hundred Days War\x01",
            "came to an end. The scars it left were slowly healing,\x01",
            "and life was returning to Liberl.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #117
        (
            "\x07\x00People gathered in the cities and towns that had\x01",
            "returned to their former state, and the revived\x01",
            "orbment trade brought the kingdom prosperity.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #118
        "\x07\x00Peace was becoming normal once again.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #119
        (
            "\x07\x00Not all that was happening in Liberl at the time\x01",
            "was so positive, however; this was also a period\x01",
            "in which corruption was rife in the military.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #120
        (
            "\x07\x00Many of the army's officers at the time cared for\x01",
            "nothing but lining their own pockets or gaining\x01",
            "power and prestige.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #121
        (
            "\x07\x00Between the development of orbal technology\x01",
            "and booming prosperity, much was forgotten...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_6D(0, 2000, 0, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3560, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, -8300, 0, -3300, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, -500, -7700, 0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(2000, 0)

    def lambda_4136():
        OP_6D(0, 0, 0, 4000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_4136)
    WaitChrThread(0x19, 0x0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1000)

    def lambda_415D():
        OP_6D(0, 0, -2340, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_415D)

    def lambda_4175():
        OP_6B(3060, 2000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4175)

    def lambda_4185():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFEB38, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4185)

    def lambda_41A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_41A0)
    WaitChrThread(0x12, 0x1)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #122
        0x12,
        "Woman",
        "#1653F...Hmm?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 45, 400)
    Sleep(800)
    OP_8C(0x12, 315, 400)
    Sleep(800)
    OP_8C(0x12, 0, 400)
    Sleep(500)

    NpcTalk(    #123
        0x12,
        "Woman",
        "#1653FIs there no one here...?\x02",
    )

    CloseMessageWindow()

    def lambda_4228():
        OP_6D(0, 0, -400, 1600)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_4228)

    def lambda_4240():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFFF614, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4240)
    WaitChrThread(0x12, 0x1)
    Sleep(500)
    OP_8C(0x12, 315, 400)
    Sleep(200)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_4288():
        OP_6D(-1380, 0, 1300, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_4288)

    def lambda_42A0():
        OP_8E(0xFE, 0xFFFFF6B4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_42A0)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 270, 500)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #124
        (
            "\x07\x05If you have a request, please write it on one of \x01",
            "the forms to the right and place it in this box.\x01",
            "                    Bracer Guild - Grancel Branch\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)
    OP_8C(0x12, 90, 400)
    Sleep(300)

    def lambda_43BB():
        OP_6D(3280, 0, 1600, 5000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_43BB)

    def lambda_43D3():
        OP_8E(0xFE, 0x76C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_43D3)
    WaitChrThread(0x12, 0x1)

    def lambda_43F3():
        OP_8E(0xFE, 0x116C, 0x0, 0xEB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_43F3)
    WaitChrThread(0x12, 0x1)

    def lambda_4413():
        OP_8E(0xFE, 0x17AC, 0x0, 0xEB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4413)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 180, 500)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    def lambda_445E():
        OP_8E(0xFE, 0xD20, 0x0, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_445E)
    WaitChrThread(0x12, 0x1)

    def lambda_447E():
        OP_8E(0xFE, 0x744, 0xFA, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_447E)
    WaitChrThread(0x12, 0x1)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    def lambda_44C2():
        OP_8F(0xFE, 0xD20, 0x0, 0x12C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_44C2)
    WaitChrThread(0x12, 0x1)

    def lambda_44E2():
        OP_6D(-300, 0, 300, 4000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_44E2)

    def lambda_44FA():
        OP_8E(0xFE, 0xD20, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_44FA)
    WaitChrThread(0x12, 0x1)

    def lambda_451A():
        OP_8E(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_451A)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 180, 500)
    Sleep(300)

    NpcTalk(    #125
        0x12,
        "Woman",
        "#1654F(It looks like it.)\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 270, 500)
    Sleep(300)

    NpcTalk(    #126
        0x12,
        "Woman",
        "#1652F(I wonder if they'd mind if I used their phone?)\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x103, 0, -500, -7700, 0)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_45D5():
        OP_8E(0xFE, 0xFFFFF9E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_45D5)
    WaitChrThread(0x12, 0x1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_45FF():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_45FF)

    def lambda_460D():
        OP_6D(0, 500, -1920, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_460D)

    def lambda_4625():
        OP_6B(3160, 2000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4625)

    def lambda_4635():
        OP_67(0, 5000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_4635)
    Sleep(1500)

    def lambda_4652():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFEB38, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4652)

    def lambda_466D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_466D)
    WaitChrThread(0x103, 0x1)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #127
        0x103,
        (
            "#1645FUgh... I'm pooped...\x02\x03",

            "I feel more like a slave than a bracer with all\x01",
            "this menial work getting dumped on me...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x12, 500)
    Sleep(300)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #128
        0x103,
        "#1643FOh, hello... Are you here to lodge a request?\x02",
    )

    CloseMessageWindow()

    def lambda_4764():
        OP_6D(-1280, 0, -780, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_4764)

    def lambda_477C():
        OP_6B(3240, 2000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_477C)

    def lambda_478C():
        OP_67(0, 4840, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_478C)

    def lambda_47A4():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFFF1F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_47A4)
    Sleep(400)
    OP_8C(0x12, 135, 500)

    def lambda_47CB():
        OP_8E(0xFE, 0xFFFFFDF8, 0x0, 0xFFFFFBF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_47CB)
    WaitChrThread(0x103, 0x1)

    def lambda_47EB():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_47EB)
    WaitChrThread(0x12, 0x1)

    def lambda_47FE():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_47FE)
    Sleep(300)

    NpcTalk(    #129
        0x12,
        "Woman",
        (
            "#1650F#2PYes, that's right...\x02\x03",

            "Umm... Might I ask your name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x103,
        (
            "#1640FI'm Scherazard Harvey. A bracer.\x02\x03",

            "I'm still a junior one, but I know what I'm doing.\x01",
            "Don't you worry about that.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #131
        0x12,
        "Woman",
        (
            "#1653F#2POh, my! Really?\x02\x03",

            "#1651FHeehee. You look so young that I had no idea\x01",
            "you were an actual bracer.\x02\x03",

            "My name is Aina. It's a pleasure to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x103,
        (
            "#1640FSo what's the request you want to make?\x01",
            "I don't have all day to stand around chatting.\x02\x03",

            "There're only two bracers at this branch right\x01",
            "now, so we're VERY busy.\x02\x03",

            "#1640FIf you can make it quick, I'd appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x12,
        (
            "#1653F#2POh, really?\x02\x03",

            "I'm terribly sorry. I had no idea you were--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x103,
        (
            "#1645FDid you not hear me?\x02\x03",

            "Or do you need me to explain to you what\x01",
            "the word 'quick' means?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x12,
        (
            "#1651F#2PO-Oh. My apologies.\x02\x03",

            "#1650FWell, you see, it's my first time visiting the city.\x02\x03",

            "I thought it might be wise to come here and\x01",
            "request that someone give me a tour of the\x01",
            "main sights and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x103,
        "#1642F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x12,
        (
            "#1651F#2PHeehee. The size of the place is rather daunting,\x01",
            "as I'm sure you can imagine.\x02\x03",

            "But with a bracer who knows their way around\x01",
            "at my side, I'd be able to enjoy all that Grancel\x01",
            "has to offer without fearing getting lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x103,
        (
            "#1645FYou've got to be kidding...\x02\x03",

            "Please tell me you didn't actually come here\x01",
            "for such a worthless request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x12,
        "#1653F#2PPardon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x103,
        (
            "#1646FYou seem to be misconstruing what bracers\x01",
            "are actually here for.\x02\x03",

            "We're not community volunteers or whatever.\x01",
            "We have a serious profession and do serious\x01",
            "work.\x02\x03",

            "#1642FAnd we're also VERY busy, as I said earlier,\x01",
            "so I'm going to have to ask you look elsewhere\x01",
            "if you want a buddy for your sightseeing trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x12,
        "#1650F#2PU-Umm... I... I wasn't trying to...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x103,
        (
            "#1645FOr, hell, just go and look around on your own.\x01",
            "Getting lost is probably part of the experience,\x01",
            "anyway.\x02\x03",

            "#1645F(Has this one lived in a box all her life?\x01",
            "Typical rich girl...)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    def lambda_4F77():

        label("loc_4F77")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_4F77")

    QueueWorkItem2(0x12, 3, lambda_4F77)

    def lambda_4F88():
        OP_8E(0xFE, 0xCBC, 0x0, 0xFFFFFEAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F88)
    WaitChrThread(0x103, 0x1)
    OP_44(0x12, 0x3)
    OP_8C(0x103, 90, 500)
    Sleep(400)

    ChrTalk(    #143
        0x103,
        (
            "#1646F#3PBesides, I need to focus on doing major jobs so\x01",
            "I can get my letter of recommendation from this\x01",
            "branch and get promoted to senior bracer.\x02\x03",

            "If you find something serious you need help with,\x01",
            "by all means come back. Until then, get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x12,
        (
            "#1656F#5P(*sigh* It looks like this isn't going to work...)\x02\x03",

            "Umm... I really am sorry for troubling you, but--\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x103, 0x3, 0x0, 0x13)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 200, -500, -7700, 0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x13, 255)

    def lambda_515C():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_515C)

    def lambda_516A():
        OP_8E(0xFE, 0xC8, 0xFFFFFF06, 0xFFFFEB38, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_516A)

    def lambda_5185():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5185)
    WaitChrThread(0x13, 0x1)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    OP_62(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #145
        0x13,
        (
            "#840FOh? Who do we have here? Have you come to make\x01",
            "a request, perchance?\x02\x03",

            "Pardon us for not properly manning the front desk.\x01",
            "That's currently my job, but I'm undertaking other\x01",
            "work at the same time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_528A():
        OP_8E(0xFE, 0xC8, 0x0, 0xFFFFF3E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_528A)
    WaitChrThread(0x13, 0x1)
    TurnDirection(0x13, 0x12, 500)
    Sleep(300)

    ChrTalk(    #146
        0x12,
        "#1653F#2POh, you don't have to apologize.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #147
        0x103,
        (
            "#1646F#3PI'd pay her no mind, if I were you. She's a waste\x01",
            "of time.\x02\x03",

            "#1642FShe seems to have gotten it into her head that\x01",
            "bracers are friends for hire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x12,
        (
            "#1655F#2P...Well, if you'll excuse me. I'll get out of your\x01",
            "hair now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_53D2():
        OP_8E(0xFE, 0xFFFFFE0C, 0xFFFFFF06, 0xFFFFEB4C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_53D2)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x13)

    ChrTalk(    #149 op#A op#5
        0x13,
        "#843F#13A#5PHmm...\x05\x02",
    )

    Sleep(500)

    ChrTalk(    #150
        0x13,
        "#843F#5PPlease don't leave just yet.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0x12, 0x13, 400)
    Sleep(500)
    OP_44(0x103, 0x3)

    def lambda_547F():
        OP_8F(0xFE, 0xCBC, 0x0, 0xFFFFFFD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_547F)
    WaitChrThread(0x103, 0x1)
    Sleep(500)
    TurnDirection(0x13, 0x103, 500)
    Sleep(300)

    ChrTalk(    #151
        0x13,
        "#840F#5PScherazard.\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x103, 0x13, 500)
    Sleep(300)

    ChrTalk(    #152
        0x103,
        (
            "#1643F...Huh?\x02\x03",

            "Wh-What is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x13,
        (
            "#840F#5PDo what she wants.\x02\x03",

            "Helping people in need is the fundamental mission\x01",
            "of us bracers. You've got no reason not to help.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5593():
        OP_8F(0xFE, 0x834, 0x0, 0xFFFFFB50, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5593)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #154
        0x103,
        (
            "#1642FWh-What...? B-But we're busy here!\x02\x03",

            "I don't have time to be playing tour guide!\x01",
            "I've got more important things to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x13,
        (
            "#843F#5PDon't worry about the other requests on the board.\x01",
            "I'll take care of those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x103,
        (
            "#1644FBut you're even busier than I am! You're even our\x01",
            "receptionist on top of it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x13,
        (
            "#842F#5PYou needn't worry about me. Besides, you're still a\x01",
            "trainee, which means you still have much to learn.\x02\x03",

            "#843FSo go.\x02\x03",

            "Once you've finished this request, I'll write you\x01",
            "your letter of recommendation. \x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #158
        0x103,
        (
            "#1643FWhat...? Really?\x02\x03",

            "A-Are you sure? This seems like way too simple of\x01",
            "a job to be awarding something like that for...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x13,
        (
            "#840F#5PI thought it was your policy to give 100% to all\x01",
            "work you undertake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x103,
        "#1645FW-Well, it is, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x13,
        "#840F#5PThen I'm counting on you with this job, too.\x02",
    )

    CloseMessageWindow()

    def lambda_5901():

        label("loc_5901")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_5901")

    QueueWorkItem2(0x12, 3, lambda_5901)

    def lambda_5912():

        label("loc_5912")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_5912")

    QueueWorkItem2(0x103, 3, lambda_5912)
    OP_8C(0x13, 315, 500)

    def lambda_592A():
        OP_8E(0xFE, 0xFFFFF768, 0x0, 0xFFFFFF74, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_592A)
    WaitChrThread(0x13, 0x1)
    OP_44(0x103, 0x3)
    OP_44(0x12, 0x3)
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #162
        0x12,
        "#1650FUmm... Thank you very much...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)
    Sleep(300)

    ChrTalk(    #163
        0x13,
        (
            "#840F#2PThink nothing of it.\x02\x03",

            "Take care, you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x103,
        "#1645F...Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x12,
        "#1650FI appreciate your assistance.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 500)
    Sleep(300)

    def lambda_5A15():
        OP_8E(0xFE, 0xFFFFFE0C, 0xFFFFFF06, 0xFFFFE91C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5A15)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    OP_43(0x103, 0x3, 0x0, 0x12)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_5A4B():
        OP_8E(0xFE, 0xFFFFFE0C, 0xFFFFFE0C, 0xFFFFE3B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5A4B)

    def lambda_5A66():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5A66)
    WaitChrThread(0x12, 0x1)
    SetChrFlags(0x12, 0x80)
    WaitChrThread(0x103, 0x3)
    Sleep(1500)

    def lambda_5A8C():
        OP_6D(-2400, 200, 60, 3000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_5A8C)

    def lambda_5AA4():
        OP_6B(3160, 3000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5AA4)
    OP_8C(0x13, 270, 400)
    Sleep(3000)

    ChrTalk(    #166
        0x13,
        "#843F#6P...This should hopefully do her good.\x02",
    )

    CloseMessageWindow()

    def lambda_5AF3():
        OP_6B(3060, 3000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5AF3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/T4100   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3D89 end

    def Function_18_5B15(): pass

    label("Function_18_5B15")

    OP_8C(0x103, 225, 500)
    Sleep(300)

    def lambda_5B27():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B27)
    WaitChrThread(0x103, 0x1)

    def lambda_5B47():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFEBEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B47)
    WaitChrThread(0x103, 0x1)

    def lambda_5B67():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFE91C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B67)
    WaitChrThread(0x103, 0x1)

    def lambda_5B87():
        OP_8E(0xFE, 0x0, 0xFFFFFE0C, 0xFFFFE3B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B87)

    def lambda_5BA2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5BA2)
    WaitChrThread(0x103, 0x1)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_18_5B15 end

    def Function_19_5BB9(): pass

    label("Function_19_5BB9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C34")
    Sleep(2000)

    def lambda_5BCD():
        OP_8F(0xFE, 0xCBC, 0x0, 0xFFFFFC54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5BCD)
    WaitChrThread(0x103, 0x1)
    Sleep(2500)

    def lambda_5BF2():
        OP_8F(0xFE, 0xCBC, 0x0, 0xFFFFFEAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5BF2)
    WaitChrThread(0x103, 0x1)
    Sleep(2500)

    def lambda_5C17():
        OP_8F(0xFE, 0xCBC, 0x0, 0x104, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C17)
    WaitChrThread(0x103, 0x1)
    Jump("Function_19_5BB9")

    label("loc_5C34")

    Return()

    # Function_19_5BB9 end

    SaveToFile()

Try(main)
