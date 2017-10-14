from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4134   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4134.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Sister Ellen',                         # 9
        'Archbishop Currant',                   # 10
        'Bishop Reval',                         # 11
        'Sister Noah',                          # 12
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
        'ED6_DT07/CH01410 ._CH',             # 00
        'ED6_DT07/CH01400 ._CH',             # 01
        'ED6_DT07/CH01670 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01410P._CP',             # 00
        'ED6_DT07/CH01400P._CP',             # 01
        'ED6_DT07/CH01670P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = -50,
        Z                   = 1000,
        Y                   = 20410,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2870,
        Z                   = 1000,
        Y                   = 18870,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -132010,
        Z                   = 0,
        Y                   = 6440,
        Direction           = 340,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclActor(
        TriggerX            = 200,
        TriggerZ            = 1000,
        TriggerY            = 17890,
        TriggerRange        = 400,
        ActorX              = -50,
        ActorZ              = 2500,
        ActorY              = 20410,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -74990,
        TriggerZ            = 0,
        TriggerY            = 66030,
        TriggerRange        = 800,
        ActorX              = -74990,
        ActorZ              = 1000,
        ActorY              = 66030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_18A",          # 00, 0
        "Function_1_18B",          # 01, 1
        "Function_2_19D",          # 02, 2
        "Function_3_1A2",          # 03, 3
        "Function_4_491",          # 04, 4
        "Function_5_4FD",          # 05, 5
        "Function_6_5A5",          # 06, 6
    )


    def Function_0_18A(): pass

    label("Function_0_18A")

    Return()

    # Function_0_18A end

    def Function_1_18B(): pass

    label("Function_1_18B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19C")

    Return()

    # Function_1_18B end

    def Function_2_19D(): pass

    label("Function_2_19D")

    Call(0, 3)
    Return()

    # Function_2_19D end

    def Function_3_1A2(): pass

    label("Function_3_1A2")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_463")
    TurnDirection(0x9, 0x109, 0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x9,
        "Oh, if it isn't Father Kevin!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        "What brings you here so late?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1060FArchbishop, has anything out\x01",
            "of the ordinary happened lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "No, I don't recall anything\x01",
            "particularly strange happening.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #5
        0x109,
        (
            "#1063FNo dice, Estelle.\x01",
            "Don't think it's around here\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)

    ChrTalk(    #6
        0x101,
        "#1002FY-Yeah, guess so.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x9, 400)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #7
        0x9,
        (
            "More importantly, Father Kevin.\x01",
            "I'd like to discuss something in\x01",
            "that report--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        (
            "#1064FAhh, sorry, sorry.\x02\x03",

            "#1066FWe've got ourselves a bit\x01",
            "of an urgent situation, so I've\x01",
            "gotta hurry on.\x02\x03",

            "I'll report later in detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        (
            "Take care, then. May you\x01",
            "receive good guidance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        "#1062FI appreciate it!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1645)
    Jump("loc_48D")

    label("loc_463")


    ChrTalk(    #12
        0x9,
        (
            "What is it?\x01",
            "Were you not in a hurry?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48D")

    TalkEnd(0x9)
    Return()

    # Function_3_1A2 end

    def Function_4_491(): pass

    label("Function_4_491")

    TalkBegin(0xFE)

    ChrTalk(    #13
        0xFE,
        (
            "We're open late in preparation\x01",
            "for the signing ceremony today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Is something troubling you?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_491 end

    def Function_5_4FD(): pass

    label("Function_5_4FD")

    TalkBegin(0xFE)

    ChrTalk(    #15
        0xFE,
        (
            "A sister's day begins and ends\x01",
            "with prayer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Morning and evening prayer both\x01",
            "take two hours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Ah, Goddess of the Sky, today,\x01",
            "too, has ended well...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_4FD end

    def Function_6_5A5(): pass

    label("Function_6_5A5")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #18
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_5A5 end

    SaveToFile()

Try(main)
