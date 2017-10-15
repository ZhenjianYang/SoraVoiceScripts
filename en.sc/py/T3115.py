from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3115   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3115.x',
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
        'Factory Chief Murdock',                # 9
        'Constance',                            # 10
        'Muriel',                               # 11
        'Maintenance Chief Gustav',             # 12
        'Hugo',                                 # 13
        'Prometheus',                           # 14
        'Professor Russell',                    # 15
        'Louise',                               # 16
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
        'ED6_DT07/CH02620 ._CH',             # 00
        'ED6_DT07/CH02623 ._CH',             # 01
        'ED6_DT07/CH01230 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
        'ED6_DT07/CH02440 ._CH',             # 04
        'ED6_DT07/CH01680 ._CH',             # 05
        'ED6_DT07/CH01100 ._CH',             # 06
        'ED6_DT07/CH02020 ._CH',             # 07
        'ED6_DT07/CH01430 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02620P._CP',             # 00
        'ED6_DT07/CH02623P._CP',             # 01
        'ED6_DT07/CH01230P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
        'ED6_DT07/CH02440P._CP',             # 04
        'ED6_DT07/CH01680P._CP',             # 05
        'ED6_DT07/CH01100P._CP',             # 06
        'ED6_DT07/CH02020P._CP',             # 07
        'ED6_DT07/CH01430P._CP',             # 08
    )

    DeclNpc(
        X                   = 4380,
        Z                   = 0,
        Y                   = 2370,
        Direction           = 90,
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
        X                   = -107400,
        Z                   = 0,
        Y                   = -90,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -104390,
        Z                   = 0,
        Y                   = 8560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -103940,
        Z                   = 0,
        Y                   = 98950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -102540,
        Z                   = 0,
        Y                   = 97610,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -103430,
        Z                   = 0,
        Y                   = 108150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 2430,
        Z                   = 0,
        Y                   = 2850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -102520,
        Z                   = 0,
        Y                   = 96150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )


    ScpFunction(
        "Function_0_1F2",          # 00, 0
        "Function_1_34C",          # 01, 1
        "Function_2_3BB",          # 02, 2
        "Function_3_2197",         # 03, 3
        "Function_4_21E8",         # 04, 4
        "Function_5_229C",         # 05, 5
        "Function_6_2822",         # 06, 6
        "Function_7_2F85",         # 07, 7
        "Function_8_366D",         # 08, 8
        "Function_9_40AC",         # 09, 9
        "Function_10_4751",        # 0A, 10
        "Function_11_4D6F",        # 0B, 11
        "Function_12_537F",        # 0C, 12
        "Function_13_58AF",        # 0D, 13
    )


    def Function_0_1F2(): pass

    label("Function_0_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 3)), scpexpr(EXPR_END)), "loc_1FE")
    ClearChrFlags(0xB, 0x10)

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_25F")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 1)
    SetChrPos(0x8, 2430, 200, 5330, 180)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0xD, -103580, 0, 99360, 180)
    ClearChrFlags(0xF, 0x80)
    OP_8C(0xF, 270, 0)
    ClearChrFlags(0xF, 0x10)
    OP_8C(0xC, 270, 0)
    Jump("loc_341")

    label("loc_25F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2C8")
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 1)
    SetChrPos(0x8, 2430, 200, 5330, 180)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, -104980, 0, 640, 0)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, -104980, 0, 1980, 180)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_341")

    label("loc_2C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2F7")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -103480, 0, 99640, 180)
    Jump("loc_341")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_324")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x10)
    OP_8C(0xC, 180, 0)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_341")

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_341")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x10)
    OP_8C(0xC, 180, 0)
    ClearChrFlags(0xF, 0x80)

    label("loc_341")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_1F2 end

    def Function_1_34C(): pass

    label("Function_1_34C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA")
    OP_6F(0x0, 29)
    OP_72(0x0, 0x10)
    OP_6F(0x1, 29)
    OP_72(0x1, 0x10)
    OP_6F(0x2, 29)
    OP_72(0x2, 0x10)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_79(0xFF, 0x2)
    OP_7A(0x18, 0x2)
    OP_7A(0x19, 0x2)
    OP_7A(0x1A, 0x2)
    OP_7B()
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0x9, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    OP_72(0xC, 0x4)

    label("loc_3BA")

    Return()

    # Function_1_34C end

    def Function_2_3BB(): pass

    label("Function_2_3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C0")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_456")
    Jump("loc_498")

    label("loc_456")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_472")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_498")

    label("loc_472")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48E")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_498")

    label("loc_48E")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_498")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jump("loc_4C3")

    label("loc_4C0")

    TalkBegin(0x8)

    label("loc_4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_7A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_739")

    ChrTalk(    #0
        0x8,
        (
            "#802FOh, you all...\x02\x03",

            "Were you able to fix the hot springs pump?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57F")

    ChrTalk(    #1
        0x107,
        "#061FYes, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1006FYup. Feel free to visit them any time you like now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EE")

    label("loc_57F")


    ChrTalk(    #3
        0x101,
        (
            "#1006FYup. Feel free to visit them any time you like now.\x02\x03",

            "#1015FWell, Tita did most of the work, really.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EE")


    ChrTalk(    #4
        0x8,
        (
            "#801FOhh, that's good news.\x02\x03",

            "I'll definitely take a trip over once\x01",
            "my work's calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#1049FPlease do. You have to remember to\x01",
            "relax sometimes.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E5")

    ChrTalk(    #6
        0x107,
        (
            "#560FY-Yeah, absolutely.\x02\x03",

            "Every machine needs maintenance, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E5")


    ChrTalk(    #7
        0x8,
        (
            "#801FHaha, thank you for your kind warning.\x01",
            "I'll be sure to remember it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_7A4")

    label("loc_739")


    ChrTalk(    #8
        0x8,
        (
            "#800FGood work fixing the pump.\x02\x03",

            "#806FPhew! I hope I can find a moment to\x01",
            "pay those springs a visit. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A4")

    Jump("loc_217D")

    label("loc_7A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1058")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C80")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81B")

    ChrTalk(    #9
        0x8,
        (
            "#802FOh... Estelle and Joshua.\x02\x03",

            "And Tita, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x107,
        "#067FHeehee, we're back.\x02",
    )

    CloseMessageWindow()
    Jump("loc_83F")

    label("loc_81B")


    ChrTalk(    #11
        0x8,
        "#802FOh... Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    label("loc_83F")


    ChrTalk(    #12
        0x101,
        "#1000FHell, sir. It's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        "#1040FI'm glad to see you're well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#801FAnd I'm glad to see you're back safely.\x02\x03",

            "Was the professor's invention of any use?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1011FThe generator?\x02\x03",

            "#1001FYou bet. It's been a huge help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1040FIf anything, the Royal Army's probably\x01",
            "more thankful than anyone.\x02\x03",

            "Until communications were restored,\x01",
            "a lot of bases were cut off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#801FI see.\x02\x03",

            "So for now at least it's having\x01",
            "the intended effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1015FYeah, which is good, but...\x02\x03",

            "#1002FChief, is the central factory okay?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC0")

    ChrTalk(    #19
        0x107,
        (
            "#063FI-I bet you guys can't really do any research\x01",
            "when it's dark like this, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0F")

    label("loc_AC0")


    ChrTalk(    #20
        0x102,
        (
            "#1043FI suppose restarting activity in\x01",
            "this situation would be difficult.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0F")


    ChrTalk(    #21
        0x8,
        (
            "#805FYes... It's a terrible situation all around.\x02\x03",

            "I'm absolutely inundated with requests for\x01",
            "help right now.\x02\x03",

            "Actually, I'm working on that right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1007FDang, sounds really rough...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1040FIf there's anything we can do,\x01",
            "we'd be happy to help.\x02\x03",

            "Just contact the guild, and we'll\x01",
            "come right over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        "#800FYes, thank you. You all take care too.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20CD)
    Jump("loc_1055")

    label("loc_C80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_END)), "loc_E14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8F")

    ChrTalk(    #25
        0x8,
        (
            "#802FOh, hello there.\x02\x03",

            "Did you get the gasoline?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1006FYeah, no problems there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#1040FThanks again for the introduction letter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#801FNo, no, not at all.\x01",
            "I only did what was natural.\x02\x03",

            "Well, then, good luck with repairing\x01",
            "the pump.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_E11")

    label("loc_D8F")


    ChrTalk(    #29
        0x8,
        (
            "#800FGood luck with repairing the pump.\x02\x03",

            "As a fan of the hot springs, I personally hope\x01",
            "to hear good news about the repairs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E11")

    Jump("loc_1055")

    label("loc_E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 0)), scpexpr(EXPR_END)), "loc_FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0D")

    ChrTalk(    #30
        0x8,
        (
            "#800FGive that introduction letter I just gave\x01",
            "you to the harbor master in Ruan.\x02\x03",

            "If the gasoline is there, I've\x01",
            "instructed him to give it to you.\x02\x03",

            "The road lights are off, so the way is\x01",
            "pretty dangerous.\x02\x03",

            "Be very careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_FA5")

    label("loc_F0D")


    ChrTalk(    #31
        0x8,
        (
            "#800FGive that introduction letter I just gave\x01",
            "you to the harbor master in Ruan.\x02\x03",

            "If the gasoline is there, I've\x01",
            "instructed him to give it to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA5")

    Jump("loc_1055")

    label("loc_FA8")


    ChrTalk(    #32
        0x8,
        (
            "#805FI'd love to resume research immediately,\x01",
            "but we have a mountain of problems to\x01",
            "get through first.\x02\x03",

            "#806FPhew! Anyway, for now I need\x01",
            "to clear up some paperwork...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1055")

    Jump("loc_217D")

    label("loc_1058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1540")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_116F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 2)), scpexpr(EXPR_END)), "loc_1168")

    ChrTalk(    #33
        0x8,
        (
            "#800FI've had a declaration of safety regarding\x01",
            "the earthquakes put out under my name.\x02\x03",

            "For now, my priority is alleviating the\x01",
            "concerns of the citizens.\x02\x03",

            "I hear you'll be heading to the capital,\x01",
            "but be careful on the roads, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116C")

    label("loc_1168")

    Call(0, 5)

    label("loc_116C")

    Jump("loc_153D")

    label("loc_116F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_126B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11D6")

    ChrTalk(    #34
        0x8,
        (
            "#800FI've explained things to Elmo Village\x01",
            "from my end.\x02\x03",

            "Well, then, be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1268")

    label("loc_11D6")


    ChrTalk(    #35
        0x8,
        (
            "#800FI've explained things to Elmo Village\x01",
            "from my end.\x02\x03",

            "If you go there, Mao should be able\x01",
            "to give you a hand.\x02\x03",

            "Well, then, be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1268")

    Jump("loc_153D")

    label("loc_126B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_13F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1340")

    ChrTalk(    #36
        0x8,
        (
            "#800FWhen things are at their worst,\x01",
            "Professor Russell's at his best.\x02\x03",

            "I suppose that's why they call him a genius.\x02\x03",

            "#806FWell, sometimes the professor's talents\x01",
            "are also a 'disaster,' mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13EE")

    label("loc_1340")


    ChrTalk(    #37
        0x8,
        (
            "#800FThis earthquake was far too odd. Even the\x01",
            "researchers can't do much more than hang\x01",
            "their heads.\x02\x03",

            "I hope Professor Russell's research\x01",
            "provides an opening, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_13EE")

    Jump("loc_153D")

    label("loc_13F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_14B6")

    ChrTalk(    #38
        0x8,
        (
            "#800FI just got word, but apparently there was\x01",
            "an earthquake at the Sanktheim Gate.\x02\x03",

            "Didn't feel any shaking over here at all,\x01",
            "though.\x02\x03",

            "It seems these earthquakes are a bit special.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_153D")

    label("loc_14B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_153D")

    ChrTalk(    #39
        0x8,
        (
            "#800FI'll try collecting information from within\x01",
            "the city on my end.\x02\x03",

            "Lately the roads have been dangerous,\x01",
            "so be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153D")

    Jump("loc_16DB")

    label("loc_1540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_15EF")

    ChrTalk(    #40
        0x8,
        (
            "#800FThe central factory will be happy to cooperate\x01",
            "with the guild's investigation on all fronts.\x02\x03",

            "I'm sure it'll be hard, but I hope you'll\x01",
            "give us your best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DB")

    label("loc_15EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1654")

    ChrTalk(    #41
        0x8,
        (
            "#800FProfessor Russell was looking for you all.\x02\x03",

            "Shouldn't you get back to the guild?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DB")

    label("loc_1654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_16DB")

    ChrTalk(    #42
        0x8,
        (
            "#800FI'll try collecting information from within\x01",
            "the city on my end.\x02\x03",

            "Lately the roads have been dangerous,\x01",
            "so be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DB")

    Jump("loc_217D")

    label("loc_16DE")

    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_18E7")

    ChrTalk(    #43
        0x8,
        "#801FOhh, Estelle.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x106, 400)

    ChrTalk(    #44
        0x8,
        "#801FAnd Agate, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        "#051FHey, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1006FHi, Chief Murdock. Long time no see.\x01",
            "Not since the birthday celebrations, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #47
        0x8,
        (
            "#801FYes, indeed.\x02\x03",

            "Seems like a lot's happened since then.\x01",
            "I'm glad to see you well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#1008FAhaha... Thanks, sir.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E4")

    ChrTalk(    #49
        0x8,
        (
            "#800FFor the moment it seems like you'll be staying\x01",
            "here to back up the Zeiss branch.\x02\x03",

            "It's very reassuring having you all here.\x01",
            "I hope for the best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E4")

    Jump("loc_1BCA")

    label("loc_18E7")


    ChrTalk(    #50
        0x8,
        "#801FOh... Estelle, you've come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1006FHi, Chief Murdock. Long time no see.\x01",
            "Not since the birthday celebrations, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#801FYes, indeed.\x02\x03",

            "A lot has happened, but...I'm\x01",
            "glad to see you are well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#1008FAhaha... Thanks, sir.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #54
        0x8,
        "#802FIncidentally, this is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1006FOh, yeah, Schera... Er, no, sorry.\x01",
            "This is my superior in the branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x103,
        (
            "#020FRolent branch guild bracer, Scherazard Harvey.\x02\x03",

            "It may not be for long, but I\x01",
            "look forward to working here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_1B11")

    ChrTalk(    #57
        0x8,
        "#801FEstelle's superior, hmm? A pleasure to meet you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BCA")

    label("loc_1B11")


    ChrTalk(    #58
        0x8,
        (
            "#801FA pleasure to meet you.\x02\x03",

            "#800FFor the moment it seems like you'll be staying\x01",
            "here to back up the Zeiss branch.\x02\x03",

            "It's very reassuring having you all here.\x01",
            "I hope for the best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_1D42")

    ChrTalk(    #59
        0x8,
        (
            "#800FSeems like you're already helping Professor\x01",
            "Russell out with his experiments.\x02\x03",

            "The central factory will be happy to cooperate\x01",
            "with the guild's investigation on all fronts.\x02\x03",

            "I'm sure it'll be hard, but I\x01",
            "hope you'll give us your best.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 3)

    ChrTalk(    #60
        0x8,
        (
            "#800FYes, if anything causes you trouble\x01",
            "contact us immediately.\x02\x03",

            "Well, then, take care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1006FYeah, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2177")

    label("loc_1D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1EE5")
    Call(0, 3)

    ChrTalk(    #62
        0x101,
        "#1006FWe'll do our best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#802FOh, yes, Professor Russell was looking for you.\x02\x03",

            "It seems like he finished preparing something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1004FOh, yeah?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1E2E")

    ChrTalk(    #65
        0x106,
        "#052FWe should probably check back with the guild.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E69")

    label("loc_1E2E")


    ChrTalk(    #66
        0x103,
        "#027FWe should probably check back in with the guild.\x02",
    )

    CloseMessageWindow()

    label("loc_1E69")


    ChrTalk(    #67
        0x8,
        (
            "#800FYes, please do.\x02\x03",

            "#806FI'm sure things'll be difficult,\x01",
            "but please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1016FY-Yeah, well later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2177")

    label("loc_1EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2177")
    Call(0, 3)

    ChrTalk(    #69
        0x101,
        (
            "#1006FYeah, we'll do our best.\x02\x03",

            "That reminds me. I hear you'll be\x01",
            "cooperating with the guild, sir.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #70
        0x8,
        (
            "#800FYes, Kilika rang me up after that earthquake.\x02\x03",

            "I'll be gathering information on whether or not\x01",
            "there was anything out of the ordinary before\x01",
            "or after that earthquake.\x02\x03",

            "#806FI've just started, though, so I don't\x01",
            "have much for you yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1015FGuess it's not that easy to get answers,\x01",
            "huh.\x02\x03",

            "#1000FWell, our next step is to check out the\x01",
            "Wolf Fort, so...\x02\x03",

            "Good luck with the investigation within\x01",
            "the city, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "#800FYes, if I find anything out\x01",
            "I'll contact the guild.\x02\x03",

            "You all take care, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1006FYeah, later.\x02",
    )

    CloseMessageWindow()

    label("loc_2177")

    OP_A2(0x1481)
    OP_A2(0x0)

    label("loc_217D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2193")
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Jump("loc_2196")

    label("loc_2193")

    TalkEnd(0x8)

    label("loc_2196")

    Return()

    # Function_2_3BB end

    def Function_3_2197(): pass

    label("Function_3_2197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_21C1")

    ChrTalk(    #74
        0x106,
        "#051FYeah, leave it to us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21E7")

    label("loc_21C1")


    ChrTalk(    #75
        0x103,
        "#525FYes, please leave it to us.\x02",
    )

    CloseMessageWindow()

    label("loc_21E7")

    Return()

    # Function_3_2197 end

    def Function_4_21E8(): pass

    label("Function_4_21E8")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2298")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 2)), scpexpr(EXPR_END)), "loc_2294")

    ChrTalk(    #76
        0xE,
        (
            "#100FThe technological prowess of our friends in\x01",
            "the 'society' is quite remarkable.\x02\x03",

            "Hmm, this is the first meaty challenge\x01",
            "I've had in some time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2298")

    label("loc_2294")

    Call(0, 5)

    label("loc_2298")

    TalkEnd(0xE)
    Return()

    # Function_4_21E8 end

    def Function_5_229C(): pass

    label("Function_5_229C")

    OP_4A(0xE, 255)

    ChrTalk(    #77
        0x8,
        "#802FOh, if it isn't Estelle.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)

    ChrTalk(    #78
        0xE,
        "#103FHaven't departed yet, hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1000FYeah, we had a bit of business still.\x02\x03",

            "#1015F...By the way, did something come up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xE,
        (
            "#100FYes, we received an investigation\x01",
            "request from the Royal Army.\x02\x03",

            "It's about that projection device.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#1011FProjection device...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2448")

    ChrTalk(    #82
        0x106,
        (
            "#050FThat weird contraption in Ruan that the enemy\x01",
            "used. The one that could create illusions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A7")

    label("loc_2448")


    ChrTalk(    #83
        0x103,
        (
            "#022FThe device in Ruan that the enemy used.\x01",
            "The one that created such ghostly illusions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A7")


    ChrTalk(    #84
        0xE,
        (
            "#104FYes, the one you told me about.\x02\x03",

            "#102FI think it's necessary to have a look at it\x01",
            "if I'm to study the Gospel properly.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x101, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_254A")
    SetChrSubChip(0xFE, 1)
    Jump("loc_254F")

    label("loc_254A")

    SetChrSubChip(0xFE, 2)

    label("loc_254F")

    OP_8C(0x8, 180, 0)
    SetChrFlags(0x8, 0x10)

    ChrTalk(    #85
        0x8,
        (
            "#800FWe were going to ask the army about it,\x01",
            "but then they sent it to us.\x02\x03",

            "We were just about to take a look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1004FWow. You already got an investigation\x01",
            "report together.\x02\x03",

            "Seems like the army's putting a lot of\x01",
            "effort into investigating the 'society.'\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_26BC")

    ChrTalk(    #87
        0x106,
        (
            "#053FYeah, it may seem obvious, but\x01",
            "the army's keeping tabs on them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2707")

    label("loc_26BC")


    ChrTalk(    #88
        0x103,
        (
            "#026FYes, it may seem obvious, but the\x01",
            "army's keeping an eye on them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2707")


    ChrTalk(    #89
        0xE,
        (
            "#100FI intend to put my all into puzzling out\x01",
            "this Gospel.\x02\x03",

            "#100FWell, then, take care of Tita.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2772():
        TurnDirection(0xF7, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2772)
    TurnDirection(0x101, 0xE, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_27AB")

    ChrTalk(    #90
        0x106,
        "#051FYeah, leave it to us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_27CA")

    label("loc_27AB")


    ChrTalk(    #91
        0x103,
        "#020FYes, leave it to us.\x02",
    )

    CloseMessageWindow()

    label("loc_27CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27F9")

    ChrTalk(    #92
        0x107,
        "#560FGood luck, Grandpa!\x02",
    )

    CloseMessageWindow()
    Jump("loc_281A")

    label("loc_27F9")


    ChrTalk(    #93
        0x101,
        "#1006FTake care, Professor.\x02",
    )

    CloseMessageWindow()

    label("loc_281A")

    OP_4B(0xE, 255)
    OP_A2(0x1642)
    Return()

    # Function_5_229C end

    def Function_6_2822(): pass

    label("Function_6_2822")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2840")
    OP_A2(0x4)

    label("loc_2840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F7")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Completed one of QST046, QST047, QST048 in previous game\x01",      # 0
            "Did not complete any of these quests in previous game\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_28EB"),
        (1, "loc_28F1"),
        (SWITCH_DEFAULT, "loc_28F7"),
    )


    label("loc_28EB")

    OP_A2(0x4)
    Jump("loc_28F7")

    label("loc_28F1")

    OP_A3(0x4)
    Jump("loc_28F7")

    label("loc_28F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_291D")
    Call(0, 8)
    Jump("loc_2C8E")

    label("loc_291D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2A42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_29C7")

    ChrTalk(    #94
        0xFE,
        (
            "If you're looking for the new girl, she should\x01",
            "be around research room somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Well, I think that girl's got the knack\x01",
            "for this kinda work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3F")

    label("loc_29C7")


    ChrTalk(    #96
        0xFE,
        "All the office newbies start as mail carriers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Well, for some people like me,\x01",
            "that start becomes the goal.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2A3F")

    Jump("loc_2C8E")

    label("loc_2A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2B92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2AE8")

    ChrTalk(    #98
        0xFE,
        (
            "Apparently that new girl got in here\x01",
            "because she has a connection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "Well, we're all about skill here, so\x01",
            "however she got in doesn't matter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B8F")

    label("loc_2AE8")


    ChrTalk(    #100
        0xFE,
        "That new girl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Apparently, she's the granddaughter of\x01",
            "some technician who used to be here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "In other words, she got this job\x01",
            "because she had an in.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2B8F")

    Jump("loc_2C8E")

    label("loc_2B92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2C2A")

    ChrTalk(    #103
        0xFE,
        "We've got a new member on our staff, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "She's a bit ditzy, but I'll be able to use her\x01",
            "like a pack horse, if nothing else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C8E")

    label("loc_2C2A")


    ChrTalk(    #105
        0xFE,
        "Man, earthquakes. I just haaaaate them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "I'll let the newbie clean up the fallen books.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2C8E")

    Jump("loc_2D22")

    label("loc_2C91")


    ChrTalk(    #107
        0xFE,
        (
            "For now I'm leaving the small stuff to\x01",
            "the newbie, so no worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "But, if something happens, I'll be\x01",
            "calling on you guys. Count on it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D22")

    Jump("loc_2F81")

    label("loc_2D25")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #109
        0xFE,
        "Oh, hey, there's a familiar face...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "You're that person who found\x01",
            "me a book a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1016FAh, yeah, that did happen.\x02\x03",

            "#1007FTh-The memory seems really painful somehow,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "Don't worry. I don't intend to put\x01",
            "out any new requests any time soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "There was a newbie posted here recently,\x01",
            "so I'm leaving little tasks to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#1000FHuh, nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "Well, for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "If something comes up that's too much for\x01",
            "her, I'll probably ask the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "I hope you'll help me out when the time comes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#1006FSure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "Thank you!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x142C)
    OP_A2(0x2)

    label("loc_2F81")

    TalkEnd(0x9)
    Return()

    # Function_6_2822 end

    def Function_7_2F85(): pass

    label("Function_7_2F85")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3094")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_301A")

    ChrTalk(    #120
        0xFE,
        "Ahhh, this is just the worst.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "I've got to go collect documents\x01",
            "from the fifth floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "Uuuhhh... I hate stairs.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_3091")

    label("loc_301A")


    ChrTalk(    #123
        0xFE,
        (
            "Without the elevator, even collecting\x01",
            "documents is a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Hmm, maybe I should catch a cold\x01",
            "before tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3091")

    Jump("loc_3669")

    label("loc_3094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_31CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3158")

    ChrTalk(    #125
        0xFE,
        (
            "It's so dark, I can't even read\x01",
            "the titles of the books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "Really, how do they even expect me to work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "My boss's gone off somewhere.\x01",
            "Maybe I should just leave...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_31C7")

    label("loc_3158")


    ChrTalk(    #128
        0xFE,
        (
            "It's so dark, I can't even read\x01",
            "the titles of the books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "Really, how do they even expect me to work?\x02",
    )

    CloseMessageWindow()

    label("loc_31C7")

    Jump("loc_3669")

    label("loc_31CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_31D8")
    Call(0, 8)
    Jump("loc_3669")

    label("loc_31D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_33E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 5)), scpexpr(EXPR_END)), "loc_327F")

    ChrTalk(    #130
        0xFE,
        (
            "Phew! Once I'm done with this I need\x01",
            "to head over to the labs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "If you want to make a good first\x01",
            "impression, you gotta go with a\x01",
            "cute smile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E3")

    label("loc_327F")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x107, 0)
    Sleep(400)

    ChrTalk(    #132
        0xFE,
        "Ah, it's Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        "#060FHi, Muriel. How's work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "Eh, it's just little jobs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Well, I know I'm a newbie, so\x01",
            "I guess that's how it goes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x107,
        (
            "#067FHeehee, everyone starts with little jobs.\x02\x03",

            "But I'm sure you can do it, Muriel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "Thanks, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "I've got a goal, so I'll hang in there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x107,
        "#061FGood luck!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1435)

    label("loc_33E3")

    Jump("loc_3669")

    label("loc_33E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_349A")

    ChrTalk(    #140
        0xFE,
        (
            "Let's see, once this is over I need to\x01",
            "stop by each of the research rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "First impressions are critical, so I gotta\x01",
            "always have a smile when I go out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3534")

    label("loc_349A")


    ChrTalk(    #142
        0xFE,
        (
            "My goal is to be the receptionist girl at\x01",
            "the factory. I was BORN to do that job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "I won't stop until my butt is planted\x01",
            "behind that counter!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3534")

    Jump("loc_3669")

    label("loc_3537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_3669")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_35BA")

    ChrTalk(    #144
        0xFE,
        "Right now I'm just an office newbie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Uuuugh. I'm getting sick of this.\x01",
            "Arranging books is soooo boring.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3669")

    label("loc_35BA")


    ChrTalk(    #146
        0xFE,
        (
            "*sigh* Just look at all this. That earthquake\x01",
            "did a real number on this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "Well, it's probably more like fifty percent\x01",
            "earthquake, fifty percent lazy boss...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3669")

    TalkEnd(0xA)
    Return()

    # Function_7_2F85 end

    def Function_8_366D(): pass

    label("Function_8_366D")

    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3696"),
        (1, "loc_37AB"),
        (2, "loc_38FD"),
        (3, "loc_3AA3"),
        (4, "loc_3C51"),
        (5, "loc_3E9A"),
        (SWITCH_DEFAULT, "loc_40A3"),
    )


    label("loc_3696")


    ChrTalk(    #148
        0xA,
        "So...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xA,
        "Can I really become the receptionist girl?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x9,
        (
            "Really, you'd be way better off just working\x01",
            "hard on your own than asking me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x9,
        (
            "And isn't that just fine?\x01",
            "It's good to have a goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x9,
        (
            "Administrative staff dripping with ambition,\x01",
            "how marvelous.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40A3")

    label("loc_37AB")


    ChrTalk(    #153
        0x9,
        (
            "Just watch out. Hazel's gonna be pretty\x01",
            "tough competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        (
            "After all, Chief Murdock thinks pretty\x01",
            "highly of her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xA,
        "Hazel's getting pretty old though, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xA,
        (
            "I think everyone'd be happier with a young,\x01",
            "pretty face greeting them at the front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xA,
        (
            "If the outfit was a miniskirt,\x01",
            "you can bet I'd run her over.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40A3")

    label("loc_38FD")


    ChrTalk(    #158
        0xA,
        (
            "That reminds me, Hazel isn't married,\x01",
            "is she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x9,
        "Nope. Single as they get.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x9,
        (
            "Hazel and I were both 'leftovers'\x01",
            "around the same time.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #161
        0xA,
        "Whaaaaat, reaaally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xA,
        "Ahhhh, that's terrible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x9,
        (
            "Men are consumables...\x01",
            "At best, durable goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x9,
        (
            "It'd be way more terrible signing my life\x01",
            "away in a contract to something like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #165
        0xA,
        "Yikes...\x02",
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40A3")

    label("loc_3AA3")


    ChrTalk(    #166
        0xA,
        "Oh, yeah! I went to the Lab on the fourth floor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xA,
        (
            "You said there was a good man there,\x01",
            "didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xA,
        (
            "But the guy that was there was such a\x01",
            "wet noodle. Wasn't my idea of a good\x01",
            "man, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x9,
        "Ah, that was Terry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x9,
        "Wasn't there anyone else in there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        "Ooooh, you meant someone else?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xA,
        (
            "Ahhh, I wasted all those smiles on\x01",
            "the wrong guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x9,
        (
            "Mmmm, it's about lunch time,\x01",
            "so Ray may have gone out.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40A3")

    label("loc_3C51")


    ChrTalk(    #174
        0x9,
        (
            "Speaking of lunch, I'm starting\x01",
            "to get hungry myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x9,
        (
            "Want to go out to Forgel or something?\x01",
            "My treat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        "Wooow, I love you, boss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xA,
        (
            "Oh, speaking of Forgel, isn't\x01",
            "that waiter there pretty hot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        "Oh, didn't you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x9,
        (
            "That guy is dating one of researchers on\x01",
            "our staff.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #180
        0xA,
        "Noooooooo... What a waste.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x9,
        (
            "Haven't you met Louise? She's young,\x01",
            "but she's got a heck of a brain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "She might not be anything special in the looks\x01",
            "department, but she rates pretty high in ability,\x01",
            "so she's up there, if you know what I mean.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40A3")

    label("loc_3E9A")


    ChrTalk(    #183
        0xA,
        (
            "Hmm, I guess people in the factory\x01",
            "tend to focus on what's inside, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x9,
        "True, that attitude is pretty prevalent here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x9,
        (
            "If your work doesn't impress,\x01",
            "no one will even turn around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xA,
        (
            "Do you think I'll be popular if\x01",
            "I become the receptionist girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x9,
        (
            "Well, certainly more popular than if\x01",
            "you stay in Archive room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xA,
        "Got'cha! Yeah, I just gotta work hard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xA,
        (
            "ALL RIGHT. I'll become the receptionist girl\x01",
            "no matter what. Just you watch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xA,
        (
            "Then I'll get some hot researcher too.\x01",
            "Teehee.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40A3")

    label("loc_40A3")

    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    Return()

    # Function_8_366D end

    def Function_9_40AC(): pass

    label("Function_9_40AC")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 3)), scpexpr(EXPR_END)), "loc_4412")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4314")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_424A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4175")

    ChrTalk(    #191
        0xB,
        (
            "#690FThe swap job for the new engine's scheduled\x01",
            "to be done at Leiston Fortress.\x02\x03",

            "The Arseille will head over from the capital,\x01",
            "and we'll take the factory ship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4247")

    label("loc_4175")


    ChrTalk(    #192
        0xB,
        (
            "#690FWe're scheduled to load the new model\x01",
            "engine onto the Arseille soon.\x02\x03",

            "We gotta have a plan for the swap\x01",
            "operation ready before long.\x02\x03",

            "That's why I've been stuck here in\x01",
            "the central factory lately.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_4247")

    Jump("loc_4311")

    label("loc_424A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_42BA")

    ChrTalk(    #193
        0xB,
        (
            "#690FStill, though, an earthquake. That's rare.\x02\x03",

            "For now, I'm just glad there wasn't any damage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4311")

    label("loc_42BA")


    ChrTalk(    #194
        0xB,
        (
            "#690FYeah, you've said hello to me plenty.\x02\x03",

            "Go and let little Tita see your face.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4311")

    Jump("loc_440F")

    label("loc_4314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43AF")

    ChrTalk(    #195
        0xB,
        (
            "#691FIt'll be good having you all around.\x02\x03",

            "If anything comes up, we'll go straight to you.\x02\x03",

            "Well, then, see you when something happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_440F")

    label("loc_43AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_440F")

    ChrTalk(    #196
        0xB,
        (
            "#691FTita's excited face...\x01",
            "Haha, I can picture it.\x02\x03",

            "After all, she does adore you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_440F")

    Jump("loc_474D")

    label("loc_4412")


    ChrTalk(    #197
        0x101,
        "#1018FAh, Gustav!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xB)
    TurnDirection(0xB, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_449C")

    ChrTalk(    #198
        0xB,
        (
            "#692FWell, well, this is a surprise!\x02\x03",

            "#691FBeen a long time, guys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44DE")

    label("loc_449C")


    ChrTalk(    #199
        0xB,
        (
            "#692FWell, well, this is a surprise!\x02\x03",

            "#691FBeen a long time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44DE")


    ChrTalk(    #200
        0x101,
        (
            "#1001FAhaha, yeah it has!\x01",
            "You're looking well, Gustav.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xB,
        "#691FHere on work again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#1006FYeah, we're filling in a bit for the Zeiss branch.\x02\x03",

            "So, we'll be in town for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xB,
        (
            "#691FWell that's good to hear.\x02\x03",

            "If anything comes up, you'll\x01",
            "be the first one I call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#1001FYeah, leave it to us!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_4672")
    TurnDirection(0xB, 0x107, 400)

    ChrTalk(    #205
        0xB,
        "#691FHey, Tita, good luck with helping the professor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x107,
        "#060FAh, yes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4742")

    label("loc_4672")


    ChrTalk(    #207
        0xB,
        "#691FBy the way, did you go see the professor yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        (
            "#1011FAh, we just went, yeah.\x02\x03",

            "#1008FW-We got quite the reception from Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xB,
        (
            "#693FHaha, I bet you did.\x02\x03",

            "She really does admire you, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4742")

    OP_A2(0x1483)
    OP_A2(0x6)
    ClearChrFlags(0xB, 0x10)

    label("loc_474D")

    TalkEnd(0xB)
    Return()

    # Function_9_40AC end

    def Function_10_4751(): pass

    label("Function_10_4751")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_491F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_487E")

    ChrTalk(    #210
        0xFE,
        (
            "Us engineers are working on a response\x01",
            "to the current phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "The more I think about it, the more I understand\x01",
            "just how unique this phenomenon is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "For now, we're still sort of floored by\x01",
            "it just happening at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "There's no plan in sight at the moment.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_491C")

    label("loc_487E")


    ChrTalk(    #214
        0xFE,
        (
            "For now, we're still sort of floored by\x01",
            "it just happening at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "The power of an existence beyond human\x01",
            "understanding...is all I can come up with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_491C")

    Jump("loc_4D6B")

    label("loc_491F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4B03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A72")

    ChrTalk(    #216
        0xFE,
        (
            "I never thought something like this would,\x01",
            "or heck, COULD happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "I'm just glad this happened after the Arseille's\x01",
            "upgrade evaluation was finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "After all, we can study the data\x01",
            "even without orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "Of course, right now the priority is on\x01",
            "comprehending and researching the\x01",
            "current phenomenon.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_4B00")

    label("loc_4A72")


    ChrTalk(    #220
        0xFE,
        (
            "I never thought something like this\x01",
            "might happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "I'm just glad this happened after the Arseille's\x01",
            "upgrade evaluation was finished.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B00")

    Jump("loc_4D6B")

    label("loc_4B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_4BAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4BA6")

    ChrTalk(    #222
        0xFE,
        (
            "Once the plug check is finished,\x01",
            "we'll prepare for embarkation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "We've gotta prepare well in advance or\x01",
            "I'm sure we'll forget something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BAA")

    label("loc_4BA6")

    Call(0, 13)

    label("loc_4BAA")

    Jump("loc_4D6B")

    label("loc_4BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_4D6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4C39")

    ChrTalk(    #224
        0xFE,
        (
            "Soon we'll be loading the new\x01",
            "engine onto the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "We'll be heading out to Leiston Fortress\x01",
            "to do the work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D6B")

    label("loc_4C39")


    ChrTalk(    #226
        0xFE,
        (
            "We're scheduled to load the new engine\x01",
            "onto the Arseille very soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "Right now I'm working with the maintenance\x01",
            "chief to put together a plan for the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "I'm really relieved there was no damage\x01",
            "from the earthquake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "It would be pretty sad if our preparations\x01",
            "for the work got delayed.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_4D6B")

    TalkEnd(0xC)
    Return()

    # Function_10_4751 end

    def Function_11_4D6F(): pass

    label("Function_11_4D6F")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_4EBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E91")

    ChrTalk(    #230
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "No matter how many times I think about it,\x01",
            "I can't come up with any explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "That object floating in the sky...\x01",
            "And this shutdown phenomenon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "There should be something connecting them,\x01",
            "but...I just don't know what that something is.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_4EBA")

    label("loc_4E91")


    ChrTalk(    #234
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        "Nope... No idea at all.\x02",
    )

    CloseMessageWindow()

    label("loc_4EBA")

    Jump("loc_537B")

    label("loc_4EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_506A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD0")

    ChrTalk(    #236
        0xFE,
        (
            "Right now we're in a situation where all\x01",
            "orbments have lost their orbal energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "A case like this happened before,\x01",
            "so I tried a logical deduction, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        "I still don't have a clue. *sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "Professor Russell might know something,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_5067")

    label("loc_4FD0")


    ChrTalk(    #240
        0xFE,
        (
            "To us, this phenomenon still has far\x01",
            "too little understood about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "I'm not sure this situation can even\x01",
            "be explained by logical deduction.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5067")

    Jump("loc_537B")

    label("loc_506A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_514B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5102")

    ChrTalk(    #242
        0xFE,
        (
            "I was just putting together data on\x01",
            "the earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "Thanks to Russell, there's a great\x01",
            "deal of information stored in Capel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5148")

    label("loc_5102")


    ChrTalk(    #244
        0xFE,
        "Oh, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "Everyone just left for Leiston Fortress.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_5148")

    Jump("loc_537B")

    label("loc_514B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_51F5")

    ChrTalk(    #246
        0xFE,
        (
            "Professor Russell is investigating the\x01",
            "earthquakes, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "Given the professor, I'm sure he'll\x01",
            "end up trying to eat a rock or something\x01",
            "and get a clue.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_537B")

    label("loc_51F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_537B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5285")

    ChrTalk(    #248
        0xFE,
        (
            "The epicenter of that last earthquake's\x01",
            "still unknown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "It may have been an earthquake\x01",
            "caused by some special source.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_537B")

    label("loc_5285")


    ChrTalk(    #250
        0xFE,
        (
            "I checked our measuring equipment\x01",
            "when the last earthquake happened,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        "It's weird.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "It doesn't share any similarities with our\x01",
            "previous data on earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "It may have been an earthquake\x01",
            "caused by some special source.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_537B")

    TalkEnd(0xD)
    Return()

    # Function_11_4D6F end

    def Function_12_537F(): pass

    label("Function_12_537F")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_5492")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5424")

    ChrTalk(    #254
        0xFE,
        (
            "Hmm, an orbal shutdown phenomenon,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        "I'm...pretty bad on the theory side.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        "I might just be in everyone's way here.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    TalkEnd(0xF)
    SetChrFlags(0xFE, 0x10)
    Return()

    label("loc_5424")


    ChrTalk(    #257
        0xFE,
        (
            "Hmm, an orbal shutdown phenomenon,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "(...I should try to look like I'm really\x01",
            "concentrating.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58AB")

    label("loc_5492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_55D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5564")

    ChrTalk(    #259
        0xFE,
        (
            "From what I've heard, the Arseille\x01",
            "made a safe splashdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "One way or another, that's a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "I'm thankful from the depths of my heart\x01",
            "to the crew who protected that ship.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_55CE")

    label("loc_5564")


    ChrTalk(    #262
        0xFE,
        (
            "From what I've heard, the Arseille\x01",
            "made a safe splashdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        "One way or another, that's a relief.\x02",
    )

    CloseMessageWindow()

    label("loc_55CE")

    Jump("loc_58AB")

    label("loc_55D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_579F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_569D")

    ChrTalk(    #264
        0xFE,
        "All right, boarding preparation complete.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "I'm sure Ursus will take care\x01",
            "of my little sister Yuriel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "Ah, is there anything better than having\x01",
            "a man that can cook AND clean?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_579C")

    label("loc_569D")


    ChrTalk(    #267
        0xFE,
        (
            "Okay, so I have all the diagrams\x01",
            "and blueprints in my case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        "Hugo's in charge of all of the orbal diagrams...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "I've got emergency snacks in case\x01",
            "I get hungry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        "Yep, I'm ready!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        "All right, I can board the factory ship any time!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_579C")

    Jump("loc_58AB")

    label("loc_579F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_58AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_58A7")

    ChrTalk(    #272
        0xFE,
        (
            "Phew! Once we finish the last checks, it'll\x01",
            "finally be time for the factory ship to launch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "For us to put such an incredible engine in\x01",
            "an already incredible machine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "I have to pinch myself sometimes to\x01",
            "make sure I'm not dreaming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58AB")

    label("loc_58A7")

    Call(0, 13)

    label("loc_58AB")

    TalkEnd(0xF)
    Return()

    # Function_12_537F end

    def Function_13_58AF(): pass

    label("Function_13_58AF")

    OP_4A(0xC, 255)
    OP_4A(0xF, 255)

    ChrTalk(    #275
        0xF,
        (
            "I've finished prepping all parts used\x01",
            "in the Arseille job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xF,
        (
            "Now we just have to check them over\x01",
            "and load them onto the ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xC,
        (
            "All right, Louise.\x01",
            "Could you check over the plugs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xC,
        (
            "You designed that area, so it'd be\x01",
            "best if you looked over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xF,
        "Sure thing. Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xC,
        (
            "I'll go check up on the dock\x01",
            "with the maintenance chief.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 255)
    OP_4B(0xF, 255)
    OP_A2(0x8)
    OP_A2(0xB)
    Return()

    # Function_13_58AF end

    SaveToFile()

Try(main)
