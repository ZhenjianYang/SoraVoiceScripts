from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4214   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4214.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Head Maid Hilda',                      # 9
        'Shea',                                 # 10
        'Primrose',                             # 11
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02540 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02540P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
    )

    DeclNpc(
        X                   = 68000,
        Z                   = 0,
        Y                   = 69570,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 72500,
        Z                   = 0,
        Y                   = 67450,
        Direction           = 90,
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
        X                   = 66670,
        Z                   = 0,
        Y                   = 99650,
        Direction           = 12,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_169",          # 01, 1
        "Function_2_18F",          # 02, 2
        "Function_3_30C",          # 03, 3
        "Function_4_330",          # 04, 4
        "Function_5_670",          # 05, 5
        "Function_6_ED7",          # 06, 6
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_136")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_168")

    label("loc_136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_14A")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_168")

    label("loc_14A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_154")
    Jump("loc_168")

    label("loc_154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_168")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168")
    SetChrFlags(0x8, 0x80)

    label("loc_168")

    Return()

    # Function_0_122 end

    def Function_1_169(): pass

    label("Function_1_169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_185")
    OP_B1("t4214_y")
    Jump("loc_18E")

    label("loc_185")

    OP_B1("t4214_n")

    label("loc_18E")

    Return()

    # Function_1_169 end

    def Function_2_18F(): pass

    label("Function_2_18F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2F6")

    label("loc_1B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2F6")

    label("loc_1CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2F6")

    label("loc_1E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FF")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2F6")

    label("loc_1FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_218")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2F6")

    label("loc_218")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_231")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2F6")

    label("loc_231")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2F6")

    label("loc_24A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_263")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2F6")

    label("loc_263")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2F6")

    label("loc_27C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_295")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2F6")

    label("loc_295")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2F6")

    label("loc_2AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2F6")

    label("loc_2C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E0")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2F6")

    label("loc_2E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F6")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2F6")

    label("loc_30B")

    Return()

    # Function_2_18F end

    def Function_3_30C(): pass

    label("Function_3_30C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32F")
    OP_8D(0xFE, 66030, 72430, 70230, 65960, 2000)
    Jump("Function_3_30C")

    label("loc_32F")

    Return()

    # Function_3_30C end

    def Function_4_330(): pass

    label("Function_4_330")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_5E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 7)), scpexpr(EXPR_END)), "loc_408")

    ChrTalk(    #0
        0xFE,
        (
            "#0713FTo Kanone, the colonel truly was everything.\x02\x03",

            "#0710FAs a fellow woman, I can empathize with\x01",
            "her actions and her feelings.\x02\x03",

            "#0714FNow we must wait for the queen to provide\x01",
            "her sanction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E4")

    label("loc_408")


    ChrTalk(    #1
        0xFE,
        (
            "#0712FLady Klaudia, Estelle...\x02\x03",

            "#0710FThat letter was no mere prank, was it?\x02\x03",

            "To think the former Intelligence Division\x01",
            "was involved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1007FYeah, really.\x02\x03",

            "#1015FI didn't think it'd come to fighting\x01",
            "Captain Amalthea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "#0713FTo Kanone, the colonel truly was everything.\x02\x03",

            "#0710FAs a fellow woman, I can empathize with\x01",
            "her actions and her feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x105,
        "#042FYou have such a kind heart, Hilda.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "#0710FNow we must wait for the queen to provide\x01",
            "her sanction.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1667)

    label("loc_5E4")

    Jump("loc_66C")

    label("loc_5E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_66C")

    ChrTalk(    #6
        0xFE,
        (
            "#0712FI couldn't have even imagined that young\x01",
            "girl being involved in all this.\x02\x03",

            "#0710FI hope you find her parents soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66C")

    TalkEnd(0x8)
    Return()

    # Function_4_330 end

    def Function_5_670(): pass

    label("Function_5_670")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75E")
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #7
        0xFE,
        "Ah, Joshua...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#1040FHi, Shea, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "Oh, good, you're back safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        "#1040FShea? What is it...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "Y-You're as beautiful as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        "#1044FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "I-It's nothing.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_7E5")

    label("loc_75E")


    ChrTalk(    #15
        0xFE,
        (
            "If you're looking for Miss Klaudia,\x01",
            "I believe I saw her walking to the\x01",
            "audience chamber.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "I think the head maid was with her.\x02",
    )

    CloseMessageWindow()

    label("loc_7E5")

    Jump("loc_ED3")

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_868")

    ChrTalk(    #17
        0xFE,
        (
            "On top of preparing for the signing\x01",
            "ceremony, cleaning up after this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "I'm worried for the queen's health.\x02",
    )

    CloseMessageWindow()
    Jump("loc_ED3")

    label("loc_868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_END)), "loc_8EC")

    ChrTalk(    #19
        0xFE,
        "You met with Mistress Hilda, didn't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Umm... Would you like me to prepare\x01",
            "something to drink for you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED3")

    label("loc_8EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E69")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96F")

    ChrTalk(    #21
        0xFE,
        "Miss Estelle?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0xFE, 0x105, 400)
    Sleep(600)
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #22
        0xFE,
        "And Miss Klaudia? Mister Zin, too?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF1")

    label("loc_96F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F6")

    ChrTalk(    #23
        0xFE,
        "Hello, Miss Klaudia...\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(600)
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #24
        0xFE,
        "And Miss Estelle! And Mister Zin, too?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF1")

    label("loc_9F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A75")

    ChrTalk(    #25
        0xFE,
        "Mister Zin?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0xFE, 0x105, 400)
    Sleep(600)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #26
        0xFE,
        "And Miss Klaudia? And Miss Estelle, too?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF1")

    label("loc_A75")

    TurnDirection(0xFE, 0x105, 0)
    Sleep(600)

    ChrTalk(    #27
        0xFE,
        "Miss Klaudia?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(600)
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #28
        0xFE,
        "And Miss Estelle! And Mister Zin, too?!\x02",
    )

    CloseMessageWindow()

    label("loc_AF1")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #29
        0xFE,
        "P-Pardon me! It's been quite some time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x108,
        "#070FHaha, it sure has!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1001FYeah, reminds me of when you lent\x01",
            "me your maid uniform, Shea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x104,
        "#033FOhh... Estelle as a maid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1000FYeah, it was to meet with the queen.\x02\x03",

            "Oh, and Joshua had to wear one, too.\x01",
            "Shea did her magic on his face with\x01",
            "her makeup!\x02\x03",

            "#1001FShe was all pumped up to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x105,
        "#044FOh, my...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "Th-Thank you very much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x104,
        (
            "#037FJoshua, who once played the role\x01",
            "of Princess Cecilia so perfectly also\x01",
            "portrayed a maidservant...\x02\x03",

            "Ohhh, noble endeavors both... I am\x01",
            "sure it must have been quite beauteous\x01",
            "to behold.\x02\x03",

            "#034FI regret all the more I could not attend\x01",
            "the duke's banquet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x105,
        (
            "#045FHaha...\x02\x03",

            "#040FOh, right, Shea. Do you know where Hilda is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "I believe Mistress Hilda is in the library.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "As I recall, she said she had something\x01",
            "to look up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1001FThe library, got it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1629)
    Jump("loc_ED3")

    label("loc_E69")


    ChrTalk(    #41
        0xFE,
        "I believe Mistress Hilda is in the library.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "As I recall, she said she had something\x01",
            "to look up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED3")

    TalkEnd(0x9)
    Return()

    # Function_5_670 end

    def Function_6_ED7(): pass

    label("Function_6_ED7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_EFB")

    ChrTalk(    #43
        0xFE,
        "Aaaaaah! No peeking!\x02",
    )

    CloseMessageWindow()

    label("loc_EFB")

    TalkEnd(0xFE)
    Return()

    # Function_6_ED7 end

    SaveToFile()

Try(main)
