from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4213   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4213.x',
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
        'Captain Schwarz',                      # 9
        'Royal Guardsman',                      # 10
        'Royal Guardsman',                      # 11
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
        'ED6_DT27/CH03580 ._CH',             # 00
        'ED6_DT07/CH01320 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT27/CH03580P._CP',             # 00
        'ED6_DT07/CH01320P._CP',             # 01
    )

    DeclNpc(
        X                   = 74150,
        Z                   = 0,
        Y                   = -35040,
        Direction           = 90,
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
        X                   = 64650,
        Z                   = 0,
        Y                   = -33590,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 70330,
        Z                   = 0,
        Y                   = -41620,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_14F",          # 01, 1
        "Function_2_175",          # 02, 2
        "Function_3_199",          # 03, 3
        "Function_4_1BD",          # 04, 4
        "Function_5_734",          # 05, 5
        "Function_6_917",          # 06, 6
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_12E")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_14E")

    label("loc_12E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_138")
    Jump("loc_14E")

    label("loc_138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_147")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_14E")

    label("loc_147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_14E")

    label("loc_14E")

    Return()

    # Function_0_11A end

    def Function_1_14F(): pass

    label("Function_1_14F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16B")
    OP_B1("t4213_y")
    Jump("loc_174")

    label("loc_16B")

    OP_B1("t4213_n")

    label("loc_174")

    Return()

    # Function_1_14F end

    def Function_2_175(): pass

    label("Function_2_175")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_198")
    OP_8D(0xFE, 62680, -31070, 69060, -36680, 2000)
    Jump("Function_2_175")

    label("loc_198")

    Return()

    # Function_2_175 end

    def Function_3_199(): pass

    label("Function_3_199")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BC")
    OP_8D(0xFE, 65860, -37440, 73950, -46540, 2000)
    Jump("Function_3_199")

    label("loc_1BC")

    Return()

    # Function_3_199 end

    def Function_4_1BD(): pass

    label("Function_4_1BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_730")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D9")

    ChrTalk(    #0
        0x8,
        "#173FPrincess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1008FYou and the Royal Guard really saved\x01",
            "our butts this time, Julia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#171FIt was all thanks to Colonel Cid's\x01",
            "swift and appropriate judgment.\x02\x03",

            "#176FAnd if Father Kevin hadn't been there,\x01",
            "it still might have been Kanone's win.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1002FCaptain Amalthea over at Leiston Fortress\x01",
            "now, right?\x02\x03",

            "I've heard that she's willing to talk about\x01",
            "Renne and the society...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#170FIf you want to know about Kanone, I can\x01",
            "tell you she understands the severity of\x01",
            "the situation and her own role in this.\x02\x03",

            "All she needs is the right chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1011FYou must know Captain Amalthea pretty well,\x01",
            "Julia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#170FShe was a rival, but our rivalry was one where\x01",
            "we brought out the best of each other back in\x01",
            "the military academy.\x02\x03",

            "I don't think that changed even after I went\x01",
            "to the Royal Guard, and she was assigned\x01",
            "to the Intelligence Division.\x02\x03",

            "#176FThinking about it, I may be who I am now\x01",
            "because of her.\x02\x03",

            "#178FI...don't think that something like this settles\x01",
            "things between us at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x105,
        "#042FJulia...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1668)
    Jump("loc_730")

    label("loc_5D9")


    ChrTalk(    #8
        0x8,
        (
            "#170FStill, though, this 'society.'\x02\x03",

            "#176FThe abilities of their Enforcers is one thing,\x01",
            "but to have the technological capability to make\x01",
            "something like that giant mechanized doll...\x02\x03",

            "#170FOur enemies are far more powerful than we'd\x01",
            "thought.\x02\x03",

            "I can hardly say I was underestimating them,\x01",
            "but clearly I need to revise how I perceive them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_730")

    TalkEnd(0xFE)
    Return()

    # Function_4_1BD end

    def Function_5_734(): pass

    label("Function_5_734")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7C7")

    ChrTalk(    #9
        0xFE,
        "Is it true there was a dragon in Bose?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "The army's airships fighting a dragon...\x01",
            "That sounds like one for the history books.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_913")

    label("loc_7C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_877")

    ChrTalk(    #11
        0xFE,
        (
            "Those Intelligence Division types, developing\x01",
            "something like that in secret...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "If the captain hadn't come, who knows\x01",
            "what would've happened to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_913")

    label("loc_877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_913")

    ChrTalk(    #13
        0xFE,
        "I'm afraid Captain Schwarz isn't here right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "She is currently stationed at Leiston Fortress\x01",
            "for the changing of the Arseille's engine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_913")

    TalkEnd(0xFE)
    Return()

    # Function_5_734 end

    def Function_6_917(): pass

    label("Function_6_917")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A12")

    ChrTalk(    #15
        0xFE,
        (
            "Even for the Royal Guard, to be unable to use\x01",
            "our guns drops our ability to fight to almost\x01",
            "nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "If the Empire attacked at a time like this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "...Oh, wait. I guess the Empire wouldn't\x01",
            "be able to use their guns, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2F")

    label("loc_A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_AAA")

    ChrTalk(    #18
        0xFE,
        (
            "The commander used to be some\x01",
            "amazingly skilled man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "He was called the Demon Commander...\x01",
            "Makes you wonder what kind of man he\x01",
            "was.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2F")

    label("loc_AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_B2F")

    ChrTalk(    #20
        0xFE,
        (
            "To think that the already state-of-the-art\x01",
            "Arseille can go even further...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "I wonder what kind of ship it'll become.\x02",
    )

    CloseMessageWindow()

    label("loc_B2F")

    TalkEnd(0xFE)
    Return()

    # Function_6_917 end

    SaveToFile()

Try(main)
