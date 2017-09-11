from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3211   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3211.x',
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
        'Percy',                                # 9
        'Ed',                                   # 10
        'Lynn',                                 # 11
        'Recia',                                # 12
        'Cyril',                                # 13
        'Addy',                                 # 14
        'Lucky',                                # 15
        'Sima',                                 # 16
        'Quantay',                              # 17
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01030 ._CH',             # 02
        'ED6_DT07/CH01150 ._CH',             # 03
        'ED6_DT07/CH01120 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01160 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH01060 ._CH',             # 08
        'ED6_DT07/CH01153 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01030P._CP',             # 02
        'ED6_DT07/CH01150P._CP',             # 03
        'ED6_DT07/CH01120P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01160P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH01060P._CP',             # 08
        'ED6_DT07/CH01153P._CP',             # 09
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )


    ScpFunction(
        "Function_0_21A",          # 00, 0
        "Function_1_4AB",          # 01, 1
        "Function_2_4AC",          # 02, 2
        "Function_3_4C2",          # 03, 3
        "Function_4_4C9",          # 04, 4
        "Function_5_554",          # 05, 5
        "Function_6_CC7",          # 06, 6
        "Function_7_F13",          # 07, 7
        "Function_8_14AB",         # 08, 8
        "Function_9_16DA",         # 09, 9
        "Function_10_1866",        # 0A, 10
        "Function_11_186D",        # 0B, 11
    )


    def Function_0_21A(): pass

    label("Function_0_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_255")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 1960, 250, 8900, 0)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4AA")

    label("loc_255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_28B")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3430, 0, 4050, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4AA")

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2C1")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -3460, 250, 8840, 350)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4AA")

    label("loc_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_32A")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1330, 250, 8540, 104)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 33700, 250, 7700, 171)
    TurnDirection(0xA, 0xB, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1880, 250, 8350, 276)
    Jump("loc_4AA")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_3A4")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3820, 0, 2790, 100)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 9)
    OP_44(0xB, 0x0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 29020, 250, 7120, 270)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2530, 0, 4070, 6)
    Jump("loc_4AA")

    label("loc_3A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_3C4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 29020, 250, 7010, 255)
    Jump("loc_4AA")

    label("loc_3C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_410")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3430, 0, 4050, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 29020, 250, 7010, 255)
    Jump("loc_4AA")

    label("loc_410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_472")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 27220, 250, 6680, 96)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 29020, 250, 7010, 255)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3430, 0, 4050, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4AA")

    label("loc_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4AA")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -2080, 250, 6150, 195)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)

    label("loc_4AA")

    Return()

    # Function_0_21A end

    def Function_1_4AB(): pass

    label("Function_1_4AB")

    Return()

    # Function_1_4AB end

    def Function_2_4AC(): pass

    label("Function_2_4AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4AC")

    label("loc_4C1")

    Return()

    # Function_2_4AC end

    def Function_3_4C2(): pass

    label("Function_3_4C2")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_3_4C2 end

    def Function_4_4C9(): pass

    label("Function_4_4C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4D6")
    Jump("loc_550")

    label("loc_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4E0")
    Jump("loc_550")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4EA")
    Jump("loc_550")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4F4")
    Jump("loc_550")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4FE")
    Jump("loc_550")

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_508")
    Jump("loc_550")

    label("loc_508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_512")
    Jump("loc_550")

    label("loc_512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_549")

    ChrTalk(    #0
        0xFE,
        "Hey, Lynn!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Bring me some more tea!\x02",
    )

    CloseMessageWindow()
    Jump("loc_550")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_550")

    label("loc_550")

    TalkEnd(0xFE)
    Return()

    # Function_4_4C9 end

    def Function_5_554(): pass

    label("Function_5_554")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_6B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_617")

    ChrTalk(    #2
        0xFE,
        (
            "The town seems so quiet when\x01",
            "there aren't any visitors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Thanks to all this quiet,\x01",
            "my daughter slept in today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I should send her to an\x01",
            "apprenticeship somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B1")

    label("loc_617")

    OP_A2(0x2)

    ChrTalk(    #5
        0xFE,
        (
            "The town seems so quiet when\x01",
            "there aren't any visitors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "It would be so nice if we could\x01",
            "have a normal, quiet Birthday\x01",
            "Celebration this year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B1")

    Jump("loc_CC3")

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_850")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_777")

    ChrTalk(    #7
        0xFE,
        (
            "When you're married, you end\x01",
            "up worrying more about dinner\x01",
            "tonight than world events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "It doesn't matter what's going\x01",
            "on in the world, my daughter\x01",
            "will still be hungry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84D")

    label("loc_777")

    OP_A2(0x2)

    ChrTalk(    #9
        0xFE,
        (
            "The Queen's Birthday Celebration\x01",
            "is coming up, but what a time\x01",
            "for it to come this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Not that worrying about it\x01",
            "will change all that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I've got to figure out what\x01",
            "we're having for dinner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84D")

    Jump("loc_CC3")

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_90C")

    ChrTalk(    #12
        0xFE,
        (
            "It sounds like something big\x01",
            "happened over in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "The world's getting to be quite\x01",
            "a scary place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I hope all that insanity doesn't\x01",
            "find its way to this place...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC3")

    label("loc_90C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_972")

    ChrTalk(    #15
        0xFE,
        "Recia! Stop slouching!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Here I am, tired as all get out,\x01",
            "making breakfast for you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC3")

    label("loc_972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9D4")

    ChrTalk(    #17
        0xFE,
        "What a daughter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "She's just like my husband\x01",
            "when he was a young man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A46")

    label("loc_9D4")

    OP_A2(0x2)
    OP_8C(0xA, 0, 400)

    ChrTalk(    #19
        0xFE,
        (
            "Recia. If you're so hungry, why\x01",
            "not help with the cooking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "It'd get finished faster...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 400)

    label("loc_A46")

    Jump("loc_CC3")

    label("loc_A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_A53")
    Jump("loc_CC3")

    label("loc_A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_ADD")

    ChrTalk(    #21
        0xFE,
        (
            "Why do I have to bring him\x01",
            "his tea? I'm working!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "If he wants it so bad, he should\x01",
            "come and get it himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA8")

    label("loc_ADD")

    OP_A2(0x2)

    ChrTalk(    #23
        0xFE,
        (
            "My husband and daughter think\x01",
            "the work stops when they're\x01",
            "finished eating...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "But somebody's got to clean\x01",
            "everything up and wash all\x01",
            "the dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Maybe I should just...not do\x01",
            "it one day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA8")

    Jump("loc_CC3")

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_C27")

    ChrTalk(    #26
        0xFE,
        (
            "Hmm...\x01",
            "Time to get ready for lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I'm almost out of seasonings.\x01",
            "I'll need to go buy more soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC3")

    label("loc_C27")

    OP_A2(0x2)

    ChrTalk(    #28
        0xFE,
        (
            "My husband is a chef in the\x01",
            "hotel kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "His food is famous with all\x01",
            "the visitors here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "He even got written about in\x01",
            "some tourist book!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC3")

    TalkEnd(0xFE)
    Return()

    # Function_5_554 end

    def Function_6_CC7(): pass

    label("Function_6_CC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_CD4")
    Jump("loc_F0F")

    label("loc_CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_CDE")
    Jump("loc_F0F")

    label("loc_CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_CE8")
    Jump("loc_F0F")

    label("loc_CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_D9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D25")

    ChrTalk(    #31
        0xFE,
        "*yawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "I didn't get enough sleep.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D97")

    label("loc_D25")

    OP_A2(0x3)

    ChrTalk(    #33
        0xFE,
        "*yawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Dad always gets up super-early,\x01",
            "and makes a TON of noise...and\x01",
            "I can never get back to sleep.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D97")

    Jump("loc_F0F")

    label("loc_D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_E04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_DE2")

    ChrTalk(    #35
        0xFE,
        "Mom, I'm hungry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "I'm starving to DEATH here!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E01")

    label("loc_DE2")

    OP_A2(0x3)

    ChrTalk(    #37
        0xFE,
        "Mom, is it ready yet?!\x02",
    )

    CloseMessageWindow()

    label("loc_E01")

    Jump("loc_F0F")

    label("loc_E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_EB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E4C")

    ChrTalk(    #38
        0xFE,
        "Wow, evening already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "I don't like the dark!\x02",
    )

    CloseMessageWindow()
    Jump("loc_EB1")

    label("loc_E4C")

    OP_A2(0x3)

    ChrTalk(    #40
        0xFE,
        (
            "Goddess, watching the house\x01",
            "can be so BORING.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I'm so hungry. I hope Mom gets\x01",
            "back soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB1")

    Jump("loc_F0F")

    label("loc_EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_EBE")
    Jump("loc_F0F")

    label("loc_EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_F08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_EE2")

    ChrTalk(    #42
        0xFE,
        "Mmm...snacks!\x02",
    )

    CloseMessageWindow()
    Jump("loc_F05")

    label("loc_EE2")

    OP_A2(0x3)

    ChrTalk(    #43
        0xFE,
        "Mom, I want some tea, too!\x02",
    )

    CloseMessageWindow()

    label("loc_F05")

    Jump("loc_F0F")

    label("loc_F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_F0F")

    label("loc_F0F")

    TalkEnd(0xFE)
    Return()

    # Function_6_CC7 end

    def Function_7_F13(): pass

    label("Function_7_F13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_FF2")

    ChrTalk(    #44
        0xFE,
        (
            "For once we had no guests today.\x01",
            "I got the day off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Still though, I can't believe the\x01",
            "cuckoo in the Maple Leaf Inn\x01",
            "actually sang for once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Her Highness has got some\x01",
            "royal authority, you bet'cha.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A7")

    label("loc_FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_FFC")
    Jump("loc_14A7")

    label("loc_FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_10E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_104F")

    ChrTalk(    #47
        0xFE,
        "Well, time for work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "I hope they catch those criminals.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10E6")

    label("loc_104F")

    OP_A2(0x4)

    ChrTalk(    #49
        0xFE,
        (
            "I heard they still haven't caught\x01",
            "those criminals in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "There's an army base near the\x01",
            "town, so I'd like to believe\x01",
            "things are safe...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E6")

    Jump("loc_14A7")

    label("loc_10E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1174")
    TurnDirection(0xFE, 0xE, 0)

    ChrTalk(    #51
        0xFE,
        (
            "C'mon, Lucky! Rise and shine!\x01",
            "It's breakfast time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "You slouch around too long,\x01",
            "and Daddy's gonna eat your\x01",
            "food!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A7")

    label("loc_1174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_12EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_11CA")
    TurnDirection(0xFE, 0xE, 0)

    ChrTalk(    #53
        0xFE,
        (
            "Here Lucky.\x01",
            "Cut the bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "I'll get the stew ready.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12EB")

    label("loc_11CA")

    OP_A2(0x4)

    ChrTalk(    #55
        0xFE,
        (
            "I used to live in Zeiss a long\x01",
            "time ago, but I like it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "I moved here with my wife Addy\x01",
            "when Lucky was born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Zeiss is a more convenient place,\x01",
            "but living here agrees with me more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "It's pretty nice being able to\x01",
            "jump into the hot springs\x01",
            "whenever I feel like it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EB")

    Jump("loc_14A7")

    label("loc_12EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_12F8")
    Jump("loc_14A7")

    label("loc_12F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_1302")
    Jump("loc_14A7")

    label("loc_1302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_130C")
    Jump("loc_14A7")

    label("loc_130C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_14A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_13DB")

    ChrTalk(    #59
        0xFE,
        (
            "Actually I work at the Maple\x01",
            "Leaf Inn...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "...but it really is a nice place.\x01",
            "You should come by!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Of course, why should you trust\x01",
            "the recommendation of one of\x01",
            "the place's staff?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A7")

    label("loc_13DB")

    OP_A2(0x4)

    ChrTalk(    #62
        0xFE,
        (
            "Are you looking for a place to\x01",
            "stay for the night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "The Maple Leaf Inn is on the\x01",
            "other side of town, just past\x01",
            "the hot water tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "It's a nice place. You should\x01",
            "stop by and have a look!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A7")

    TalkEnd(0xFE)
    Return()

    # Function_7_F13 end

    def Function_8_14AB(): pass

    label("Function_8_14AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_14B8")
    Jump("loc_16D6")

    label("loc_14B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_15BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_150B")

    ChrTalk(    #65
        0xFE,
        "I should get dinner ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "I wonder what to make today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BC")

    label("loc_150B")

    OP_A2(0x5)

    ChrTalk(    #67
        0xFE,
        "I saw Lucky just outside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Kids are so resilient. Even after\x01",
            "hearing that terrible news he's\x01",
            "back out playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "I hope everyone can stay safe\x01",
            "living in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BC")

    Jump("loc_16D6")

    label("loc_15BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_15C9")
    Jump("loc_16D6")

    label("loc_15C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_15D3")
    Jump("loc_16D6")

    label("loc_15D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_15DD")
    Jump("loc_16D6")

    label("loc_15DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_15E7")
    Jump("loc_16D6")

    label("loc_15E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1648")

    ChrTalk(    #70
        0xFE,
        "Maybe I'll warm up the stew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Yes. And add one more\x01",
            "vegetable...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CC")

    label("loc_1648")

    OP_A2(0x5)

    ChrTalk(    #72
        0xFE,
        (
            "I should start getting dinner ready\x01",
            "during the post-lunch downtime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Working two jobs can be so\x01",
            "exhausting sometimes...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CC")

    Jump("loc_16D6")

    label("loc_16CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_16D6")

    label("loc_16D6")

    TalkEnd(0xFE)
    Return()

    # Function_8_14AB end

    def Function_9_16DA(): pass

    label("Function_9_16DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_16E7")
    Jump("loc_1862")

    label("loc_16E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_16F1")
    Jump("loc_1862")

    label("loc_16F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_16FB")
    Jump("loc_1862")

    label("loc_16FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1721")

    ChrTalk(    #74
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "*yawn*\x02",
    )

    CloseMessageWindow()
    Jump("loc_1742")

    label("loc_1721")

    OP_A2(0x6)

    ChrTalk(    #76
        0xFE,
        "Ohhh...I'm still sleepy.\x02",
    )

    CloseMessageWindow()

    label("loc_1742")

    Jump("loc_1862")

    label("loc_1745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_183D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_17CF")

    ChrTalk(    #77
        0xFE,
        (
            "Dad hates housework.\x01",
            "He's real bad at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "That's why he works at\x01",
            "the inn. So he can avoid\x01",
            "it most of the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183A")

    label("loc_17CF")

    OP_A2(0x6)
    TurnDirection(0xFE, 0xC, 0)

    ChrTalk(    #79
        0xFE,
        (
            "Okay Dad, let's get that\x01",
            "stew warmed up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "And while it's heating,\x01",
            "I'll slice the bread.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183A")

    Jump("loc_1862")

    label("loc_183D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_1847")
    Jump("loc_1862")

    label("loc_1847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_1851")
    Jump("loc_1862")

    label("loc_1851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_185B")
    Jump("loc_1862")

    label("loc_185B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1862")

    label("loc_1862")

    TalkEnd(0xFE)
    Return()

    # Function_9_16DA end

    def Function_10_1866(): pass

    label("Function_10_1866")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_1866 end

    def Function_11_186D(): pass

    label("Function_11_186D")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_186D end

    SaveToFile()

Try(main)
