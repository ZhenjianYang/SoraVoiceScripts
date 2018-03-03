from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3132   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Martina',                              # 9
        'Emma',                                 # 10
        'Dodge',                                # 11
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
        'ED6_DT07/CH01210 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01210 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01210P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01210P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
    )

    DeclNpc(
        X                   = -1700,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 192,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 68290,
        Z                   = 0,
        Y                   = 91600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 68100,
        Z                   = 0,
        Y                   = 56310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -1290,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = -1700,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4000,
        TriggerZ            = 0,
        TriggerY            = 4000,
        TriggerRange        = 800,
        ActorX              = -4000,
        ActorZ              = 1000,
        ActorY              = 4000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_172",          # 00, 0
        "Function_1_18E",          # 01, 1
        "Function_2_18F",          # 02, 2
        "Function_3_1B3",          # 03, 3
        "Function_4_1B8",          # 04, 4
        "Function_5_407",          # 05, 5
        "Function_6_606",          # 06, 6
        "Function_7_7C9",          # 07, 7
    )


    def Function_0_172(): pass

    label("Function_0_172")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_18D")

    Return()

    # Function_0_172 end

    def Function_1_18E(): pass

    label("Function_1_18E")

    Return()

    # Function_1_18E end

    def Function_2_18F(): pass

    label("Function_2_18F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B2")
    OP_8D(0xFE, 67200, 90290, 68610, 92730, 2000)
    Jump("Function_2_18F")

    label("loc_1B2")

    Return()

    # Function_2_18F end

    def Function_3_1B3(): pass

    label("Function_3_1B3")

    Call(0, 4)
    Return()

    # Function_3_1B3 end

    def Function_4_1B8(): pass

    label("Function_4_1B8")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_403")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2BC")

    ChrTalk(    #0
        0x10,
        (
            "We've been getting an increasing number\x01",
            "of guests from Calvard lately, which is great\x01",
            "news for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "...but the way Emma's been behaving lately,\x01",
            "I can't help but worry she'll do something\x01",
            "stupid and drive them away. I hope not...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_403")

    label("loc_2BC")


    ChrTalk(    #2
        0x10,
        (
            "I was in the linen room earlier, and I was\x01",
            "weirdly...shocked by what I found there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "Someone has hidden a disturbing number\x01",
            "of lamps under the shelves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        "...I know who's responsible, too. It's that Emma.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "What in Aidios' name possessed her to buy THAT\x01",
            "many of them? What are we ever going to need \x01",
            "them for?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_403")

    TalkEnd(0x10)
    Return()

    # Function_4_1B8 end

    def Function_5_407(): pass

    label("Function_5_407")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_602")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4CA")

    ChrTalk(    #6
        0xFE,
        (
            "Now, even if we can't turn the regular lights on,\x01",
            "we'll have a massive supply of lamps to light the\x01",
            "rooms. It's perfect!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "I can focus on my work without any worries!\x02",
    )

    CloseMessageWindow()
    Jump("loc_602")

    label("loc_4CA")


    ChrTalk(    #8
        0xFE,
        (
            "Ever since that time when I couldn't turn on the\x01",
            "orbal lamps in here, I've been worried about the\x01",
            "same thing happening again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "...so I decided to make sure it couldn't by buying\x01",
            "every single lamp I could get my hands on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Now I'll never have to worry about that\x01",
            "happening ever again! ...Right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_602")

    TalkEnd(0xFE)
    Return()

    # Function_5_407 end

    def Function_6_606(): pass

    label("Function_6_606")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_7C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6D0")

    ChrTalk(    #11
        0xFE,
        (
            "So far, I haven't run into any trouble while\x01",
            "I've been here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "My business talks have been going well, too...\x01",
            "Maybe this trip will be a little more successful\x01",
            "than the last?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C5")

    label("loc_6D0")


    ChrTalk(    #13
        0xFE,
        (
            "I make a living buying orbments, and this isn't\x01",
            "my first time coming here to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Last time I did, all the power in the town went\x01",
            "off, unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "So I ended up going back empty handed...\x01",
            "I hope nothing happens this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_7C5")

    TalkEnd(0xFE)
    Return()

    # Function_6_606 end

    def Function_7_7C9(): pass

    label("Function_7_7C9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #16
        (
            "\x07\x05Linen Room\x01\x09\x09\x09\x09",
            "※Employees Only\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_7C9 end

    SaveToFile()

Try(main)
