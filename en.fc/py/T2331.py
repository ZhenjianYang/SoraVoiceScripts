from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2331   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2331.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Rex',                                  # 9
        'Carla',                                # 10
        'Matron Theresa',                       # 11
        'Daniel',                               # 12
        'Mary',                                 # 13
        'Polly',                                # 14
        'Clem',                                 # 15
        'Mayor Dalmore',                        # 16
        'Steward Gilbert',                      # 17
        'Carna',                                # 18
        'Alvin',                                # 19
        'Shelby',                               # 20
        'Lucia',                                # 21
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02640 ._CH',             # 02
        'ED6_DT07/CH02630 ._CH',             # 03
        'ED6_DT07/CH02570 ._CH',             # 04
        'ED6_DT07/CH02410 ._CH',             # 05
        'ED6_DT07/CH02420 ._CH',             # 06
        'ED6_DT07/CH01030 ._CH',             # 07
        'ED6_DT07/CH01240 ._CH',             # 08
        'ED6_DT07/CH02500 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01070 ._CH',             # 0C
        'ED6_DT06/CH20093 ._CH',             # 0D
        'ED6_DT06/CH20101 ._CH',             # 0E
        'ED6_DT06/CH20053 ._CH',             # 0F
        'ED6_DT07/CH01023 ._CH',             # 10
        'ED6_DT07/CH01143 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02640P._CP',             # 02
        'ED6_DT07/CH02630P._CP',             # 03
        'ED6_DT07/CH02570P._CP',             # 04
        'ED6_DT07/CH02410P._CP',             # 05
        'ED6_DT07/CH02420P._CP',             # 06
        'ED6_DT07/CH01030P._CP',             # 07
        'ED6_DT07/CH01240P._CP',             # 08
        'ED6_DT07/CH02500P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01070P._CP',             # 0C
        'ED6_DT06/CH20093P._CP',             # 0D
        'ED6_DT06/CH20101P._CP',             # 0E
        'ED6_DT06/CH20053P._CP',             # 0F
        'ED6_DT07/CH01023P._CP',             # 10
        'ED6_DT07/CH01143P._CP',             # 11
    )

    DeclNpc(
        X                   = -25500,
        Z                   = 0,
        Y                   = 43210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -37500,
        Z                   = 0,
        Y                   = 44500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -50190,
        Z                   = 0,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -50850,
        Z                   = 0,
        Y                   = 180,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -50850,
        Z                   = 0,
        Y                   = 1400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -50570,
        Z                   = 0,
        Y                   = -2840,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -49420,
        Z                   = 0,
        Y                   = -2280,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -400,
        Z                   = 0,
        Y                   = 45400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -33200,
        Z                   = 150,
        Y                   = 41740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -32060,
        Z                   = 150,
        Y                   = 42960,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -23900,
        Z                   = 0,
        Y                   = -1170,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )


    DeclActor(
        TriggerX            = -37020,
        TriggerZ            = 0,
        TriggerY            = 42970,
        TriggerRange        = 400,
        ActorX              = -37500,
        ActorZ              = 1500,
        ActorY              = 44500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26870,
        TriggerZ            = 0,
        TriggerY            = 42820,
        TriggerRange        = 400,
        ActorX              = -25500,
        ActorZ              = 1500,
        ActorY              = 43210,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_322",          # 00, 0
        "Function_1_5D0",          # 01, 1
        "Function_2_5D1",          # 02, 2
        "Function_3_5E7",          # 03, 3
        "Function_4_5EC",          # 04, 4
        "Function_5_14F6",         # 05, 5
        "Function_6_14FB",         # 06, 6
        "Function_7_1D21",         # 07, 7
        "Function_8_1DB7",         # 08, 8
        "Function_9_1E25",         # 09, 9
        "Function_10_22A9",        # 0A, 10
        "Function_11_2375",        # 0B, 11
        "Function_12_2465",        # 0C, 12
        "Function_13_24F2",        # 0D, 13
        "Function_14_2597",        # 0E, 14
        "Function_15_2641",        # 0F, 15
        "Function_16_266E",        # 10, 16
        "Function_17_5380",        # 11, 17
        "Function_18_5391",        # 12, 18
        "Function_19_53A2",        # 13, 19
        "Function_20_53B3",        # 14, 20
        "Function_21_53C4",        # 15, 21
        "Function_22_53D5",        # 16, 22
        "Function_23_69D7",        # 17, 23
        "Function_24_69F8",        # 18, 24
        "Function_25_6A19",        # 19, 25
        "Function_26_6A3A",        # 1A, 26
        "Function_27_6A68",        # 1B, 27
        "Function_28_6A9B",        # 1C, 28
        "Function_29_6ACE",        # 1D, 29
        "Function_30_6B01",        # 1E, 30
    )


    def Function_0_322(): pass

    label("Function_0_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_389")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -48350, 0, 150, 215)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -50850, 0, 180, 135)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -50570, 0, -2840, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -49420, 0, -2280, 315)
    Jump("loc_59A")

    label("loc_389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_421")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, -53290, 0, 2040, 180)
    SetChrPos(0xA, -53080, 0, -870, 180)
    SetChrPos(0xB, -50850, 0, -230, 270)
    SetChrPos(0xD, -50850, 0, -1430, 270)
    SetChrPos(0xC, -52530, 0, -2420, 0)
    SetChrPos(0xE, -50800, 0, 1470, 270)
    Jump("loc_59A")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_506")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 15)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 15)
    SetChrPos(0x11, -53000, 0, 2040, 90)
    SetChrPos(0xA, -53000, 0, -870, 90)
    SetChrChipByIndex(0xA, 13)
    SetChrChipByIndex(0x11, 14)
    OP_44(0x11, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrPos(0xB, -50850, 0, -230, 270)
    SetChrPos(0xD, -50850, 0, -1430, 270)
    SetChrPos(0xC, -52530, 0, -2420, 0)
    SetChrPos(0xE, -50800, 0, 1470, 270)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_59A")

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_51A")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x12, 0x10)
    Jump("loc_59A")

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_56B")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -48450, 0, -990, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -49690, 0, -120, 90)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -47720, 0, 2100, 0)
    Jump("loc_59A")

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_575")
    Jump("loc_59A")

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_57F")
    Jump("loc_59A")

    label("loc_57F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_589")
    Jump("loc_59A")

    label("loc_589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_593")
    Jump("loc_59A")

    label("loc_593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_59A")

    label("loc_59A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (107, "loc_5A6"),
        (SWITCH_DEFAULT, "loc_5CF"),
    )


    label("loc_5A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B9")
    OP_A2(0x428)
    Event(0, 16)

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC")
    OP_A2(0x436)
    Event(0, 22)

    label("loc_5CC")

    Jump("loc_5CF")

    label("loc_5CF")

    Return()

    # Function_0_322 end

    def Function_1_5D0(): pass

    label("Function_1_5D0")

    Return()

    # Function_1_5D0 end

    def Function_2_5D1(): pass

    label("Function_2_5D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5D1")

    label("loc_5E6")

    Return()

    # Function_2_5D1 end

    def Function_3_5E7(): pass

    label("Function_3_5E7")

    Call(0, 4)
    Return()

    # Function_3_5E7 end

    def Function_4_5EC(): pass

    label("Function_4_5EC")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64C")
    OP_0D()
    OP_A9(0x2A)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_64C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65D")
    TalkEnd(0x8)
    Return()

    label("loc_65D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1D")
    EventBegin(0x0)
    OP_69(0x8, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF6")

    ChrTalk(    #0
        0x8,
        "Welcome to the White Magnolia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "I don't recall seeing you before.\x01",
            "Are you here on vacation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#006FNo, we're just passing through\x01",
            "on our way to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#010FWe came from Bose, by way\x01",
            "of the Krone Pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "You're joking!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "Wow...I never thought I'd meet another\x01",
            "person brave enough to handle that\x01",
            "place, in this day and age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        "You're into hiking, I assume?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#501FNo, not especially.\x02\x03",

            "#501FIt sure works up an appetite,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#010FIs there anything you'd\x01",
            "particularly recommend?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "Oh, yes...I'd suggest trying\x01",
            "the box lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#004FWhat's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "That windmill at the edge of town\x01",
            "has a platform with a great view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "Every day at lunch, lots of\x01",
            "people buy them and take them\x01",
            "there to eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#001FOh, that might be nice.♪\x02\x03",

            "From what you're saying,\x01",
            "it sounds like something\x01",
            "I'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#019FWell, why don't we try it?\x02\x03",

            "#010FWhat kind of box lunches\x01",
            "are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "Well, there's the smoked ham\x01",
            "sandwich and the seafood paella...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "Either would be good,\x01",
            "in my opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#501FHmm...I think I'll try the sandwich.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        "#010FThen I'll have the seafood paella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "Thank you. That'll be 120 mira.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B65")

    label("loc_AF6")


    ChrTalk(    #20
        0x8,
        (
            "My two favorite box lunches are\x01",
            "the smoked ham sandwich and\x01",
            "the seafood paella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "That'll be 120 mira.\x02",
    )

    CloseMessageWindow()

    label("loc_B65")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Buy]\x01",             # 0
            "[Never mind]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BC9"),
        (1, "loc_D4D"),
        (SWITCH_DEFAULT, "loc_E18"),
    )


    label("loc_BC9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CF0")
    OP_4F(0x12, (scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #22
        "\x07\x00Received '\x07\x02Special Boxed Lunch\x07\x00'.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x33C, 1)

    ChrTalk(    #23
        0x8,
        (
            "And I'll toss in some herb tea\x01",
            "at no charge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        "It's my specialty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#001FThanks! ㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #26
        0x102,
        (
            "#010FWant to go over to the\x01",
            "viewing platform?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #27
        0x101,
        "#006FSure!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x413)
    Jump("loc_D4A")

    label("loc_CF0")


    ChrTalk(    #28
        0x8,
        (
            "Oh...it looks like you don't\x01",
            "have enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "Perhaps you could come\x01",
            "back later?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x401)

    label("loc_D4A")

    Jump("loc_E18")

    label("loc_D4D")


    ChrTalk(    #30
        0x8,
        "Would you prefer to eat here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "We do have several other items\x01",
            "on the menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#007FAww, I kinda had my heart\x01",
            "set on eating outside.\x02\x03",

            "#008FI'm sorry. Let me think on\x01",
            "it for a little bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x401)
    Jump("loc_E18")

    label("loc_E18")

    EventEnd(0x1)
    Jump("loc_14F2")

    label("loc_E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_EFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA8")
    OP_A2(0x0)

    ChrTalk(    #33
        0x8,
        (
            "So those dirty muggers have\x01",
            "been caught, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "I hope they'll take the time to\x01",
            "think about what they've done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFA")

    label("loc_EA8")


    ChrTalk(    #35
        0x8,
        (
            "I hope those muggers take this\x01",
            "opportunity to think about what\x01",
            "they've done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFA")

    Jump("loc_14F2")

    label("loc_EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_F4D")

    ChrTalk(    #36
        0x8,
        (
            "It's already pitch-black out there.\x01",
            "Be careful on your way back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F2")

    label("loc_F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_10AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101D")
    OP_A2(0x0)

    ChrTalk(    #37
        0x8,
        (
            "It's almost time for the\x01",
            "campus festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "I think the kids from the\x01",
            "orphanage are going, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "I just hope they can forget about\x01",
            "all this mess, at least for a\x01",
            "little while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A9")

    label("loc_101D")


    ChrTalk(    #40
        0x8,
        (
            "I think the kids from the\x01",
            "orphanage are going, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "I just hope they can forget about\x01",
            "all this mess, at least for a\x01",
            "little while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A9")

    Jump("loc_14F2")

    label("loc_10AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_111C")

    ChrTalk(    #42
        0x8,
        (
            "I saw a boy from the orphanage go\x01",
            "running by, a little while ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        "I wonder what happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_14F2")

    label("loc_111C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_1236")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E8")
    OP_A2(0x0)

    ChrTalk(    #44
        0x8,
        (
            "Was everything destroyed in\x01",
            "the fire at the orphanage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "I went ahead and let the kids\x01",
            "use my room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "If you wouldn't mind, could you go\x01",
            "and try to cheer them up a little?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1233")

    label("loc_11E8")


    ChrTalk(    #47
        0x8,
        (
            "If you wouldn't mind, could you go\x01",
            "and try to cheer them up a little?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1233")

    Jump("loc_14F2")

    label("loc_1236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1286")

    ChrTalk(    #48
        0x8,
        "Not much wind today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "It'd be nice to walk on\x01",
            "the beach...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F2")

    label("loc_1286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_13ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1370")
    OP_A2(0x0)

    ChrTalk(    #50
        0x8,
        (
            "Most folks who come here are\x01",
            "here to check out the scenery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "We also get the occasional\x01",
            "mountain climbers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "Used to be, we got all our\x01",
            "business from people going back\x01",
            "and forth between Ruan and Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13EA")

    label("loc_1370")


    ChrTalk(    #53
        0x8,
        (
            "How was the view from\x01",
            "the windmill?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "I never get tired of the sight\x01",
            "of the windmill and the blue\x01",
            "ocean together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13EA")

    Jump("loc_14F2")

    label("loc_13ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_1490")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1466")
    OP_A2(0x0)

    ChrTalk(    #55
        0x8,
        "Hey, weren't you here earlier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        "Is everything okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "A little boy?\x01",
            "Haven't seen him...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_148D")

    label("loc_1466")


    ChrTalk(    #58
        0x8,
        (
            "A little boy?\x01",
            "Haven't seen him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_148D")

    Jump("loc_14F2")

    label("loc_1490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_14F2")

    ChrTalk(    #59
        0x8,
        (
            "That windmill at the edge of town has\x01",
            "a platform with a fantastic view. (* Tentative)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F2")

    TalkEnd(0x8)
    Return()

    # Function_4_5EC end

    def Function_5_14F6(): pass

    label("Function_5_14F6")

    Call(0, 6)
    Return()

    # Function_5_14F6 end

    def Function_6_14FB(): pass

    label("Function_6_14FB")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155B")
    OP_0D()
    OP_A9(0x29)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_155B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156C")
    TalkEnd(0x9)
    Return()

    label("loc_156C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1604")

    ChrTalk(    #60
        0x9,
        (
            "I heard that the arsonist\x01",
            "was caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "I think he should experience some\x01",
            "street justice before he's turned\x01",
            "over to the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D1D")

    label("loc_1604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_164E")

    ChrTalk(    #62
        0x9,
        "How could this have happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        "I won't stand for this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D1D")

    label("loc_164E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F1")
    OP_A2(0x1)

    ChrTalk(    #64
        0x9,
        (
            "The orphans and Matron Theresa\x01",
            "are being well looked after,\x01",
            "never you fear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "We have to come together in\x01",
            "times of trouble, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1742")

    label("loc_16F1")


    ChrTalk(    #66
        0x9,
        (
            "The orphans and Matron Theresa\x01",
            "are being well looked after,\x01",
            "never you fear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1742")

    Jump("loc_1D1D")

    label("loc_1745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_17A1")

    ChrTalk(    #67
        0x9,
        "I think Clem just ran out of here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "I wonder what could be\x01",
            "the matter?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D1D")

    label("loc_17A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_197E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F5")
    OP_A2(0x1)

    ChrTalk(    #69
        0x9,
        (
            "Oh, that's a royal academy\x01",
            "uniform...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "Is your name Kloe,\x01",
            "by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x105,
        "#040FYes...why do you ask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        (
            "The children from the orphanage\x01",
            "talk about you a great deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "They're all upstairs in the\x01",
            "big room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        (
            "You should go and see them,\x01",
            "whenever you get the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x105,
        "#040FOh...I will. Pardon me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_197B")

    label("loc_18F5")


    ChrTalk(    #76
        0x9,
        (
            "The children from the orphanage\x01",
            "talk about you a great deal, Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "You should go and see them,\x01",
            "whenever you get the chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197B")

    Jump("loc_1D1D")

    label("loc_197E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1A71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A19")
    OP_A2(0x1)

    ChrTalk(    #78
        0x9,
        (
            "Okay...next up is getting the\x01",
            "laundry done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "Today's supposed to be sunny,\x01",
            "so I'll have no better chance\x01",
            "to dry the clothes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6E")

    label("loc_1A19")


    ChrTalk(    #80
        0x9,
        (
            "Today's supposed to be sunny,\x01",
            "so I'll have no better chance\x01",
            "to dry the clothes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6E")

    Jump("loc_1D1D")

    label("loc_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1BB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3D")
    OP_A2(0x1)

    ChrTalk(    #81
        0x9,
        (
            "The magnolias are blooming\x01",
            "in twos and threes again,\x01",
            "this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "This village has no particular specialties,\x01",
            "but we sometimes have some people who come\x01",
            "to see those flowers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAF")

    label("loc_1B3D")


    ChrTalk(    #83
        0x9,
        (
            "This village has no particular specialties,\x01",
            "but we sometimes have some people who come\x01",
            "to see those flowers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAF")

    Jump("loc_1D1D")

    label("loc_1BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_1C21")

    ChrTalk(    #84
        0x9,
        (
            "A little boy?\x01",
            "Nope, I haven't seen him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x9,
        (
            "I did see a girl from the royal\x01",
            "academy, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D1D")

    label("loc_1C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1D1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE9")
    OP_A2(0x1)

    ChrTalk(    #86
        0x9,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x9,
        (
            "Care for some food? We'd be happy\x01",
            "to have you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "I make it all myself, with the\x01",
            "help of my husband, and I'm quite\x01",
            "confident you'll love every bite!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D1D")

    label("loc_1CE9")


    ChrTalk(    #89
        0x9,
        (
            "Care for some food? We'd be happy\x01",
            "to have you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1D")

    TalkEnd(0x9)
    Return()

    # Function_6_14FB end

    def Function_7_1D21(): pass

    label("Function_7_1D21")

    TalkBegin(0x12)

    ChrTalk(    #90
        0xFE,
        (
            "The matron and the kids are\x01",
            "sleeping here. I'll keep watch\x01",
            "over them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "Please, find the scum who did\x01",
            "this, so we can all relax again.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_7_1D21 end

    def Function_8_1DB7(): pass

    label("Function_8_1DB7")

    TalkBegin(0x13)

    ChrTalk(    #92
        0xFE,
        (
            "Hmm... I don't know if we can\x01",
            "do much to help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "...but say the word and we're\x01",
            "here for you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_8_1DB7 end

    def Function_9_1E25(): pass

    label("Function_9_1E25")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_207F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_202F")
    OP_A2(0x4)

    ChrTalk(    #94
        0xFE,
        (
            "#750FOh, my...hello again.\x02\x03",

            "I heard that the criminals have\x01",
            "been arrested.\x02\x03",

            "You keep helping us so much and\x01",
            "I've no way to properly repay you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#000FYou really don't need to worry...\x01",
            "It's nothing to be embarrassed\x01",
            "over.\x02\x03",

            "Really...\x02\x03",

            "(Hmm...it's probably better not\x01",
            "to tell her everything, just yet.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        (
            "#010FWe're going back to Ruan for a little\x01",
            "bit, so we can deliver our report.\x02\x03",

            "Carna's keeping an eye on the\x01",
            "prisoners, so you can relax on\x01",
            "that score.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "#750FThank you so much...\x02",
    )

    CloseMessageWindow()
    Jump("loc_207C")

    label("loc_202F")


    ChrTalk(    #98
        0xFE,
        (
            "#750FYou keep helping us so much and\x01",
            "I've no way to properly repay you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_207C")

    Jump("loc_22A5")

    label("loc_207F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_20B7")

    AnonymousTalk(    #99
        "\x07\x05Matron Theresa is sleeping peacefully.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_22A5")

    label("loc_20B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2167")

    ChrTalk(    #100
        0xFE,
        (
            "#750FOh, hello...\x02\x03",

            "I'm truly indebted to you, for a\x01",
            "multitude of reasons...\x02\x03",

            "The Manorians greatly appreciate \x01",
            "all that you've done. We must\x01",
            "thank you properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A5")

    label("loc_2167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_22A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_223F")
    OP_A2(0x4)

    ChrTalk(    #101
        0xFE,
        (
            "#750FMary told me what happened.\x02\x03",

            "This is terrible... What an awful\x01",
            "thing for him to overhear...\x02\x03",

            "I beg of you...please, find Clem\x01",
            "and bring him back safely.\x02\x03",

            "I'll be right behind you soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A5")

    label("loc_223F")


    ChrTalk(    #102
        0xFE,
        (
            "#750FI beg of you...please, find Clem\x01",
            "and bring him back safely.\x02\x03",

            "I'll be right behind you soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A5")

    TalkEnd(0xFE)
    Return()

    # Function_9_1E25 end

    def Function_10_22A9(): pass

    label("Function_10_22A9")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2313")

    ChrTalk(    #103
        0xFE,
        (
            "#770FOh...hi, Miss Estelle!\x02\x03",

            "Did you really find those guys\x01",
            "and beat them up?\x02\x03",

            "Awesome!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2371")

    label("loc_2313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_2371")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #104
        0xFE,
        (
            "#773FMister Joshua...\x02\x03",

            "I hope I grow up to be as strong\x01",
            "as you, someday...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2371")

    TalkEnd(0xE)
    Return()

    # Function_10_22A9 end

    def Function_11_2375(): pass

    label("Function_11_2375")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_23D6")

    ChrTalk(    #105
        0xFE,
        (
            "The matron finally woke up,\x01",
            "earlier this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "Hee hee...thank Aidios.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2461")

    label("loc_23D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_2442")

    ChrTalk(    #107
        0xFE,
        (
            "Everyone's finally calmed down\x01",
            "a little bit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Now, if the matron would\x01",
            "just wake up...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2461")

    label("loc_2442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2461")

    ChrTalk(    #109
        0xFE,
        "Please, find Clem!\x02",
    )

    CloseMessageWindow()

    label("loc_2461")

    TalkEnd(0xC)
    Return()

    # Function_11_2375 end

    def Function_12_2465(): pass

    label("Function_12_2465")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_24A6")

    ChrTalk(    #110
        0xFE,
        (
            "Man...I'm so relieved.\x01",
            "Now I'm staaaaarving...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24EE")

    label("loc_24A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_24C5")

    ChrTalk(    #111
        0xFE,
        "*hic* *sniffle*\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EE")

    label("loc_24C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_24EE")

    ChrTalk(    #112
        0xFE,
        "What got Clem all worked up?\x02",
    )

    CloseMessageWindow()

    label("loc_24EE")

    TalkEnd(0xB)
    Return()

    # Function_12_2465 end

    def Function_13_24F2(): pass

    label("Function_13_24F2")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2521")

    ChrTalk(    #113
        0xFE,
        "Yaaaay! Matron's uppy again!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2593")

    label("loc_2521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_254D")

    ChrTalk(    #114
        0xFE,
        "Matron's gon'be okay, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2593")

    label("loc_254D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2593")

    ChrTalk(    #115
        0xFE,
        (
            "Clem din't say anyfing since\x01",
            "when we were eatin' puddin'.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2593")

    TalkEnd(0xD)
    Return()

    # Function_13_24F2 end

    def Function_14_2597(): pass

    label("Function_14_2597")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2611")

    ChrTalk(    #116
        0xFE,
        (
            "I'm guarding the donations until\x01",
            "the matron wakes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I won't fail this time.\x01",
            "You can count on me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_263D")

    label("loc_2611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_263D")

    AnonymousTalk(    #118
        "\x07\x05Carna is sleeping peacefully.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_263D")

    TalkEnd(0x11)
    Return()

    # Function_14_2597 end

    def Function_15_2641(): pass

    label("Function_15_2641")

    TalkBegin(0x14)

    ChrTalk(    #119
        0xFE,
        "I've gotta go cheer everyone up.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_15_2641 end

    def Function_16_266E(): pass

    label("Function_16_266E")

    EventBegin(0x0)
    OP_6D(-50180, 0, -790, 0)
    OP_6B(2800, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, -52390, 0, 510, 90)
    SetChrPos(0xB, -50850, 0, 180, 315)
    SetChrPos(0xD, -50850, 0, 1400, 225)
    SetChrPos(0xC, -50570, 0, -2840, 45)
    SetChrPos(0xE, -49420, 0, -2280, 225)
    SetChrPos(0x101, -46270, 0, -1540, 270)
    SetChrPos(0x102, -46100, 0, -760, 270)
    SetChrPos(0x136, -47050, 0, -1030, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #120
        0x136,
        "#043FMatron! Everyone...!\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xD, 255)
    OP_4A(0xC, 255)
    OP_4A(0xE, 255)

    def lambda_27FA():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_27FA)

    def lambda_2808():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2808)

    def lambda_2816():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2816)

    def lambda_2824():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2824)

    def lambda_2832():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2832)
    Sleep(400)

    ChrTalk(    #121
        0xE,
        "#774FMiss Kloe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        "You came!\x02",
    )

    CloseMessageWindow()

    def lambda_2869():
        OP_6D(-50670, 0, -380, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2869)

    def lambda_2881():
        OP_8F(0xFE, 0xFFFF41A6, 0x0, 0xFFFFFE8E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_2881)
    Sleep(100)

    def lambda_28A1():
        OP_8E(0xFE, 0xFFFF3DD2, 0x0, 0x21C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_28A1)
    Sleep(100)

    def lambda_28C1():
        OP_8E(0xFE, 0xFFFF3D5A, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_28C1)

    def lambda_28DC():
        OP_8E(0xFE, 0xFFFF3FD0, 0x0, 0xFFFFFB50, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_28DC)
    Sleep(100)

    def lambda_28FC():
        OP_8E(0xFE, 0xFFFF4322, 0x0, 0xFFFFFBD2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_28FC)
    WaitChrThread(0xE, 0x2)
    TurnDirection(0xE, 0x136, 400)

    ChrTalk(    #123
        0x136,
        "#042F#2PIs anyone hurt?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        "#1PWe're okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xD,
        "Heehee... I is okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x136,
        "#048F#2PThank goodness...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x4)
    OP_8E(0xA, 0xFFFF394A, 0x0, 0xB4, 0x7D0, 0x0)

    ChrTalk(    #127
        0xA,
        (
            "#750FHa ha... I'm glad you're here.\x02\x03",

            "#751FIs that Estelle and Joshua I see\x01",
            "with you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A02():

        label("loc_2A02")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2A02")

    QueueWorkItem2(0xA, 1, lambda_2A02)

    def lambda_2A13():

        label("loc_2A13")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_2A13")

    QueueWorkItem2(0xB, 1, lambda_2A13)

    def lambda_2A24():

        label("loc_2A24")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_2A24")

    QueueWorkItem2(0xD, 1, lambda_2A24)

    def lambda_2A35():

        label("loc_2A35")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_2A35")

    QueueWorkItem2(0xC, 1, lambda_2A35)

    def lambda_2A46():

        label("loc_2A46")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_2A46")

    QueueWorkItem2(0xE, 1, lambda_2A46)

    def lambda_2A57():

        label("loc_2A57")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_2A57")

    QueueWorkItem2(0x136, 1, lambda_2A57)

    def lambda_2A68():
        OP_8E(0xFE, 0xFFFF4124, 0x0, 0xFFFFF498, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A68)
    Sleep(500)

    def lambda_2A88():
        OP_8E(0xFE, 0xFFFF441C, 0x0, 0xFFFFF5F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2A88)
    WaitChrThread(0x101, 0x2)

    def lambda_2AA8():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AA8)
    WaitChrThread(0x102, 0x2)

    def lambda_2ABB():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2ABB)
    Sleep(500)
    OP_44(0xA, 0xFF)

    ChrTalk(    #128
        0x101,
        (
            "#000FYes, since someone contacted\x01",
            "the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x102,
        (
            "#010FWe're investigating the incident\x01",
            "and thought we'd stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xA,
        (
            "#750FI see... Thank you for taking\x01",
            "the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xE,
        (
            "#772F#2PInvestigating... You mean about\x01",
            "the fire, right?\x02\x03",

            "Do you know who did it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#003FUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x102,
        "#013FWell, how to put it...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #134
        "\x07\x05Estelle and Joshua exchanged awkward glances.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x136, 0x101, 400)
    OP_62(0x136, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x136)
    OP_44(0x136, 0xFF)
    TurnDirection(0x136, 0xB, 400)
    Sleep(200)
    TurnDirection(0x136, 0x102, 400)

    ChrTalk(    #135
        0x136,
        (
            "#040FSo, um, who's hungry?\x02\x03",

            "I missed breakfast, so I was\x01",
            "thinking about getting some\x01",
            "food.\x02\x03",

            "#041FGood boys and girls who join\x01",
            "me will get some sweet treats!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D32():

        label("loc_2D32")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_2D32")

    QueueWorkItem2(0x101, 1, lambda_2D32)

    def lambda_2D43():

        label("loc_2D43")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_2D43")

    QueueWorkItem2(0x102, 1, lambda_2D43)
    Sleep(50)

    def lambda_2D59():

        label("loc_2D59")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_2D59")

    QueueWorkItem2(0xA, 1, lambda_2D59)
    OP_44(0xB, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    Sleep(50)

    def lambda_2D7F():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2D7F)

    def lambda_2D8D():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2D8D)
    Sleep(50)

    def lambda_2DA0():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2DA0)

    def lambda_2DAE():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2DAE)

    ChrTalk(    #136
        0xB,
        "#1PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xD,
        "I's wants some puddin'!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xE,
        "#773F#3PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xC,
        "#1P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 400)

    ChrTalk(    #140
        0xC,
        "#1PC'mon, Clem!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xC, 400)

    ChrTalk(    #141
        0xE,
        "#774F#4PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xC,
        "#1PQuit griping and come on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xC,
        "#1PLet's go downstairs, Miss Kloe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x136,
        "#048FHa ha, okay.\x02",
    )

    CloseMessageWindow()
    OP_43(0x136, 0x2, 0x0, 0x11)
    OP_43(0xE, 0x2, 0x0, 0x12)
    OP_43(0xC, 0x2, 0x0, 0x13)
    OP_43(0xB, 0x2, 0x0, 0x14)
    OP_43(0xD, 0x2, 0x0, 0x15)

    def lambda_2EC8():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_2EC8)
    Sleep(600)

    def lambda_2EE8():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2EE8)
    Sleep(50)

    def lambda_2F08():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2F08)
    Sleep(200)

    def lambda_2F28():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2F28)
    Sleep(300)

    def lambda_2F48():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2F48)
    WaitChrThread(0x136, 0x1)
    SetChrFlags(0x136, 0x80)
    WaitChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    WaitChrThread(0xD, 0x1)
    SetChrFlags(0xD, 0x80)
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xA, 0xFF)

    ChrTalk(    #145
        0x101,
        (
            "#007FPhew... That was close.\x02\x03",

            "I really wouldn't want the\x01",
            "little kids to hear about\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x102,
        (
            "#015F#4PIndeed.\x02\x03",

            "#010FAlthough I get the feeling\x01",
            "that Mary understands at least\x01",
            "some of what's happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xA,
        (
            "#751FHa ha... Yes, isn't she great?\x01",
            "I'm happy to have her around.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 0)
    Sleep(300)

    ChrTalk(    #148
        0xA,
        (
            "#750FNow, you were saying...?\x02\x03",

            "Please, tell me what you can.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 0)
    Sleep(100)
    TurnDirection(0x102, 0xA, 0)

    ChrTalk(    #149
        0x102,
        "#012F#4PThanks for your understanding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#002FOkay, then...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -49200, 0, -1200, 0)
    SetChrPos(0x102, -50100, 0, -990, 45)
    SetChrPos(0xA, -49670, 0, 200, 180)
    OP_6D(-50810, 0, 340, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #151
        0x102,
        (
            "#012FFirst, we checked out where\x01",
            "the fire started...\x02\x03",

            "...and it does appear that it\x01",
            "was set deliberately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xA,
        (
            "#754F#2PMy suspicions were correct, then.\x02\x03",

            "I've always been very careful\x01",
            "about fire, so I suspected it\x01",
            "might be something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x102,
        (
            "#012FDo you have any idea who could\x01",
            "have done this?\x02\x03",

            "Whoever was responsible must have\x01",
            "had some kind of motivation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xA,
        (
            "#757F#2PI have no idea...\x02\x03",

            "We have no real money to speak\x01",
            "of, nor has anyone ever borne\x01",
            "a grudge against us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        (
            "#002FSo, it wasn't a robbery,\x01",
            "and it wasn't for revenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x102,
        (
            "#012FWe have to acknowledge the\x01",
            "possibility that someone did \x01",
            "it just for fun...\x02\x03",

            "Did you happen to notice anything\x01",
            "unusual leading up to or during\x01",
            "the incident?\x02\x03",

            "Any strange people hanging\x01",
            "around the orphanage, for\x01",
            "instance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xA,
        (
            "#756F#2PYes, actually...\x02\x03",

            "Not during the daytime when you\x01",
            "were there, but afterward...\x02\x03",

            "#757F...Though I can't imagine HE would\x01",
            "do something like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        "#002FWho's 'he'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xA,
        (
            "#754F#2PWhile we were trying to escape\x01",
            "from the burning building...\x02\x03",

            "...the beams fell in and blocked\x01",
            "our way through the entry hall.\x02\x03",

            "#750FBut then he showed up and\x01",
            "helped us all get free...\x02\x03",

            "We owe him our lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        (
            "#004FR-Really...\x02\x03",

            "Was he Manorian?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xA,
        (
            "#756F#2PRight after he helped us, he\x01",
            "called the villagers over and\x01",
            "left in the confusion.\x02\x03",

            "I asked the other villagers\x01",
            "about him, but no one seemed\x01",
            "to know anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x102,
        (
            "#012F...Sounds suspicious.\x02\x03",

            "What business would anyone\x01",
            "have around the orphanage at\x01",
            "such a late hour?\x02\x03",

            "Did you notice anything in\x01",
            "particular about him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xA,
        (
            "#750F#2PHe was a man, maybe in his\x01",
            "late twenties.\x02\x03",

            "He also had brilliant silver hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x102,
        "#014FSilver hair...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        (
            "#750F#2PHe had a troubled look about him,\x01",
            "though...that made him seem far\x01",
            "older than he looked.\x02\x03",

            "But he didn't strike me as\x01",
            "a bad man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#000FHe sounds suspicious,\x01",
            "but he did help you out.\x02\x03",

            "Doesn't sound like our guy\x01",
            "to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x102,
        "#014F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 300)

    ChrTalk(    #168
        0x101,
        (
            "#002F#4PJoshua?\x02\x03",

            "What's with the goofy stare?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 200)

    ChrTalk(    #169
        0x102,
        (
            "#013F#1POh, it's nothing...\x02\x03",

            "Perhaps he was just a bracer\x01",
            "who happened to pass by.\x02\x03",

            "#015FI think that we should\x01",
            "disregard him as a suspect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        "#002F#4PUm, okay...\x02",
    )

    CloseMessageWindow()
    OP_22(0x10, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #171
        0x136,
        "#1PPardon me...\x02",
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0x136, 0xA, 0)
    ClearChrFlags(0x136, 0x80)

    def lambda_3A74():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A74)

    def lambda_3A82():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3A82)

    def lambda_3A90():
        OP_6D(-49000, 0, -520, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A90)

    def lambda_3AA8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 3, lambda_3AA8)
    OP_8E(0x136, 0xFFFF4818, 0x0, 0xFFFFFCAE, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(    #172
        0x101,
        "#000FOh, hi, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x102,
        "#010FWhere are the children?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x136,
        (
            "#041FHa ha... They're downstairs,\x01",
            "having some dessert.\x02\x03",

            "#040FMatron Theresa...you have a guest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        "#753FHmm?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xF, -44560, 0, -1000, 0)
    SetChrPos(0x10, -44420, 0, -1440, 0)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xF, 0xA, 0)

    NpcTalk(    #176
        0xF,
        "A man's voice",
        "#1PPardon my intrusion.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x136, 0xFFFF44B2, 0x0, 0xFFFFF8D0, 0x7D0, 0x0)

    def lambda_3BFF():

        label("loc_3BFF")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3BFF")

    QueueWorkItem2(0x136, 1, lambda_3BFF)

    def lambda_3C10():

        label("loc_3C10")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3C10")

    QueueWorkItem2(0x101, 1, lambda_3C10)

    def lambda_3C21():

        label("loc_3C21")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3C21")

    QueueWorkItem2(0x102, 1, lambda_3C21)

    def lambda_3C32():

        label("loc_3C32")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_3C32")

    QueueWorkItem2(0xA, 1, lambda_3C32)
    ClearChrFlags(0xF, 0x80)

    def lambda_3C48():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_3C48)

    def lambda_3C5A():
        OP_8E(0xFE, 0xFFFF4926, 0x0, 0xFFFFFD76, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3C5A)
    Sleep(500)
    ClearChrFlags(0x10, 0x80)

    def lambda_3C7F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_3C7F)

    def lambda_3C91():
        OP_8E(0xFE, 0xFFFF4DD6, 0x0, 0xFFFFFA60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3C91)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #177
        0x101,
        "#004FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x102,
        "#014FMayor Dalmore...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xF,
        (
            "#660F#2POh, so the bracers I met\x01",
            "yesterday are here as well.\x02\x03",

            "Jean's reputation for responding\x01",
            "quickly is well-earned.\x02\x03",

            "#664FNow, then...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D6B():
        OP_8E(0xFE, 0xFFFF443A, 0x0, 0xFA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3D6B)
    Sleep(500)

    def lambda_3D8B():
        OP_8E(0xFE, 0xFFFF4796, 0x0, 0xFFFFFC68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3D8B)
    WaitChrThread(0xF, 0x1)
    TurnDirection(0xF, 0xA, 400)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #180
        0xF,
        (
            "#660F#4PIt's good to see you again,\x01",
            "Matron Theresa.\x02\x03",

            "After I heard what happened,\x01",
            "I came over as quickly as I could. \x02\x03",

            "I'm glad that you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        (
            "#750FThank you, Mayor.\x02\x03",

            "It's very kind of you to come\x01",
            "by. I know you're a very busy\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xF,
        (
            "#660F#4PNonsense... It is my responsibility\x01",
            "to look after all areas of the\x01",
            "region.\x02\x03",

            "#664FMore to the point, those who\x01",
            "did this must not be allowed\x01",
            "to get away with it.\x02\x03",

            "Joseph always loved that place...\x01",
            "Such an atrocity...\x02\x03",

            "#662FAllow me to express my most heartfelt\x01",
            "condolences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xA,
        (
            "#754FThank you...\x02\x03",

            "But I am sure that he would just be\x01",
            "relieved that the children are alive and well.\x02\x03",

            "#757FMy sole regret is that all my\x01",
            "mementos of him were lost to\x01",
            "the fire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x136,
        "#043FMatron Theresa...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 225, 300)

    ChrTalk(    #185
        0xF,
        (
            "#662FTell me, bracers. Have you any\x01",
            "thoughts on who might have\x01",
            "done this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x102,
        (
            "#012FWe've only just begun our\x01",
            "investigation, so it's too\x01",
            "early to say, sir.\x02\x03",

            "It does look like it might have\x01",
            "been done simply out of malice,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xF,
        (
            "#664FI see...\x01",
            "What a terrible thought.\x02\x03",

            "For something so heinous to happen\x01",
            "in such a peaceful place...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 315, 400)

    ChrTalk(    #188
        0x10,
        "#673FPardon me, Mayor...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(    #189
        0xF,
        "#660FHmm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x10,
        (
            "#671FDo you think that those people\x01",
            "might have a hand in this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xF,
        "#662F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#004FWhoa, hold up! Who do you\x01",
            "mean by 'those people'?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 300)

    ChrTalk(    #193
        0x10,
        (
            "#671FYou encountered them yesterday.\x02\x03",

            "The ruffians down in the\x01",
            "warehouse district of Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        "#002FOh, them...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x136,
        "#043F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x102,
        (
            "#012FPardon my bluntness...but what\x01",
            "makes you suspect them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x10,
        (
            "#671FThey've been openly defying the mayor for\x01",
            "quite some time now.\x02\x03",

            "They certainly seem to get their kicks out\x01",
            "of causing trouble for him.\x02\x03",

            "#673FAnd since he and Matron Theresa\x01",
            "are friends, it--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xF,
        "#665FGilbert!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 315, 400)

    ChrTalk(    #199
        0x10,
        "#676FS-Sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xF,
        (
            "#663FWild speculation does no\x01",
            "one any good.\x02\x03",

            "This is a dire offense. We must\x01",
            "have no false accusations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x10,
        (
            "#676FM-My apologies, sir.\x01",
            "That was foolish of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xF,
        (
            "#664FI think it would be best to\x01",
            "let the bracers identify and\x01",
            "locate the ones responsible.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 225, 400)

    ChrTalk(    #203
        0xF,
        "#660FCan I count on your help?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#006FSure! Leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        (
            "#010FWe will devote our full\x01",
            "attention to it, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xF,
        (
            "#661FGood, good.\x01",
            "I'm glad to hear it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xA, 400)
    Sleep(500)
    OP_8C(0x10, 270, 0)

    ChrTalk(    #207
        0xF,
        (
            "#660F#4PBy the way, Matron Theresa...\x01",
            "I do have one question to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xA,
        "#753FWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xF,
        (
            "#660F#4PWhat do you plan to do with\x01",
            "the orphanage now?\x02\x03",

            "Rebuilding will take time and\x01",
            "a not inconsiderable amount of\x01",
            "mira to complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xA,
        (
            "#757F...\x02\x03",

            "Honestly, I'm at a loss.\x02\x03",

            "We have a modest reserve of mira,\x01",
            "but the cost will be phenomenal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#003FMatron...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x136,
        "#043F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xF,
        (
            "#664F#4PI was afraid of that.\x02\x03",

            "#660FWell, I have a proposal of\x01",
            "sorts for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xA,
        "#750F...What might that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xF,
        (
            "#660F#4PAt the Dalmore estate in\x01",
            "Grancel, I have a villa.\x02\x03",

            "It's only used for special\x01",
            "occasions, so...\x02\x03",

            "What say you to having the\x01",
            "children stay there for a\x01",
            "little while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xA,
        "#753FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xF,
        (
            "#660F#4PAnd of course, charging rent\x01",
            "would be particularly boorish\x01",
            "of me.\x02\x03",

            "You'd be welcome to stay there\x01",
            "for as long as the rebuilding\x01",
            "process takes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xA,
        (
            "#757FB-But there's no need for\x01",
            "you to shoulder the burden\x01",
            "of our troubles...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xF,
        (
            "#661F#4PBut the villa sits unused.\x02\x03",

            "If you have misgivings, then I\x01",
            "will grant you control of the\x01",
            "grounds.\x02\x03",

            "Think of it as a well-deserved\x01",
            "reward, if you will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xA,
        (
            "#756FMayor...\x02\x03",

            "...\x02\x03",

            "#757FMay I have some time to think\x01",
            "it over?\x02\x03",

            "Your offer is most generous,\x01",
            "but I can barely process it\x01",
            "with everything going on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xF,
        (
            "#664F#4PPerfectly understandable.\x01",
            "You should get some rest.\x02\x03",

            "#660FI must be off as well.\x02\x03",

            "If you decide to accept,\x01",
            "please feel free to contact\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xA,
        "#750FI will... Thank you so very much.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(    #223
        0xF,
        "#660FLet us go, Gilbert.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)

    ChrTalk(    #224
        0x10,
        "#670FYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10, 0xFFFF4818, 0x0, 0xFFFFF9B6, 0x7D0, 0x0)
    OP_8C(0x10, 0, 400)

    def lambda_4C63():
        OP_8E(0xFE, 0xFFFF4F20, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4C63)
    WaitChrThread(0xF, 0x1)

    def lambda_4C83():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_4C83)

    def lambda_4C95():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4C95)
    Sleep(300)

    def lambda_4CB5():
        OP_8E(0xFE, 0xFFFF4F20, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4CB5)
    WaitChrThread(0x10, 0x1)

    def lambda_4CD5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_4CD5)

    def lambda_4CE7():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4CE7)
    WaitChrThread(0xF, 0x1)
    SetChrFlags(0xF, 0x80)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    Sleep(500)

    def lambda_4D1B():
        OP_6D(-49600, 0, -480, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D1B)
    Sleep(1000)

    ChrTalk(    #225
        0x101,
        (
            "#008FWow... That was a shock.\x02\x03",

            "He's certainly the generous type.\x01",
            "On par with Mayor Maybelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x102,
        (
            "#010FIndeed. Particularly in light\x01",
            "of his being a former noble.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x136, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x136)

    def lambda_4DF9():
        OP_6D(-49200, 0, 70, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4DF9)
    OP_44(0x136, 0xFF)
    OP_8E(0x136, 0xFFFF4354, 0x0, 0xFFFFFF9C, 0x7D0, 0x0)
    TurnDirection(0x136, 0xA, 400)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_4E3C():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E3C)

    def lambda_4E4A():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E4A)
    TurnDirection(0xA, 0x136, 400)

    ChrTalk(    #227
        0x136,
        (
            "#049FWhat do you intend to do in\x01",
            "regards to the mayor's offer,\x01",
            "Matron?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xA,
        (
            "#754FWell, what do you think of\x01",
            "the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x136,
        (
            "#049F...\x02\x03",

            "#049FConventional wisdom dictates\x01",
            "that you should accept it.\x02\x03",

            "However, once you've gone to\x01",
            "Grancel...\x02\x03",

            "#043FOh... Never mind me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xA,
        (
            "#750FHa ha... You always were such\x01",
            "a thoughtful child.\x02\x03",

            "It's all right. I want you to\x01",
            "give me your honest opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x136,
        (
            "#043F...\x02\x03",

            "#049FThe herb garden and the people\x01",
            "I care about would be gone...\x02\x03",

            "So... And...\x02\x03",

            "#047FWith you and Joseph gone,\x01",
            "I feel like all of my good\x01",
            "memories will fade away...\x02\x03",

            "I'm sorry... I'm just being\x01",
            "stupid and selfish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xA,
        (
            "#750FHa ha... I share your feelings.\x02\x03",

            "The orphanage is home to my\x01",
            "memories of him, as well as\x01",
            "the children's memories.\x02\x03",

            "But...though memories are precious,\x01",
            "having a place to live is of the\x01",
            "utmost importance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x136,
        "#049FYes, ma'am...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xA,
        (
            "#750FI believe this will all be\x01",
            "settled soon.\x02\x03",

            "Please, try to focus on tending\x01",
            "to the campus festival, for now.\x02\x03",

            "The children are really\x01",
            "looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x136,
        "#048F...Yes, ma'am.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 300)

    ChrTalk(    #236
        0xA,
        (
            "#750FEstelle and Joshua...\x02\x03",

            "I wish I could be of more\x01",
            "help, but I must leave the\x01",
            "investigation in your hands.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 0)
    Sleep(100)
    TurnDirection(0x102, 0xA, 0)

    ChrTalk(    #237
        0x102,
        "#010FWe will handle it, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        (
            "#006FWe're going to take the culprit\x01",
            "down! You can count on it!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_266E end

    def Function_17_5380(): pass

    label("Function_17_5380")

    Sleep(1500)
    OP_9F(0x136, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_17_5380 end

    def Function_18_5391(): pass

    label("Function_18_5391")

    Sleep(2000)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_18_5391 end

    def Function_19_53A2(): pass

    label("Function_19_53A2")

    Sleep(2500)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_19_53A2 end

    def Function_20_53B3(): pass

    label("Function_20_53B3")

    Sleep(3000)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_20_53B3 end

    def Function_21_53C4(): pass

    label("Function_21_53C4")

    Sleep(3500)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_21_53C4 end

    def Function_22_53D5(): pass

    label("Function_22_53D5")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-50180, 0, -790, 0)
    AddParty(0x5, 0xFF)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, -52430, 0, 480, 0)
    SetChrPos(0xB, -50850, 0, -1230, 270)
    SetChrPos(0xD, -51540, 0, -2430, 0)
    SetChrPos(0xC, -52530, 0, -2420, 0)
    SetChrPos(0xE, -50800, 0, 1470, 270)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrPos(0x101, -44330, 0, -1080, 270)
    SetChrPos(0x102, -44330, 0, -1080, 270)
    SetChrPos(0x105, -44330, 0, -1080, 270)
    SetChrPos(0x106, -44330, 0, -1080, 270)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x9, 255)
    OP_4A(0xB, 255)
    OP_4A(0xD, 255)
    OP_4A(0xC, 255)
    OP_4A(0xE, 255)
    SetChrFlags(0x106, 0x80)
    FadeToBright(1000, 0)
    OP_43(0x105, 0x1, 0x0, 0x19)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_43(0x101, 0x1, 0x0, 0x17)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_43(0x102, 0x1, 0x0, 0x18)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x11, 0x1)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_55C4():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_55C4)

    def lambda_55D2():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_55D2)

    def lambda_55E0():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_55E0)

    def lambda_55EE():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_55EE)

    def lambda_55FC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_55FC)

    ChrTalk(    #239
        0xE,
        "#775F#2POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xC,
        "Miss Kloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x105,
        "#043FEveryone...\x02",
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x0, 0x1A)
    OP_43(0xC, 0x1, 0x0, 0x1B)
    OP_43(0xE, 0x1, 0x0, 0x1C)
    OP_43(0xD, 0x1, 0x0, 0x1D)
    WaitChrThread(0xB, 0x1)
    OP_43(0x9, 0x1, 0x0, 0x1E)

    ChrTalk(    #242
        0xB,
        "Waaaahhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xD,
        "#1PIt was so scary!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x101,
        (
            "#008FThank goodness you're\x01",
            "all safe...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)

    def lambda_56C8():

        label("loc_56C8")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_56C8")

    QueueWorkItem2(0x102, 1, lambda_56C8)

    ChrTalk(    #245
        0x102,
        (
            "#012FPardon me, but what about the\x01",
            "others? How is Matron Theresa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x9,
        "Don't worry. They're not hurt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x9,
        (
            "They haven't woken up, though,\x01",
            "which has me a little worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x102,
        (
            "#015FIf I may, then, I'd like\x01",
            "to see them.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x102, 0x4)

    def lambda_57C5():

        label("loc_57C5")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_57C5")

    QueueWorkItem2(0x101, 1, lambda_57C5)

    def lambda_57D6():

        label("loc_57D6")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_57D6")

    QueueWorkItem2(0x105, 1, lambda_57D6)

    def lambda_57E7():

        label("loc_57E7")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_57E7")

    QueueWorkItem2(0xE, 1, lambda_57E7)

    def lambda_57F8():

        label("loc_57F8")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_57F8")

    QueueWorkItem2(0xC, 1, lambda_57F8)

    def lambda_5809():

        label("loc_5809")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_5809")

    QueueWorkItem2(0x9, 1, lambda_5809)
    OP_8E(0x102, 0xFFFF42DC, 0x0, 0x5A, 0x7D0, 0x0)
    OP_8E(0x102, 0xFFFF3F6C, 0x0, 0x3CA, 0x7D0, 0x0)

    def lambda_5842():
        OP_6D(-52260, 0, -520, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5842)
    OP_8E(0x102, 0xFFFF3896, 0x0, 0x226, 0x7D0, 0x0)
    OP_8E(0x102, 0xFFFF30EE, 0x0, 0x1F4, 0x7D0, 0x0)
    OP_8C(0x102, 0, 400)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_8C(0x102, 180, 400)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #249
        0x102,
        (
            "#013FNo doubt about it...\x01",
            "Someone used sleeping powder.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #250
        0x101,
        "#004FS-Sleeping powder?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #251
        0x102,
        (
            "#012FYes. There's still a faint\x01",
            "hint of it in the air.\x02\x03",

            "It's probably the kind without\x01",
            "side effects, so there's no real\x01",
            "need for concern...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(    #252
        0x101,
        "#009FHmm...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)

    def lambda_59EA():
        OP_6D(-50370, 0, -640, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_59EA)
    OP_8E(0x102, 0xFFFF3A80, 0x0, 0xF0, 0x7D0, 0x0)
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #253
        0x101,
        (
            "#002FHey, Clem. Can you tell us\x01",
            "what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xE,
        "#773F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #255
        0xC,
        "I'll tell you...\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)

    def lambda_5A80():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A80)

    def lambda_5A8E():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5A8E)
    Sleep(50)

    def lambda_5AA1():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5AA1)

    def lambda_5AAF():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5AAF)
    Sleep(50)

    def lambda_5AC2():
        TurnDirection(0xFE, 0xC, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AC2)

    def lambda_5AD0():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5AD0)
    Sleep(50)
    OP_44(0xE, 0xFF)
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(    #256
        0xC,
        (
            "#1PWe were walking along the coast\x01",
            "road with the bracer lady...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xC,
        (
            "#1P...and these strange guys in\x01",
            "masks showed up outta nowhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xC,
        (
            "#1PThe bracer lady fought them\x01",
            "for a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xC,
        "#1P...but they surrounded her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xC,
        (
            "#1PShe fought 'em to save us and\x01",
            "Matron Theresa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xC,
        "#1PThat's why...*sniffle*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        (
            "#003FThere, there... It must have\x01",
            "been so scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xE,
        (
            "#773FThey... They took an envelope\x01",
            "from the matron...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C9D():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C9D)
    Sleep(50)

    def lambda_5CB0():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5CB0)
    Sleep(50)

    def lambda_5CC3():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5CC3)
    Sleep(50)

    def lambda_5CD6():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5CD6)
    Sleep(50)
    TurnDirection(0x102, 0xE, 400)
    Sleep(500)

    ChrTalk(    #264
        0xE,
        (
            "#775FI wanted really bad to get\x01",
            "it back...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xE, 0xFF)
    TurnDirection(0xE, 0x102, 300)

    ChrTalk(    #265
        0xE,
        (
            "#777FMr. Joshua...\x01",
            "I couldn't help her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x102,
        (
            "#015F#1PDon't think that way, Clem.\x02\x03",

            "I know that Matron Theresa would\x01",
            "just be happy that all of you\x01",
            "are safe.\x02\x03",

            "#012FThat's why you mustn't blame\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xE,
        "#777FBut I... I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xC,
        "*sob*...*sniffle*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#005FI don't believe this! Who\x01",
            "would do such a thing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x105,
        "#047F#2P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #271
        0x105,
        (
            "#042F#2PWhoever it is...must certainly\x01",
            "be skilled at hiding his or her\x01",
            "presence.\x02\x03",

            "After all, the bracer wasn't\x01",
            "alerted, and Matron Theresa\x01",
            "is unconscious...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F27():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F27)

    def lambda_5F35():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5F35)

    def lambda_5F43():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5F43)
    TurnDirection(0xE, 0x105, 400)

    ChrTalk(    #272
        0x101,
        "#004FKloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x105,
        (
            "#042F#2PI get the feeling that this\x01",
            "was very deliberate.\x02\x03",

            "I'd say that the criminals were\x01",
            "probably targeting the donations\x01",
            "Matron Theresa had on her.\x02\x03",

            "If we find the money,\x01",
            "we'll find the culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x102,
        "#012F#1PYes, you're probably right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x101,
        (
            "#006FYou seem a little calmer\x01",
            "than earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x105,
        (
            "#043F#2PYes... In order to help the\x01",
            "matron and the kids, I must\x01",
            "compose myself.\x02\x03",

            "Regardless, we must find who\x01",
            "did this as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x106, -44560, 0, -1160, 0)
    TurnDirection(0x106, 0x105, 0)
    ClearChrFlags(0x106, 0x80)

    NpcTalk(    #277
        0x106,
        "A young man's voice",
        "#1PShe's right, you know.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x106, 15)

    def lambda_61C0():
        OP_6D(-49600, 0, -620, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_61C0)
    ClearChrFlags(0x106, 0x80)

    def lambda_61DD():
        OP_8E(0xFE, 0xFFFF4598, 0x0, 0xFFFFFD08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_61DD)

    def lambda_61F8():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_61F8)

    def lambda_6206():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6206)

    def lambda_6214():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6214)

    def lambda_6222():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6222)

    def lambda_6230():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6230)

    def lambda_623E():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_623E)

    def lambda_624C():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_624C)

    def lambda_625A():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_625A)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x106, 0x1)

    ChrTalk(    #278
        0x101,
        "#004FAaahh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x102,
        "#014FAgate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x106,
        (
            "#051FI heard what was going on\x01",
            "at the guild.\x02\x03",

            "Looks like you've gotten wrapped\x01",
            "up in one hell of a mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x101,
        (
            "#0005FHey! Don't make light of\x01",
            "the situation!\x02\x03",

            "Carna got hurt, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x106,
        (
            "#053FI know that...so quit your\x01",
            "yapping.\x02\x03",

            "#050FCarna's no amateur, either.\x01",
            "It'd take someone pretty\x01",
            "skilled to beat her.\x02\x03",

            "How about you give me a quick\x01",
            "rundown of what's been going\x01",
            "on here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x102,
        "#012FOkay...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #284
        (
            "\x07\x05Joshua and Estelle told Agate the whole story about the donations for the\x01",
            "orphanage.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #285
        0x106,
        (
            "#053FHuh... All right, then.\x01",
            "There's definitely something\x01",
            "weird going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x101,
        "#002FWeird how?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x106,
        (
            "#050FWell, here's the thing...\x02\x03",

            "You know that Raven gang that was\x01",
            "hanging out at the warehouse? They're\x01",
            "all gone now. Warehouse is empty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        (
            "#004FThen...\x02\x03",

            "#005FThey must be the ones who\x01",
            "assaulted Matron Theresa!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x102,
        (
            "#012FI'm not so sure about that.\x02\x03",

            "I really doubt they'd have what\x01",
            "it takes to get the upper hand\x01",
            "on Carna.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x101,
        (
            "#007FYeah, that's true...\x02\x03",

            "They talk a big game, but I\x01",
            "don't think they could back\x01",
            "it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x106,
        (
            "#057FYeah, give 'em a single hard\x01",
            "look and they shut right up. \x02\x03",

            "However, today they're suddenly\x01",
            "nowhere to be found.\x02\x03",

            "Couple that with today's little incident,\x01",
            "and what do you get? Like I said, something\x01",
            "weird is going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x102,
        (
            "#012FEven if they're not directly responsible\x01",
            "for the fire, I do feel like they're\x01",
            "involved, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x106,
        (
            "#050FYeah, but this ain't the time\x01",
            "to go checking that out.\x02\x03",

            "Come on, greenhorns.\x01",
            "Let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x101,
        (
            "#004FWhat are you talking about?\x02\x03",

            "#002FWhere are we going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x106,
        (
            "#053FYou slow in the head or something? \x01",
            "Obviously, we're going to the seaside\x01",
            "path where the crime happened.\x02\x03",

            "How those idiots did it\x01",
            "doesn't matter right now...\x02\x03",

            "#054FWe've gotta focus on finding some\x01",
            "clues as to where they are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x101,
        "#004FAh... True.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x102,
        "#012FUnderstood. We'll help.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_53D5 end

    def Function_23_69D7(): pass

    label("Function_23_69D7")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4070, 0x0, 0xFFFFFA6A, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_23_69D7 end

    def Function_24_69F8(): pass

    label("Function_24_69F8")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF430E, 0x0, 0xFFFFFD44, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_24_69F8 end

    def Function_25_6A19(): pass

    label("Function_25_6A19")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF3EA4, 0x0, 0xFFFFFE52, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_25_6A19 end

    def Function_26_6A3A(): pass

    label("Function_26_6A3A")

    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3C42, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_26_6A3A end

    def Function_27_6A68(): pass

    label("Function_27_6A68")

    Sleep(150)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3F8A, 0x0, 0xFFFFF7B8, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_27_6A68 end

    def Function_28_6A9B(): pass

    label("Function_28_6A9B")

    Sleep(100)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3F12, 0x0, 0x10E, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_28_6A9B end

    def Function_29_6ACE(): pass

    label("Function_29_6ACE")

    Sleep(50)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3D28, 0x0, 0xFFFFFAB0, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_29_6ACE end

    def Function_30_6B01(): pass

    label("Function_30_6B01")

    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    OP_8E(0x9, 0xFFFF3922, 0x0, 0x15E, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF3E4A, 0x0, 0x3F2, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF4336, 0x0, 0x35C, 0x7D0, 0x0)
    TurnDirection(0x9, 0x102, 400)
    Return()

    # Function_30_6B01 end

    SaveToFile()

Try(main)
