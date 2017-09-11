from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1300   ._SN',
        MapName             = 'Bose',
        Location            = 'T1300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1300   ._SN',
            'ED6_DT01/T1300_1 ._SN',
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
        'Private Cutinger',                     # 9
        'Sting',                                # 10
        'Hardt',                                # 11
        'Melvin',                               # 12
        'Camera',                               # 13
        'Private Usher',                        # 14
        'Private Mikey',                        # 15
        'Manoria Byroad',                       # 16
        'West Bose Highway',                    # 17
    )

    DeclEntryPoint(
        Unknown_00              = -42300,
        Unknown_04              = -500,
        Unknown_08              = 29000,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 225,
        Unknown_32              = 180,
        Unknown_34              = 270,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01620 ._CH',             # 01
        'ED6_DT07/CH01120 ._CH',             # 02
        'ED6_DT07/CH01760 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01620P._CP',             # 01
        'ED6_DT07/CH01120P._CP',             # 02
        'ED6_DT07/CH01760P._CP',             # 03
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -42500,
        Z                   = -50,
        Y                   = 16500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 99500,
        Z                   = -50,
        Y                   = 99500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -42500,
        Z                   = -50,
        Y                   = 16500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -42500,
        Z                   = -50,
        Y                   = 16500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -48000,
        Z                   = -50,
        Y                   = -10000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -47600,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -50220,
        Z                   = -500,
        Y                   = -35780,
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
        X                   = -40370,
        Z                   = -500,
        Y                   = 36990,
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


    DeclEvent(
        X                   = -51360,
        Y                   = -2000,
        Z                   = 11340,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = -51690,
        TriggerZ            = -470,
        TriggerY            = 23510,
        TriggerRange        = 1500,
        ActorX              = -51690,
        ActorZ              = 1800,
        ActorY              = 23510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -53780,
        TriggerZ            = -510,
        TriggerY            = -19530,
        TriggerRange        = 1500,
        ActorX              = -53780,
        ActorZ              = 1900,
        ActorY              = -19530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_252",          # 00, 0
        "Function_1_336",          # 01, 1
        "Function_2_38A",          # 02, 2
        "Function_3_3A0",          # 03, 3
        "Function_4_C54",          # 04, 4
        "Function_5_10D8",         # 05, 5
        "Function_6_1869",         # 06, 6
        "Function_7_1B49",         # 07, 7
        "Function_8_2126",         # 08, 8
        "Function_9_26CF",         # 09, 9
        "Function_10_2965",        # 0A, 10
        "Function_11_29F5",        # 0B, 11
        "Function_12_2A85",        # 0C, 12
    )


    def Function_0_252(): pass

    label("Function_0_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_26B")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_2B8")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_284")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_2B8")

    label("loc_284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_293")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_2B8")

    label("loc_293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2A2")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_2B8")

    label("loc_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2AC")
    Jump("loc_2B8")

    label("loc_2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2B8")
    ClearChrFlags(0x9, 0x80)

    label("loc_2B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30D")
    RemoveParty(0x34, 0xFF)
    SetMapFlags(0x400000)
    ClearChrFlags(0xA, 0x80)
    OP_6C(270000, 0)
    OP_6B(3400, 0)
    OP_6D(-44000, 0, 24400, 0)
    Event(1, 0)

    label("loc_30D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_319"),
        (SWITCH_DEFAULT, "loc_335"),
    )


    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_332")
    OP_B1("t1300_y")
    Event(0, 7)

    label("loc_332")

    Jump("loc_335")

    label("loc_335")

    Return()

    # Function_0_252 end

    def Function_1_336(): pass

    label("Function_1_336")

    OP_16(0x2, 0xFA0, 0xFFFD48B0, 0xFFFE17B8, 0x30044)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_360")
    OP_B1("t1300_y")
    Jump("loc_369")

    label("loc_360")

    OP_B1("t1300_n")

    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37A")
    OP_1B(0x3, 0x0, 0x9)

    label("loc_37A")

    OP_71(0x0, 0x10)
    OP_1C(0x0, 0x0, 0xC)
    OP_1C(0x1, 0x0, 0xC)
    Return()

    # Function_1_336 end

    def Function_2_38A(): pass

    label("Function_2_38A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_38A")

    label("loc_39F")

    Return()

    # Function_2_38A end

    def Function_3_3A0(): pass

    label("Function_3_3A0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_403")

    ChrTalk(    #0
        0xFE,
        (
            "I've still got time until I go\x01",
            "on duty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Maybe I should catch a\x01",
            "few winks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C50")

    label("loc_403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_58B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_528")
    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "Since this is the middle of the\x01",
            "mountains, it's really inconvenient\x01",
            "to get food brought up here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "We usually get our stuff delivered\x01",
            "from Bose or Ruan along the trail\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "And along with the deliverer's\x01",
            "own escort we have to go and\x01",
            "meet them along the way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_588")

    label("loc_528")


    ChrTalk(    #5
        0xFE,
        (
            "It gets really bad when it's the\x01",
            "middle of the winter and we've\x01",
            "got snow piled up to here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_588")

    Jump("loc_C50")

    label("loc_58B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_61F")

    ChrTalk(    #6
        0xFE,
        "It's almost time for training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "In light of the monsters attacking\x01",
            "the checkpoint, I need to get\x01",
            "myself ready for anything else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C50")

    label("loc_61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_7A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70B")
    OP_A2(0x0)

    ChrTalk(    #8
        0xFE,
        (
            "Hey there. Thanks again for your\x01",
            "help with the wolves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "You may be young, but you're bracers.\x01",
            "I should know better than to under-\x01",
            "estimate you guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "That was excellent work you\x01",
            "made of those monsters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A6")

    label("loc_70B")


    ChrTalk(    #11
        0xFE,
        (
            "You may be young, but you're bracers.\x01",
            "I should know better than to under-\x01",
            "estimate you guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "That was excellent work you\x01",
            "made of those monsters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A6")

    Jump("loc_C50")

    label("loc_7A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_86D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82A")
    OP_A2(0x0)

    ChrTalk(    #13
        0xFE,
        (
            "What's wrong? You're welcome to\x01",
            "go in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "If you feel like taking a rest, please\x01",
            "let the chief know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86A")

    label("loc_82A")


    ChrTalk(    #15
        0xFE,
        (
            "If you feel like taking a rest, please\x01",
            "let the chief know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86A")

    Jump("loc_C50")

    label("loc_86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_994")
    OP_A2(0x0)

    ChrTalk(    #16
        0xFE,
        (
            "It seems like nobody's been able\x01",
            "to figure out exactly where the\x01",
            "sky bandits really are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "The border garrison often comes\x01",
            "here to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "That's because the Bose region\x01",
            "is covered with mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "This area is the perfect place for\x01",
            "criminals to hide.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0E")

    label("loc_994")


    ChrTalk(    #20
        0xFE,
        (
            "That's because the Bose region\x01",
            "is covered with mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "This area is the perfect place for\x01",
            "criminals to hide.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0E")

    Jump("loc_C50")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_AC3")

    ChrTalk(    #22
        0xFE,
        (
            "It seems as though the missing\x01",
            "airliner was found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "However, since the criminals weren't\x01",
            "apprehended, these security checks\x01",
            "are going to continue for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C50")

    label("loc_AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_BA0")

    ChrTalk(    #24
        0xFE,
        (
            "Sky bandits, huh? Sounds like a\x01",
            "troublesome group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "However, this time General Morgan\x01",
            "is spearheading the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "It's only a matter of time until\x01",
            "he's got this bunch locked up\x01",
            "behind bars.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C50")

    label("loc_BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_C50")

    ChrTalk(    #27
        0xFE,
        "Are you heading to Ruan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "If that's the case, then you'll need\x01",
            "to fill out some paperwork inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "That's because we're in a state\x01",
            "of high alert right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C50")

    TalkEnd(0x8)
    Return()

    # Function_3_3A0 end

    def Function_4_C54(): pass

    label("Function_4_C54")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC9")
    OP_A2(0x35F)

    ChrTalk(    #30
        0x101,
        "#006F(Huh, who's this guy...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#010F(Umm, he looks like a bracer if\x01",
            "you ask me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#000FUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#002FHello? Is anybody there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#020FAs unfriendly as ever, aren't you,\x01",
            "Sting?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #37
        0xFE,
        (
            "Weren't you...that bracer in training\x01",
            "from some time ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        (
            "#020FYou got it.\x02\x03",

            "And thanks to you I can call\x01",
            "myself a senior bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Hmm...I almost didn't recognize you.\x01",
            "Do you have some work here at the\x01",
            "Bose branch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        "#020FAt the moment, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Right now we are dealing with a\x01",
            "number of incidents, so we're a\x01",
            "little shorthanded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Any help you could give us would\x01",
            "be useful.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)

    ChrTalk(    #43
        0x101,
        (
            "#002F(So he was one of Schera's acquaintances,\x01",
            "huh? He does seem like a bit of a scary\x01",
            "guy if you ask me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#010F(That may be so, but with the way he\x01",
            "carries himself...he looks pretty\x01",
            "capable as a bracer.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D4")

    label("loc_FC9")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #45
        0x103,
        (
            "#020FSo, Sting, has there been any\x01",
            "kind of trouble in this area?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "Oh, it's you, Scherazard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I came here to investigate since\x01",
            "we received some reports of\x01",
            "monsters unfamiliar to the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#020FWell, good work and good luck\x01",
            "with that.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)

    label("loc_10D4")

    TalkEnd(0x9)
    Return()

    # Function_4_C54 end

    def Function_5_10D8(): pass

    label("Function_5_10D8")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1133")

    ChrTalk(    #49
        0xFE,
        (
            "Everybody up here in the fort is\x01",
            "talking about the mayor being\x01",
            "arrested.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_1133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_1271")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11ED")
    OP_A2(0x8)

    ChrTalk(    #50
        0xFE,
        "It was my day to cook today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Then the warrant officer came and told\x01",
            "me to let him cook in my place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "That guy really likes cooking,\x01",
            "let me tell you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126E")

    label("loc_11ED")


    ChrTalk(    #53
        0xFE,
        (
            "The warrant officer just came and told\x01",
            "me to let him cook in my place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "That guy really likes cooking,\x01",
            "let me tell you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126E")

    Jump("loc_1865")

    label("loc_1271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1370")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131A")
    OP_A2(0x8)

    ChrTalk(    #55
        0xFE,
        (
            "The Bose region has been rather\x01",
            "quiet since the sky bandits were\x01",
            "apprehended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Well, I guess it's better than\x01",
            "an endless string of events.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136D")

    label("loc_131A")


    ChrTalk(    #57
        0xFE,
        (
            "The Bose region has been rather\x01",
            "quiet since the sky bandits were\x01",
            "apprehended.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136D")

    Jump("loc_1865")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1404")

    ChrTalk(    #58
        0xFE,
        (
            "Those monsters the other day were\x01",
            "a lot stronger than I imagined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Which means I'll have to train a\x01",
            "lot harder than I have been.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_1404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_14A0")

    ChrTalk(    #60
        0xFE,
        (
            "The attack on the checkpoint\x01",
            "last night was good practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "I guess I should be better prepared\x01",
            "for an emergency--both in body and\x01",
            "mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_14A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1537")

    ChrTalk(    #62
        0xFE,
        (
            "With the border garrison's investigation\x01",
            "carrying on this long, I'm sure they're\x01",
            "tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I hope they'll find some new leads\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_1537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1606")

    ChrTalk(    #64
        0xFE,
        (
            "This area is covered with mountains\x01",
            "and filled with monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Not to mention there are big,\x01",
            "vicious ones roaming around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Daily training is an essential\x01",
            "part of being a soldier here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_1606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1702")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169F")
    OP_A2(0x8)

    ChrTalk(    #67
        0xFE,
        (
            "This is due to the rugged terrain\x01",
            "which covers the Krone Range.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "The sky bandits may just be\x01",
            "hiding around here somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FF")

    label("loc_169F")


    ChrTalk(    #69
        0xFE,
        (
            "Which is why the border garrison\x01",
            "has already investigated this area\x01",
            "on multiple occasions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FF")

    Jump("loc_1865")

    label("loc_1702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D9")
    OP_A2(0x8)

    ChrTalk(    #70
        0xFE,
        (
            "On a normal day, we almost get\x01",
            "no travelers coming through the\x01",
            "steep pass here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "But now, with the airliners being\x01",
            "stopped, those in a hurry to get to\x01",
            "Ruan or Bose are making the trip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_17D9")


    ChrTalk(    #72
        0xFE,
        (
            "That said, I would tell anybody\x01",
            "to avoid trying to come through\x01",
            "this pass at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "It's way too dangerous for a\x01",
            "normal traveler.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1865")

    TalkEnd(0xD)
    Return()

    # Function_5_10D8 end

    def Function_6_1869(): pass

    label("Function_6_1869")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_18E5")

    ChrTalk(    #74
        0xFE,
        (
            "Is it true that the mayor of Ruan\x01",
            "was arrested?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Who knew that something like\x01",
            "that could ever happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B45")

    label("loc_18E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_1980")

    ChrTalk(    #76
        0xFE,
        (
            "The wound I got from that\x01",
            "monster has finally healed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "I guess I'm going to need to train\x01",
            "harder to make sure that never\x01",
            "happens again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B45")

    label("loc_1980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1A17")

    ChrTalk(    #78
        0xFE,
        "The warrant officer loves to cook.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Even when it's not his turn to cook,\x01",
            "there are times when he still makes\x01",
            "things in the kitchen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B45")

    label("loc_1A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1AB3")

    ChrTalk(    #80
        0xFE,
        "We're almost out of firewood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "After I finish my training today and\x01",
            "report back to the chief, I think\x01",
            "I'll go and gather some more wood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B45")

    label("loc_1AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_1AEB")

    ChrTalk(    #82
        0xFE,
        "Owowow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "That monster got me good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B45")

    label("loc_1AEB")


    ChrTalk(    #84
        0xFE,
        (
            "It's almost time for me to go\x01",
            "on duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "I'd better hurry up and eat\x01",
            "while I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B45")

    TalkEnd(0xE)
    Return()

    # Function_6_1869 end

    def Function_7_1B49(): pass

    label("Function_7_1B49")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, -43430, -550, 25300, 225)
    SetChrPos(0x102, -43600, -600, 26890, 225)
    OP_6D(-46560, -50, -15120, 0)
    OP_67(0, 5210, -10000, 0)
    OP_6B(5140, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_6D(-48090, -50, 16940, 8000)
    Fade(500)
    OP_6D(-44280, -480, 24940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 3)), scpexpr(EXPR_END)), "loc_1D46")

    ChrTalk(    #86
        0x101,
        (
            "#501F#1PMan, we finally made it up here.\x02\x03",

            "Once we pass through this checkpoint,\x01",
            "we're supposed to be in the Ruan\x01",
            "region, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#010FYep. That's supposed to be what's\x01",
            "on the other side.\x02\x03",

            "#013FBut unfortunately...it's almost\x01",
            "sundown.\x02\x03",

            "Maybe we should ask them to let\x01",
            "us stay here for the night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E75")

    label("loc_1D46")


    ChrTalk(    #88
        0x101,
        (
            "#501F#1PMan, it looks like we finally\x01",
            "made it.\x02\x03",

            "So is that building supposed to\x01",
            "be the checkpoint?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        (
            "#010FIt seems like it to me. Once we\x01",
            "pass through there, we'll be in\x01",
            "the Ruan region.\x02\x03",

            "#013FBut unfortunately...it's almost\x01",
            "sundown.\x02\x03",

            "Maybe we should ask them to let\x01",
            "us stay here for the night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E75")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #90
        0x101,
        (
            "#000F#1PI guess we could do that...\x02\x03",

            "But we've also got the option to hurry\x01",
            "down through the pass and rest at an\x01",
            "inn at the foot of the mountain, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #91
        0x102,
        (
            "#015FCrossing through the pass at night would\x01",
            "be dangerous. With our field of vision\x01",
            "limited, we would be on bad footing.\x02\x03",

            "There's also the possibility we\x01",
            "could fall off a cliff if we were\x01",
            "attacked by nocturnal monsters.\x02\x03",

            "#010FI wouldn't recommend it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #92
        0x101,
        (
            "#007F#1PYou're right. I guess it could be\x01",
            "pretty dangerous.\x02\x03",

            "It looks like all we can do is\x01",
            "explain our situation to the\x01",
            "soldiers at the checkpoint.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetMapFlags(0x1)
    Fade(1000)
    OP_6D(-43600, -554, 24000, 0)
    SetChrPos(0x0, -43600, -550, 26890, 180)
    SetChrPos(0x1, -43600, -550, 26890, 180)
    OP_0D()
    EventEnd(0x2)
    OP_A2(0x402)
    OP_1B(0x3, 0x0, 0x9)
    Return()

    # Function_7_1B49 end

    def Function_8_2126(): pass

    label("Function_8_2126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26CE")
    OP_A2(0x403)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    TurnDirection(0x0, 0x8, 0)
    TurnDirection(0x1, 0x8, 0)
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    ClearMapFlags(0x1)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xC, 0x3E8)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #93
        0x8,
        (
            "Well, this is unusual...\x01",
            "We don't get many travelers\x01",
            "at this hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "Did you get lost hiking along\x01",
            "the trail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#000FNo, not exactly.\x02\x03",

            "We're bracers, just so you know.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #96
        "\x07\x05Estelle showed the soldier her junior bracer emblem.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #97
        0x8,
        (
            "Wow, I'm surprised to see that\x01",
            "someone your age is a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        "So are you here with work then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        (
            "#010FNo, actually we're traveling around the\x01",
            "kingdom to become senior bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#006FAnd so we figured we'd travel\x01",
            "on foot to get in some training\x01",
            "instead of using an airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "You're going to travel around the\x01",
            "whole kingdom on foot?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "Maybe it has to do with being\x01",
            "young, but kids are certainly\x01",
            "fired up these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#006FTee hee, maybe that's a bit\x01",
            "of an overstatement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "But I'm going to have to tell you\x01",
            "that trying to head down through\x01",
            "the pass now would be suicide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "Recently, we've had an untold number\x01",
            "of monsters appearing in the area.\x01",
            "It's quite peculiar, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "We've got a rest stop for travelers,\x01",
            "so it would be best to stay there\x01",
            "for the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#001FSweet! Thanks a bunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x102,
        "#010FThis will really help us out a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        "Don't mention it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "Just talk to the chief warrant officer when\x01",
            "you're ready to hit the sack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "He's in the guard station,\x01",
            "straight ahead.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    OP_4B(0x8, 255)
    EventEnd(0x1)

    label("loc_26CE")

    Return()

    # Function_8_2126 end

    def Function_9_26CF(): pass

    label("Function_9_26CF")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2819")
    OP_A2(0xA)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27BC")

    ChrTalk(    #112
        0x102,
        (
            "#010FThe sun is setting and it would\x01",
            "be too dangerous to head back\x01",
            "to the highway.\x02\x03",

            "Let's explain the situation to the\x01",
            "soldiers and ask them to let us\x01",
            "stay here for the night.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #113
        0x101,
        "#000FGot it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2816")

    label("loc_27BC")


    ChrTalk(    #114
        0x102,
        (
            "#010FIt's already getting late. Let's spend\x01",
            "the night at the checkpoint's rest stop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2816")

    Jump("loc_293A")

    label("loc_2819")

    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28E0")

    ChrTalk(    #115
        0x102,
        (
            "#010FThe sun is setting and it would\x01",
            "be too dangerous to head back\x01",
            "to the highway.\x02\x03",

            "Let's explain the situation to the\x01",
            "soldiers and ask them to let us\x01",
            "stay here for the night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293A")

    label("loc_28E0")


    ChrTalk(    #116
        0x102,
        (
            "#010FIt's already getting late. Let's spend\x01",
            "the night at the checkpoint's rest stop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_293A")

    Fade(1000)
    SetChrPos(0x0, -43600, -550, 26890, 180)
    SetChrPos(0x1, -43600, -550, 26890, 180)
    OP_0D()
    EventEnd(0x2)
    Return()

    # Function_9_26CF end

    def Function_10_2965(): pass

    label("Function_10_2965")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #117
        (
            "\x07\x05Northeast: Bose City - 441 selge\x01",
            "Southwest: Ruan City - 669 selge\x01",
            "Manoria Village - 357 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_2965 end

    def Function_11_29F5(): pass

    label("Function_11_29F5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #118
        (
            "\x07\x05Southwest: Ruan City - 669 selge\x01",
            "Manoria Village - 357 selge\x01",
            "Northeast: Bose City - 441 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_29F5 end

    def Function_12_2A85(): pass

    label("Function_12_2A85")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_12_2A85 end

    SaveToFile()

Try(main)
