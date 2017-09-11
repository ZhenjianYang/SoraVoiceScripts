from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3210   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'ED6_DT07/CH01273 ._CH',             # 09
        'ED6_DT07/CH01153 ._CH',             # 0A
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
        'ED6_DT07/CH01273P._CP',             # 09
        'ED6_DT07/CH01153P._CP',             # 0A
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
        "Function_0_222",          # 00, 0
        "Function_1_4C1",          # 01, 1
        "Function_2_4E3",          # 02, 2
        "Function_3_4F9",          # 03, 3
        "Function_4_500",          # 04, 4
        "Function_5_58B",          # 05, 5
        "Function_6_D6F",          # 06, 6
        "Function_7_FE7",          # 07, 7
        "Function_8_157F",         # 08, 8
        "Function_9_17AE",         # 09, 9
        "Function_10_193A",        # 0A, 10
        "Function_11_1941",        # 0B, 11
    )


    def Function_0_222(): pass

    label("Function_0_222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_258")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 1750, 250, 8900, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4C0")

    label("loc_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_28E")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3430, 0, 4050, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4C0")

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2C4")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -3460, 250, 8840, 350)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4C0")

    label("loc_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_32D")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1330, 250, 8540, 104)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 33700, 250, 7700, 171)
    TurnDirection(0xA, 0xB, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1880, 250, 8350, 276)
    Jump("loc_4C0")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_394")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3820, 0, 2790, 100)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 29020, 250, 7010, 255)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2530, 0, 4070, 6)
    Jump("loc_4C0")

    label("loc_394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_3B4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 28000, 250, 5350, 0)
    Jump("loc_4C0")

    label("loc_3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_413")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3430, 0, 4050, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 10)
    OP_44(0xB, 0x0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 29020, 250, 7120, 270)
    Jump("loc_4C0")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_48D")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x9, 28090, 0, 8600, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 10)
    OP_44(0xB, 0x0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 29020, 250, 7120, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3430, 0, 4050, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)
    Jump("loc_4C0")

    label("loc_48D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4C0")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -3600, 250, 8850, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27020, 0, 2570, 277)

    label("loc_4C0")

    Return()

    # Function_0_222 end

    def Function_1_4C1(): pass

    label("Function_1_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D9")
    OP_B1("t3210_y")
    Jump("loc_4E2")

    label("loc_4D9")

    OP_B1("t3210_n")

    label("loc_4E2")

    Return()

    # Function_1_4C1 end

    def Function_2_4E3(): pass

    label("Function_2_4E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4E3")

    label("loc_4F8")

    Return()

    # Function_2_4E3 end

    def Function_3_4F9(): pass

    label("Function_3_4F9")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_3_4F9 end

    def Function_4_500(): pass

    label("Function_4_500")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_50D")
    Jump("loc_587")

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_517")
    Jump("loc_587")

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_521")
    Jump("loc_587")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_52B")
    Jump("loc_587")

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_535")
    Jump("loc_587")

    label("loc_535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_53F")
    Jump("loc_587")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_549")
    Jump("loc_587")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_580")

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
    Jump("loc_587")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_587")

    label("loc_587")

    TalkEnd(0xFE)
    Return()

    # Function_4_500 end

    def Function_5_58B(): pass

    label("Function_5_58B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_6EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_64E")

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
    Jump("loc_6E8")

    label("loc_64E")

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

    label("loc_6E8")

    Jump("loc_D6B")

    label("loc_6EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_887")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7AE")

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
    Jump("loc_884")

    label("loc_7AE")

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

    label("loc_884")

    Jump("loc_D6B")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_943")

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
    Jump("loc_D6B")

    label("loc_943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_9B0")
    TurnDirection(0xFE, 0xB, 0)

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
    Jump("loc_D6B")

    label("loc_9B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_A79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_A12")

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
    Jump("loc_A76")

    label("loc_A12")

    OP_A2(0x2)

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

    label("loc_A76")

    Jump("loc_D6B")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_A83")
    Jump("loc_D6B")

    label("loc_A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_ADF")

    ChrTalk(    #21
        0xFE,
        (
            "You know what'd be great?\x01",
            "If my husband bothered to\x01",
            "clean a dish. Just once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D6B")

    label("loc_ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B69")

    ChrTalk(    #22
        0xFE,
        (
            "Why do I have to bring him\x01",
            "his tea? I'm working!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "If he wants it so bad, he should\x01",
            "come and get it himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C50")

    label("loc_B69")

    OP_A2(0x2)

    ChrTalk(    #24
        0xFE,
        (
            "My husband and daughter think\x01",
            "the work stops when they're\x01",
            "finished eating...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "But somebody's got to clean\x01",
            "everything up and wash all\x01",
            "the dishes.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0xFE,
        (
            "Maybe I should just...not do\x01",
            "it one day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C50")

    Jump("loc_D6B")

    label("loc_C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_CCF")

    ChrTalk(    #27
        0xFE,
        (
            "Hmm...\x01",
            "Time to get ready for lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I'm almost out of seasonings.\x01",
            "I'll need to go buy more soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D6B")

    label("loc_CCF")

    OP_A2(0x2)

    ChrTalk(    #29
        0xFE,
        (
            "My husband is a chef in the\x01",
            "hotel kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "His food is famous with all\x01",
            "the visitors here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "He even got written about in\x01",
            "some tourist book!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6B")

    TalkEnd(0xFE)
    Return()

    # Function_5_58B end

    def Function_6_D6F(): pass

    label("Function_6_D6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_D7C")
    Jump("loc_FE3")

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_D86")
    Jump("loc_FE3")

    label("loc_D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_D90")
    Jump("loc_FE3")

    label("loc_D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_DCD")

    ChrTalk(    #32
        0xFE,
        "*yawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "I didn't get enough sleep.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E3F")

    label("loc_DCD")

    OP_A2(0x3)

    ChrTalk(    #34
        0xFE,
        "*yawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Dad always gets up super-early,\x01",
            "and makes a TON of noise...and\x01",
            "I can never get back to sleep.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3F")

    Jump("loc_FE3")

    label("loc_E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_EAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E8A")

    ChrTalk(    #36
        0xFE,
        "Mom, I'm hungry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "I'm starving to DEATH here!\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA9")

    label("loc_E8A")

    OP_A2(0x3)

    ChrTalk(    #38
        0xFE,
        "Mom, is it ready yet?!\x02",
    )

    CloseMessageWindow()

    label("loc_EA9")

    Jump("loc_FE3")

    label("loc_EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_F5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_EF4")

    ChrTalk(    #39
        0xFE,
        "Wow, evening already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "I don't like the dark!\x02",
    )

    CloseMessageWindow()
    Jump("loc_F59")

    label("loc_EF4")

    OP_A2(0x3)

    ChrTalk(    #41
        0xFE,
        (
            "Goddess, watching the house\x01",
            "can be so BORING.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I'm so hungry. I hope Mom gets\x01",
            "back soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F59")

    Jump("loc_FE3")

    label("loc_F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_F92")

    ChrTalk(    #43
        0xFE,
        "All right, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "What to do...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE3")

    label("loc_F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_FB6")

    ChrTalk(    #45
        0xFE,
        "Mmm...snacks!\x02",
    )

    CloseMessageWindow()
    Jump("loc_FD9")

    label("loc_FB6")

    OP_A2(0x3)

    ChrTalk(    #46
        0xFE,
        "Mom, I want some tea, too!\x02",
    )

    CloseMessageWindow()

    label("loc_FD9")

    Jump("loc_FE3")

    label("loc_FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_FE3")

    label("loc_FE3")

    TalkEnd(0xFE)
    Return()

    # Function_6_D6F end

    def Function_7_FE7(): pass

    label("Function_7_FE7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_10C6")

    ChrTalk(    #47
        0xFE,
        (
            "For once we had no guests today.\x01",
            "I got the day off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Still though, I can't believe the\x01",
            "cuckoo in the Maple Leaf Inn\x01",
            "actually sang for once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Her Highness has got some\x01",
            "royal authority, you bet'cha.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157B")

    label("loc_10C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_10D0")
    Jump("loc_157B")

    label("loc_10D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_11BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1123")

    ChrTalk(    #50
        0xFE,
        "Well, time for work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "I hope they catch those criminals.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11BA")

    label("loc_1123")

    OP_A2(0x4)

    ChrTalk(    #52
        0xFE,
        (
            "I heard they still haven't caught\x01",
            "those criminals in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "There's an army base near the\x01",
            "town, so I'd like to believe\x01",
            "things are safe...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11BA")

    Jump("loc_157B")

    label("loc_11BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1248")
    TurnDirection(0xFE, 0xE, 0)

    ChrTalk(    #54
        0xFE,
        (
            "C'mon, Lucky! Rise and shine!\x01",
            "It's breakfast time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "You slouch around too long,\x01",
            "and Daddy's gonna eat your\x01",
            "food!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157B")

    label("loc_1248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_13C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_129E")
    TurnDirection(0xFE, 0xE, 0)

    ChrTalk(    #56
        0xFE,
        (
            "Here Lucky.\x01",
            "Cut the bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "I'll get the stew ready.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13BF")

    label("loc_129E")

    OP_A2(0x4)

    ChrTalk(    #58
        0xFE,
        (
            "I used to live in Zeiss a long\x01",
            "time ago, but I like it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "I moved here with my wife Addy\x01",
            "when Lucky was born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Zeiss is a more convenient place,\x01",
            "but living here agrees with me more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "It's pretty nice being able to jump\x01",
            "into the hot springs whenever\x01",
            "I feel like it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BF")

    Jump("loc_157B")

    label("loc_13C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_13CC")
    Jump("loc_157B")

    label("loc_13CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_13D6")
    Jump("loc_157B")

    label("loc_13D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_13E0")
    Jump("loc_157B")

    label("loc_13E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_157B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_14AF")

    ChrTalk(    #62
        0xFE,
        (
            "Actually I work at the Maple\x01",
            "Leaf Inn...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "...but it really is a nice place.\x01",
            "You should come by!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Of course, why should you trust\x01",
            "the recommendation of one of\x01",
            "the place's staff?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157B")

    label("loc_14AF")

    OP_A2(0x4)

    ChrTalk(    #65
        0xFE,
        (
            "Are you looking for a place to\x01",
            "stay for the night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "The Maple Leaf Inn is on the\x01",
            "other side of town, just past\x01",
            "the hot water tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "It's a nice place. You should\x01",
            "stop by and have a look!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157B")

    TalkEnd(0xFE)
    Return()

    # Function_7_FE7 end

    def Function_8_157F(): pass

    label("Function_8_157F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_158C")
    Jump("loc_17AA")

    label("loc_158C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1693")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_15DF")

    ChrTalk(    #68
        0xFE,
        "I should get dinner ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "I wonder what to make today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1690")

    label("loc_15DF")

    OP_A2(0x5)

    ChrTalk(    #70
        0xFE,
        "I saw Lucky just outside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Kids are so resilient. Even after\x01",
            "hearing that terrible news he's\x01",
            "back out playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I hope everyone can stay safe\x01",
            "living in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1690")

    Jump("loc_17AA")

    label("loc_1693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_169D")
    Jump("loc_17AA")

    label("loc_169D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_16A7")
    Jump("loc_17AA")

    label("loc_16A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_16B1")
    Jump("loc_17AA")

    label("loc_16B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_16BB")
    Jump("loc_17AA")

    label("loc_16BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_171C")

    ChrTalk(    #73
        0xFE,
        "Maybe I'll warm up the stew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "Yes. And add one more\x01",
            "vegetable...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A0")

    label("loc_171C")

    OP_A2(0x5)

    ChrTalk(    #75
        0xFE,
        (
            "I should start getting dinner ready\x01",
            "during the post-lunch downtime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Working two jobs can be so\x01",
            "exhausting sometimes...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A0")

    Jump("loc_17AA")

    label("loc_17A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_17AA")

    label("loc_17AA")

    TalkEnd(0xFE)
    Return()

    # Function_8_157F end

    def Function_9_17AE(): pass

    label("Function_9_17AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_17BB")
    Jump("loc_1936")

    label("loc_17BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_17C5")
    Jump("loc_1936")

    label("loc_17C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_17CF")
    Jump("loc_1936")

    label("loc_17CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1819")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_17F5")

    ChrTalk(    #77
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "*yawn*\x02",
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_17F5")

    OP_A2(0x6)

    ChrTalk(    #79
        0xFE,
        "Ohhh...I'm still sleepy.\x02",
    )

    CloseMessageWindow()

    label("loc_1816")

    Jump("loc_1936")

    label("loc_1819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1911")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_18A3")

    ChrTalk(    #80
        0xFE,
        (
            "Dad hates housework.\x01",
            "He's real bad at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "That's why he works at\x01",
            "the inn. So he can avoid\x01",
            "it most of the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190E")

    label("loc_18A3")

    OP_A2(0x6)
    TurnDirection(0xFE, 0xC, 0)

    ChrTalk(    #82
        0xFE,
        (
            "Okay Dad, let's get that\x01",
            "stew warmed up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "And while it's heating,\x01",
            "I'll slice the bread.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190E")

    Jump("loc_1936")

    label("loc_1911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_191B")
    Jump("loc_1936")

    label("loc_191B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_1925")
    Jump("loc_1936")

    label("loc_1925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_192F")
    Jump("loc_1936")

    label("loc_192F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1936")

    label("loc_1936")

    TalkEnd(0xFE)
    Return()

    # Function_9_17AE end

    def Function_10_193A(): pass

    label("Function_10_193A")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_193A end

    def Function_11_1941(): pass

    label("Function_11_1941")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_1941 end

    SaveToFile()

Try(main)
