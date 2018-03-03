from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4120   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4120.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Chaeli',                               # 9
        'Shepard',                              # 10
        'Zacharias',                            # 11
        'Tom',                                  # 12
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH01140 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01043 ._CH',             # 03
        'ED6_DT07/CH01680 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01140P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01043P._CP',             # 03
        'ED6_DT07/CH01680P._CP',             # 04
    )

    DeclNpc(
        X                   = 1260,
        Z                   = 0,
        Y                   = -240,
        Direction           = 236,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 129840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58580,
        Z                   = 0,
        Y                   = 360,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 120030,
        Z                   = 0,
        Y                   = -1260,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = -10,
        TriggerZ            = 0,
        TriggerY            = -1600,
        TriggerRange        = 800,
        ActorX              = 1260,
        ActorZ              = 1500,
        ActorY              = -240,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60410,
        TriggerZ            = 0,
        TriggerY            = 390,
        TriggerRange        = 800,
        ActorX              = 58580,
        ActorZ              = 1500,
        ActorY              = 360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 119960,
        TriggerZ            = 0,
        TriggerY            = 650,
        TriggerRange        = 800,
        ActorX              = 120030,
        ActorZ              = 1500,
        ActorY              = -1260,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BE",          # 00, 0
        "Function_1_1F0",          # 01, 1
        "Function_2_21E",          # 02, 2
        "Function_3_242",          # 03, 3
        "Function_4_247",          # 04, 4
        "Function_5_4EF",          # 05, 5
        "Function_6_4F4",          # 06, 6
        "Function_7_733",          # 07, 7
        "Function_8_738",          # 08, 8
        "Function_9_9CA",          # 09, 9
    )


    def Function_0_1BE(): pass

    label("Function_0_1BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1D4")
    Jump("loc_1EF")

    label("loc_1D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1DE")
    Jump("loc_1EF")

    label("loc_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1E8")
    Jump("loc_1EF")

    label("loc_1E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1EF")

    label("loc_1EF")

    Return()

    # Function_0_1BE end

    def Function_1_1F0(): pass

    label("Function_1_1F0")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_B1("t4120_n")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21D")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)

    label("loc_21D")

    Return()

    # Function_1_1F0 end

    def Function_2_21E(): pass

    label("Function_2_21E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_241")
    OP_8D(0xFE, 1470, 131290, -1690, 128210, 2000)
    Jump("Function_2_21E")

    label("loc_241")

    Return()

    # Function_2_21E end

    def Function_3_242(): pass

    label("Function_3_242")

    Call(0, 4)
    Return()

    # Function_3_242 end

    def Function_4_247(): pass

    label("Function_4_247")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_254")
    Jump("loc_4EB")

    label("loc_254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_38F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2E7")

    ChrTalk(    #0
        0x12,
        (
            "If you're looking for Tom, he's up on the third\x01",
            "floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x12,
        (
            "Why not go see him? He offers his own special\x01",
            "services up there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C")

    label("loc_2E7")


    ChrTalk(    #2
        0x12,
        "Tom's got a way with his fingers, you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x12,
        "He can mend orbments and the like in a flash.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x12,
        (
            "He just seems to have a natural talent for it,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_38C")

    Jump("loc_4EB")

    label("loc_38F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_399")
    Jump("loc_4EB")

    label("loc_399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_4EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_42C")

    ChrTalk(    #5
        0x12,
        (
            "If you're looking for Tom, he's up on the third\x01",
            "floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x12,
        (
            "Why not go see him? He offers his own special\x01",
            "services up there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EB")

    label("loc_42C")


    ChrTalk(    #7
        0x12,
        (
            "I started this shop with my friend who I go way\x01",
            "back with, Tom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x12,
        (
            "He's got the technical expertise, and I've got the\x01",
            "management expertise. Together, I'm sure we'll\x01",
            "make this work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4EB")

    TalkEnd(0x12)
    Return()

    # Function_4_247 end

    def Function_5_4EF(): pass

    label("Function_5_4EF")

    Call(0, 6)
    Return()

    # Function_5_4EF end

    def Function_6_4F4(): pass

    label("Function_6_4F4")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_501")
    Jump("loc_72F")

    label("loc_501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_5FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5AA")

    ChrTalk(    #9
        0x10,
        (
            "My husband and I only got married recently,\x01",
            "as it so happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "Heehee. He might not talk much, but that's\x01",
            "part of why I find him kind of cool.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA")

    label("loc_5AA")


    ChrTalk(    #11
        0x10,
        "La la laaa... La la laaaaaa... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        "Oh, hello! Welcome to our store!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_5FA")

    Jump("loc_72F")

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_607")
    Jump("loc_72F")

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_72F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6C9")

    ChrTalk(    #13
        0x10,
        (
            "All my husband does is stay in the back and\x01",
            "deal with stock. He never comes out to sell\x01",
            "anything at the counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "So I'll just have to handle things here in his\x01",
            "place!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F")

    label("loc_6C9")


    ChrTalk(    #15
        0x10,
        "Welcome to our store!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "Have a look around, and let me know if something\x01",
            "catches your eye!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_72F")

    TalkEnd(0x10)
    Return()

    # Function_6_4F4 end

    def Function_7_733(): pass

    label("Function_7_733")

    Call(0, 8)
    Return()

    # Function_7_733 end

    def Function_8_738(): pass

    label("Function_8_738")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_745")
    Jump("loc_9C6")

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_867")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7E0")

    ChrTalk(    #17
        0x13,
        (
            "If not for Zacharias, there's no way I would've\x01",
            "even dreamed of opening a shop like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x13,
        "I owe him a hell of a lot, that I do.\x02",
    )

    CloseMessageWindow()
    Jump("loc_864")

    label("loc_7E0")


    ChrTalk(    #19
        0x13,
        "Starting this shop up was all Zacharias' idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x13,
        (
            "He said it was a good idea to actually get to \x01",
            "see my customers' faces.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_864")

    Jump("loc_9C6")

    label("loc_867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_871")
    Jump("loc_9C6")

    label("loc_871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_9C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_92C")

    ChrTalk(    #21
        0x13,
        (
            "I-I'm kind of bad at dealing with customers,\x01",
            "you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x13,
        (
            "They make me really nervous... All I want to do\x01",
            "is mess with orbments without having to talk to\x01",
            "anyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C6")

    label("loc_92C")


    ChrTalk(    #23
        0x13,
        "W-Welcome...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x13,
        (
            "Umm... This is the counter where I handle \x01",
            "repairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x13,
        (
            "If you have any orbments that need fixing, \x01",
            "I can repair them for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_9C6")

    TalkEnd(0x13)
    Return()

    # Function_8_738 end

    def Function_9_9CA(): pass

    label("Function_9_9CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_9D7")
    Jump("loc_C3D")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_B0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A45")

    ChrTalk(    #26
        0xFE,
        (
            "I do feel bad about leaving everything at the\x01",
            "front to my wife, but what else can I do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B08")

    label("loc_A45")


    ChrTalk(    #27
        0xFE,
        (
            "I always seem to end up leaving manning the \x01",
            "front counter to my wife...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "She doesn't seem to mind as such, but it doesn't\x01",
            "stop me from feeling bad. We've only just gotten\x01",
            "married...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_B08")

    Jump("loc_C3D")

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_B15")
    Jump("loc_C3D")

    label("loc_B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_C3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B95")

    ChrTalk(    #29
        0xFE,
        (
            "If you want to buy anything, go and speak to my\x01",
            "wife at the counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "She'll be happy to sell to you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C3D")

    label("loc_B95")


    ChrTalk(    #31
        0xFE,
        "...Welcome to our store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "If you're looking to buy something, though,\x01",
            "you should head back up the stairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "My wife's manning the counter at the moment.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_C3D")

    TalkEnd(0xFE)
    Return()

    # Function_9_9CA end

    SaveToFile()

Try(main)
