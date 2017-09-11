from ED6ScenarioHelper import *

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
        'ED6_DT07/CH02230 ._CH',             # 02
        'ED6_DT07/CH02240 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02540P._CP',             # 01
        'ED6_DT07/CH02230P._CP',             # 02
        'ED6_DT07/CH02240P._CP',             # 03
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_240",          # 01, 1
        "Function_2_24A",          # 02, 2
        "Function_3_3C7",          # 03, 3
        "Function_4_634",          # 04, 4
        "Function_5_957",          # 05, 5
        "Function_6_FDA",          # 06, 6
        "Function_7_298F",         # 07, 7
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_134")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_142")
    OP_A3(0x3FA)
    Event(0, 5)

    label("loc_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_150")
    OP_A3(0x3FB)
    Event(0, 7)

    label("loc_150")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_15C"),
        (SWITCH_DEFAULT, "loc_172"),
    )


    label("loc_15C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16F")
    OP_A2(0x642)
    Event(0, 6)

    label("loc_16F")

    Jump("loc_172")

    label("loc_172")

    OP_A2(0x639)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_19C")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 64129, 0, 99150, 167)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_23F")

    label("loc_19C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1C3")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 70620, 0, 69790, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_23F")

    label("loc_1C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_1CD")
    Jump("loc_23F")

    label("loc_1CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_1F4")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 70630, 0, 98590, 48)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_23F")

    label("loc_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_1FE")
    Jump("loc_23F")

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_23F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 64129, 0, 99150, 167)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 70630, 0, 98590, 48)
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_23F")

    Return()

    # Function_0_10A end

    def Function_1_240(): pass

    label("Function_1_240")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_240 end

    def Function_2_24A(): pass

    label("Function_2_24A")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3B1")

    label("loc_26F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_288")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3B1")

    label("loc_288")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A1")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3B1")

    label("loc_2A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3B1")

    label("loc_2BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3B1")

    label("loc_2D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3B1")

    label("loc_2EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_305")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3B1")

    label("loc_305")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3B1")

    label("loc_31E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_337")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3B1")

    label("loc_337")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_350")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3B1")

    label("loc_350")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3B1")

    label("loc_369")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3B1")

    label("loc_382")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3B1")

    label("loc_39B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3B1")

    label("loc_3C6")

    Return()

    # Function_2_24A end

    def Function_3_3C7(): pass

    label("Function_3_3C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_3D4")
    Jump("loc_630")

    label("loc_3D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3DE")
    Jump("loc_630")

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_3E8")
    Jump("loc_630")

    label("loc_3E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_471")

    ChrTalk(    #0
        0xFE,
        (
            "Joshua, your skin is almost\x01",
            "as soft as a woman's!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "It's absolutely perfect for make-up.\x01",
            "I'm actually kind of jealous!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_630")

    label("loc_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_47B")
    Jump("loc_630")

    label("loc_47B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_630")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_517")

    ChrTalk(    #2
        0xFE,
        (
            "It...will be a bit longer yet\x01",
            "before dinner is ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "In the meantime, please, feel\x01",
            "free to look around to your\x01",
            "heart's content!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_630")

    label("loc_517")

    OP_A2(0x1)

    ChrTalk(    #4
        0xFE,
        "Oh! Is everything all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Has something happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#000FNo, not at all. I just wanted\x01",
            "to look around a bit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "It...will be a bit longer yet\x01",
            "before dinner is ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "In the meantime, please, feel\x01",
            "free to look around to your\x01",
            "heart's content!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_630")

    TalkEnd(0xFE)
    Return()

    # Function_3_3C7 end

    def Function_4_634(): pass

    label("Function_4_634")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_72E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6AE")

    ChrTalk(    #10
        0x8,
        (
            "#710FYou must be tired from the\x01",
            "Birthday Celebration.\x02\x03",

            "If you need anything, please\x01",
            "let me know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72B")

    label("loc_6AE")

    OP_A2(0x0)

    ChrTalk(    #11
        0x8,
        (
            "#710FAh, Madam Estelle!\x02\x03",

            "You must be tired from the\x01",
            "Birthday Celebration.\x02\x03",

            "If you need anything, please\x01",
            "let me know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72B")

    Jump("loc_953")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_83F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7AD")

    ChrTalk(    #12
        0x8,
        (
            "#710FThe town is no doubt abuzz\x01",
            "with festivities.\x02\x03",

            "If you are to attend them yourself,\x01",
            "please take care.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83C")

    label("loc_7AD")

    OP_A2(0x0)

    ChrTalk(    #13
        0x8,
        (
            "#711FOh, are you two heading out?\x02\x03",

            "The town is no doubt abuzz\x01",
            "with festivities.\x02\x03",

            "If you are to attend them yourself,\x01",
            "please take care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83C")

    Jump("loc_953")

    label("loc_83F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_849")
    Jump("loc_953")

    label("loc_849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_853")
    Jump("loc_953")

    label("loc_853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_85D")
    Jump("loc_953")

    label("loc_85D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_953")

    ChrTalk(    #14
        0x8,
        (
            "#710FRegarding dinner...\x02\x03",

            "The pre-cooking is being done\x01",
            "now. Please remain patient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#710FThe pre-cooking is done, so we\x01",
            "will be starting the banquet\x01",
            "shortly.\x02\x03",

            "Please wait in your room. We\x01",
            "will call you when the time\x01",
            "comes.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x49, 0x1, 0x800)

    label("loc_953")

    TalkEnd(0xFE)
    Return()

    # Function_4_634 end

    def Function_5_957(): pass

    label("Function_5_957")

    EventBegin(0x0)
    OP_6D(62970, 640, 71000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 64390, 0, 71030, 270)
    SetChrPos(0x101, 61580, 0, 71540, 90)
    SetChrPos(0x102, 61580, 0, 70620, 90)

    ChrTalk(    #16
        0x8,
        (
            "#710F...I understand.\x02\x03",

            "You need to deliver Professor\x01",
            "Russell's message to Her Majesty.\x02\x03",

            "Correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#000FRight...\x02\x03",

            "If now's not a good time,\x01",
            "we can try later, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#710FNo, it's not an issue...\x02\x03",

            "But those Special Ops men have had\x01",
            "the Royal Keep under constant\x01",
            "surveillance for some time now.\x02\x03",

            "Only the duke, the colonel, and\x01",
            "hired attendants such as myself\x01",
            "are allowed in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#000FWhich means that a private\x01",
            "audience is probably a no-go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#010FWhat do you think, Estelle?\x02\x03",

            "We could ask Hilda to relay\x01",
            "the professor's message to\x01",
            "Her Majesty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#000FHmmm... No, I'd really rather\x01",
            "speak to her face-to-face.\x02\x03",

            "There are just too many particulars\x01",
            "we don't know, that we'd really need\x01",
            "to discuss directly...\x02\x03",

            "Like what Duke Dunan and\x01",
            "Colonel Richard are after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#710FEstelle and Joshua...\x02\x03",

            "I have a bit of an idea.\x02\x03",

            "Could I get you to return here,\x01",
            "once the dinner party is over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#000FWhy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        (
            "#010FHave you thought of a way\x01",
            "for us to see Her Majesty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#710FI believe I have.\x02\x03",

            "It may be difficult...but\x01",
            "I think it's worth a try.\x02\x03",

            "I'm going to need some time to\x01",
            "get ready, so can you come back\x01",
            "after the dinner party?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#000FAwesome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#010FUnderstood.\x01",
            "We'll be back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "#710FI'll be waiting.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F29")

    ChrTalk(    #29
        0x8,
        (
            "#710FOh, and about the party...\x02\x03",

            "Preparing the food is going\x01",
            "to take some time, so please,\x01",
            "bear with me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FAB")

    label("loc_F29")


    ChrTalk(    #30
        0x8,
        (
            "#710FFood prep is done, so I think\x01",
            "we'll begin serving shortly.\x02\x03",

            "For now, it's probably best\x01",
            "if you wait in your room.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x49, 0x1, 0x800)

    label("loc_FAB")

    Sleep(300)
    Fade(1000)
    SetChrPos(0x101, 62550, 0, 68550, 45)
    SetChrPos(0x102, 62550, 0, 68550, 45)
    EventEnd(0x0)
    Return()

    # Function_5_957 end

    def Function_6_FDA(): pass

    label("Function_6_FDA")

    EventBegin(0x0)
    OP_6D(67590, 0, 65319, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 70120, 0, 69770, 225)
    SetChrPos(0x101, 66580, 0, 64769, 45)
    SetChrPos(0x102, 67630, 0, 64590, 45)

    def lambda_102B():
        OP_6D(69520, 0, 68800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_102B)

    def lambda_1043():
        OP_8E(0xFE, 0x10B6C, 0x0, 0x10BE4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1043)

    def lambda_105E():
        OP_8E(0xFE, 0x1113E, 0x0, 0x1095A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_105E)
    WaitChrThread(0x102, 0x2)
    TurnDirection(0x102, 0x8, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #31
        0x8,
        (
            "#710FAh, there you are. I've\x01",
            "been waiting for you.\x02\x03",

            "You're awfully late, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#000FSorry about that...\x02\x03",

            "We kinda got caught by\x01",
            "Colonel Richard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "#710FDid you, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#010FHe had some things to tell\x01",
            "us about our dad.\x02\x03",

            "I don't think he has any idea\x01",
            "what we're up to, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "#710FI see...\x02\x03",

            "Ah, yes. That letter of introduction\x01",
            "did mention that you were Mister\x01",
            "Cassius' children.\x02\x03",

            "I can understand at least some\x01",
            "of how Colonel Richard feels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#000FOh, do you know our dad, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#710FHe used to come here when he\x01",
            "worked as General Morgan's\x01",
            "aide-de-camp.\x02\x03",

            "I'm told that he was a school\x01",
            "friend of the late prince's...\x01",
            "Her Majesty's son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#000F'Late prince'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        "#010FPrincess Klaudia's father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "#710FYes... He was killed, fifteen\x01",
            "years ago, in a tragic shipwreck.\x02\x03",

            "Would that he were still\x01",
            "alive today, none of this\x01",
            "would be happening...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#710F...But lamenting what might\x01",
            "have been is a fool's errand.\x02\x03",

            "Evening is fast approaching. We\x01",
            "must make our preparations at once.\x02\x03",

            "Come on in, Shea.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 69050, 0, 75720, 180)

    def lambda_14BF():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14BF)

    def lambda_14CD():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14CD)

    def lambda_14DB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14DB)
    Sleep(300)

    def lambda_14EE():

        label("loc_14EE")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_14EE")

    QueueWorkItem2(0x9, 1, lambda_14EE)

    def lambda_14FF():
        OP_8E(0xFE, 0x10CCA, 0x0, 0x112B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14FF)

    def lambda_151A():

        label("loc_151A")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_151A")

    QueueWorkItem2(0x8, 1, lambda_151A)

    def lambda_152B():

        label("loc_152B")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_152B")

    QueueWorkItem2(0x101, 1, lambda_152B)

    def lambda_153C():

        label("loc_153C")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_153C")

    QueueWorkItem2(0x102, 1, lambda_153C)
    OP_6D(70030, 0, 70300, 2000)

    ChrTalk(    #43
        0x101,
        "#000FOh, hey... Aren't you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        "#010F...Shea, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "Yes, thank you for remembering.\x01",
            "You look well, Estelle. Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "I've been told of your\x01",
            "current predicament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#710FYou won't find a more\x01",
            "dependable child.\x02\x03",

            "She's a great help to us whenever\x01",
            "the princess is in the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#000FPrincess Klaudia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        "#010FThat shouldn't pose a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        "Th-Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "If you're ready, you should go\x01",
            "change into your uniforms...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "The ribbons and the headpiece\x01",
            "are tricky, so I'll adjust them\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#000FWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        "#010FWhat do you mean...?\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #55
        0x8,
        (
            "#710FEstelle is going to need to dress\x01",
            "as one of the maids in order to\x01",
            "get into the Royal Keep.\x02\x03",

            "A little playing with the hair,\x01",
            "and you'll blend right in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#000FOhhhh, I get it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        (
            "#010FUniforms don't allow for much\x01",
            "in the way of personalization.\x02\x03",

            "That should be ideal for\x01",
            "sneaking in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#000FHuh...\x01",
            "Me, in a maid's outfit.\x02\x03",

            "I've been wanting to try one on since we first\x01",
            "met Lila.\x02\x03",

            "Cute, breezy and easy to move in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "Ha ha... Well, if our uniforms weren't easy to\x01",
            "move in, they'd make the cleaning much more\x01",
            "difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#000FI thought so.\x02\x03",

            "Well, let's get this sucker on me!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #61
        0x102,
        (
            "#010FWhy so excited?\x02\x03",

            "I'm glad you're in high spirits,\x01",
            "but you need to remember your\x01",
            "manners in front of the queen.\x02\x03",

            "You won't have me to\x01",
            "lean on this time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #62
        0x101,
        (
            "#000FWhy not?\x02\x03",

            "You're changing too,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#010F...\x02\x03",

            "...Err?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B0A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1B0A)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #64
        0x8,
        "#710FPardon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#000FI mean, he DID play the\x01",
            "princess during the play\x01",
            "at the campus festival.\x02\x03",

            "Is there really that much of\x01",
            "a difference between the fancy\x01",
            "dress and a maid outfit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x102,
        (
            "#010FThat's different.\x01",
            "It was a play.\x02\x03",

            "I can't appear before Her\x01",
            "Majesty in women's clothes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#000FOh, you'll be fine. It's not\x01",
            "at all shameful or anything.\x02\x03",

            "Besides, you made such\x01",
            "a gorgeous princess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#010FN-Not this again...\x01",
            "Cut the jokes, will you?\x02\x03",

            "Hilda... Shea... Help me\x01",
            "out here. Say something...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D1B():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D1B)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #69
        0x8,
        "#710F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        "...\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #71
        0x102,
        "#010FAnyone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "#710FI see...\x01",
            "That shouldn't pose a problem.\x02\x03",

            "Shea, don't you have that extra\x01",
            "hairpiece designed for the princess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        "Y-Yes... It's never been used, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        (
            "He has that full, dark hair,\x01",
            "so it would probably look\x01",
            "good on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        "#010FHey, hold on a second...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#000FWell, it looks like a three-to-one\x01",
            "vote. Majority rules! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "This way, please. We can use\x01",
            "this as a changing room.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F06():

        label("loc_1F06")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1F06")

    QueueWorkItem2(0x8, 1, lambda_1F06)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)

    def lambda_1F2B():
        OP_8E(0xFE, 0x10C48, 0x0, 0x12D4A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1F2B)
    Sleep(300)
    OP_8E(0x101, 0x10FF4, 0x0, 0x10AEA, 0xBB8, 0x0)

    ChrTalk(    #78
        0x102,
        (
            "#010FW-Wait a minute, I don't remember ever agreeing\x01",
            "to changing!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0x10FEA, 0x0, 0x1090A, 0x7D0, 0x0)
    OP_8C(0x102, 180, 400)

    def lambda_1FC1():
        OP_6D(69970, 0, 72360, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1FC1)

    def lambda_1FD9():
        OP_8E(0xFE, 0x10C48, 0x0, 0x12D4A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FD9)

    def lambda_1FF4():
        OP_8F(0xFE, 0x10C48, 0x0, 0x12D4A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FF4)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)

    ChrTalk(    #79
        0x102,
        (
            "#010FAll right, all right. If I have\x01",
            "to change, I can do it myself...\x02\x03",

            "Uh...Shea... You're not planning\x01",
            "on using makeup, too, are you...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8)

    ChrTalk(    #80
        0x8,
        "#710F*sigh* Kids these days...\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(69200, 0, 72370, 0)
    SetChrPos(0x8, 68890, 0, 69520, 0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    FadeToBright(2000, 0)

    def lambda_2126():
        OP_8E(0xFE, 0x11062, 0x0, 0x116F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2126)
    Sleep(600)

    def lambda_2146():
        OP_8E(0xFE, 0x10E00, 0x0, 0x11D78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2146)
    WaitChrThread(0x9, 0x1)

    def lambda_2166():
        OP_8E(0xFE, 0x1090A, 0x0, 0x11E18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2166)
    WaitChrThread(0x9, 0x1)

    def lambda_2186():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2186)

    ChrTalk(    #81
        0x8,
        "#710FOh, my...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 317, 400)
    OP_8C(0x101, 75, 400)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #82
        0x101,
        (
            "#000FTa-dah!\x02\x03",

            "Hee hee...\x01",
            "What do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        (
            "Heehee...\x01",
            "I think it suits her very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "#710FSuch a bright, active maid-in-training, and\x01",
            "after only just coming to the castle, too...\x01",
            "You certainty have me convinced!\x02\x03",

            "And with the hair down like that,\x01",
            "no one will be any the wiser.\x02\x03",

            "Perhaps you'd like to work\x01",
            "at Grancel Castle when this\x01",
            "is all settled?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#000FW-Well, we already work\x01",
            "as bracers, so, uh...\x02\x03",

            "Anyway...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #86
        0x101,
        (
            "#000FCome on, Joshua.\x01",
            "Get out here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_239D():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_239D)

    def lambda_23AB():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23AB)
    OP_6D(69080, 0, 73680, 1000)

    ChrTalk(    #87
        0x102,
        (
            "#010F*sigh*...\x02\x03",

            "No chance I can talk\x01",
            "you out of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#000FNone at all.\x02\x03",

            "You're just making this take longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        (
            "#010FFine...\x02\x03",

            "You're impossible sometimes...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2474():

        label("loc_2474")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2474")

    QueueWorkItem2(0x9, 1, lambda_2474)

    def lambda_2485():

        label("loc_2485")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2485")

    QueueWorkItem2(0x8, 1, lambda_2485)

    def lambda_2496():

        label("loc_2496")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2496")

    QueueWorkItem2(0x101, 1, lambda_2496)
    OP_8E(0x102, 0x10DBA, 0x0, 0x11DC8, 0x3E8, 0x0)

    ChrTalk(    #90
        0x102,
        "#010F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#710FWell... It's almost frightening\x01",
            "how good that looks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#000FIsn't it awesome?!\x02\x03",

            "It looks better on him than\x01",
            "it does on me, and I'm an\x01",
            "actual girl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        (
            "Ha ha... A bit of makeup can\x01",
            "make all the difference in\x01",
            "the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        (
            "#010FPlease...\x01",
            "Just say you're done.\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(68990, 0, 71660, 1000)

    def lambda_25EC():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25EC)

    def lambda_25FA():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25FA)

    ChrTalk(    #95
        0x8,
        (
            "#710FWell... I suppose so.\x02\x03",

            "I'll show you the way\x01",
            "to the Royal Keep.\x02\x03",

            "You need to make certain you\x01",
            "watch me and learn how a maid\x01",
            "handles herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#000FY-Yes, ma'am.\x02\x03",

            "*gulp* We're finally gonna\x01",
            "meet the queen in person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        (
            "#010FYes...\x01",
            "This is the do-or-die moment.\x02\x03",

            "We just have to stay focused \x01",
            "and get to the Royal Keep.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #98
        0x101,
        (
            "#000F*snicker*... It's hard to take\x01",
            "you seriously in that outfit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 800)

    ChrTalk(    #99
        0x102,
        (
            "#010FW-Well, excuse me!\x02\x03",

            "This was YOUR idea! I can't\x01",
            "believe you've got the nerve\x01",
            "to pick on--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#000FSorry, sorry...\x01",
            "Don't get all mad.\x02\x03",

            "I'll treat you to some\x01",
            "ice cream later, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        (
            "#010FHmph. I'm not like you. I'm\x01",
            "not obsessed with food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#000FH-Hey! I'm not obsessed with food...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        (
            "Ha ha ha... They get along\x01",
            "so well, don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "#710FWe're out of time. Let's\x01",
            "go to the Royal Keep.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4A, 0x1, 0x20)
    OP_28(0x4A, 0x1, 0x40)
    SetChrFlags(0x8, 0x40)

    def lambda_2957():
        OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2957)
    EventEnd(0x0)
    AddParty(0x37, 0xFF)
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)
    SetChrFlags(0x8, 0x80)
    Return()

    # Function_6_FDA end

    def Function_7_298F(): pass

    label("Function_7_298F")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_6D(68370, 0, 69650, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 68920, 0, 70070, 180)
    SetChrPos(0x9, 67750, 0, 70350, 180)
    RemoveParty(0x37, 0xFF)
    SetChrPos(0x101, 67080, 0, 68350, 0)
    SetChrPos(0x102, 68360, 0, 68190, 0)
    OP_0D()

    ChrTalk(    #105
        0x101,
        (
            "#000FThanks for everything!\x01",
            "Both of you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x102,
        (
            "#010FIf not for you, I don't know\x01",
            "what we'd have done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        (
            "#710FPlease. It was the least we could\x01",
            "do in Her Majesty's service.\x02\x03",

            "I only ask that you complete\x01",
            "the request she made of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x9,
        "U-Umm... I feel the same way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        (
            "I beg of you, do everything in\x01",
            "your power to save the princess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#000FOh... Are you one of\x01",
            "her royal retainers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x9,
        (
            "Y-Yes... I regret that I rarely\x01",
            "get the chance to serve her\x01",
            "directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "She's so kind and open...\x01",
            "She's always treated me more\x01",
            "like a friend than a servant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x9,
        (
            "The thought of her being held\x01",
            "captive keeps me up at night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#000FI understand. Well, you can rest\x01",
            "easy now that we're on the job!\x01",
            "We'll save her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        "#010FShall we be going?\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_7_298F end

    SaveToFile()

Try(main)
