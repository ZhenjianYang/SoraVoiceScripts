from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1111   ._SN',
        MapName             = 'Bose',
        Location            = 'T1111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        'Mayor Maybelle',                       # 9
        'Lila',                                 # 10
        'Butler Mayner',                        # 11
        'Sarah',                                # 12
        'Mirano',                               # 13
    )

    DeclEntryPoint(
        Unknown_00              = 48000,
        Unknown_04              = -3000,
        Unknown_08              = 27000,
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
        'ED6_DT07/CH02360 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01560 ._CH',             # 02
        'ED6_DT07/CH01230 ._CH',             # 03
        'ED6_DT07/CH02370 ._CH',             # 04
        'ED6_DT07/CH00003 ._CH',             # 05
        'ED6_DT07/CH00013 ._CH',             # 06
        'ED6_DT07/CH00023 ._CH',             # 07
        'ED6_DT07/CH00033 ._CH',             # 08
        'ED6_DT07/CH02363 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH02360P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01560P._CP',             # 02
        'ED6_DT07/CH01230P._CP',             # 03
        'ED6_DT07/CH02370P._CP',             # 04
        'ED6_DT07/CH00003P._CP',             # 05
        'ED6_DT07/CH00013P._CP',             # 06
        'ED6_DT07/CH00023P._CP',             # 07
        'ED6_DT07/CH00033P._CP',             # 08
        'ED6_DT07/CH02363P._CP',             # 09
    )

    DeclNpc(
        X                   = -120760,
        Z                   = 200,
        Y                   = 68570,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -3220,
        Z                   = -4000,
        Y                   = 68110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 500,
        Y                   = -870,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -33400,
        Z                   = -3000,
        Y                   = 35100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -120820,
        Z                   = 0,
        Y                   = 66250,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_2F6",          # 01, 1
        "Function_2_2F7",          # 02, 2
        "Function_3_30D",          # 03, 3
        "Function_4_331",          # 04, 4
        "Function_5_393",          # 05, 5
        "Function_6_12F3",         # 06, 6
        "Function_7_1B93",         # 07, 7
        "Function_8_2AAF",         # 08, 8
        "Function_9_2C4D",         # 09, 9
        "Function_10_326E",        # 0A, 10
        "Function_11_3B85",        # 0B, 11
        "Function_12_4AAA",        # 0C, 12
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1CB")
    SetChrPos(0xB, -64150, -3000, 66390, 0)
    SetChrPos(0x9, -123500, 0, 66690, 275)
    SetChrChipByIndex(0x8, 9)
    Jump("loc_27E")

    label("loc_1CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1FA")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xB, -64150, -3000, 66390, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x8, 9)
    Jump("loc_27E")

    label("loc_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_213")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrChipByIndex(0x8, 9)
    Jump("loc_27E")

    label("loc_213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_23D")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xB, -64150, -3000, 66390, 0)
    SetChrChipByIndex(0x8, 9)
    Jump("loc_27E")

    label("loc_23D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_256")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrChipByIndex(0x8, 9)
    Jump("loc_27E")

    label("loc_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_276")
    SetChrPos(0xB, -65000, -3000, 64650, 270)
    SetChrChipByIndex(0x8, 9)
    Jump("loc_27E")

    label("loc_276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27E")

    label("loc_27E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0xB, -6030, 4500, 2470, 275)

    label("loc_2AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2B9")
    OP_A3(0x3FA)
    Event(0, 12)

    label("loc_2B9")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2C9"),
        (110, "loc_2DF"),
        (SWITCH_DEFAULT, "loc_2F5"),
    )


    label("loc_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC")
    OP_A2(0x309)
    Event(0, 10)

    label("loc_2DC")

    Jump("loc_2F5")

    label("loc_2DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F2")
    OP_A2(0x317)
    Event(0, 11)

    label("loc_2F2")

    Jump("loc_2F5")

    label("loc_2F5")

    Return()

    # Function_0_19A end

    def Function_1_2F6(): pass

    label("Function_1_2F6")

    Return()

    # Function_1_2F6 end

    def Function_2_2F7(): pass

    label("Function_2_2F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2F7")

    label("loc_30C")

    Return()

    # Function_2_2F7 end

    def Function_3_30D(): pass

    label("Function_3_30D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_330")
    OP_8D(0xFE, -37400, -6200, -27800, -1300, 2000)
    Jump("Function_3_30D")

    label("loc_330")

    Return()

    # Function_3_30D end

    def Function_4_331(): pass

    label("Function_4_331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_350")

    label("loc_338")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_338")

    label("loc_34D")

    Jump("loc_392")

    label("loc_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_37D")

    label("loc_357")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37A")
    OP_8D(0xFE, -34800, 34500, -31600, 36300, 2000)
    Jump("loc_357")

    label("loc_37A")

    Jump("loc_392")

    label("loc_37D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_392")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_37D")

    label("loc_392")

    Return()

    # Function_4_331 end

    def Function_5_393(): pass

    label("Function_5_393")

    TalkBegin(0x8)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B8")
    SetChrSubChip(0xFE, 1)
    Jump("loc_3D3")

    label("loc_3B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CE")
    SetChrSubChip(0xFE, 0)
    Jump("loc_3D3")

    label("loc_3CE")

    SetChrSubChip(0xFE, 2)

    label("loc_3D3")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_7A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_776")
    OP_A2(0x0)

    ChrTalk(    #0
        0x8,
        "#613FOh... Are you all going somewhere?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#000FYeah, we're getting ready to leave.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#010FWe appreciate all your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#610FNonsense! I should be\x01",
            "the one saying thank you.\x02\x03",

            "It would certainly be great if we had\x01",
            "bracers like you in Bose all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#008FI-I think you're giving us a little\x01",
            "too much credit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#610FThere's no need to be modest.\x02\x03",

            "And I'd like you to let me thank you\x01",
            "on behalf of the citizens of Bose.\x02\x03",

            "I am really grateful to the two of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#501FMayor Maybelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#610FWell, I guess it wouldn't be right\x01",
            "of me to keep you any longer.\x02\x03",

            "Estelle and Joshua, please be\x01",
            "careful in your travels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#001FWe will. You take care of yourself\x01",
            "Mayor Maybelle. And don't work\x01",
            "too hard either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#617FHa ha. Lila just lectured me\x01",
            "about the same thing.\x02\x03",

            "I'll try and be more careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#010FI hope we'll meet again sometime,\x01",
            "but for now it's farewell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A2")

    label("loc_776")


    ChrTalk(    #11
        0x8,
        "#610FI agree, that would be wonderful.\x02",
    )

    CloseMessageWindow()

    label("loc_7A2")

    Jump("loc_12EA")

    label("loc_7A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_B2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAC")
    OP_A2(0x0)

    ChrTalk(    #12
        0xFE,
        (
            "#610FMirano was just asking me about\x01",
            "the situation in the Bose Market.\x02\x03",

            "#612FIt appears the effects of the missing\x01",
            "airliner incident are farther reaching\x01",
            "than I had imagined.\x02\x03",

            "#610FAnd the look on your faces tells me\x01",
            "that you've found something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#006FYou could really tell that just\x01",
            "by looking at our faces?\x02\x03",

            "Well, we didn't get anything for\x01",
            "certain, but we did manage to\x01",
            "gather a little information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#010FWe should be able to give you some\x01",
            "sort of a report in the near future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x103,
        (
            "#020FWe might be just swinging at\x01",
            "empty air on this one...\x02\x03",

            "But I'd like you to hold on just a\x01",
            "little longer while we see what\x01",
            "we can dig up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "#610FSure, I'll be looking forward to\x01",
            "seeing what you come up with.\x02\x03",

            "But whatever you do, please\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2C")

    label("loc_AAC")


    ChrTalk(    #17
        0xFE,
        (
            "#612FI've really had it up to here...\x02\x03",

            "Not only am I drowning in work, but now\x01",
            "I've got all these burglaries to deal with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2C")

    Jump("loc_12EA")

    label("loc_B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_D85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCE")
    OP_A2(0x0)

    ChrTalk(    #18
        0xFE,
        (
            "#615FI have a female friend by the\x01",
            "name of Mirano...\x02\x03",

            "Her father was aboard the airliner\x01",
            "that went missing.\x02\x03",

            "#612FI am sure there are a lot of other people\x01",
            "also worried about family members who\x01",
            "still haven't returned.\x02\x03",

            "There's a high possibility that these\x01",
            "burglars and sky bandits may be\x01",
            "one and the same.\x02\x03",

            "I hope this investigation can yield\x01",
            "some pertinent information about this\x01",
            "group.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D82")

    label("loc_CCE")


    ChrTalk(    #19
        0xFE,
        (
            "#612FThere's a high possibility that these\x01",
            "burglars and sky bandits may be\x01",
            "one and the same.\x02\x03",

            "I hope this investigation can yield\x01",
            "some pertinent information about this\x01",
            "group.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D82")

    Jump("loc_12EA")

    label("loc_D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_10CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1003")
    OP_A2(0x0)

    ChrTalk(    #20
        0xFE,
        (
            "#610FI should be the one\x01",
            "saying thank you.\x02\x03",

            "How is the investigation coming along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#000FWell, to tell you the truth, we're having a\x01",
            "hard time coming up with anything.\x02\x03",

            "But we have managed to gather\x01",
            "a number of clues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#010FWell, it's more like unreliable information\x01",
            "than clues...\x02\x03",

            "But even still, we were thinking about\x01",
            "heading over to Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "#610FRavennue Village...? But I heard\x01",
            "the army had already finished its\x01",
            "investigation there...\x02\x03",

            "I guess if that's the only clue we have to\x01",
            "go on, maybe it's worth re-investigating\x01",
            "the place.\x02\x03",

            "Anyway, please keep me posted\x01",
            "as to what you find.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C7")

    label("loc_1003")


    ChrTalk(    #24
        0xFE,
        (
            "#610FRavennue Village...? But I heard\x01",
            "the army had already finished its\x01",
            "investigation there...\x02\x03",

            "I guess if that's the only clue we have to\x01",
            "go on, maybe it's worth re-investigating\x01",
            "the place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C7")

    Jump("loc_12EA")

    label("loc_10CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1205")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A9")
    OP_A2(0x0)

    ChrTalk(    #25
        0xFE,
        (
            "#612FDealing with this hijacking is my\x01",
            "top priority.\x02\x03",

            "I'll have to worry about these other\x01",
            "documents later.\x02\x03",

            "#611FBoy, oh, boy... It looks like things\x01",
            "are going to get really busy around\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1202")

    label("loc_11A9")


    ChrTalk(    #26
        0xFE,
        (
            "#611FBoy, oh, boy... It looks like things\x01",
            "are going to get really busy around\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1202")

    Jump("loc_12EA")

    label("loc_1205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_12EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A2")
    OP_A2(0x0)

    ChrTalk(    #27
        0xFE,
        (
            "#610FI'm looking forward to hearing a\x01",
            "good report from you bracers.\x02\x03",

            "When you meet with General Morgan\x01",
            "please give him my regards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EA")

    label("loc_12A2")


    ChrTalk(    #28
        0xFE,
        (
            "#610FWhen you meet with General Morgan\x01",
            "please give him my regards.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EA")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0x8)
    Return()

    # Function_5_393 end

    def Function_6_12F3(): pass

    label("Function_6_12F3")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_13AB")

    ChrTalk(    #29
        0xFE,
        (
            "#621FIt looks like Miss Maybelle will\x01",
            "finally be able to get a good\x01",
            "night's rest.\x02\x03",

            "This is all thanks to you...so please\x01",
            "allow me to express my sincere\x01",
            "appreciation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8F")

    label("loc_13AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_147B")

    ChrTalk(    #30
        0xFE,
        (
            "Not only has Mayor Maybelle been up until\x01",
            "late working overtime repeatedly, she's been\x01",
            "dealing with these incidents on top of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I need to lecture her more about\x01",
            "managing her health...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8F")

    label("loc_147B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_16DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1659")
    OP_A2(0x1)

    ChrTalk(    #32
        0xFE,
        (
            "#620FI hear you all had a stroke of bad luck.\x02\x03",

            "Mayor Maybelle received a message\x01",
            "from the Bracer Guild about what\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#002FI guess it was kind of unavoidable,\x01",
            "but I'm still ashamed to say it\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#010FWell, it was out of our control to begin\x01",
            "with. And I can't say that the Royal\x01",
            "Army was necessarily at fault either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#009FYeah, whatever.\x02\x03",

            "And if any of you sky bandits can\x01",
            "hear me...you just wait until I get\x01",
            "my hands on you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DA")

    label("loc_1659")


    ChrTalk(    #36
        0xFE,
        (
            "#620FI hear you all had a stroke of bad luck.\x02\x03",

            "Mayor Maybelle received a message\x01",
            "from the Bracer Guild about what\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DA")

    Jump("loc_1B8F")

    label("loc_16DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_17DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1791")
    OP_A2(0x1)

    ChrTalk(    #37
        0xFE,
        (
            "Miss Maybelle is one of those people\x01",
            "who become more alive the busier\x01",
            "she gets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I am sure she gets that from her father,\x01",
            "the previous Mayor of Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D8")

    label("loc_1791")


    ChrTalk(    #39
        0xFE,
        (
            "I'm more worried about Miss Maybelle's\x01",
            "health than anything else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D8")

    Jump("loc_1B8F")

    label("loc_17DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_19AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190E")
    OP_A2(0x1)

    ChrTalk(    #40
        0xFE,
        (
            "#620FGeneral Morgan has come here to\x01",
            "visit on several occasions.\x02\x03",

            "He's a little difficult to describe, but what\x01",
            "I can say is that he IS a respectable man...\x01",
            "There's no doubt in my mind about that.\x02\x03",

            "#623FBut in both a good and a bad sense,\x01",
            "he has the temperament of a military\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19AA")

    label("loc_190E")


    ChrTalk(    #41
        0xFE,
        (
            "#620FThere is no doubt that General Morgan\x01",
            "is a respectable man...\x02\x03",

            "#623FBut in both a good and a bad sense,\x01",
            "he has the temperament of a military\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19AA")

    Jump("loc_1B8F")

    label("loc_19AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1B8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFC")
    OP_A2(0x1)

    ChrTalk(    #42
        0xFE,
        (
            "#620FMiss Maybelle may not look it,\x01",
            "but she has been really hung up\x01",
            "over these incidents.\x02\x03",

            "There's been a string of break-ins,\x01",
            "you see...if you hadn't already heard.\x02\x03",

            "#621FIf there is anything you bracers can\x01",
            "do to assist Miss Maybelle...\x02\x03",

            "I am asking you, as her lowly maid,\x01",
            "to help her shoulder the burden.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8F")

    label("loc_1AFC")


    ChrTalk(    #43
        0xFE,
        (
            "#621FIf there is anything you bracers\x01",
            "can do to assist Miss Maybelle...\x02\x03",

            "I am asking you, as her lowly maid,\x01",
            "to help her shoulder the burden.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8F")

    TalkEnd(0x9)
    Return()

    # Function_6_12F3 end

    def Function_7_1B93(): pass

    label("Function_7_1B93")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1DB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD1")
    OP_A2(0x2)

    ChrTalk(    #44
        0xFE,
        (
            "I honestly couldn't be more grateful\x01",
            "to you all than I am now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I just hope Mayor Maybelle will\x01",
            "consider putting down her work\x01",
            "for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Unfortunately, she's the type who adds more \x01",
            "onto her own plate whenever she finds she\x01",
            "has a minute, and that's what has me worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB2")

    label("loc_1CD1")


    ChrTalk(    #47
        0xFE,
        (
            "I just hope Mayor Maybelle will\x01",
            "consider putting down her work\x01",
            "for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Unfortunately, she's the type who adds more\x01",
            "onto her own plate whenever she finds she\x01",
            "has a minute, and that's what has me worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB2")

    Jump("loc_2AAB")

    label("loc_1DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_20F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FEA")
    OP_A2(0x2)

    ChrTalk(    #49
        0xFE,
        (
            "The city of Bose was destroyed\x01",
            "and occupied by the Empire in\x01",
            "the war 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "However, Mayor Maybelle's father...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "In other words, the previous mayor took the helm\x01",
            "and made extensive efforts to rebuild the city \x01",
            "with the help of other merchants like himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "For merchants who generally only care about making\x01",
            "a few quick mira, this was the first time in\x01",
            "history that so many came together like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "It seems as though it was at this time\x01",
            "that Mayor Maybelle made the decision\x01",
            "to follow in her father's footsteps.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20F5")

    label("loc_1FEA")


    ChrTalk(    #54
        0xFE,
        (
            "After the war, Mayor Maybelle's father took the\x01",
            "helm and made extensive efforts to rebuild Bose\x01",
            "with the help of other merchants like himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "It seems as though it was at this time\x01",
            "that Mayor Maybelle made the decision\x01",
            "to follow in her father's footsteps.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20F5")

    Jump("loc_2AAB")

    label("loc_20F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2302")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2260")
    OP_A2(0x2)

    ChrTalk(    #56
        0xFE,
        (
            "I have recommended to the mayor that\x01",
            "she take a break from her labors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "But she has stated that alleviating the\x01",
            "citizens' concerns and bringing back\x01",
            "peace to Bose comes first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "I couldn't be more happy that Mayor Maybelle has\x01",
            "matured into such a fine young woman, but I wish\x01",
            "she would take better care of herself sometimes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22FF")

    label("loc_2260")


    ChrTalk(    #59
        0xFE,
        (
            "I couldn't be more happy that Mayor\x01",
            "Maybelle has matured into such a\x01",
            "fine young woman...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "But I wish she would take better care\x01",
            "of herself sometimes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22FF")

    Jump("loc_2AAB")

    label("loc_2302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2503")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248B")
    OP_A2(0x2)

    ChrTalk(    #61
        0xFE,
        (
            "When Mayor Maybelle was elected,\x01",
            "she received a lot of backlash from\x01",
            "those around her because of her age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "However, because of numerous commercial policies\x01",
            "and her efforts for the city, those who have seen\x01",
            "her in action have gradually changed their minds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "Trino and his daughter Mirano are just\x01",
            "a few of the influential merchants who\x01",
            "support Mayor Maybelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2500")

    label("loc_248B")


    ChrTalk(    #64
        0xFE,
        (
            "Mirano may be young, but she carries\x01",
            "a lot of weight as a merchant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "And even Mayor Maybellle respects\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2500")

    Jump("loc_2AAB")

    label("loc_2503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_END)), "loc_2594")

    ChrTalk(    #66
        0xFE,
        (
            "Good work, you all. I hear your investigation\x01",
            "has seen some progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "Mayor Maybelle has been very\x01",
            "excited about it as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAB")

    label("loc_2594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_25FF")

    ChrTalk(    #68
        0xFE,
        "I'm glad to see you all again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Mayor Maybelle has been excitedly\x01",
            "awaiting your report.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAB")

    label("loc_25FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_27A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2700")
    OP_A2(0x2)

    ChrTalk(    #70
        0xFE,
        "Huh? May I help you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "So...I see you've met with the mayor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Please stop by again if there is anything to\x01",
            "report to the mayor regarding her request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I have been informed by Mayor\x01",
            "Maybelle to let you in at any time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27A4")

    label("loc_2700")


    ChrTalk(    #74
        0xFE,
        (
            "Please stop by again if there is anything to\x01",
            "report to the mayor regarding her request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I have been informed by Mayor\x01",
            "Maybelle to let you in at any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27A4")

    Jump("loc_2AAB")

    label("loc_27A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_2969")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2869")

    ChrTalk(    #76
        0xFE,
        (
            "I am sure you already know by now,\x01",
            "but if you don't, the market is in the\x01",
            "center of the north block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "You will see it directly to your\x01",
            "front when you leave this house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2966")

    label("loc_2869")

    OP_A2(0x2)

    ChrTalk(    #78
        0xFE,
        (
            "Oh, I see you were able to meet\x01",
            "up with Lila, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "So where is the mayor right now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x134,
        (
            "#621FShe's in the market. We're just\x01",
            "on our way to meet her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Ha ha. I expect no less from Mayor\x01",
            "Maybelle. She's always dedicated\x01",
            "to her work...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2966")

    Jump("loc_2AAB")

    label("loc_2969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2A0A")

    ChrTalk(    #82
        0xFE,
        (
            "The mayor is currently out and has\x01",
            "gone to worship at the chapel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "She is accompanied by a maid, so please\x01",
            "use that as a way to pinpoint her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAB")

    label("loc_2A0A")


    ChrTalk(    #84
        0xFE,
        (
            "I'm sorry to say this, but the mayor\x01",
            "is currently out at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "If you have some business with her,\x01",
            "could I ask you to come back at\x01",
            "a later time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAB")

    TalkEnd(0xA)
    Return()

    # Function_7_1B93 end

    def Function_8_2AAF(): pass

    label("Function_8_2AAF")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD0")
    OP_A2(0x3)

    ChrTalk(    #86
        0xFE,
        (
            "According to Mayor Maybelle,\x01",
            "the missing airliner appears to\x01",
            "be the work of the sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "If it's a ransom they're after, then\x01",
            "it's probably a pretty safe bet to\x01",
            "say that my father is still alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "I hope my mother won't be so\x01",
            "worried after hearing this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C49")

    label("loc_2BD0")


    ChrTalk(    #89
        0xFE,
        (
            "So I've heard you bracers are\x01",
            "investigating the incident.\x01",
            "Is that true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Bring back my father safely,\x01",
            "will you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C49")

    TalkEnd(0xC)
    Return()

    # Function_8_2AAF end

    def Function_9_2C4D(): pass

    label("Function_9_2C4D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2DAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D28")
    OP_A2(0x4)

    ChrTalk(    #91
        0xFE,
        (
            "Recently, Lila has been deciding\x01",
            "the mayor's menu for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Let's see... It looks like I'm a little\x01",
            "short on vegetables.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "I guess I'll have to make a quick\x01",
            "trip to the market later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DAB")

    label("loc_2D28")


    ChrTalk(    #94
        0xFE,
        (
            "Let's see... It looks like I'm a little\x01",
            "short on vegetables.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "I guess I'll have to make a quick\x01",
            "trip to the market later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DAB")

    Jump("loc_326A")

    label("loc_2DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2E8D")

    ChrTalk(    #96
        0xFE,
        (
            "Mayor Maybelle looks really busy...\x01",
            "I hope this incident will be resolved\x01",
            "sooner rather than later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "After things settle down and we have\x01",
            "some free time, Lila and I have\x01",
            "promised to go shopping together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_326A")

    label("loc_2E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2F08")

    ChrTalk(    #98
        0xFE,
        "It's almost tea time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "I may be a klutz, but I am just as\x01",
            "skilled as Lila when it comes to\x01",
            "pouring tea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_326A")

    label("loc_2F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2FAD")

    ChrTalk(    #100
        0xFE,
        (
            "Mayor Maybelle is not only a\x01",
            "beautiful woman, but she's\x01",
            "smart and dignified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I really look up to her, and I hope\x01",
            "that I can be like her someday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_326A")

    label("loc_2FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_31E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3041")
    TurnDirection(0xFE, 0x134, 0)

    ChrTalk(    #102
        0xFE,
        (
            "L-Lila... Look, I'm almost done\x01",
            "with the cleaning, if you were\x01",
            "wondering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "I wasn't sneaking off to eat ice cream.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31E3")

    label("loc_3041")

    OP_A2(0x4)
    TurnDirection(0xFE, 0x134, 0)

    ChrTalk(    #104
        0xFE,
        "O-Oh...Lila?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(700)

    ChrTalk(    #105
        0xFE,
        "A-Are you back already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x134,
        (
            "#620FNo...I'm on my way to meet the\x01",
            "mayor at the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "I-I see... Well, look, I'm almost\x01",
            "done with the cleaning, if you\x01",
            "were wondering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "I wasn't sneaking off to eat ice cream.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#505F(I wonder if this 'Lila' is\x01",
            "scary or something?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        (
            "#010F(Who knows, but she does seem to\x01",
            "have her own distinct...ah,\x01",
            "personality.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E3")

    Jump("loc_326A")

    label("loc_31E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_326A")

    ChrTalk(    #111
        0xFE,
        (
            "I'd better hurry and get this\x01",
            "cleaning done ASAP...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(700)

    ChrTalk(    #112
        0xFE,
        "Or else Lila's going to get really mad.\x02",
    )

    CloseMessageWindow()

    label("loc_326A")

    TalkEnd(0xB)
    Return()

    # Function_9_2C4D end

    def Function_10_326E(): pass

    label("Function_10_326E")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 4000, 0, -5860, 0)
    SetChrPos(0x102, 3280, 0, -7224, 0)
    SetChrPos(0x103, 4570, 0, -6990, 0)
    SetChrPos(0xA, -1454, 500, 3536, 135)

    def lambda_32BF():
        OP_6D(840, 500, 1500, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_32BF)
    Sleep(2500)
    Sleep(500)

    ChrTalk(    #113
        0x101,
        (
            "#004FWow, now isn't this a gorgeous\x01",
            "place...\x02\x03",

            "#001FCheck out that crazy-expensive\x01",
            "looking chandelier!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #114
        0x102,
        "#017FCalm down, Estelle.\x02",
    )

    CloseMessageWindow()

    def lambda_3371():
        OP_6D(2860, 500, -380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3371)

    def lambda_3389():
        OP_8E(0x101, 0x12B6, 0x0, 0xFFFFF27C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3389)
    Sleep(200)

    def lambda_33A9():
        OP_8E(0x102, 0xC9E, 0x0, 0xFFFFF060, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_33A9)
    Sleep(500)
    OP_8E(0x103, 0x10E0, 0x0, 0xFFFFEF02, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #115
        0x103,
        (
            "#020FIt looks like this is the mayor's\x01",
            "place, all right.\x02\x03",

            "Now I just wonder if she's home.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)
    OP_4A(0xA, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    Sleep(500)

    def lambda_3466():

        label("loc_3466")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_3466")

    QueueWorkItem2(0x101, 1, lambda_3466)

    def lambda_3477():

        label("loc_3477")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_3477")

    QueueWorkItem2(0x102, 1, lambda_3477)

    def lambda_3488():

        label("loc_3488")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_3488")

    QueueWorkItem2(0x103, 1, lambda_3488)
    OP_8E(0xA, 0xFFFFFD9E, 0x1F4, 0x474, 0x7D0, 0x0)
    TurnDirection(0xA, 0x103, 400)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x0, 0x0)
    Sleep(500)
    OP_71(0x0, 0x800)

    ChrTalk(    #116
        0xA,
        "Oh, do we have visitors?\x02",
    )

    CloseMessageWindow()

    def lambda_3504():
        OP_6D(3750, 250, -2570, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3504)
    OP_8E(0xA, 0xCE4, 0x1F4, 0xFFFFFCAE, 0xBB8, 0x0)
    OP_8C(0xA, 180, 400)

    ChrTalk(    #117
        0xA,
        (
            "Welcome to the Bose mayor's\x01",
            "residence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        "May I ask who you are, please?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        (
            "#020FWe're with the Bracer Guild.\x02\x03",

            "The mayor made a request to the\x01",
            "guild and we've come here to\x01",
            "inquire about the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xA,
        (
            "Well, I have heard from the mayor\x01",
            "that we would be expecting you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xA,
        (
            "However, I am sorry to inform you\x01",
            "that the mayor is currently out at\x01",
            "the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xA,
        (
            "She has gone to worship at\x01",
            "the chapel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        "#010FWhen do you expect her back, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xA,
        "Well, let me see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xA,
        (
            "Actually, I would imagine her to be\x01",
            "making a return any moment now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#501FWell, we're kinda in a hurry to\x01",
            "meet her...\x02\x03",

            "Do you think it would be all right\x01",
            "to call on her at the chapel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xA,
        (
            "W-Well...I don't wish to inconvenience\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#000FDon't worry, it would probably save\x01",
            "the both of us some trouble.\x02\x03",

            "But if you don't mind me asking...what\x01",
            "does the mayor look like?\x02\x03",

            "Like the typical wealthy person?\x01",
            "Big hat with feathers in it?\x01",
            "Dripping gemstones from every pore?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xA,
        (
            "Feathers? Gemstones from every...what?\x01",
            "Umm...how...colorful, but quite off the\x01",
            "mark, I assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xA,
        (
            "How would I describe her?\x01",
            "Should I say she looks splendid or\x01",
            "should I say beautifully mature...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xA,
        (
            "If she could just find the right man,\x01",
            "then I could retire in peace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xA,
        (
            "Uh...never mind. I was just thinking\x01",
            "out loud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xA,
        (
            "Ah, yes, this may help: the mayor\x01",
            "has a maid accompanying her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xA,
        (
            "That might be the easiest way to\x01",
            "find her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        (
            "#010FThe mayor is being accompanied\x01",
            "by a maid, huh? That sounds easy\x01",
            "enough to find in a crowd of people.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #137
        0x101,
        (
            "#006FLet's hurry and head over to the\x01",
            "chapel.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x8)
    OP_4B(0xA, 0)
    EventEnd(0x0)
    Return()

    # Function_10_326E end

    def Function_11_3B85(): pass

    label("Function_11_3B85")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-120000, 0, 67000, 0)
    SetChrPos(0x8, -120760, 200, 68570, 180)
    SetChrPos(0x101, -118370, 0, 64050, 0)
    SetChrPos(0x102, -117260, 0, 64450, 315)
    SetChrPos(0x103, -117990, 0, 62790, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(314000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #138
        0x8,
        (
            "#612FDealing with complaints from\x01",
            "the citizens...\x02\x03",

            "Late deliveries of goods to the\x01",
            "Bose Market because of the\x01",
            "airspace being a no-fly zone...\x02\x03",

            "#615FServicing the sewer facilities...\x02\x03",

            "Selecting a congratulatory gift\x01",
            "for Her Majesty the Queen...\x02\x03",

            "Harm incurred by monsters on\x01",
            "the New Ansel Path...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #139
        0x8,
        (
            "#616FWhen will all this paperwork\x01",
            "finally end?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        "#008FUm...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 1)
    OP_6D(-120700, 0, 68200, 1000)

    ChrTalk(    #141
        0x8,
        (
            "#613FUh...hello?\x02\x03",

            "#617FOh, are you back already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        (
            "#010FYou look pretty busy...so would\x01",
            "it be better if we came back at\x01",
            "a later time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x8,
        (
            "#615FAhem! Ah, no, you're fine.\x02\x03",

            "#611FSo you found out something from\x01",
            "General Morgan, right? I'd like to\x01",
            "hear about it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-120570, 1000, 67100, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(314000, 0)
    OP_6E(280, 0)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x101, -120910, 0, 66260, 0)
    SetChrPos(0x102, -119750, 0, 66130, 0)
    SetChrPos(0x103, -120500, 0, 65129, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #144
        0x8,
        (
            "#615FGood work. I feel like I have a much\x01",
            "clearer picture of the situation now.\x02\x03",

            "First, there was a hijacking by\x01",
            "the sky bandits, and now a\x01",
            "ransom demand...?\x02\x03",

            "#612FThe situation is much more serious\x01",
            "than I had originally anticipated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#007FIf the general hadn't found out we\x01",
            "were bracers, I think we could\x01",
            "have learned more, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x8,
        (
            "#610FNo, it's all right. I'm just glad\x01",
            "to know that it wasn't a crash.\x02\x03",

            "With this information, I should be able\x01",
            "to take effective countermeasures\x01",
            "with the city.\x02\x03",

            "Now I need to think of a way to inform\x01",
            "the citizens of Bose and deal with the\x01",
            "families of the passengers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        (
            "#010FI imagine that'll be quite a difficult\x01",
            "task considering that you're already\x01",
            "as busy as you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "#611FHa ha, well, that's just the duty\x01",
            "of a mayor.\x02\x03",

            "#612FAnd since the identity of the\x01",
            "criminals is now known...\x02\x03",

            "May I ask that you continue your\x01",
            "investigation of the incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x103,
        (
            "#020FOf course. That was our plan to\x01",
            "begin with.\x02\x03",

            "We've already had a run-in with\x01",
            "these sky bandits before.\x02\x03",

            "And I'll wager the honor of the guild\x01",
            "that this is one group we cannot\x01",
            "simply leave up to the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#006FYeah, that's for sure!\x02\x03",

            "There's Dad to find, and then we need\x01",
            "to deal with these sky bandits once\x01",
            "and for all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        "#015F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #152
        0x101,
        "#000F#1PHuh? What's with the look, Joshua?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #153
        0x102,
        (
            "#013F#2PI was just thinking, and...\x02\x03",

            "No matter which way I look at\x01",
            "things, I just can't believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#002F#1PWhat can't you believe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x102,
        (
            "#012F#2PThat Dad could get beaten by\x01",
            "a bunch of sky bandits.\x02\x03",

            "Basing my judgment on the ability of\x01",
            "the group that appeared in Rolent...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x103,
        (
            "#022FI'm in agreement with you there.\x02\x03",

            "Cassius could have easily dealt\x01",
            "with a group of that caliber.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(    #157
        0x101,
        (
            "#007F#1PCome on, Joshua! You too, Schera!\x01",
            "You're giving him way more credit\x01",
            "than he deserves.\x02\x03",

            "He's pretty good, I'll give you that,\x01",
            "but I think it would be a bit of a\x01",
            "stretch to take on an entire group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        (
            "#613F...\x02\x03",

            "Umm, do you mind if I ask you\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_472F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_472F)

    def lambda_473D():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_473D)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #159
        0x8,
        (
            "#612FAre you trying to tell me that your\x01",
            "father was aboard that airliner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        (
            "#008FOh, didn't I mention that...?\x02\x03",

            "I'm embarrassed to say it, but\x01",
            "yeah, he was. Not to mention\x01",
            "he's a bracer, too.\x02\x03",

            "His name's Cassius Bright.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #161
        0x8,
        "#614FDid you just say...Cassius Bright?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        (
            "#004FUh...yeah. Why?\x02\x03",

            "Do you know my dad or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x8,
        (
            "#612FI've never met him in person,\x01",
            "but I've heard a great deal\x01",
            "about him.\x02\x03",

            "I'm sorry...I just don't know\x01",
            "what to say...\x02\x03",

            "But we might be able to use this to\x01",
            "get some information from the army...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        "#002FExcuse me, mayor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x8,
        (
            "#615FI'm very sorry, and I can empathize\x01",
            "with what you must be going through.\x02\x03",

            "#610FIf there's anything I can do to help\x01",
            "you clear up this incident, then I am\x01",
            "at your disposal.\x02\x03",

            "If there's anything you need,\x01",
            "please don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x400000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_3B85 end

    def Function_12_4AAA(): pass

    label("Function_12_4AAA")

    OP_A2(0x32B)
    OP_28(0x37, 0x4, 0x2)
    OP_28(0x37, 0x4, 0x4)
    OP_28(0xF, 0x4, 0x40)
    OP_28(0x10, 0x4, 0x40)
    OP_28(0x12, 0x4, 0x40)
    OP_28(0x17, 0x4, 0x40)
    EventBegin(0x0)
    OP_6D(-63360, 0, -3290, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x8, -64900, 200, -3990, 90)
    SetChrPos(0x101, -62760, 200, -5590, 0)
    SetChrPos(0x102, -60990, 200, -5640, 0)
    SetChrPos(0x103, -60990, 200, -2330, 180)
    SetChrPos(0x104, -62760, 200, -2330, 180)
    SetChrChipByIndex(0x8, 9)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x104, 8)
    SetChrSubChip(0x102, 1)
    SetChrSubChip(0x103, 2)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #166
        0x101,
        "#007FI can't believe you were released.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x103,
        "#027FIt's like a stroke of bad luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x104,
        (
            "#031FHa ha ha. Please don't lay on\x01",
            "the compliments so thick.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 2)
    Sleep(300)

    ChrTalk(    #169
        0x104,
        (
            "#030FHowever, it pains my soul that\x01",
            "I partook of such a fine wine\x01",
            "without paying a single mira.\x02\x03",

            "Shall I play the piano in the restaurant\x01",
            "per our contract to remedy that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        (
            "#610FI think I'm going to have to\x01",
            "pass on that.\x02\x03",

            "After what happened, I think it\x01",
            "would be a bit awkward having\x01",
            "you back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#007F(I for one, don't think he'd mind\x01",
            "a bit...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x102,
        (
            "#019F(Yeah, he sure does seem to\x01",
            "have some thick skin...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#610FLet's just think of this as an\x01",
            "unfortunate incident for the\x01",
            "both of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x104,
        (
            "#033FBut...I don't think I can just let\x01",
            "things go like this...\x02\x03",

            "Let's see...\x02\x03",

            "#030FIt seems like you're investigating\x01",
            "something at the moment, right?\x02\x03",

            "How about I lend my assistance\x01",
            "in return for the wine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x8,
        (
            "#611FWell, that does sound interesting.\x02\x03",

            "Could I ask you to join these\x01",
            "bracers in their work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x104,
        "#030FHa, could you ever!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0)
    Sleep(300)

    ChrTalk(    #178
        0x104,
        (
            "#031FSo it's settled! Let our new working\x01",
            "relationship bloom like a magnolia\x01",
            "at the height of spring!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        (
            "#009FHold on a sec... Wh-What did we\x01",
            "do to deserve this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x103,
        (
            "#020FYour general weirdness aside, simply\x01",
            "having an amateur like you around is\x01",
            "honestly going to be a pain...\x02\x03",

            "Are you confident that you won't be a\x01",
            "drag on our work? Or our sanity...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 1)
    Sleep(300)

    ChrTalk(    #181
        0x104,
        (
            "#035F#6PWell, I'm somewhat confident in\x01",
            "my marksmanship and magic.\x02\x03",

            "But of course, I'd be distressed\x01",
            "if you tried to list my music\x01",
            "genius in the same group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#007FThat's the kind of line that\x01",
            "gets me really worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x102,
        (
            "#010FBut maybe we could use an extra\x01",
            "hand.\x02\x03",

            "As long as we can't count on the army\x01",
            "to help us out, I have the feeling\x01",
            "that we'll be short on manpower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x103,
        (
            "#026F...\x02\x03",

            "#020FWell, all right, then. We'll use you\x01",
            "for what you're worth.\x02\x03",

            "However, if we do happen to conclude\x01",
            "that you're not worth your weight,\x01",
            "you're dumped from the party.\x02\x03",

            "Are you going to be okay with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x104,
        (
            "#031F#6PHa ha, of course I don't mind.\x02\x03",

            "I'd never let you down, so please\x01",
            "be reassured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#008FWell, my expectations of you are\x01",
            "pretty much at rock bottom anyway,\x01",
            "so I know you won't let ME down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x8,
        (
            "#615FHeehee. I'm glad things\x01",
            "are settled between you all.\x02\x03",

            "#612FBut before you go, there's something\x01",
            "I need to tell you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0x104, 0)
    Sleep(100)
    SetChrSubChip(0x104, 2)
    Sleep(300)

    ChrTalk(    #188
        0x101,
        "#501F#2PTell us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x103,
        (
            "#020FActually, the town DID seem\x01",
            "pretty noisy as we were headed\x01",
            "here...\x02\x03",

            "What happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x8,
        (
            "#612FTruth be told...\x02\x03",

            "Last night, there was a large-scale\x01",
            "burglary in Bose's south block.\x02\x03",

            "The weapon shop and orbal factory\x01",
            "were targeted, as were a number of\x01",
            "private residences.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #191
        0x101,
        "#004F#2PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x102,
        (
            "#012F#2PSo...was this the work of the\x01",
            "sky bandits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x8,
        (
            "#612FIt's unknown at this time,\x01",
            "but it seems highly probable.\x02\x03",

            "A unit of the Royal Army is currently\x01",
            "conducting an investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x103,
        (
            "#022FI see. Guess we'd better do an\x01",
            "investigation of our own, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x8,
        (
            "#610FYes. I'd like to formally request\x01",
            "that you do just that.\x02\x03",

            "I'll send a payment over to the\x01",
            "guild for the work you've done\x01",
            "so far.\x02\x03",

            "Please make use of the money\x01",
            "for your current investigation\x01",
            "expenses.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x35, 0x4, 0x10)
    OP_28(0x36, 0x4, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x101, 3450, 0, -5820, 0)
    SetChrPos(0x102, 4730, 0, -4890, 315)
    SetChrPos(0x103, 2900, 0, -4059, 135)
    SetChrPos(0x104, 4170, 0, -3340, 180)
    SetChrPos(0xA, -6290, 500, -8460, 296)
    SetChrPos(0x8, -120760, 0, 68570, 180)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x104, 65535)
    TurnDirection(0x101, 0x104, 0)
    TurnDirection(0x102, 0x103, 0)
    TurnDirection(0x103, 0x102, 0)
    TurnDirection(0x104, 0x101, 0)
    OP_6D(2900, 0, -3860, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #196
        0x101,
        (
            "#006F#1PI have a feeling that the army is\x01",
            "going to get in our way again...\x02\x03",

            "But I guess when that happens,\x01",
            "it happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x102,
        (
            "#012F#2PWhether they get in our way or\x01",
            "not...\x02\x03",

            "I don't think we should be forthcoming\x01",
            "with the army about any information\x01",
            "we come across.\x02\x03",

            "Because if there's really a spy\x01",
            "in their midst, they'll just leak\x01",
            "it to the sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x103,
        (
            "#020F#6PThough I'm reluctant to say it,\x01",
            "I also think it's for the best to\x01",
            "keep quiet about our findings.\x02\x03",

            "Anyway, let's act with prudence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x104,
        (
            "#035F#2P#4PAll-righty, my bosom companions!\x01",
            "Shall we head to the south block?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        (
            "#005F#1PLook, buddy, who made you king\x01",
            "of the show?!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_12_4AAA end

    SaveToFile()

Try(main)
