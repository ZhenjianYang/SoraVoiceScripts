from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1603   ._SN',
        MapName             = 'Bose',
        Location            = 'C1603.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60125",
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
        'Silver-Haired Youth',                  # 9
        'Weissmann',                            # 10
        'Ancient Dragon Ragnard',               # 11
        '竜',                                   # 12
        'Target',                               # 13
        'Target',                               # 14
        '金耀石の塊・Estelle',                  # 15
        '金耀石の塊・Agate',                    # 16
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
        'ED6_DT07/CH02040 ._CH',             # 00
        'ED6_DT27/CH03550 ._CH',             # 01
        'ED6_DT26/CH20340 ._CH',             # 02
        'ED6_DT06/CH20091 ._CH',             # 03
        'ED6_DT26/CH20341 ._CH',             # 04
        'ED6_DT27/CH04000 ._CH',             # 05
        'ED6_DT27/CH04001 ._CH',             # 06
        'ED6_DT27/CH04002 ._CH',             # 07
        'ED6_DT07/CH00120 ._CH',             # 08
        'ED6_DT07/CH00121 ._CH',             # 09
        'ED6_DT07/CH00122 ._CH',             # 0A
        'ED6_DT07/CH00130 ._CH',             # 0B
        'ED6_DT07/CH00131 ._CH',             # 0C
        'ED6_DT07/CH00132 ._CH',             # 0D
        'ED6_DT07/CH00140 ._CH',             # 0E
        'ED6_DT07/CH00141 ._CH',             # 0F
        'ED6_DT07/CH00142 ._CH',             # 10
        'ED6_DT07/CH00170 ._CH',             # 11
        'ED6_DT07/CH00171 ._CH',             # 12
        'ED6_DT07/CH00172 ._CH',             # 13
        'ED6_DT07/CH00160 ._CH',             # 14
        'ED6_DT07/CH00161 ._CH',             # 15
        'ED6_DT07/CH00162 ._CH',             # 16
        'ED6_DT07/CH00150 ._CH',             # 17
        'ED6_DT07/CH00151 ._CH',             # 18
        'ED6_DT07/CH00152 ._CH',             # 19
        'ED6_DT07/CH00154 ._CH',             # 1A
        'ED6_DT07/CH00155 ._CH',             # 1B
        'ED6_DT06/CH20137 ._CH',             # 1C
        'ED6_DT06/CH20085 ._CH',             # 1D
        'ED6_DT26/CH20282 ._CH',             # 1E
        'ED6_DT27/CH04540 ._CH',             # 1F
        'ED6_DT26/CH20352 ._CH',             # 20
        'ED6_DT26/CH20353 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT07/CH02040P._CP',             # 00
        'ED6_DT27/CH03550P._CP',             # 01
        'ED6_DT26/CH20340P._CP',             # 02
        'ED6_DT06/CH20091P._CP',             # 03
        'ED6_DT26/CH20341P._CP',             # 04
        'ED6_DT27/CH04000P._CP',             # 05
        'ED6_DT27/CH04001P._CP',             # 06
        'ED6_DT27/CH04002P._CP',             # 07
        'ED6_DT07/CH00120P._CP',             # 08
        'ED6_DT07/CH00121P._CP',             # 09
        'ED6_DT07/CH00122P._CP',             # 0A
        'ED6_DT07/CH00130P._CP',             # 0B
        'ED6_DT07/CH00131P._CP',             # 0C
        'ED6_DT07/CH00132P._CP',             # 0D
        'ED6_DT07/CH00140P._CP',             # 0E
        'ED6_DT07/CH00141P._CP',             # 0F
        'ED6_DT07/CH00142P._CP',             # 10
        'ED6_DT07/CH00170P._CP',             # 11
        'ED6_DT07/CH00171P._CP',             # 12
        'ED6_DT07/CH00172P._CP',             # 13
        'ED6_DT07/CH00160P._CP',             # 14
        'ED6_DT07/CH00161P._CP',             # 15
        'ED6_DT07/CH00162P._CP',             # 16
        'ED6_DT07/CH00150P._CP',             # 17
        'ED6_DT07/CH00151P._CP',             # 18
        'ED6_DT07/CH00152P._CP',             # 19
        'ED6_DT07/CH00154P._CP',             # 1A
        'ED6_DT07/CH00155P._CP',             # 1B
        'ED6_DT06/CH20137P._CP',             # 1C
        'ED6_DT06/CH20085P._CP',             # 1D
        'ED6_DT26/CH20282P._CP',             # 1E
        'ED6_DT27/CH04540P._CP',             # 1F
        'ED6_DT26/CH20352P._CP',             # 20
        'ED6_DT26/CH20353P._CP',             # 21
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1048609,
        ChipIndex           = 0x21,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1048609,
        ChipIndex           = 0x21,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1048609,
        ChipIndex           = 0x21,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1048609,
        ChipIndex           = 0x21,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2BA",          # 00, 0
        "Function_1_303",          # 01, 1
        "Function_2_344",          # 02, 2
        "Function_3_CF7",          # 03, 3
        "Function_4_D3F",          # 04, 4
        "Function_5_D48",          # 05, 5
        "Function_6_209F",         # 06, 6
        "Function_7_20DC",         # 07, 7
        "Function_8_2119",         # 08, 8
        "Function_9_6205",         # 09, 9
        "Function_10_6221",        # 0A, 10
        "Function_11_6240",        # 0B, 11
        "Function_12_6294",        # 0C, 12
        "Function_13_62E8",        # 0D, 13
        "Function_14_6320",        # 0E, 14
        "Function_15_643C",        # 0F, 15
        "Function_16_6465",        # 10, 16
        "Function_17_6498",        # 11, 17
        "Function_18_64C1",        # 12, 18
        "Function_19_654D",        # 13, 19
        "Function_20_667A",        # 14, 20
        "Function_21_6828",        # 15, 21
        "Function_22_6956",        # 16, 22
        "Function_23_6B0F",        # 17, 23
        "Function_24_6D10",        # 18, 24
        "Function_25_6D6E",        # 19, 25
        "Function_26_6E10",        # 1A, 26
        "Function_27_6E99",        # 1B, 27
    )


    def Function_0_2BA(): pass

    label("Function_0_2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2DE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x1, 0x4)
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)
    Jump("loc_302")

    label("loc_2DE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2EA"),
        (SWITCH_DEFAULT, "loc_302"),
    )


    label("loc_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FF")
    OP_71(0x1, 0x4)
    Event(0, 4)

    label("loc_2FF")

    Jump("loc_302")

    label("loc_302")

    Return()

    # Function_0_2BA end

    def Function_1_303(): pass

    label("Function_1_303")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x44F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_325")
    OP_4F(0x29, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x36), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_END)), "loc_33E")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_72(0x3, 0x2)
    Jump("loc_343")

    label("loc_33E")

    OP_71(0x3, 0x2)

    label("loc_343")

    Return()

    # Function_1_303 end

    def Function_2_344(): pass

    label("Function_2_344")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-270, 0, -16520, 0)
    OP_67(0, 5490, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(200000, 0)
    OP_6E(360, 0)
    SetChrPos(0x9, 3570, 0, -26960, 0)
    SetChrPos(0x8, 2570, 0, -27960, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 970)
    SetMapFlags(0x10)
    OP_11(0xC8, 0xC8, 0xC8, 0x61A8, 0x9470, 0x0)
    FadeToBright(2000, 0)

    def lambda_3F8():
        OP_8E(0xFE, 0x24E, 0x0, 0xFFFFC414, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3F8)
    Sleep(300)
    OP_8E(0x8, 0xFFFFFE0C, 0x0, 0xFFFFC054, 0x7D0, 0x0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x8,
        "#126F#6PThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#1154F#6PYes... I thought it would be here.\x02\x03",

            "#1150FBehold, Loewe.\x01",
            "A majestic thing, is it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "#124F#6P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)

    ChrTalk(    #3
        0x8,
        (
            "#120F#4PAre you really going to perform an\x01",
            "experiment on something like this?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #4
        0x9,
        (
            "#1150F#6PI understand your apprehension.\x02\x03",

            "Without this data, however, we\x01",
            "have no hope of completing the\x01",
            "beta. We MUST know.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(380, 100, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #5
        "\x07\x05...Who...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x8, 0x0, 0x0, 0x3)

    def lambda_63C():
        OP_6D(1720, 4250, -8690, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63C)

    def lambda_654():
        OP_67(0, 1070, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_654)

    def lambda_66C():
        OP_6B(3230, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_66C)

    def lambda_67C():
        OP_6C(351000, 7000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_67C)

    def lambda_68C():
        OP_6E(553, 7000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_68C)
    OP_B0(0x0, 0x5)
    OP_6F(0x0, 980)
    OP_70(0x0, 0x398)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 920)
    OP_70(0x0, 0x366)

    ChrTalk(    #6
        0x9,
        (
            "#1153F#5POh, I see we woke you.\x02\x03",

            "#1154FYour first time in the waking world\x01",
            "of mortals in twenty years, yes?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #7
        "\x07\x05...Mmmrrrgh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #8
        0x9,
        (
            "#1150F#5PThis is the first time we've met.\x01",
            "Allow me to introduce myself.\x02\x03",

            "You may call me Georg Weissmann.\x02\x03",

            "I am one of the Anguis--caretaker of\x01",
            "Ouroboros.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #9
        (
            "\x07\x05...\x02\x03",

            "Begone...\x02\x03",

            "This power which hangs about thee\x01",
            "like a mist... Familiar it be, somehow, but...\x02\x03",

            "Thy eyes betray thy purpose.\x02\x03",

            "In those windows I see a soul twisted and\x01",
            "bent...incapable of joy unyoked from bringing\x01",
            "suffering and agony to thy fellow man.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #10
        0x9,
        (
            "#1151F#5PWell, well! Such compliments!\x02\x03",

            "But I'm afraid I must deny your request--\x01",
            "I won't be going anywhere.\x02\x03",

            "After all, we've business regarding the\x01",
            "treasure of Aidios.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #11
        "\x07\x05...What...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #12
        0x9,
        "#1154F#5PShow him, Loewe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        "#121F#5P...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-1360, 0, -17130, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(206000, 0)
    OP_6E(360, 0)
    OP_8C(0x8, 0, 0)
    OP_8C(0x9, 0, 0)
    LoadEffect(0x0, "battle\\\\mgaria0.eff")
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)
    OP_99(0x8, 0x0, 0x4, 0x3E8)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(380, 100, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #14
        "\x07\x05...That...!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #15
        0x9,
        (
            "#1151F#5POh? Does this stir up memories\x01",
            "from twelve hundred years ago?\x02\x03",

            "It's merely a replica, but I dare say\x01",
            "it's well made enough, wouldn't you?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(380, 100, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #16
        (
            "\x07\x05...Surely thou dost not...\x02\x03",

            "Thou cannot mean...the Shining Ring!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #17
        0x9,
        "#1154F#5PAh, but I do.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)

    def lambda_C0C():
        OP_99(0x9, 0x0, 0x3, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_C0C)
    PlayEffect(0x0, 0x0, 0xFF, 590, 0, -15340, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_C56():
        OP_99(0x9, 0x3, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_C56)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x0, 0x2)
    Sleep(1000)

    def lambda_C78():
        OP_99(0x9, 0x7, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_C78)
    Sleep(1000)

    ChrTalk(    #18
        0x9,
        "#1155F#5PNow, then. Our final test...awaits.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_AD(0x2400A8, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x1A00)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0100   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_2_344 end

    def Function_3_CF7(): pass

    label("Function_3_CF7")

    Sleep(500)

    def lambda_D02():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D02)
    Sleep(100)

    def lambda_D15():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D15)
    Sleep(5000)

    def lambda_D28():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D28)

    def lambda_D36():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D36)
    Return()

    # Function_3_CF7 end

    def Function_4_D3F(): pass

    label("Function_4_D3F")

    Call(0, 5)
    Call(0, 8)
    Return()

    # Function_4_D3F end

    def Function_5_D48(): pass

    label("Function_5_D48")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5F")
    Call(0, 26)
    Call(0, 27)

    label("loc_D5F")

    OP_6D(3160, 0, -25690, 0)
    OP_67(0, 9710, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0xAFC8, 0x11170, 0x0)
    SetChrPos(0x101, 2800, 0, -25400, 0)
    SetChrPos(0x106, 4180, 0, -25530, 0)
    SetChrPos(0x107, 4310, 0, -26920, 0)
    SetChrPos(0xF9, 2780, 0, -26920, 0)
    OP_A1(0xA, 0x0)
    SetChrPos(0xA, 10000, 300, 14130, 192)
    OP_6F(0x0, 970)
    OP_70(0x0, 0x410)
    OP_8C(0xB, 180, 0)
    OP_CF(0xB, 0x0, "Frame127_FireEmitter")
    SetChrFlags(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x249F0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x7D0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EFB")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F39")

    label("loc_EFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F22")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F39")

    label("loc_F22")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F39")

    Sleep(1000)

    ChrTalk(    #19
        0x101,
        "#1020F#6P(Whoa...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x106,
        "#057F#6P(There it is.)\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x51)
    Sleep(400)

    def lambda_F84():
        OP_6D(8480, 0, 16800, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F84)

    def lambda_F9C():
        OP_67(0, 4000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F9C)

    def lambda_FB4():
        OP_6B(4090, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_FB4)

    def lambda_FC4():
        OP_6C(347000, 6000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_FC4)
    OP_6E(421, 6000)
    Sleep(1500)
    Fade(500)
    OP_6D(3160, 0, -25690, 0)
    OP_67(0, 9710, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #21
        0x107,
        "#065F#5P(Is it sleeping?)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A0")

    ChrTalk(    #22
        0x103,
        (
            "#022F#6P(Looks like it.)\x02\x03",

            "(I don't see Loewe around anywhere,\x01",
            "either.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DE")

    label("loc_10A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1107")

    ChrTalk(    #23
        0x105,
        (
            "#043F#6P(It appears to be, yes.)\x02\x03",

            "(I don't see that Loewe man anywhere,\x01",
            "either.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DE")

    label("loc_1107")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_117B")

    ChrTalk(    #24
        0x104,
        (
            "#035F#6P(It appears so.)\x02\x03",

            "#030F(Our lion-hearted friend also appears\x01",
            "to have taken his exit.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DE")

    label("loc_117B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DE")

    ChrTalk(    #25
        0x108,
        (
            "#070F(Looks like it.)\x02\x03",

            "(That man called Loewe doesn't\x01",
            "seem to be here, either.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DE")


    ChrTalk(    #26
        0x101,
        "#1006F#6P(This might be our chance.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    def lambda_1215():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1215)
    Sleep(300)

    ChrTalk(    #27
        0x101,
        "#1002F#6P(Agate, what should we do?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)
    Sleep(500)

    ChrTalk(    #28
        0x106,
        (
            "#053F#4P(First, let me close in by myself.)\x02\x03",

            "#051F(With a bit of luck, I can break that\x01",
            "Gospel with one good swing.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1002F#6P(Okay...good luck.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x107,
        "#063F#5P(Agate...!)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)

    ChrTalk(    #31
        0x106,
        (
            "#051F#4P(Don't worry, shortstuff, I'll be fine.)\x02\x03",

            "(Just be ready to back me up if\x01",
            "I screw this up.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x107,
        "#560F#5P(Okay!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1006F#6P(Be careful!)\x02",
    )

    CloseMessageWindow()

    def lambda_13B4():
        OP_69(0xFE, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_13B4)

    def lambda_13C2():
        OP_67(0, 5580, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13C2)

    def lambda_13DA():
        OP_6C(336000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13DA)

    def lambda_13EA():

        label("loc_13EA")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_13EA")

    QueueWorkItem2(0x101, 2, lambda_13EA)

    def lambda_13FB():

        label("loc_13FB")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_13FB")

    QueueWorkItem2(0x107, 2, lambda_13FB)

    def lambda_140C():

        label("loc_140C")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_140C")

    QueueWorkItem2(0xF9, 2, lambda_140C)
    Sleep(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 23)
    SetChrSubChip(0x106, 0)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    SetChrFlags(0x106, 0x4)
    OP_C4(0x0, 0x40)
    OP_6A(0x106)
    Sleep(300)
    OP_8C(0x106, 0, 400)
    Sleep(300)
    OP_8E(0x106, 0xF5A, 0x0, 0xFFFFD5D0, 0x1F40, 0x0)
    OP_8C(0x106, 180, 400)
    Sleep(1000)
    OP_6A(0xFF)
    OP_C4(0x1, 0x40)
    OP_44(0x101, 0x2)
    OP_44(0x107, 0x2)
    OP_44(0xF9, 0x2)

    def lambda_148F():
        OP_6D(6440, 0, 6810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_148F)

    def lambda_14A7():
        OP_6B(2960, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14A7)
    OP_6E(206, 3000)
    Sleep(1000)

    ChrTalk(    #34
        0x106,
        "#057F#2P(So that's a Gospel, huh?)\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sleep(200)
    Fade(500)
    OP_6D(3410, 0, -10000, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(336000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x106, 0x40)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 32)
    OP_0D()
    Sleep(300)
    OP_22(0x9D, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp009_00.eff")

    def lambda_1577():

        label("loc_1577")

        OP_99(0xFE, 0x1, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1577")

    QueueWorkItem2(0x106, 2, lambda_1577)
    Sleep(1000)

    ChrTalk(    #35
        0x106,
        "#053F(Let's do this.)\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_44(0x106, 0x2)

    def lambda_15B3():
        OP_6D(5910, 0, -11000, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15B3)
    ClearChrFlags(0x106, 0x2)
    SetChrFlags(0x106, 0x800)
    SetChrChipByIndex(0x106, 24)
    SetChrSubChip(0x106, 0)

    def lambda_15DF():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_15DF)

    def lambda_15ED():
        OP_96(0xFE, 0x1716, 0x0, 0xFFFFD508, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_15ED)
    WaitChrThread(0x106, 0x2)
    WaitChrThread(0x106, 0x3)

    def lambda_1615():
        OP_6D(7100, 0, 4690, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1615)
    SetChrFlags(0x106, 0x1000)

    ChrTalk(    #36 op#5
        0x106,
        "#054F#2P#3SRAAAAAAAGH!\x05\x02",
    )

    OP_8E(0x106, 0x1D56, 0x0, 0x12C, 0x2EE0, 0x0)
    OP_44(0x106, 0x1)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1674():
        OP_6D(7100, 2000, 4690, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1674)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1691():
        OP_96(0x106, 0x1CE8, 0x578, 0xD48, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1691)
    Sleep(100)
    SetChrChipByIndex(0x106, 25)

    def lambda_16B9():
        OP_99(0xFE, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_16B9)

    def lambda_16C9():
        OP_6D(6810, 0, 5420, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_16C9)

    def lambda_16E1():
        OP_67(0, 7660, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16E1)

    def lambda_16F9():
        OP_6B(2860, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16F9)

    def lambda_1709():
        OP_6C(336000, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1709)
    Sleep(300)

    def lambda_171E():
        OP_99(0xFE, 0x4, 0x5, 0x9C4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_171E)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x320)
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0x106, 0x2)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 1045)
    OP_20(0x0)
    OP_22(0x9B, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 7850, 2000, 4370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x106, 24)
    SetChrSubChip(0x106, 0)

    def lambda_17A3():
        OP_96(0x106, 0x1BE4, 0x0, 0x672, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_17A3)
    WaitChrThread(0x106, 0x0)
    OP_8C(0x106, 45, 0)
    SetChrChipByIndex(0x106, 25)

    def lambda_17D2():
        OP_99(0x106, 0x5, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_17D2)

    def lambda_17E2():
        OP_96(0x106, 0x14A0, 0x0, 0xFFFFF894, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_17E2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetMapFlags(0x10)
    OP_6D(6460, 0, 13890, 0)
    OP_67(0, 3020, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(351000, 0)
    OP_6E(498, 0)
    WaitChrThread(0x106, 0x0)
    SetChrChipByIndex(0x106, 23)
    ClearChrFlags(0x106, 0x800)
    OP_0D()
    Sleep(500)
    OP_22(0x12C, 0x0, 0x5A)
    Sleep(2000)

    ChrTalk(    #37
        0x106,
        "#054FDid I get it?!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    LoadEffect(0x2, "map\\\\mp007_00.eff")
    OP_22(0x90, 0x0, 0x64)
    PlayEffect(0x2, 0x1, 0xB, 900, 900, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_18E0():
        OP_6B(3380, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18E0)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 28)
    SetChrSubChip(0x106, 0)
    Sleep(500)
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0x19)
    OP_6F(0x0, 970)
    OP_70(0x0, 0x410)
    OP_8F(0xA, 0x26AC, 0x12C, 0x36CE, 0x2710, 0x0)
    OP_8F(0xA, 0x2710, 0x12C, 0x3732, 0x2710, 0x0)
    OP_8F(0xA, 0x26AC, 0x12C, 0x36CE, 0x2710, 0x0)
    OP_8F(0xA, 0x2710, 0x12C, 0x3732, 0x2710, 0x0)
    OP_8F(0xA, 0x26AC, 0x12C, 0x36CE, 0x2710, 0x0)
    OP_8F(0xA, 0x2710, 0x12C, 0x3732, 0x2710, 0x0)
    OP_73(0x0)
    OP_82(0x1, 0x2)
    OP_1D(0x36)
    Sleep(500)

    def lambda_19BC():
        OP_6D(7030, 2640, 15970, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19BC)

    def lambda_19D4():
        OP_67(0, 1000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19D4)

    def lambda_19EC():
        OP_6C(15000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19EC)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 1045)
    OP_70(0x0, 0x42E)
    OP_22(0x122, 0x0, 0x64)
    OP_73(0x0)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 125)
    OP_70(0x0, 0xB4)
    OP_8C(0x106, 0, 0)
    Sleep(75)
    OP_8C(0x106, 315, 0)
    Sleep(425)
    OP_23(0x193)
    Sleep(700)
    Sleep(100)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x37)
    Fade(500)
    OP_6D(-840, 0, 5360, 0)
    OP_67(0, 4730, -10000, 0)
    OP_6B(4190, 0)
    OP_6C(315000, 0)
    OP_6E(352, 0)
    SetChrPos(0x106, 3860, 0, -4770, 0)
    OP_8C(0x106, 0, 0)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 28)
    SetChrSubChip(0x106, 3)
    OP_0D()

    ChrTalk(    #38
        0x106,
        "#057F#5PAw, hell! Too shallow!\x02",
    )

    CloseMessageWindow()

    def lambda_1B18():
        OP_6D(-500, 1060, 12470, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B18)

    def lambda_1B30():
        OP_67(0, 3440, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B30)

    def lambda_1B48():
        OP_6B(3500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B48)

    def lambda_1B58():
        OP_6C(339000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1B58)
    Sleep(500)
    Sleep(200)
    LoadEffect(0x3, "monster\\ms30703.eff")
    OP_72(0x0, 0x20)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x78)
    Sleep(1000)

    def lambda_1BA0():
        OP_6D(3510, 380, 5270, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BA0)

    def lambda_1BB8():
        OP_67(0, 2900, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BB8)

    def lambda_1BD0():
        OP_6B(3190, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BD0)

    def lambda_1BE0():
        OP_6C(339000, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1BE0)

    def lambda_1BF0():
        OP_6E(462, 300)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_1BF0)
    PlayEffect(0x3, 0x0, 0xB, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x106, 0, 0, 0, 0)
    OP_22(0x121, 0x0, 0x64)
    Sleep(100)
    OP_43(0x106, 0x0, 0x0, 0x7)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x37)
    Sleep(1000)
    SetChrPos(0x107, 9710, 0, -14620, 0)

    ChrTalk(    #39
        0x107,
        "#2PAgate!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    LoadEffect(0x3, "map\\\\mp019_00.eff")
    SetChrPos(0xC, 6500, 5510, 9600, 0)
    OP_22(0x1FA, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0xFF, 14500, 5730, -23660, 0, 0, 0, 1000, 1000, 1000, 0xB, 0, 1500, 0, 0)
    Fade(500)
    OP_6D(5000, 2150, 160, 0)
    OP_67(0, 1730, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(339000, 0)
    OP_6E(530, 0)
    SetChrPos(0x106, 8020, 0, -5130, 0)
    SetChrSubChip(0x106, 2)
    Sleep(1500)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x4B)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x37)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x107, 0x40)
    SetChrFlags(0xF9, 0x40)
    SetChrPos(0x101, 12470, 0, -15800, 0)
    SetChrPos(0x107, 14010, 0, -16620, 0)
    SetChrPos(0xF9, 13000, 0, -17160, 0)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 21)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 6)
    SetChrSubChip(0xF9, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1DD9"),
        (3, "loc_1DE1"),
        (4, "loc_1DE9"),
        (7, "loc_1DF1"),
        (SWITCH_DEFAULT, "loc_1DF9"),
    )


    label("loc_1DD9")

    SetChrChipByIndex(0xF9, 9)
    Jump("loc_1DF9")

    label("loc_1DE1")

    SetChrChipByIndex(0xF9, 12)
    Jump("loc_1DF9")

    label("loc_1DE9")

    SetChrChipByIndex(0xF9, 15)
    Jump("loc_1DF9")

    label("loc_1DF1")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_1DF9")

    label("loc_1DF9")

    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x107, 0x1000)
    SetChrFlags(0xF9, 0x1000)

    def lambda_1E0E():
        OP_8E(0xFE, 0x1B76, 0x0, 0xFFFFEA16, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E0E)

    def lambda_1E29():
        OP_8E(0xFE, 0x20F8, 0x0, 0xFFFFE408, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1E29)
    Sleep(200)

    def lambda_1E49():
        OP_8E(0xFE, 0x1BB2, 0x0, 0xFFFFE1CE, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1E49)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 0)
    WaitChrThread(0x107, 0x1)
    SetChrChipByIndex(0x107, 20)
    SetChrSubChip(0x107, 0)
    WaitChrThread(0xF9, 0x1)
    SetChrSubChip(0xF9, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1E9F"),
        (3, "loc_1EA7"),
        (4, "loc_1EAF"),
        (7, "loc_1EB7"),
        (SWITCH_DEFAULT, "loc_1EBF"),
    )


    label("loc_1E9F")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_1EBF")

    label("loc_1EA7")

    SetChrChipByIndex(0xF9, 11)
    Jump("loc_1EBF")

    label("loc_1EAF")

    SetChrChipByIndex(0xF9, 14)
    Jump("loc_1EBF")

    label("loc_1EB7")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_1EBF")

    label("loc_1EBF")


    ChrTalk(    #40
        0x101,
        "#1005F#5PAgate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x106,
        (
            "#054F#2PI cracked it but didn't quite break it!\x02\x03",

            "I just need one more good swing!\x02\x03",

            "Give me a hand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1006F#5PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x107,
        "#062F#5POkay!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F8C")

    ChrTalk(    #44
        0x103,
        "#024F#5PLet's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2011")

    label("loc_1F8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB8")

    ChrTalk(    #45
        0x105,
        "#046F#5PI'm with you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2011")

    label("loc_1FB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FEA")

    ChrTalk(    #46
        0x104,
        "#530F#5POnward, my friends!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2011")

    label("loc_1FEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2011")

    ChrTalk(    #47
        0x108,
        "#076F#5PHere we go!\x02",
    )

    CloseMessageWindow()

    label("loc_2011")

    Fade(500)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 125)
    OP_70(0x0, 0xB4)
    Sleep(1300)

    def lambda_2034():
        OP_6B(1500, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2034)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    Sleep(800)
    FadeToBright(0, 0)
    OP_0D()
    OP_44(0x101, 0x2)
    OP_23(0x90)
    Battle(0x44F, 0x0, 0x0, 0x80, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2094"),
        (SWITCH_DEFAULT, "loc_2099"),
    )


    label("loc_2094")

    OP_B4(0x0)
    Jump("loc_2099")

    label("loc_2099")

    OP_20(0x0)
    Return()

    # Function_5_D48 end

    def Function_6_209F(): pass

    label("Function_6_209F")

    ClearChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 24)
    OP_96(0x106, 0xF14, 0x0, 0xFFFFED5E, 0x1F4, 0x1770)
    OP_8C(0x106, 0, 0)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 2)
    SetChrChipByIndex(0x106, 28)
    Return()

    # Function_6_209F end

    def Function_7_20DC(): pass

    label("Function_7_20DC")

    ClearChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 24)
    OP_96(0x106, 0x2490, 0x0, 0xFFFFEC82, 0x1F4, 0x1770)
    OP_8C(0x106, 0, 0)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 2)
    SetChrChipByIndex(0x106, 28)
    Return()

    # Function_7_20DC end

    def Function_8_2119(): pass

    label("Function_8_2119")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(9500, 9450, 12390, 0)
    OP_67(0, 5510, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(346000, 0)
    OP_6E(510, 0)
    OP_71(0x1, 0x4)
    SetChrPos(0x106, 4950, 0, -2860, 0)
    SetChrPos(0x101, 3900, 0, -3700, 0)
    SetChrPos(0x107, 5990, 0, -3790, 0)
    SetChrPos(0xF9, 5500, 0, -4500, 0)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 3)
    SetChrChipByIndex(0x106, 28)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x107, 20)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0xF9, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_21ED"),
        (3, "loc_21F5"),
        (4, "loc_21FD"),
        (7, "loc_2205"),
        (SWITCH_DEFAULT, "loc_220D"),
    )


    label("loc_21ED")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_220D")

    label("loc_21F5")

    SetChrChipByIndex(0xF9, 11)
    Jump("loc_220D")

    label("loc_21FD")

    SetChrChipByIndex(0xF9, 14)
    Jump("loc_220D")

    label("loc_2205")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_220D")

    label("loc_220D")

    OP_A1(0xA, 0x0)
    SetChrPos(0xA, 10000, 300, 14130, 192)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 630)
    OP_70(0x0, 0x280)
    OP_8C(0xB, 180, 0)
    OP_CF(0xB, 0x0, "Frame127_FireEmitter")
    SetChrFlags(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x249F0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    OP_43(0xA, 0x0, 0x0, 0x19)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 640)
    OP_70(0x0, 0x29E)
    Sleep(3000)
    Fade(500)
    OP_6D(4300, 0, -3270, 0)
    OP_67(0, 7030, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_2306():
        OP_6D(4300, 0, -4270, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2306)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2370")
    OP_62(0xF9, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_23A4")

    label("loc_2370")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2392")
    OP_62(0xF9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_23A4")

    label("loc_2392")

    OP_62(0xF9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_23A4")

    OP_43(0xF9, 0x1, 0x0, 0x12)
    Sleep(100)
    OP_43(0x101, 0x1, 0x0, 0xF)
    Sleep(50)
    OP_43(0x107, 0x1, 0x0, 0x11)
    Sleep(100)
    OP_43(0x106, 0x1, 0x0, 0x10)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #48
        0x107,
        "#065F#5PAaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1005F#6POh, come on! I thought we beat it!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_245D")

    ChrTalk(    #50
        0x103,
        "#523F#5PImmortal...just like the legends!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2555")

    label("loc_245D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B1")

    ChrTalk(    #51
        0x105,
        (
            "#042F#5PIts life force is infinite...just as the\x01",
            "legends say!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2555")

    label("loc_24B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2506")

    ChrTalk(    #52
        0x104,
        (
            "#039F#5PAs the legends state...no weapon\x01",
            "of man can defeat it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2555")

    label("loc_2506")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2555")

    ChrTalk(    #53
        0x108,
        (
            "#077F#5PNo man can best it...\x01",
            "It's just as the legends say.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2555")

    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2577():
        OP_6D(3260, 8370, -1910, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2577)

    def lambda_258F():
        OP_67(0, 2800, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_258F)

    def lambda_25A7():
        OP_6B(3400, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25A7)

    def lambda_25B7():
        OP_6C(315000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_25B7)

    def lambda_25C7():
        OP_6E(342, 2500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_25C7)
    WaitChrThread(0x101, 0x0)
    Sleep(1500)
    Fade(500)
    OP_6D(4300, 0, -4270, 0)
    OP_67(0, 7030, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #54
        0x106,
        "#054F#6PTita! You got a flash canister left?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)
    Sleep(500)

    ChrTalk(    #55
        0x107,
        "#064F#5PYeah!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2700")

    ChrTalk(    #56
        0x106,
        (
            "#054F#6PLoad it!\x01",
            "Get ready to give us an opening!\x02\x03",

            "Estelle, Scherazard!\x02\x03",

            "Keep that thing cornered for just a second!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2892")

    label("loc_2700")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2789")

    ChrTalk(    #57
        0x106,
        (
            "#054F#6PLoad it!\x01",
            "Get ready to give us an opening!\x02\x03",

            "Estelle! Princess!\x02\x03",

            "Keep that thing cornered for just\x01",
            "a second!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2892")

    label("loc_2789")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2811")

    ChrTalk(    #58
        0x106,
        (
            "#054F#6PLoad it! Get ready to give us an opening!\x02\x03",

            "Estelle! Blondie!\x02\x03",

            "Keep that thing cornered for just a second!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2892")

    label("loc_2811")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2892")

    ChrTalk(    #59
        0x106,
        (
            "#054F#6PLoad it! Get ready to give us an opening!\x02\x03",

            "Estelle! Zin!\x02\x03",

            "Keep that thing cornered for just a second!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2892")


    ChrTalk(    #60
        0x101,
        "#1020F#6PHuh?!\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 23)
    SetChrSubChip(0x106, 0)
    OP_21()
    OP_1D(0x2B)
    Sleep(500)

    def lambda_28CD():
        OP_69(0xFE, 0x5DC)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_28CD)
    OP_67(0, 4500, -10000, 1500)
    OP_C4(0x0, 0x40)
    OP_6A(0x106)

    def lambda_28F5():

        label("loc_28F5")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_28F5")

    QueueWorkItem2(0x101, 1, lambda_28F5)

    def lambda_2906():

        label("loc_2906")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_2906")

    QueueWorkItem2(0x107, 1, lambda_2906)

    def lambda_2917():

        label("loc_2917")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_2917")

    QueueWorkItem2(0xF9, 1, lambda_2917)
    ClearChrFlags(0x106, 0x2)
    ClearChrFlags(0x106, 0x20)
    ClearChrFlags(0x106, 0x10)
    SetChrFlags(0x106, 0x4)
    SetChrFlags(0x106, 0x20)
    SetChrFlags(0x106, 0x1000)
    Sleep(500)
    OP_43(0x106, 0x0, 0x0, 0xD)
    OP_8E(0x106, 0xFFFFF0CE, 0x0, 0xFFFFFE8E, 0x2710, 0x0)
    OP_44(0x106, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x106, 2)
    OP_96(0x106, 0xFFFFEC32, 0x7D0, 0x53C, 0x9C4, 0x2710)
    SetChrSubChip(0x106, 3)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x106, 270, 0)
    SetChrSubChip(0x106, 4)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x106, 6)
    OP_96(0x106, 0xFFFFDDF0, 0xFA0, 0x62C, 0x9C4, 0x2710)
    SetChrSubChip(0x106, 7)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x106, 0, 0)
    SetChrSubChip(0x106, 6)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x106, 2)
    OP_96(0x106, 0xFFFFD698, 0x1770, 0x1112, 0x9C4, 0x2710)
    SetChrSubChip(0x106, 3)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    SetChrSubChip(0x106, 4)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x106, 6)
    OP_96(0x106, 0xFFFFD1A2, 0x1F40, 0x1DE2, 0x9C4, 0x2710)
    SetChrSubChip(0x106, 7)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x106, 90, 0)
    SetChrSubChip(0x106, 0)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x106, 2)
    OP_96(0x106, 0xFFFFE55C, 0x2710, 0x1EDC, 0x9C4, 0x2710)
    SetChrSubChip(0x106, 3)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    SetChrChipByIndex(0x106, 23)
    SetChrSubChip(0x106, 0)
    ClearChrFlags(0x106, 0x20)
    Sleep(200)
    OP_6A(0xFF)
    OP_C4(0x1, 0x40)

    def lambda_2AA5():
        OP_6B(2800, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AA5)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 8)
    SetChrChipByIndex(0x106, 32)
    OP_0D()
    Sleep(300)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(500)

    def lambda_2ADE():

        label("loc_2ADE")

        OP_99(0xFE, 0x9, 0xF, 0x5DC)
        OP_48()
        Jump("loc_2ADE")

    QueueWorkItem2(0x106, 2, lambda_2ADE)
    Sleep(1000)
    Fade(500)
    OP_6D(4300, 0, -4270, 0)
    OP_67(0, 7030, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x101, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)
    OP_0D()

    ChrTalk(    #61
        0x107,
        "#560F#2PAh!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B89")

    ChrTalk(    #62
        0x103,
        "#020F#5PI see... That's your idea!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C32")

    label("loc_2B89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BC1")

    ChrTalk(    #63
        0x105,
        "#040F#5PYou're going to... I see!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C32")

    label("loc_2BC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BFE")

    ChrTalk(    #64
        0x104,
        "#030F#5PHeh... A bold move, my friend!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C32")

    label("loc_2BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C32")

    ChrTalk(    #65
        0x108,
        "#070F#5PSo that's what you mean!\x02",
    )

    CloseMessageWindow()

    label("loc_2C32")

    TurnDirection(0x101, 0x107, 500)

    ChrTalk(    #66
        0x101,
        (
            "#1005F#6PTita! Fire it up, not at the dragon!\x02\x03",

            "We'll keep it still!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #67
        0x107,
        "#062F#2POkay!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x1, "Scraft\\\\sc003_12.eff")
    LoadEffect(0x2, "battle\\\\btgun60.eff")
    OP_8C(0x107, 0, 400)
    OP_8C(0x101, 0, 400)
    OP_8C(0xF9, 0, 400)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 22)
    SetChrSubChip(0x107, 1)
    OP_0D()
    Sleep(500)
    WaitChrThread(0x101, 0x3)
    PlayEffect(0x2, 0xFF, 0x107, 0, 500, 500, 0, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2D38():
        OP_99(0x107, 0x1, 0xD, 0x5DC)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2D38)
    PlayEffect(0x1, 0xFF, 0xFF, 5990, 11000, -2000, 0, -70, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(500)
    OP_6D(7850, 19290, 3840, 0)
    OP_67(0, 8119, -10000, 0)
    OP_6B(1530, 0)
    OP_6C(315000, 0)
    OP_6E(594, 0)
    OP_0D()
    Sleep(200)
    LoadEffect(0x3, "map\\\\mp080_00.eff")
    PlayEffect(0x3, 0x1, 0xFF, 7490, 22750, 4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x12D, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_22(0x195, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    Sleep(2000)
    Fade(500)
    OP_6D(4140, 0, -4630, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(3310, 0)
    OP_6C(302000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #68
        0x101,
        "#1002F#6P(Now!)\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2EAE():
        OP_6D(6170, 3860, 9530, 2000)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2EAE)

    def lambda_2EC6():
        OP_67(0, 5160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2EC6)

    def lambda_2EDE():
        OP_6B(3200, 2000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2EDE)

    def lambda_2EEE():
        OP_6C(315000, 2000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_2EEE)

    def lambda_2EFE():
        OP_6E(447, 2000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2EFE)
    LoadEffect(0x1, "scraft\\\\sc000_11.eff")
    OP_43(0x101, 0x1, 0x0, 0x13)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_2F3F"),
        (3, "loc_2F49"),
        (4, "loc_2F68"),
        (7, "loc_2F72"),
        (SWITCH_DEFAULT, "loc_2F7C"),
    )


    label("loc_2F3F")

    OP_43(0xF9, 0x1, 0x0, 0x15)
    Jump("loc_2F7C")

    label("loc_2F49")

    LoadEffect(0x3, "battle\\btgun00.eff")
    OP_43(0xF9, 0x1, 0x0, 0x14)
    Jump("loc_2F7C")

    label("loc_2F68")

    OP_43(0xF9, 0x1, 0x0, 0x16)
    Jump("loc_2F7C")

    label("loc_2F72")

    OP_43(0xF9, 0x1, 0x0, 0x17)
    Jump("loc_2F7C")

    label("loc_2F7C")

    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF9, 0x1)

    def lambda_2F8C():

        label("loc_2F8C")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_2F8C")

    QueueWorkItem2(0x101, 3, lambda_2F8C)

    def lambda_2F9D():

        label("loc_2F9D")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_2F9D")

    QueueWorkItem2(0xF9, 3, lambda_2F9D)
    WaitChrThread(0xF9, 0x1)
    SetChrFlags(0x107, 0x80)

    def lambda_2FB8():
        OP_6D(3460, 0, 11500, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2FB8)

    def lambda_2FD0():
        OP_67(0, 3840, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FD0)

    def lambda_2FE8():
        OP_6B(5090, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2FE8)

    def lambda_2FF8():
        OP_6C(327000, 2500)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2FF8)

    def lambda_3008():
        OP_6E(358, 2500)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_3008)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 675)
    OP_70(0x0, 0x2CB)
    Sleep(1000)
    OP_22(0x88, 0x0, 0x64)
    OP_73(0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(3240, 0, 860, 0)
    OP_67(0, 4340, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(3000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(2000)
    Fade(500)
    OP_44(0x101, 0x3)
    OP_44(0xF9, 0x3)
    SetChrPos(0x101, -3310, 0, -12120, 0)
    SetChrPos(0x107, -1730, 0, -13800, 0)
    SetChrPos(0xF9, -2970, 0, -14040, 0)
    OP_6D(-6970, 10090, 7890, 0)
    OP_67(0, 3200, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x106, 0x2)
    ClearChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 27)
    OP_C4(0x0, 0x40)
    OP_69(0x106, 0x0)
    OP_6A(0x106)
    OP_0D()
    Sleep(500)

    ChrTalk(    #69
        0x106,
        "#053F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_3150():
        OP_6B(3200, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3150)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 8)
    SetChrChipByIndex(0x106, 32)
    OP_0D()

    ChrTalk(    #70 op#5
        0x106,
        "#054F#5SHYAAAAAAAAAAAAH!\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    Fade(250)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 8)
    SetChrChipByIndex(0x106, 32)

    def lambda_31C2():

        label("loc_31C2")

        OP_99(0xFE, 0x9, 0xF, 0x7D0)
        OP_48()
        Jump("loc_31C2")

    QueueWorkItem2(0x106, 2, lambda_31C2)
    Sleep(300)
    LoadEffect(0x1, "map\\\\mp009_00.eff")
    LoadEffect(0x2, "map\\\\mp081_00.eff")
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x106, 0x2)
    SetChrFlags(0x106, 0x4)

    def lambda_3219():
        OP_6C(0, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3219)
    SetChrSubChip(0x106, 17)
    Sleep(200)
    SetChrSubChip(0x106, 18)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_323D():
        OP_96(0x106, 0xA5A, 0x640, 0xFFFFF31C, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_323D)
    Sleep(500)
    Fade(500)
    OP_6D(840, 0, -2170, 0)
    OP_67(0, 20860, -10000, 0)
    OP_6C(327000, 0)
    OP_6B(890, 0)
    OP_6E(503, 0)

    def lambda_32A2():
        OP_6D(2000, 0, -2900, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_32A2)

    def lambda_32BA():
        OP_6B(630, 500)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_32BA)
    SetChrSubChip(0x106, 19)
    SetChrFlags(0x106, 0x800)
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0x106, 0x1)
    OP_6A(0xFF)
    OP_C4(0x1, 0x40)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x1F4)
    OP_20(0x0)
    OP_22(0x9B, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 3000, 1700, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 2650, 1600, -3300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_75(0x0, 0xC, 0x7)
    OP_22(0x268, 0x0, 0x64)
    Sleep(300)
    Sleep(1000)
    OP_6F(0x0, 720)
    OP_70(0x0, 0x32A)
    OP_22(0x195, 0x0, 0x64)
    ClearChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 25)
    SetChrSubChip(0x106, 6)
    OP_8C(0x106, 45, 0)
    SetChrFlags(0x106, 0x800)
    SetChrFlags(0x106, 0x20)
    OP_82(0x0, 0x2)

    def lambda_33BD():
        OP_96(0x106, 0x370, 0x0, 0xFFFFE3B8, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_33BD)

    def lambda_33DB():
        OP_99(0xFE, 0x5, 0x0, 0x9C4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_33DB)
    WaitChrThread(0x106, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_91(0x106, 0x0, 0x0, 0xFFFFF830, 0xFA0, 0x0)
    WaitChrThread(0x106, 0x1)
    SetChrChipByIndex(0x106, 26)

    def lambda_3413():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3413)
    Sleep(500)
    Fade(500)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(5300, 0, 8070, 0)
    OP_67(0, 7510, -10000, 0)
    OP_6B(3680, 0)
    OP_6C(341000, 0)
    OP_6E(435, 0)
    ClearChrFlags(0x106, 0x800)
    Sleep(2500)
    OP_22(0x88, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x193, 0x0, 0x64)
    OP_73(0x0)
    Sleep(300)
    Fade(500)
    OP_6D(-2870, 0, -12330, 0)
    OP_67(0, 6010, -10000, 0)
    OP_6B(2490, 0)
    OP_6C(336000, 0)
    OP_6E(329, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x107, 65535)
    SetChrChipByIndex(0xF9, 65535)
    ClearChrFlags(0x107, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0xF9, 0x80)
    OP_0D()
    OP_75(0x0, 0xD, 0x7)
    Sleep(500)

    ChrTalk(    #71
        0x101,
        "#1008FWe did it!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3558")

    ChrTalk(    #72
        0x103,
        "#021F#6PThe Gospel's broken!\x02",
    )

    CloseMessageWindow()
    Jump("loc_35F9")

    label("loc_3558")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_358C")

    ChrTalk(    #73
        0x105,
        "#542F#6PThe Gospel is broken!\x02",
    )

    CloseMessageWindow()
    Jump("loc_35F9")

    label("loc_358C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35CB")

    ChrTalk(    #74
        0x104,
        "#030FWell struck! The Gospel is no more!\x02",
    )

    CloseMessageWindow()
    Jump("loc_35F9")

    label("loc_35CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35F9")

    ChrTalk(    #75
        0x108,
        "#070FThe Gospel shattered!\x02",
    )

    CloseMessageWindow()

    label("loc_35F9")

    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #76
        0x107,
        "#065F#5PAgate!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x1)
    Sleep(300)

    def lambda_3631():
        OP_8E(0xFE, 0x244, 0x0, 0xFFFFD6FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3631)
    Sleep(300)

    def lambda_3651():
        OP_8E(0xFE, 0xFFFFFD3A, 0x0, 0xFFFFDF30, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3651)

    def lambda_366C():
        OP_6D(-330, 0, -7100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_366C)

    def lambda_3684():
        OP_67(0, 5350, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3684)

    def lambda_369C():
        OP_6C(348000, 3000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_369C)
    Sleep(100)

    def lambda_36B1():
        OP_8E(0xFE, 0xFFFFFD1C, 0x0, 0xFFFFD760, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_36B1)
    WaitChrThread(0x107, 0x1)

    def lambda_36D1():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_36D1)
    WaitChrThread(0x101, 0x1)

    def lambda_36E4():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36E4)
    WaitChrThread(0xF9, 0x1)
    TurnDirection(0xF9, 0x106, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #77
        0x107,
        "#065F#5PAgate! You okay?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x106,
        "#053F#5PYeah... I'm fine.\x02",
    )

    CloseMessageWindow()
    OP_99(0x106, 0x3, 0x0, 0x5DC)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x106, 0x800)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x106, 225, 400)
    Sleep(500)

    ChrTalk(    #79
        0x106,
        "#051F#2PLooks like it worked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#1001F#6PYeah! Holy Stregas, that was cool!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3824")

    ChrTalk(    #81
        0x103,
        (
            "#021F#5PHeh. Nice job taking the spotlight\x01",
            "there, Mister Heavy Blade.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38EB")

    label("loc_3824")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_385E")

    ChrTalk(    #82
        0x105,
        "#041F#5PAgate, that was incredible!\x02",
    )

    CloseMessageWindow()
    Jump("loc_38EB")

    label("loc_385E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38B9")

    ChrTalk(    #83
        0x104,
        (
            "#031F#5PGoodness. You've stolen the spotlight\x01",
            "and my heart entirely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38EB")

    label("loc_38B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38EB")

    ChrTalk(    #84
        0x108,
        "#071F#5PHaha! Very impressive.\x02",
    )

    CloseMessageWindow()

    label("loc_38EB")


    ChrTalk(    #85
        0x106,
        (
            "#051F#2PHeh.\x02\x03",

            "Well, we've managed to defeat the dragon,\x01",
            "somehow, so I guess that means things're--\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #86
        "\x07\x05...Impressive...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39FF")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A3D")

    label("loc_39FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A26")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A3D")

    label("loc_3A26")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3A3D")

    Sleep(1000)

    ChrTalk(    #87
        0x101,
        "#1020F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x107,
        "#065FTh-That voice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x106,
        "#055F#2PWhere the hell's it comin' from?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ACD")

    ChrTalk(    #90
        0x103,
        "#024F#5PCould it be...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B43")

    label("loc_3ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AF9")

    ChrTalk(    #91
        0x105,
        "#043F#5PImpossible...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B43")

    label("loc_3AF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B1E")

    ChrTalk(    #92
        0x104,
        "#033F#5POh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B43")

    label("loc_3B1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B43")

    ChrTalk(    #93
        0x108,
        "#073F#5PAidios...\x02",
    )

    CloseMessageWindow()

    label("loc_3B43")

    OP_43(0xA, 0x0, 0x0, 0xC)

    def lambda_3B50():
        OP_6D(1620, 4000, -2120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B50)

    def lambda_3B68():
        OP_67(0, 1110, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3B68)

    def lambda_3B80():
        OP_6C(359000, 3000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3B80)

    def lambda_3B90():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3B90)

    def lambda_3BA0():
        OP_6E(603, 3000)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_3BA0)
    OP_6F(0x0, 815)
    OP_70(0x0, 0x361)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 870)
    OP_70(0x0, 0x398)
    WaitChrThread(0x106, 0x3)
    Sleep(500)
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #94
        (
            "\x07\x05Impressive...children of Man.\x02\x03",

            "Your kind call me Ragnard.\x01",
            "Scion of the great wyrms who\x01",
            "long have dwelt in this land.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #95
        0x101,
        "#1004F#5PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x106,
        "#052F#5PNo way... It's talking?!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #97
        (
            "\x07\x05My words carry not through tongue\x01",
            "or sound...\x02\x03",

            "...but as an impulse through the void\x01",
            "connecting my mind to thine.\x02\x03",

            "Though should it please thee, thou\x01",
            "mayst utter aloud what flickers in the\x01",
            "dawning of thy thoughts.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #98
        0x106,
        "#055F#5PUh, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x107,
        "#064F#5PWoooow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1015F#5POoookay, if we can talk, then I just\x01",
            "wanna be sure...\x02\x03",

            "You don't want to, like, eat us or\x01",
            "anything anymore, right?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #101
        (
            "\x07\x05I do not. My wrath, which thou didst\x01",
            "witness, was invoked by that infernal\x01",
            "device.\x02\x03",

            "It is well that I am now free from its\x01",
            "foul tether.\x02\x03",

            "Thou hast my gratitude.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #102
        0x101,
        "#1016F#5PAhaha... Umm, you're welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x106,
        (
            "#053F#5PHmph. We don't need your thanks.\x02\x03",

            "#057FWe didn't come here to set you free.\x02\x01",

            "We came here to stop you from destroying\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #104
        (
            "\x07\x05Thy concern is full-warranted. Through me,\x01",
            "a city and a village came to ruin.\x02\x03",

            "The will was not my own, but still,\x01",
            "the burden of these actions is mine to bear.\x02\x03",

            "I cast myself upon thy mercies, as to make\x01",
            "amends. Ask of me what boon thou willst.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #105
        0x101,
        (
            "#1025F#5PWell, um, this is really all Ouroboros' fault.\x02\x03",

            "And some people were hurt, but nobody\x01",
            "died, so...\x02\x03",

            "#1016FAs long as you express your sincerity,\x01",
            "I'm sure they'll forgive you. I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x106,
        "#552F#5P...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #107
        (
            "\x07\x05Sincerity...\x02\x03",

            "I am uncertain whether this shall\x01",
            "make sufficient amends, given the\x01",
            "sorrow I have wrought...\x02\x03",

            "Children of Man, wouldst thou approach me?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #108
        0x101,
        "#1004F#5POookay? Umm, sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x106,
        "#555F#5PUgh, what now?\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x106, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_4303():
        OP_6D(2860, 3050, 3590, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4303)

    def lambda_431B():
        OP_67(0, 3540, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_431B)

    def lambda_4333():
        OP_6C(347000, 2000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_4333)

    def lambda_4343():
        OP_6E(596, 2000)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_4343)

    def lambda_4353():
        OP_6B(2970, 2000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_4353)

    def lambda_4363():
        OP_8E(0xFE, 0x35C, 0x0, 0xFFFFF574, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4363)
    Sleep(100)
    ClearChrFlags(0x106, 0x1000)
    ClearChrFlags(0x106, 0x20)

    def lambda_438D():
        OP_8E(0xFE, 0x8C0, 0x0, 0xFFFFF452, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_438D)
    Sleep(100)

    def lambda_43AD():
        OP_8E(0xFE, 0x762, 0x0, 0xFFFFEF98, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_43AD)
    Sleep(100)

    def lambda_43CD():
        OP_8E(0xFE, 0x1FE, 0x0, 0xFFFFF0BA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_43CD)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(300)
    LoadEffect(0x0, "map\\\\mp075_00.eff")
    Sleep(100)
    SetChrPos(0xC, 1100, 9000, -2550, 0)
    SetChrPos(0xD, 2420, 9000, -2650, 0)
    PlayEffect(0x0, 0x1, 0xC, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xD, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x89, 0x0, 0x64)
    Sleep(2000)

    def lambda_44A6():
        OP_91(0xFE, 0x0, 0xFFFFDFF8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_44A6)

    def lambda_44C1():
        OP_91(0xFE, 0x0, 0xFFFFE0C0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_44C1)
    Sleep(1000)
    Fade(500)
    OP_6D(2180, 0, -4750, 0)
    OP_67(0, 7100, -10000, 0)
    OP_6B(1240, 0)
    OP_6C(166000, 0)
    OP_6E(611, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 33)
    SetChrSubChip(0x101, 15)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 7)
    OP_0D()
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xD, 0x1)
    SetChrPos(0xE, 1150, 0, -2550, 0)
    SetChrPos(0xF, 2500, 130, -2650, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_23(0x89)

    ChrTalk(    #110
        0x106,
        "#052F#5PHoly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x107,
        "#560F#6PWow!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1004F#5PThis is a...septium crystal! It's HUGE!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4646")

    ChrTalk(    #113
        0x103,
        (
            "#023F#4PThis golden shine...\x02\x03",

            "This is a crystal of goldia with\x01",
            "the power of space!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B0")

    label("loc_4646")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46CC")

    ChrTalk(    #114
        0x105,
        (
            "#044F#4PThis warm, golden glow...\x02\x03",

            "This can only be goldia, a septium\x01",
            "crystal which harness the power of\x01",
            "space.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B0")

    label("loc_46CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_474E")

    ChrTalk(    #115
        0x104,
        (
            "#033F#4PSuch golden radiance...\x02\x03",

            "This is pure goldia, a septium crystal\x01",
            "which harnesses the power of space.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B0")

    label("loc_474E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47B0")

    ChrTalk(    #116
        0x108,
        (
            "#073F#4PThis golden light...\x02\x03",

            "A goldia crystal, containing the power\x01",
            "of space!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47B0")

    SetMessageWindowPos(50, 75, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #117
        (
            "\x07\x05Scars such as I have left in this land\x01",
            "must be atoned for in kind.\x02\x03",

            "Wouldst thou convey my regrets and\x01",
            "recompense to those whose lives I have\x01",
            "cast into disarray?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(500)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #118
        0x101,
        (
            "#1008F#5PUhhh...\x02\x03",

            "#1006FSure, I guess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x106,
        "#053F#5PNot good enough.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #120
        0x101,
        "#1019F#2PYou can't be serious...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x107,
        "#063F#4PC-C'mon, Agate...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 75, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #122
        (
            "\x07\x05Such chastisement is perhaps warranted.\x01",
            "True absolution dwells not in the realm that\x01",
            "coin, gem, or gift can secure.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #123
        0x106,
        (
            "#053F#5PNo, that's not what I meant.\x02\x03",

            "#050FGiven the size...this one's worth an\x01",
            "easy ten million mira.\x02\x03",

            "Give us one more crystal about...\x01",
            "a ten-thousandth that size or so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        "#1004F#2PAre you kidding me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x106,
        (
            "#051F#5PWith the exception of policing criminal\x01",
            "activity, hirin' bracers costs money.\x02\x03",

            "Transportation of goods inside a province\x01",
            "usually comes out to about a thousand\x01",
            "mira.\x02\x03",

            "Since this wasn't ever a criminal case,\x01",
            "so long as you can pay that, we'll take\x01",
            "the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x107,
        "#560F#4PI get it...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1007F#2P...'Wasn't ever a'...\x01",
            "You know, I never thought you could\x01",
            "manage to be THAT roundabout.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 75, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #128
        (
            "\x07\x05Be it as thou wilt.\x02\x03",

            "I shall purchase of thee thy services.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(2860, 3050, 3590, 0)
    OP_67(0, 3540, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(347000, 0)
    OP_6E(596, 0)
    OP_0D()
    SetChrPos(0xC, 2420, 9000, -2650, 0)
    PlayEffect(0x0, 0x0, 0xC, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x89, 0x0, 0x64)
    Sleep(200)

    def lambda_4D77():
        OP_91(0xFE, 0x0, 0xFFFFE0C0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_4D77)
    Sleep(500)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 3)
    WaitChrThread(0xC, 0x3)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 33)
    SetChrSubChip(0xF, 17)
    SetChrPos(0xF, 2500, 200, -2650, 0)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_23(0x89)
    Sleep(300)
    Fade(500)
    ClearChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    SetChrFlags(0xF, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #129
        0x106,
        (
            "#051F#5PAll right. Contract accepted, Mr. Ragnard.\x02\x03",

            "We'll deliver these to the mayors of Bose\x01",
            "and Ravennue.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #130
        (
            "\x07\x05The matter rests in thy hands, then.\x02\x03",

            "...Haha... Truly, t'was a fine attack.\x02\x03",

            "But a lack of focus afflicted thee in\x01",
            "thy battle 'gainst the swordsman.\x02\x03",

            "Perhaps thou hast sloughed off aimless\x01",
            "fury to gird thyself in stronger resolve.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4FA0():
        OP_8C(0xFE, 25, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FA0)

    ChrTalk(    #131
        0x106,
        "#055F#5PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x107,
        "#064F#5PYou remember what happened at the mine?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(2710, 5820, 8720, 0)
    OP_67(0, 880, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(355000, 0)
    OP_6E(596, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #133
        (
            "\x07\x05Though this body acted of its own accord,\x01",
            "still did my consciousness remain clear.\x02\x03",

            "Small daughter of Man, thy bravery and\x01",
            "courage were worthy of the songs of\x01",
            "minstrels and the praise of poets.\x02\x03",

            "In thou I see the strength and virtue of\x01",
            "humanity held fast, despite the passing\x01",
            "of the ages.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #134
        0x107,
        "#562F#5PAww...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1016F#5PHahaha! You're more of a teaser\x01",
            "than I would've guessed, Ragnard.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #136
        (
            "\x07\x05Hrrrm, and as for thee...\x02\x03",

            "...Ah. Yes, it is well I know thy scent.\x02\x03",

            "Thou art the offspring of the Divine Blade?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #137
        0x101,
        "#1004F#3S#5PHuh?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52F5")

    ChrTalk(    #138
        0x103,
        "#023F#5PH-How in the world do you know Cassius?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5392")

    label("loc_52F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_534C")

    ChrTalk(    #139
        0x108,
        (
            "#073F#5PNow this is a surprise...\x01",
            "You know Cassius, Ancient One?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5392")

    label("loc_534C")


    ChrTalk(    #140
        0x106,
        (
            "#055F#5PWhoa, whoa, whoa.\x01",
            "How the hell do you know the old man?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5392")

    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #141
        (
            "\x07\x05Twenty years past, ere I took to my slumber,\x01",
            "a son of man stood before me.\x02\x03",

            "Challenge me he did, in his folly, claiming\x01",
            "he strove to master the way of the blade.\x02\x03",

            "Doth he remain hale?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #142
        0x101,
        (
            "#1015F#5PUhh, y-yeah, he's doing fine.\x02\x03",

            "#1019FHe never casually mentioned knowing\x01",
            "a dragon, though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5525")

    ChrTalk(    #143
        0x105,
        "#045F#5PSomehow, that doesn't surprise me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_55CA")

    label("loc_5525")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_558E")

    ChrTalk(    #144
        0x104,
        (
            "#031F#5PTo no one's surprise, Cassius Bright\x01",
            "is ever full of surprises of his own!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CA")

    label("loc_558E")


    ChrTalk(    #145
        0x106,
        (
            "#551F#5PGood friggin'...\x01",
            "The old man's a damn lunatic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55CA")


    ChrTalk(    #146
        0x101,
        (
            "#1004F#5POh, that reminds me.\x02\x03",

            "#1002FUm, Ragnard, sir, may I ask a question?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #147
        "\x07\x05Speak, child.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #148
        0x101,
        (
            "#1002F#5PThe Gospel was attached to you by that\x01",
            "Loewe guy, wasn't it?\x02\x03",

            "He said something about an experiment...\x01",
            "Do you know what they were trying to do?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #149
        (
            "\x07\x05#5PHrrmmm... First I must dispel the\x01",
            "confusion that clouds thy understanding.\x02\x03",

            "'Twas not the silver swordsman who placed\x01",
            "the black device upon my brow.\x02\x03",

            "Rather, 'twas a man in white possessed\x01",
            "of an unsettling power, 'The Professor' his\x01",
            "appellation.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #150
        0x101,
        "#1005F#5PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x106,
        "#052F#5PYou're kiddin'!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #152
        (
            "\x07\x05At the professor's side didst the swordsman\x01",
            "arrive...\x02\x03",

            "And in the throes of my ire, the swordsman\x01",
            "plied the extent of his art to limit the wrack\x01",
            "and ruin I wrought.\x02\x03",

            "Had he not lifted his hand, surely both the\x01",
            "city and village would have been seared to\x01",
            "ash, not a stone left upon another.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #153
        0x101,
        "#1026F#5PNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x106,
        "#552F#5PWhat the hell's his deal?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #155
        (
            "\x07\x05He had but a single aim.\x02\x03",

            "To test his machine and see whether it\x01",
            "could subvert a will such as mine, and\x01",
            "in doing so, proclaim it worthy...\x02\x03",

            "...as a Gospel of the Aureole.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #156
        0x106,
        "#054F#5PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x107,
        "#065F#5PTh-The Aureole?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        (
            "#1020F#5PWhoa, wait a minute!\x02\x03",

            "Do you know what the Shining Ring is?!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #159
        (
            "\x07\x05Mmm...\x02\x03",

            "Nowhere is it to be found, and yet it is\x01",
            "everywhere.\x02\x03",

            "Possessed of infinite power and the\x01",
            "sum of all wisdom, yet the harbinger\x01",
            "of bottomless despair...\x02\x03",

            "And when thou standeth in its presence...\x01",
            "Man must offer up an answer.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #160
        0x101,
        "#1004F#5PUh.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CA6")

    ChrTalk(    #161
        0x103,
        "#022F#5PWhat does that mean, Ragnard?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D74")

    label("loc_5CA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CDF")

    ChrTalk(    #162
        0x105,
        "#043F#5PWhat do you mean, exactly?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D74")

    label("loc_5CDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D2C")

    ChrTalk(    #163
        0x104,
        "#032F#5PI fear this is too great a riddle for even me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D74")

    label("loc_5D2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D74")

    ChrTalk(    #164
        0x108,
        (
            "#072F#5PI'm afraid we don't understand,\x01",
            "Ancient One.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D74")

    SetMessageWindowPos(320, 200, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #165
        (
            "\x07\x05I regret that I may impart nothing\x01",
            "further regarding the matter unto thee.\x02\x03",

            "The ancient oaths prevent me from\x01",
            "interfering beyond this extent.\x02\x03",

            "No aid can I render unto thee...\x01",
            "Nor can I guard thee from the fangs\x01",
            "of this 'society.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(990, 9040, 6400, 0)
    OP_67(0, 9540, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(302000, 0)
    OP_6E(537, 0)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_A1(0xA, 0x1)
    OP_75(0x1, 0xD, 0x7)
    OP_75(0x1, 0xC, 0x7)
    SetChrFlags(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x249F0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x1, 225)
    OP_70(0x1, 0x113)
    OP_B0(0x1, 0xA)
    OP_6F(0x1, 185)
    OP_70(0x1, 0xE1)
    Sleep(1000)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x1)
    OP_6F(0x1, 225)
    OP_70(0x1, 0xF8)
    OP_B0(0x1, 0xA)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 235)
    OP_70(0x1, 0xF8)
    Fade(500)
    OP_6D(4560, 4330, 2550, 0)
    OP_67(0, 1770, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(359000, 0)
    OP_6E(644, 0)
    OP_43(0x101, 0x0, 0x0, 0xC)
    OP_43(0xA, 0x3, 0x0, 0x9)
    OP_0D()

    ChrTalk(    #166
        0x101,
        "#1020F#5PWaaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x106,
        "#052F#5PH-Hey!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(320, 175, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #168
        (
            "\x07\x05Farewell, children of Man.\x02\x03",

            "In time, you shall have an answer to offer up,\x01",
            "and on that day, our paths again shall cross.\x02\x03",

            "I pray for the hastening of that day, that hour.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(7520, 0, 15130, 0)
    OP_67(0, 14200, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(340000, 0)
    OP_6E(473, 0)
    OP_44(0xA, 0x3)
    OP_0D()
    OP_43(0xA, 0x3, 0x0, 0xA)
    Fade(500)
    OP_72(0x1, 0x20)
    OP_73(0x1)
    OP_D8(0x1, 0x1F4)
    OP_6F(0x1, 545)
    OP_70(0x1, 0x234)

    def lambda_616C():
        OP_6D(7000, 3000, 21300, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_616C)

    def lambda_6184():
        OP_67(0, 18800, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6184)

    def lambda_619C():
        OP_6B(2810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_619C)

    def lambda_61AC():
        OP_6C(2000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_61AC)

    def lambda_61BC():
        OP_6E(595, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_61BC)
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 565)
    OP_70(0x1, 0x249)
    OP_43(0x106, 0x0, 0x0, 0xE)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2119 end

    def Function_9_6205(): pass

    label("Function_9_6205")

    Sleep(400)

    label("loc_620A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6220")
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    Jump("loc_620A")

    label("loc_6220")

    Return()

    # Function_9_6205 end

    def Function_10_6221(): pass

    label("Function_10_6221")

    OP_22(0x120, 0x0, 0x64)
    Sleep(2100)
    OP_22(0x120, 0x0, 0x64)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x64)
    Sleep(2000)
    Return()

    # Function_10_6221 end

    def Function_11_6240(): pass

    label("Function_11_6240")


    def lambda_6246():

        label("loc_6246")

        OP_8C(0xFE, 0, 400)
        OP_48()
        Jump("loc_6246")

    QueueWorkItem2(0x106, 1, lambda_6246)
    Sleep(100)

    def lambda_625C():

        label("loc_625C")

        OP_8C(0xFE, 0, 400)
        OP_48()
        Jump("loc_625C")

    QueueWorkItem2(0x101, 1, lambda_625C)
    Sleep(100)

    def lambda_6272():

        label("loc_6272")

        OP_8C(0xFE, 0, 400)
        OP_48()
        Jump("loc_6272")

    QueueWorkItem2(0x107, 1, lambda_6272)
    Sleep(100)

    def lambda_6288():

        label("loc_6288")

        OP_8C(0xFE, 0, 400)
        OP_48()
        Jump("loc_6288")

    QueueWorkItem2(0xF9, 1, lambda_6288)
    Return()

    # Function_11_6240 end

    def Function_12_6294(): pass

    label("Function_12_6294")


    def lambda_629A():

        label("loc_629A")

        OP_8C(0xFE, 45, 400)
        OP_48()
        Jump("loc_629A")

    QueueWorkItem2(0x106, 1, lambda_629A)
    Sleep(100)

    def lambda_62B0():

        label("loc_62B0")

        OP_8C(0xFE, 45, 400)
        OP_48()
        Jump("loc_62B0")

    QueueWorkItem2(0x101, 1, lambda_62B0)
    Sleep(100)

    def lambda_62C6():

        label("loc_62C6")

        OP_8C(0xFE, 45, 400)
        OP_48()
        Jump("loc_62C6")

    QueueWorkItem2(0x107, 1, lambda_62C6)
    Sleep(100)

    def lambda_62DC():

        label("loc_62DC")

        OP_8C(0xFE, 45, 400)
        OP_48()
        Jump("loc_62DC")

    QueueWorkItem2(0xF9, 1, lambda_62DC)
    Return()

    # Function_12_6294 end

    def Function_13_62E8(): pass

    label("Function_13_62E8")

    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 29)
    OP_99(0x106, 0x0, 0x7, 0x9C4)
    OP_99(0x106, 0x0, 0x7, 0x9C4)
    OP_99(0x106, 0x0, 0x7, 0x9C4)
    OP_99(0x106, 0x0, 0x7, 0x9C4)
    OP_99(0x106, 0x0, 0x7, 0x9C4)
    Return()

    # Function_13_62E8 end

    def Function_14_6320(): pass

    label("Function_14_6320")


    def lambda_6326():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6326)
    Sleep(300)

    def lambda_6346():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6346)
    Sleep(300)

    def lambda_6366():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6366)
    Sleep(300)

    def lambda_6386():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6386)
    Sleep(300)

    def lambda_63A6():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_63A6)
    Sleep(200)

    def lambda_63C6():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_63C6)
    Sleep(200)

    def lambda_63E6():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_63E6)
    Sleep(200)

    def lambda_6406():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6406)
    Sleep(200)

    def lambda_6426():
        OP_91(0xFE, 0x0, 0x13880, 0xFFFFD8F0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6426)
    Return()

    # Function_14_6320 end

    def Function_15_643C(): pass

    label("Function_15_643C")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 6)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 5)
    Return()

    # Function_15_643C end

    def Function_16_6465(): pass

    label("Function_16_6465")

    ClearChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 24)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    SetChrFlags(0x106, 0x2)
    SetChrSubChip(0x106, 3)
    SetChrChipByIndex(0x106, 28)
    Return()

    # Function_16_6465 end

    def Function_17_6498(): pass

    label("Function_17_6498")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 21)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 20)
    Return()

    # Function_17_6498 end

    def Function_18_64C1(): pass

    label("Function_18_64C1")

    SetChrSubChip(0xF9, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_64DF"),
        (3, "loc_64E7"),
        (4, "loc_64EF"),
        (7, "loc_64F7"),
        (SWITCH_DEFAULT, "loc_64FF"),
    )


    label("loc_64DF")

    SetChrChipByIndex(0xF9, 9)
    Jump("loc_64FF")

    label("loc_64E7")

    SetChrChipByIndex(0xF9, 12)
    Jump("loc_64FF")

    label("loc_64EF")

    SetChrChipByIndex(0xF9, 15)
    Jump("loc_64FF")

    label("loc_64F7")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_64FF")

    label("loc_64FF")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_652C"),
        (3, "loc_6534"),
        (4, "loc_653C"),
        (7, "loc_6544"),
        (SWITCH_DEFAULT, "loc_654C"),
    )


    label("loc_652C")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_654C")

    label("loc_6534")

    SetChrChipByIndex(0xF9, 11)
    Jump("loc_654C")

    label("loc_653C")

    SetChrChipByIndex(0xF9, 14)
    Jump("loc_654C")

    label("loc_6544")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_654C")

    label("loc_654C")

    Return()

    # Function_18_64C1 end

    def Function_19_654D(): pass

    label("Function_19_654D")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x1734, 0x0, 0x2436, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_6580():
        OP_96(0xFE, 0x1EBE, 0x9C4, 0x36B0, 0xBB8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_6580)
    Sleep(100)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 7)

    def lambda_65AD():
        OP_99(0xFE, 0x0, 0x9, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_65AD)
    Sleep(100)
    OP_22(0x1F4, 0x0, 0x64)
    Sleep(300)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 7870, 2800, 15500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x0)
    WaitChrThread(0xFE, 0x2)

    def lambda_661C():
        OP_96(0xFE, 0x154A, 0x0, 0x334A, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_661C)

    def lambda_663A():
        OP_99(0xFE, 0xA, 0xC, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_663A)
    WaitChrThread(0xFE, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    SetChrSubChip(0xFE, 0)
    Sleep(100)
    OP_96(0xFE, 0x47E, 0x0, 0x286E, 0x1F4, 0xFA0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_19_654D end

    def Function_20_667A(): pass

    label("Function_20_667A")

    Sleep(100)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 12)
    OP_8E(0xFE, 0x10F4, 0x0, 0xFFFFFDEE, 0x2710, 0x0)
    OP_8E(0xF9, 0x2F26, 0x0, 0x1BC6, 0x2710, 0x0)
    OP_22(0xD8, 0x0, 0x64)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 13)

    def lambda_66D2():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_66D2)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0x104, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 12930, 3530, 13500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x2)
    Sleep(100)

    def lambda_677D():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_677D)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x3, 0xFF, 0x104, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 12930, 3530, 13500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x2)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 11)
    Return()

    # Function_20_667A end

    def Function_21_6828(): pass

    label("Function_21_6828")

    Sleep(100)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x10F4, 0x0, 0xFFFFFDEE, 0x2710, 0x0)
    OP_8E(0xFE, 0x2C6A, 0x0, 0x20F8, 0x2710, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_687B():
        OP_96(0xFE, 0x32F0, 0x0, 0x32C8, 0xDAC, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_687B)
    Sleep(300)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_68A8():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_68A8)
    Sleep(100)
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(100)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 12930, 3530, 13500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x0)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0x2D5A, 0x0, 0x1856, 0xC8, 0x1388)
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_21_6828 end

    def Function_22_6956(): pass

    label("Function_22_6956")

    Sleep(100)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 15)
    OP_8E(0xFE, 0x10F4, 0x0, 0xFFFFFDEE, 0x2710, 0x0)
    OP_8E(0xFE, 0x33FE, 0x0, 0x366A, 0x2710, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 16)

    def lambda_69A9():
        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_69A9)
    OP_22(0x1F8, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 13310, 800, 15900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x2)

    def lambda_6A09():
        OP_99(0xFE, 0x1, 0x7, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6A09)
    OP_22(0x1F8, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 13310, 800, 15900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x2)
    Sleep(100)
    SetChrFlags(0xFE, 0x4)

    def lambda_6A73():
        OP_99(0xFE, 0x1, 0x7, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6A73)

    def lambda_6A83():
        OP_8E(0xFE, 0x3430, 0x1F4, 0x3908, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_6A83)
    OP_22(0x1F8, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 13310, 800, 16500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x0)
    WaitChrThread(0xFE, 0x2)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0x2D5A, 0x0, 0x1856, 0xC8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_22_6956 end

    def Function_23_6B0F(): pass

    label("Function_23_6B0F")

    Sleep(100)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 18)
    OP_8E(0xFE, 0x10F4, 0x0, 0xFFFFFDEE, 0x2710, 0x0)
    OP_8E(0xFE, 0x3138, 0x0, 0x23BE, 0x2710, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 30)

    def lambda_6B62():
        OP_99(0xFE, 0x0, 0x9, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6B62)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_6B81():
        OP_96(0xFE, 0x3282, 0xDCA, 0x32C8, 0xFA0, 0x2710)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_6B81)
    OP_99(0xFE, 0x0, 0x3, 0xDAC)
    SetChrSubChip(0xFE, 3)
    SetChrChipByIndex(0xFE, 30)
    WaitChrThread(0xFE, 0x0)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0xFF, 0xFF, 12930, 4000, 14500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x106, 0x3, 0x0, 0x18)
    Sleep(200)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    OP_99(0xFE, 0x4, 0x7, 0x5DC)
    OP_99(0xFE, 0x4, 0x7, 0x5DC)
    OP_A2(0x0)

    def lambda_6C2F():
        OP_99(0xFE, 0x8, 0xF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6C2F)
    Sleep(600)
    PlayEffect(0x1, 0xFF, 0xFF, 12930, 4000, 14500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    OP_22(0x22A, 0x0, 0x64)
    OP_22(0x22A, 0x0, 0x64)
    OP_22(0x22A, 0x0, 0x64)
    OP_22(0x22A, 0x0, 0x64)
    OP_22(0x22A, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)

    def lambda_6CA8():
        OP_96(0xFE, 0x34C6, 0x0, 0x2EC2, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_6CA8)

    def lambda_6CC6():
        OP_99(0xFE, 0x10, 0x17, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6CC6)
    WaitChrThread(0xFE, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    Sleep(100)
    OP_96(0xFE, 0x3192, 0x0, 0x16DA, 0x1F4, 0x1388)
    Return()

    # Function_23_6B0F end

    def Function_24_6D10(): pass

    label("Function_24_6D10")

    Sleep(200)

    label("loc_6D15")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D6D")
    OP_22(0x321, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 12930, 4000, 14500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6D65")
    OP_23(0x321)
    Jump("loc_6D6D")

    label("loc_6D65")

    Sleep(100)
    Jump("loc_6D15")

    label("loc_6D6D")

    Return()

    # Function_24_6D10 end

    def Function_25_6D6E(): pass

    label("Function_25_6D6E")

    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    Sleep(1000)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    Sleep(1000)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    Sleep(1000)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    Return()

    # Function_25_6D6E end

    def Function_26_6E10(): pass

    label("Function_26_6E10")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6E8C"),
        (1, "loc_6E92"),
        (SWITCH_DEFAULT, "loc_6E98"),
    )


    label("loc_6E8C")

    OP_A2(0x1200)
    Jump("loc_6E98")

    label("loc_6E92")

    OP_A2(0x1201)
    Jump("loc_6E98")

    label("loc_6E98")

    Return()

    # Function_26_6E10 end

    def Function_27_6E99(): pass

    label("Function_27_6E99")

    ClearMapFlags(0x1)
    OP_6D(97010, 0, 95840, 0)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_27_6E99 end

    SaveToFile()

Try(main)
