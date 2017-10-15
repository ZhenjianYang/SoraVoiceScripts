from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4215   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4215.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Head Cook Gervais',                    # 9
        'Folk',                                 # 10
        'Regis',                                # 11
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
        'ED6_DT07/CH01280 ._CH',             # 00
        'ED6_DT07/CH01520 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01280P._CP',             # 00
        'ED6_DT07/CH01520P._CP',             # 01
    )

    DeclNpc(
        X                   = -68800,
        Z                   = 0,
        Y                   = 73020,
        Direction           = 284,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -70370,
        Z                   = 0,
        Y                   = 69400,
        Direction           = 356,
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
        X                   = -70550,
        Z                   = 0,
        Y                   = 74650,
        Direction           = 173,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_182",          # 01, 1
        "Function_2_1A8",          # 02, 2
        "Function_3_468",          # 03, 3
        "Function_4_6F7",          # 04, 4
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_133")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_181")

    label("loc_133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_13D")
    Jump("loc_181")

    label("loc_13D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_147")
    Jump("loc_181")

    label("loc_147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_181")
    SetChrPos(0x8, -61660, 0, 68030, 87)
    SetChrPos(0x9, -70230, 0, 65550, 181)
    SetChrPos(0xA, -69850, 0, 77540, 273)

    label("loc_181")

    Return()

    # Function_0_11A end

    def Function_1_182(): pass

    label("Function_1_182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19E")
    OP_B1("t4215_y")
    Jump("loc_1A7")

    label("loc_19E")

    OP_B1("t4215_n")

    label("loc_1A7")

    Return()

    # Function_1_182 end

    def Function_2_1A8(): pass

    label("Function_2_1A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2CE")

    ChrTalk(    #0
        0xFE,
        (
            "It's true that you can cook up a\x01",
            "certain unique zest using coal fires\x01",
            "and fireplaces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "The problem, however, is that it takes\x01",
            "much longer to produce such fine flavors,\x01",
            "and I'm short on time as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I suspect any complex meals will\x01",
            "be out of my reach for some time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464")

    label("loc_2CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3E8")

    ChrTalk(    #3
        0xFE,
        (
            "There will be a party held to celebrate\x01",
            "the signing ceremony at the villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I'm currently whipping up a possible\x01",
            "menu for the buffet I'm planning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "On my honor as a chef, I shall serve the\x01",
            "best food I'm able to ensure that the signing\x01",
            "ceremony goes smoothly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464")

    label("loc_3E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_464")

    ChrTalk(    #6
        0xFE,
        (
            "Why, Your Highness Klaudia,\x01",
            "I see you are most well today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "May I ask what brings you\x01",
            "to my humble kitchen?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_464")

    TalkEnd(0xFE)
    Return()

    # Function_2_1A8 end

    def Function_3_468(): pass

    label("Function_3_468")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_50A")

    ChrTalk(    #8
        0xFE,
        (
            "The signing ceremony after-party\x01",
            "went over as well as it ever could!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "All parties were more than delighted\x01",
            "to partake in Mr. Gervais' food.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F3")

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_670")

    ChrTalk(    #10
        0xFE,
        (
            "We'll be heading out to the villa a\x01",
            "day in advance to start prepping the\x01",
            "food for the event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "There's going to be a lot of important\x01",
            "people, so we need to keep close track\x01",
            "of our ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Not only could food poisoning turn a motion\x01",
            "for peace into an international incident, it could\x01",
            "potentially stain Mr. Gervais' name as a chef.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F3")

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_6F3")

    ChrTalk(    #13
        0xFE,
        (
            "The head cook is incredible. It's crazy how\x01",
            "many recipes that guy knows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Maybe I can get him to teach me a few...\x02",
    )

    CloseMessageWindow()

    label("loc_6F3")

    TalkEnd(0xFE)
    Return()

    # Function_3_468 end

    def Function_4_6F7(): pass

    label("Function_4_6F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_796")

    ChrTalk(    #15
        0xFE,
        (
            "Warming or boiling water is easy\x01",
            "enough even with just plain ol' fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "It's not quite so easy to control fire\x01",
            "conjured from an orbment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91F")

    label("loc_796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_82B")

    ChrTalk(    #17
        0xFE,
        (
            "Let's see... I need to make sure\x01",
            "I don't miss anything crucial for\x01",
            "the food stocks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "We're gonna start gettin' reeeeal\x01",
            "busy soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91F")

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_91F")

    ChrTalk(    #19
        0xFE,
        (
            "Once we closed that door leadin' into\x01",
            "the sewers, we finally stopped gettin'\x01",
            "so many rats in our storehouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Really, the nerve they had to chew on\x01",
            "food that people put so much effort to\x01",
            "bring in! Nasty, nasty little creatures.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91F")

    TalkEnd(0xFE)
    Return()

    # Function_4_6F7 end

    SaveToFile()

Try(main)
