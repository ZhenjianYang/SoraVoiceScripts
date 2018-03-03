from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M4303   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M4303.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'Lord of Phantasma',                    # 9
        'Rostrum',                              # 10
        'Sealing Stone',                        # 11
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02770 ._CH',             # 00
        'ED6_DT26/CH20630 ._CH',             # 01
        'ED6_DT27/CH04082 ._CH',             # 02
        'ED6_DT26/CH20631 ._CH',             # 03
        'ED6_DT26/CH20297 ._CH',             # 04
        'ED6_DT26/CH20641 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02770P._CP',             # 00
        'ED6_DT26/CH20630P._CP',             # 01
        'ED6_DT27/CH04082P._CP',             # 02
        'ED6_DT26/CH20631P._CP',             # 03
        'ED6_DT26/CH20297P._CP',             # 04
        'ED6_DT26/CH20641P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -170,
        Y                   = -1000,
        Z                   = 23130,
        Range               = 4000,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 14,
    )


    ScpFunction(
        "Function_0_15A",          # 00, 0
        "Function_1_1AE",          # 01, 1
        "Function_2_1D8",          # 02, 2
        "Function_3_1E1",          # 03, 3
        "Function_4_2B22",         # 04, 4
        "Function_5_2B5B",         # 05, 5
        "Function_6_2B99",         # 06, 6
        "Function_7_2BD7",         # 07, 7
        "Function_8_2C15",         # 08, 8
        "Function_9_49A4",         # 09, 9
        "Function_10_4C0F",        # 0A, 10
        "Function_11_4C4C",        # 0B, 11
        "Function_12_4C8E",        # 0C, 12
        "Function_13_4CD0",        # 0D, 13
        "Function_14_4D12",        # 0E, 14
        "Function_15_6214",        # 0F, 15
        "Function_16_6374",        # 10, 16
        "Function_17_6452",        # 11, 17
        "Function_18_651F",        # 12, 18
        "Function_19_6635",        # 13, 19
    )


    def Function_0_15A(): pass

    label("Function_0_15A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_172"),
        (SWITCH_DEFAULT, "loc_179"),
    )


    label("loc_172")

    Event(0, 16)
    Jump("loc_179")

    label("loc_179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_18F")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_1AD")

    label("loc_18F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_1AD")

    Return()

    # Function_0_15A end

    def Function_1_1AE(): pass

    label("Function_1_1AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C7")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C7")

    OP_1B(0x1, 0x0, 0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7")
    OP_82(0x80, 0x0)

    label("loc_1D7")

    Return()

    # Function_1_1AE end

    def Function_2_1D8(): pass

    label("Function_2_1D8")

    Call(0, 3)
    Call(0, 8)
    Return()

    # Function_2_1D8 end

    def Function_3_1E1(): pass

    label("Function_3_1E1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp254_00.eff")
    LoadEffect(0x1, "map\\mp254_01.eff")
    LoadEffect(0x2, "map\\mp253_00.eff")
    LoadEffect(0x3, "map\\mp253_01.eff")
    LoadEffect(0x4, "monster\\msc1000.eff")
    OP_E0(238, 0x46, 0x2)
    OP_E0(238, 0x47, 0x3)
    OP_E0(239, 0x48, 0x2)
    OP_E0(239, 0x49, 0x3)
    OP_E0(240, 0x4A, 0x2)
    OP_E0(240, 0x4B, 0x3)
    OP_E0(241, 0x4C, 0x2)
    OP_E0(241, 0x4D, 0x3)
    OP_6D(-550, 4850, 9540, 0)
    OP_67(0, 10710, -10000, 0)
    OP_6B(3110, 0)
    OP_6C(45000, 0)
    OP_6E(417, 0)
    SetChrPos(0x109, -1180, 0, -23280, 0)
    SetChrPos(0x10F, 550, 0, -24030, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_309")
    SetChrPos(0x10E, -1090, 0, -25610, 0)
    SetChrPos(0xF1, 560, 0, -26500, 0)
    Jump("loc_339")

    label("loc_309")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_339")
    SetChrPos(0x10E, -1090, 0, -25610, 0)
    SetChrPos(0xF0, 560, 0, -26500, 0)

    label("loc_339")

    OP_43(0x109, 0x0, 0x0, 0x4)
    OP_43(0x10F, 0x0, 0x0, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_366")
    OP_43(0x10E, 0x0, 0x0, 0x6)
    OP_43(0xF1, 0x0, 0x0, 0x7)
    Jump("loc_382")

    label("loc_366")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    OP_43(0x10E, 0x0, 0x0, 0x6)
    OP_43(0xF0, 0x0, 0x0, 0x7)

    label("loc_382")


    def lambda_388():
        OP_6D(-90, 0, -9340, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_388)

    def lambda_3A0():
        OP_67(0, 7570, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3A0)

    def lambda_3B8():
        OP_6B(3110, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3B8)

    def lambda_3C8():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_3C8)

    def lambda_3D8():
        OP_6E(417, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_3D8)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x1)
    Fade(1000)
    OP_6D(320, 0, -9000, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(45000, 0)
    OP_6E(256, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(1000)

    ChrTalk(    #0
        0x10F,
        "#1443F#5PKevin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        "#1063F#5PYeah. It's that smell again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10E,
        (
            "#178F#6PThe same one that you smelled before that \x01",
            "coffin-like devil appeared?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_515")

    ChrTalk(    #3
        0x102,
        "#1503F#6P(...Where's it coming from?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AD")

    label("loc_515")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53C")

    ChrTalk(    #4
        0x107,
        "#065F#6PUh-oh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AD")

    label("loc_53C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57D")

    ChrTalk(    #5
        0x10B,
        "#215F#6PW-Well, that doesn't sound good...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AD")

    label("loc_57D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AD")

    ChrTalk(    #6
        0x10D,
        "#277F#6P...Heh. Bring it on.\x02",
    )

    CloseMessageWindow()

    label("loc_5AD")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 600, 17880, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #7
        0x10,
        "Hoarse Voice",
        (
            "\x07\x02So you noticed the smell, did you?\x02\x03",

            "The dogs of the church have good noses...\x01",
            "if nothing else.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A3")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_70A")

    label("loc_6A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CB")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_70A")

    label("loc_6CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F3")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_70A")

    label("loc_6F3")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_70A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_737")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_79E")

    label("loc_737")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_79E")

    label("loc_75F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_787")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_79E")

    label("loc_787")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_79E")

    Sleep(1000)

    def lambda_7A9():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7A9)
    Sleep(50)

    def lambda_7BC():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7BC)
    Sleep(50)

    def lambda_7CF():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_7CF)
    Sleep(50)
    OP_8C(0xF1, 0, 600)

    ChrTalk(    #8
        0x109,
        "#1069F#6PWho's there?!\x02",
    )

    CloseMessageWindow()
    OP_1D(0xB0)

    def lambda_807():
        OP_6D(670, 600, 18340, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_807)

    def lambda_81F():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_81F)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    OP_22(0xBA, 0x1, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 0, 600, 17880, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Fade(1000)

    def lambda_87D():
        OP_6B(2950, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_87D)
    PlayEffect(0x1, 0x1, 0xFF, 0, 600, 17880, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_22(0x59, 0x0, 0x64)

    def lambda_8C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_8C7)
    OP_0D()
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0xBA)
    Sleep(1000)

    ChrTalk(    #9
        0x109,
        "#1079F#5P#4S...!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(0, 400, 23390, 0)
    OP_67(-210, 3050, -14480, 0)
    OP_6B(1890, 0)
    OP_6C(0, 0)
    OP_6E(403, 0)
    OP_0D()

    def lambda_958():
        OP_6D(0, 800, 12570, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_958)

    def lambda_970():
        OP_67(-210, 4120, -14480, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_970)

    def lambda_988():
        OP_6B(1820, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_988)

    def lambda_998():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_998)

    def lambda_9A8():
        OP_6E(406, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_9A8)
    SetChrPos(0x109, -760, 0, -2080, 0)
    SetChrPos(0x10F, 550, 0, -3930, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A07")
    SetChrPos(0x10E, 1050, 0, -4180, 0)
    SetChrPos(0xF1, -1400, 0, -4280, 0)
    Jump("loc_A37")

    label("loc_A07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A37")
    SetChrPos(0x10E, -1400, 0, -4280, 0)
    SetChrPos(0xF0, 1050, 0, -4180, 0)

    label("loc_A37")

    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 6)
    SetChrSubChip(0x109, 0)

    def lambda_A4C():
        OP_8E(0xFE, 0xFFFFFD08, 0x0, 0x1BA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A4C)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 8)
    SetChrSubChip(0x10F, 0)

    def lambda_A7B():
        OP_8E(0xFE, 0x226, 0x0, 0x1B12, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_A7B)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFF")
    Sleep(150)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 10)
    SetChrSubChip(0x10E, 0)

    def lambda_AB8():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x14A0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_AB8)
    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 12)
    SetChrSubChip(0xF1, 0)

    def lambda_AE7():
        OP_8E(0xFE, 0x41A, 0x0, 0x143C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_AE7)
    Jump("loc_B6B")

    label("loc_AFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6B")
    Sleep(150)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 12)
    SetChrSubChip(0x10E, 0)

    def lambda_B27():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x14A0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_B27)
    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 10)
    SetChrSubChip(0xF0, 0)

    def lambda_B56():
        OP_8E(0xFE, 0x41A, 0x0, 0x143C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_B56)

    label("loc_B6B")

    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #10
        0x10F,
        "#1441F#6PWho are you?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        (
            "#1075F#6PI was wondering when you'd finally show your face.\x02\x03",

            "#1060FYou're the 'lord' that knight spoke of, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS417._CH")
    OP_C6(0x0, 0x0, 140000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1200)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Masked Person")

    AnonymousTalk(    #12
        (
            "\x07\x02Haha. I suppose I am.\x02\x03",

            "I do, after all, rule this land of Phantasma...\x01",
            "Such a name is only fitting.\x02\x03",

            "You may call me the Lord of Phantasma if you so wish.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    Sleep(1000)

    ChrTalk(    #13
        0x10F,
        "#1802F#6PThe Lord of Phantasma...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "\x07\x02#1580FIndeed.\x02\x03",

            "That's not a name ever mentioned in your beloved \x01",
            "Testaments, is it, Ries Argent?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x10F,
        "#1441F#6PSo you know who I am, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        "#1063F#6PHmph. Someone's brushed up on their homework.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 4)
    SetChrSubChip(0x10E, 0)
    OP_51(0x10E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(500)

    ChrTalk(    #17
        0x10E,
        (
            "#176F#6PThat's enough time spent on trivial greetings.\x02\x03",

            "#178FListen to me, Lord of Phantasma, or whatever\x01",
            "your name is.\x02\x03",

            "If all we've seen here is your doing...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(2570, 0, 8230, 0)
    OP_67(0, 3720, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(140000, 0)
    OP_6E(274, 0)
    SetChrPos(0x109, -500, 0, 7650, 0)
    SetChrPos(0x10F, 950, 0, 7110, 0)
    SetChrPos(0x10E, -2000, 0, 7290, 0)
    OP_51(0x10E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC9")
    SetChrPos(0xF1, 130, 0, 5410, 0)
    Jump("loc_FE8")

    label("loc_FC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE8")
    SetChrPos(0xF0, 130, 0, 5410, 0)

    label("loc_FE8")

    OP_0D()
    Sleep(300)
    Fade(250)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103E")
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x10E, 1)
    OP_0D()
    Sleep(300)
    OP_22(0x1F8, 0x0, 0x64)
    OP_51(0x10E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10E, 0x23, (scpexpr(EXPR_PUSH_LONG, 0x8F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10E, 10)
    SetChrSubChip(0x10E, 0)
    Jump("loc_1086")

    label("loc_103E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1086")
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x10E, 1)
    OP_0D()
    Sleep(300)
    OP_22(0x1F8, 0x0, 0x64)
    OP_51(0x10E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10E, 0x23, (scpexpr(EXPR_PUSH_LONG, 0x8F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10E, 12)
    SetChrSubChip(0x10E, 0)

    label("loc_1086")

    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x10E,
        (
            "#177F#5P#3S...then return Grancel to the way it used\x01",
            "to be at once!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #19
        0x10E,
        (
            "#177F#5P#3SShould you refuse to comply, I shall cut\x01",
            "you down here myself!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #20
        0x10,
        (
            "\x07\x02#1580F#5PMy, my. Your request is so meaningless, I scarcely\x01",
            "know how to respond.\x02\x03",

            "There's no harm in devotion, but done in excess,\x01",
            "it can only serve to cloud your eyes to the truth.\x02\x03",

            "Well? Do you understand now, Julia Schwarz?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10E,
        "#173F#5PWh-What?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1752")

    ChrTalk(    #22
        0x102,
        (
            "#1505F#5PI see my suspicions were right after all.\x02\x03",

            "#1502FThe Grancel we've been fighting our way through \x01",
            "isn't even the real thing, is it? It's just an imitation\x01",
            "of it.\x02\x03",

            "A replica of the city created here in Phantasma.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0xFFFFFF38, 1800, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x10E)

    ChrTalk(    #23
        0x10E,
        "#177F#5PThat can't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10F,
        "#1802F#5PCould that really be true...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        (
            "#1063F#6PIf we assume it is, everything falls into place.\x01",
            "Everything we thought was strange suddenly\x01",
            "makes complete sense.\x02\x03",

            "#1065FHow that giant black gate appeared at the\x01",
            "city's entrance, how it ended up completely\x01",
            "devoid of people...\x02\x03",

            "Even how the room with the elevator went\x01",
            "back to the way it used to be and the sealed\x01",
            "area's structure completely changed.\x02\x03",

            "#1060FAm I on the right track, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#1500F#5PPrecisely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "\x07\x02#1580F#5POh, dear... You're a little too capable for your\x01",
            "own good.\x02\x03",

            "If only you could be more darling and naive.\x01",
            "It would make things much more fun for me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#1505F#5PDo I look like I care about whether you're\x01",
            "having fun or not?\x02\x03",

            "#1502FAll I care about is Estelle's safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "\x07\x02#1580F#5PAhh. But of course.\x02\x03",

            "Still, much like Julia Schwarz's devotion to those\x01",
            "she serves, love, too, can serve to keep the truth\x01",
            "forever out of reach. \x02\x03",

            "Is that not so, Joshua Bright?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        "#1503F#5P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_18AB")

    label("loc_1752")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18AB")

    ChrTalk(    #31
        0x109,
        (
            "#1075F#5PI see my suspicions were right after all.\x02\x03",

            "#1060FThe Grancel we've been fighting our way through \x01",
            "isn't even the real thing, is it? It's just an imitation\x01",
            "of it.\x02\x03",

            "A replica of the city created here in Phantasma.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0xFFFFFF38, 1800, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x10E)

    ChrTalk(    #32
        0x10E,
        "#177F#5PThat can't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10F,
        "#1802F#5PCould that really be true...?\x02",
    )

    CloseMessageWindow()

    label("loc_18AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A94")

    ChrTalk(    #34
        0x10D,
        (
            "#272F#5PThat would explain everything.\x02\x03",

            "#270FYet the thought leaves a bitter taste in my mouth.\x01",
            "Have we done nothing more than act out some\x01",
            "repulsive play devised for your own self-satisfaction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "\x07\x02#1580F#5PThat you have.\x02\x03",

            "Though I would prefer you thought of it as\x01",
            "a valuable, unique experience.\x02\x03",

            "It's not often that one has the chance to\x01",
            "play both the actors and their audience,\x01",
            "is it, Mueller Vander?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10D,
        "#277F#5PHmph. It's not an experience I ever wanted.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E1C")

    label("loc_1A94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C32")

    ChrTalk(    #37
        0x10B,
        (
            "#216F#5PW-Wait...\x02\x03",

            "Does that mean the Bobcat at the port is a\x01",
            "fake, too?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "\x07\x02#1580F#5PI'm afraid that's a question I have no\x01",
            "intention of answering at the present\x01",
            "time.\x02\x03",

            "Perhaps that is the real ship after all. \x01",
            "Or is the real one hidden elsewhere?\x02\x03",

            "Only time will tell...and only time will tell\x01",
            "where your dear brothers are, too.\x02\x03",

            "What do you think, Josette Capua?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10B,
        "#212F#5PUgh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E1C")

    label("loc_1C32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E1C")

    ChrTalk(    #40
        0x107,
        (
            "#062F#5PStill, that would explain all the weird things we've\x01",
            "been struggling to figure out...\x02\x03",

            "#561F...even if it wouldn't explain just what Phantasma\x01",
            "really is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "\x07\x02#1580F#5PHaha. I would be rather troubled if it did.\x01",
            "Where's the fun in handing out the answers\x01",
            "all at once?\x02\x03",

            "Still, you are quite right, and your understanding\x01",
            "is deepening at the pace I hoped it would.\x02\x03",

            "I'm rather pleased with you, Tita Russell.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x107,
        (
            "#065F#5PH-Huh...?!\x02\x03",

            "I'm glad, I...umm...guess?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1C")

    Sleep(300)
    Fade(500)
    OP_6D(1240, 400, 12120, 0)
    OP_67(0, 3970, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(45000, 0)
    OP_6E(303, 0)
    OP_51(0x10E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10E, 0x23, (scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(500)

    ChrTalk(    #43
        0x10E,
        (
            "#176F#6PSo all this time, Her Majesty and Princess Klaudia\x01",
            "were safe...\x02\x03",

            "#171FOh, Aidios... Thank you for your unwavering mercy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        (
            "\x07\x02#1580F#5POh? Your relief strikes me as coming more than a\x01",
            "little prematurely...\x02\x03",

            "Whoever said that those you care about are safe?\x01",
            "It wasn't me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10E,
        "#173F#6PPardon...?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    ClearChrFlags(0x12, 0x80)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x12, -600, 1600, 17100, 0)
    PlayEffect(0x2, 0x7, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x80, 0x0, 0x64)
    OP_0D()
    Sleep(300)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x10E,
        (
            "#177F#6PNo!\x02\x03",

            "D-Does that contain...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        (
            "\x07\x02#1580F#5PHaha... Think of this as the final reward placed\x01",
            "for you to earn on this second plane.\x02\x03",

            "Of course, rewards aren't given for free. If you\x01",
            "wish to earn it, you will have to overcome a trial\x01",
            "first.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    PlayEffect(0x4, 0x3, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x10, 8)
    Sleep(200)
    LoadEffect(0x0, "map\\mp251_00.eff")
    LoadEffect(0x1, "map\\mp251_01.eff")
    LoadEffect(0x5, "monster\\ms32000.eff")
    LoadEffect(0x6, "monster\\ms32000b.eff")
    OP_20(0x5DC)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(4680, 0, 8610, 0)
    OP_67(-210, 6250, -14480, 0)
    OP_6B(1930, 0)
    OP_6C(126000, 0)
    OP_6E(513, 0)
    SetChrPos(0x12, -600, 1600, 17500, 0)
    Sleep(300)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 10080, 200, 930, 0, 0, 0, 1600, 1600, 1600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    OP_21()
    OP_1D(0x9A)
    OP_22(0x85, 0x1, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, 10080, 200, 930, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    def lambda_2302():

        label("loc_2302")

        OP_7C(0x50, 0x50, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_2302")

    QueueWorkItem2(0x10F, 3, lambda_2302)

    def lambda_231D():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_231D)
    Sleep(100)

    def lambda_2330():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2330)
    Sleep(100)

    def lambda_2343():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2343)
    Sleep(100)
    OP_8C(0xF0, 135, 400)

    def lambda_235D():
        OP_6D(10520, 0, 730, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_235D)

    def lambda_2375():
        OP_67(-210, 7810, -14480, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2375)

    def lambda_238D():
        OP_6B(1710, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_238D)

    def lambda_239D():
        OP_6C(131000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_239D)

    def lambda_23AD():
        OP_6E(460, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_23AD)
    WaitChrThread(0x109, 0x0)
    SetChrPos(0x11, 10080, -8000, 930, 310)
    OP_A1(0x11, 0x6)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_B0(0x6, 0x1E)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x28)

    def lambda_23F0():
        OP_8F(0xFE, 0x2760, 0x3E8, 0x3A2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_23F0)
    Sleep(1000)

    def lambda_2410():
        OP_6D(16540, 0, 1480, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2410)

    def lambda_2428():
        OP_67(-210, 8380, -14480, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2428)

    def lambda_2440():
        OP_6B(2040, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2440)

    def lambda_2450():
        OP_6C(83000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2450)

    def lambda_2460():
        OP_6E(428, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2460)
    WaitChrThread(0x11, 0x0)
    OP_44(0x10F, 0x3)
    OP_23(0x85)
    PlayEffect(0x5, 0x2, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x109, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x3, 0x2)
    Sleep(1000)
    OP_22(0x99, 0x0, 0x64)

    def lambda_24C9():
        OP_6B(1500, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_24C9)
    FadeToDark(300, 16777215, -1)
    OP_0D()
    OP_44(0x109, 0x2)
    OP_6D(10430, 1200, 4300, 0)
    OP_67(-210, 2770, -14480, 0)
    OP_6B(4470, 0)
    OP_6C(122000, 0)
    OP_6E(206, 0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, -700, 0, 9440, 135)
    SetChrPos(0x10F, 1900, 0, 9040, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_257E")
    SetChrPos(0x10E, -990, 0, 7530, 135)
    SetChrPos(0xF1, 1210, 0, 7350, 135)
    Jump("loc_25AE")

    label("loc_257E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25AE")
    SetChrPos(0x10E, -990, 0, 7530, 135)
    SetChrPos(0xF0, 1210, 0, 7350, 135)

    label("loc_25AE")

    SetChrPos(0x11, 9650, 0, 2770, 305)
    FadeToBright(1000, 16777215)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2629")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2690")

    label("loc_2629")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2651")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2690")

    label("loc_2651")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2679")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2690")

    label("loc_2679")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2690")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26BD")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2724")

    label("loc_26BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E5")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2724")

    label("loc_26E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_270D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2724")

    label("loc_270D")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2724")

    Sleep(1000)

    ChrTalk(    #48
        0x10E,
        "#173F#6P#4S...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2767")

    ChrTalk(    #49
        0x102,
        "#1506F#6PA devil?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_280A")

    label("loc_2767")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_278D")

    ChrTalk(    #50
        0x107,
        "#065F#6POh, no!\x02",
    )

    CloseMessageWindow()
    Jump("loc_280A")

    label("loc_278D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C3")

    ChrTalk(    #51
        0x10B,
        "#216F#6PWh-What IS that thing?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_280A")

    label("loc_27C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_280A")

    ChrTalk(    #52
        0x10D,
        "#271F#6PThis is what a genuine devil looks like...?\x02",
    )

    CloseMessageWindow()

    label("loc_280A")


    ChrTalk(    #53
        0x10F,
        (
            "#1446F#6PThis is another of the seventy-seven devils\x01",
            "mentioned in the Testaments...\x02\x03",

            "One of the two gatekeepers of Gehenna\x01",
            "and leader of a vast army of minions...\x02\x03",

            "#1441F...Rostrum the Savage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x109,
        (
            "#1069F#6PGah... Are you INSANE?!\x02\x03",

            "How do you think you can handle something\x01",
            "that powerful after bringing it to life?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "\x07\x02#1580F#5PI need not worry, for I have you to defeat it\x01",
            "for me.\x02\x03",

            "Enjoy!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_29A6():
        OP_6D(15210, 500, -670, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_29A6)

    def lambda_29BE():
        OP_67(-210, 2910, -14480, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_29BE)

    def lambda_29D6():
        OP_6B(2900, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_29D6)

    def lambda_29E6():
        OP_6C(122000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_29E6)

    def lambda_29F6():
        OP_6E(330, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_29F6)
    OP_22(0x1E6, 0x0, 0x64)
    OP_72(0x2006, 0x0)
    ExitThread()
    OP_B0(0x6, 0x1E)
    OP_6F(0x6, 141)
    OP_70(0x6, 0x96)
    OP_73(0x6)
    OP_71(0x2006, 0x0)
    ExitThread()
    OP_6F(0x6, 151)
    OP_70(0x6, 0xA0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    WaitChrThread(0x109, 0x2)
    OP_72(0x2006, 0x0)
    ExitThread()
    OP_D8(0x6, 0x1F4)
    SetMapFlags(0x100000)
    OP_22(0x85, 0x1, 0x64)

    def lambda_2A5D():

        label("loc_2A5D")

        OP_7C(0x78, 0x78, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_2A5D")

    QueueWorkItem2(0x10F, 3, lambda_2A5D)
    OP_23(0x1E6)
    OP_22(0xF3, 0x0, 0x64)
    OP_22(0x1EF, 0x0, 0x64)
    OP_22(0x148, 0x0, 0x64)
    OP_6F(0x6, 161)
    OP_70(0x6, 0xAA)
    OP_73(0x6)
    OP_71(0x2006, 0x0)
    ExitThread()
    OP_6F(0x6, 171)
    OP_70(0x6, 0xBE)

    def lambda_2AAF():

        label("loc_2AAF")

        OP_7C(0x12C, 0x12C, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_2AAF")

    QueueWorkItem2(0x10F, 3, lambda_2AAF)

    def lambda_2ACA():
        OP_6D(15210, 1200, -670, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2ACA)

    def lambda_2AE2():
        OP_6B(1800, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2AE2)

    def lambda_2AF2():
        OP_6E(560, 2500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2AF2)
    Sleep(2300)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x10F, 0x1)
    OP_44(0x10F, 0x3)
    OP_23(0x85)
    Battle(0xF9, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_1E1 end

    def Function_4_2B22(): pass

    label("Function_4_2B22")

    OP_8E(0xFE, 0xFFFFF9F2, 0x0, 0xFFFFDD1E, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    Return()

    # Function_4_2B22 end

    def Function_5_2B5B(): pass

    label("Function_5_2B5B")

    Sleep(200)
    OP_8E(0xFE, 0xAA, 0x0, 0xFFFFDCD8, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    Return()

    # Function_5_2B5B end

    def Function_6_2B99(): pass

    label("Function_6_2B99")

    Sleep(200)
    OP_8E(0xFE, 0xFFFFF813, 0x0, 0xFFFFD5B2, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    Return()

    # Function_6_2B99 end

    def Function_7_2BD7(): pass

    label("Function_7_2BD7")

    Sleep(250)
    OP_8E(0xFE, 0x190, 0x0, 0xFFFFD684, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    Return()

    # Function_7_2BD7 end

    def Function_8_2C15(): pass

    label("Function_8_2C15")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0xB0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "battle\\btgun10.eff")
    LoadEffect(0x4, "battle\\damage2.eff")
    OP_E0(238, 0x46, 0x2)
    OP_E0(238, 0x47, 0x5)
    OP_E0(239, 0x48, 0x2)
    OP_E0(239, 0x49, 0x5)
    OP_E0(240, 0x4A, 0x2)
    OP_E0(240, 0x4B, 0x5)
    OP_E0(241, 0x4C, 0x2)
    OP_E0(241, 0x4D, 0x5)
    SetChrChipByIndex(0x10F, 5)
    SetChrSubChip(0x10F, 3)
    OP_71(0x406, 0x0)
    ExitThread()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 600, 17880, 180)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x20)
    ClearChrFlags(0x12, 0x80)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x12, -400, 1600, 17100, 0)
    PlayEffect(0x1, 0x0, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -1870, 0, 5950, 90)
    SetChrPos(0x10F, 110, 0, 5890, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB4")
    SetChrPos(0x10E, -1990, 0, 4100, 90)
    SetChrPos(0xF1, 0, 0, 4090, 90)
    Jump("loc_2DE4")

    label("loc_2DB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE4")
    SetChrPos(0x10E, -1990, 0, 4100, 90)
    SetChrPos(0xF0, 0, 0, 4090, 90)

    label("loc_2DE4")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0xEE, 7)
    SetChrSubChip(0xEE, 3)
    SetChrChipByIndex(0xEF, 9)
    SetChrSubChip(0xEF, 3)
    SetChrChipByIndex(0xF0, 11)
    SetChrSubChip(0xF0, 3)
    SetChrChipByIndex(0xF1, 13)
    SetChrSubChip(0xF1, 3)
    OP_6D(7770, 3500, -150, 0)
    OP_67(0, 7270, -10000, 0)
    OP_6B(3770, 0)
    OP_6C(66000, 0)
    OP_6E(308, 0)
    Sleep(500)

    def lambda_2E7C():
        OP_6D(-3580, 3500, 3000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2E7C)

    def lambda_2E94():
        OP_67(0, 7270, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2E94)

    def lambda_2EAC():
        OP_6B(3500, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2EAC)

    def lambda_2EBC():
        OP_6C(66000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2EBC)

    def lambda_2ECC():
        OP_6E(300, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2ECC)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_6D(440, 0, 5710, 0)
    OP_67(0, 6310, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(56000, 0)
    OP_6E(262, 0)
    OP_43(0x109, 0x0, 0x0, 0xA)
    OP_43(0x10F, 0x0, 0x0, 0xB)
    OP_43(0xF0, 0x0, 0x0, 0xC)
    OP_43(0xF1, 0x0, 0x0, 0xD)
    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x109,
        "#1070F#6PGah... Th-That thing was crazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10F,
        "#1445F#5PI can't believe...we were able to defeat it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10E,
        "#172F#6PB-But now...!\x02",
    )

    CloseMessageWindow()
    OP_44(0x109, 0x0)
    OP_44(0x10F, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    Fade(250)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302C")
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    Sleep(100)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    Sleep(100)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    Sleep(100)
    SetChrChipByIndex(0xF1, 65535)
    SetChrSubChip(0xF1, 0)
    Jump("loc_3071")

    label("loc_302C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3071")
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    Sleep(100)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    Sleep(100)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    Sleep(100)
    SetChrChipByIndex(0xF0, 65535)
    SetChrSubChip(0xF0, 0)

    label("loc_3071")

    OP_0D()

    def lambda_3078():
        OP_6D(970, 300, 12540, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3078)

    def lambda_3090():
        OP_67(0, 3800, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3090)

    def lambda_30A8():
        OP_6B(3250, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_30A8)

    def lambda_30B8():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_30B8)

    def lambda_30C8():
        OP_6E(331, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_30C8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3123")

    def lambda_30E6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_30E6)
    Sleep(100)

    def lambda_30F9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_30F9)
    Sleep(100)

    def lambda_310C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_310C)
    Sleep(100)
    OP_8C(0xF1, 0, 400)
    Jump("loc_3171")

    label("loc_3123")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3171")

    def lambda_3137():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_3137)
    Sleep(100)

    def lambda_314A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_314A)
    Sleep(100)

    def lambda_315D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_315D)
    Sleep(100)
    OP_8C(0xF0, 0, 400)

    label("loc_3171")

    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #59
        0x10,
        (
            "\x07\x02#1580FHaha... That was a truly delightful spectacle.\x02\x03",

            "Well, take your reward. You've earned it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x99, 0x0, 0x64)
    SetChrPos(0x12, -1850, -10000, 4970, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_6D(1040, 0, 4350, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(3490, 0)
    OP_6C(140000, 0)
    OP_6E(246, 0)
    SetChrPos(0x109, -960, 0, 7350, 0)
    SetChrPos(0x10F, 950, 0, 7010, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_329C")
    SetChrPos(0x10E, -900, 0, 5450, 0)
    SetChrPos(0xF1, 1130, 0, 5210, 0)
    Jump("loc_32CC")

    label("loc_329C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CC")
    SetChrPos(0x10E, -900, 0, 5450, 0)
    SetChrPos(0xF0, 1130, 0, 5210, 0)

    label("loc_32CC")

    OP_0D()
    Sleep(500)
    Fade(250)
    OP_22(0x99, 0x0, 0x64)
    SetChrPos(0x12, -900, 1000, 6250, 0)
    PlayEffect(0x1, 0x0, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()

    def lambda_335E():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_335E)
    Sleep(50)

    def lambda_3371():
        OP_8C(0xFE, 225, 600)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3371)
    Sleep(80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3396")
    OP_8C(0xF1, 270, 600)
    Jump("loc_33AB")

    label("loc_3396")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33AB")
    OP_8C(0xF0, 270, 600)

    label("loc_33AB")


    ChrTalk(    #60
        0x10E,
        "#173F#11POh...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10E, 5)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x12, 0xFFFFFDA8, 0x41A, 0x1644, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    SetChrFlags(0x12, 0x80)
    OP_0D()
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #61
        "\x07\x05Received \x1F\x57\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x357, 1)
    Sleep(1000)

    ChrTalk(    #62
        0x10E,
        "#171F#11PThank goodness...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34B7")

    ChrTalk(    #63
        0x102,
        "#1500F#5PI'm glad we got it for you, Julia.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3543")

    label("loc_34B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34F4")

    ChrTalk(    #64
        0x107,
        "#560F#5PHeehee. I'm so glad we got it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3543")

    label("loc_34F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_351D")

    ChrTalk(    #65
        0x10B,
        "#210F#5PCaptain...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3543")

    label("loc_351D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3543")

    ChrTalk(    #66
        0x10D,
        "#277F#5PCaptain...\x02",
    )

    CloseMessageWindow()

    label("loc_3543")


    def lambda_3549():
        OP_6D(2009, 0, 9850, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3549)

    def lambda_3561():
        OP_67(0, 4260, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3561)

    def lambda_3579():
        OP_6B(3800, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3579)

    def lambda_3589():
        OP_6E(274, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_3589)
    Sleep(500)

    def lambda_359E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_359E)
    Sleep(100)

    def lambda_35B1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_35B1)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35D6")
    OP_8C(0xF1, 0, 400)
    Jump("loc_35EB")

    label("loc_35D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35EB")
    OP_8C(0xF0, 0, 400)

    label("loc_35EB")

    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #67
        0x109,
        (
            "#1075F#2PHeh. Surprised you make good on your promises.\x02\x03",

            "#1063FNow, you ready to cut down to the chase?\x01",
            "What do you want from us?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #68
        0x109,
        "#1069F#2P#3SWhat the hell is the point of all of this?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        (
            "\x07\x02#1580F#5PHaha. Poor Kevin Graham. Poor, pitiful Kevin.\x02\x03",

            "Please try not to let me down any more than you\x01",
            "already have.\x02\x03",

            "I am a phantasm--a shadow. Much as a shadow only\x01",
            "exists when there is something to cast it, I, too,\x01",
            "only exist because of something within your number.\x02\x03",

            "Do you grasp my meaning?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x109,
        "#1079F#2P...Wha...?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_22(0x164, 0x0, 0x64)
    OP_AD(0x240112, 0x0, 0x0, 0x5DC)
    Sleep(500)
    OP_AE(0x3E8)
    Sleep(1000)
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #71
        0x10F,
        "#1802F#5PKevin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x109,
        (
            "#1075F#2P...Hmph. How could I? You're just spouting nonsense.\x02\x03",

            "#1840FIf you think being all cryptic is gonna confuse us and\x01",
            "lead us astray, you're very much mistaken, buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        (
            "\x07\x02#1580F#5PTrue enough. Spouting cryptic nonsense is simply\x01",
            "what I do.\x02\x03",

            "That IS what you believe, is it? Then it must be true.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #74
        0x109,
        "#1076F#2P...rew you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10,
        (
            "\x07\x02#1580F#5PHaha. Perhaps I ought to go by a different\x01",
            "name after all.\x02\x03",

            "How do you think Lord of Nonsense sounds?\x01",
            "More fitting, perhaps?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x109, 0x14, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #76
        0x109,
        "#1069F#2P#4SI said, SCREW YOU!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(150)
    Fade(500)

    def lambda_3AC4():
        OP_6D(1570, 0, 5000, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3AC4)

    def lambda_3ADC():
        OP_6B(3100, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3ADC)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    OP_0D()
    SetChrChipByIndex(0x109, 2)
    OP_99(0x109, 0x0, 0x7, 0xBB8)
    OP_22(0xD8, 0x0, 0x64)
    Fade(500)
    OP_6D(970, 300, 12000, 0)
    OP_67(0, 3500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(331, 0)
    SetChrPos(0x109, -1870, 0, 5950, 0)
    SetChrPos(0x10F, 110, 0, 5890, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA0")
    SetChrPos(0x10E, -1990, 0, 4100, 0)
    SetChrPos(0xF1, 0, 0, 4090, 0)
    Jump("loc_3BD0")

    label("loc_3BA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BD0")
    SetChrPos(0x10E, -1990, 0, 4100, 0)
    SetChrPos(0xF0, 0, 0, 4090, 0)

    label("loc_3BD0")

    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3BE0():
        OP_6D(360, 600, 18500, 1000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3BE0)

    def lambda_3BF8():
        OP_67(0, 4710, -10000, 1000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3BF8)

    def lambda_3C10():
        OP_6B(3450, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 2, lambda_3C10)

    def lambda_3C20():
        OP_6E(212, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_3C20)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_3C35():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3C35)
    PlayEffect(0x3, 0x0, 0x109, 0, 1250, 750, 0, 0, 0, 500, 500, 500, 0x10, 0, 700, 0, 0)
    Sleep(200)

    def lambda_3C7F():
        OP_8C(0x10F, 0, 600)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3C7F)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_3C92():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3C92)
    PlayEffect(0x3, 0x1, 0x109, 0, 1250, 750, 0, 0, 0, 500, 500, 500, 0x10, 0, 700, 0, 0)
    Sleep(200)
    OP_43(0x10, 0x0, 0x0, 0x9)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_3CE8():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3CE8)
    PlayEffect(0x3, 0x2, 0x109, 0, 1250, 750, 0, 0, 0, 500, 500, 500, 0x10, 0, 700, 0, 0)
    Sleep(200)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_3D37():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3D37)
    PlayEffect(0x3, 0x3, 0x109, 0, 1250, 750, 0, 0, 0, 500, 500, 500, 0x10, 0, 700, 0, 0)
    Sleep(200)
    WaitChrThread(0x10, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DCD")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E34")

    label("loc_3DCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF5")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E34")

    label("loc_3DF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E1D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E34")

    label("loc_3E1D")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3E34")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E61")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3EC8")

    label("loc_3E61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E89")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3EC8")

    label("loc_3E89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EB1")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3EC8")

    label("loc_3EB1")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3EC8")

    Sleep(1000)
    Fade(1000)
    OP_6D(970, 0, 11370, 0)
    OP_67(0, 3700, -10000, 0)
    OP_6B(3220, 0)
    OP_6C(45000, 0)
    OP_6E(331, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F36")

    ChrTalk(    #77
        0x107,
        "#065FWhoa!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F57")

    label("loc_3F36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F57")

    ChrTalk(    #78
        0x10B,
        "#216FWha...?!\x02",
    )

    CloseMessageWindow()

    label("loc_3F57")

    OP_8C(0x10F, 270, 600)

    ChrTalk(    #79
        0x10F,
        (
            "#1802F#2PKevin?!\x02\x03",

            "Wh-What's wrong with you...?\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x109, 0x7, 0x0, 0x7D0)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #80
        0x109,
        (
            "#1065F#6PNothing. Don't worry.\x02\x01",

            "#1063FThat's literally just a shadow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10F,
        "#1444F#2P...It is?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)
    OP_22(0x117, 0x0, 0x64)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
    Sleep(1000)

    ChrTalk(    #82
        0x10F,
        "#1802F#2POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10E,
        (
            "#178F#4PSo that was a body double...or an empty shell\x01",
            "is more appropriate in this case.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40F1")

    ChrTalk(    #84
        0x102,
        (
            "#1502FThey must have switched while we were fighting\x01",
            "that devil.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C9")

    label("loc_40F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_414E")

    ChrTalk(    #85
        0x10D,
        (
            "#272FHmph. They must have switched while we were \x01",
            "fighting that devil.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41C9")

    label("loc_414E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_418D")

    ChrTalk(    #86
        0x107,
        "#063FW-We barely took our eyes off them!\x02",
    )

    CloseMessageWindow()
    Jump("loc_41C9")

    label("loc_418D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41C9")

    ChrTalk(    #87
        0x10B,
        "#212FW-We barely took our eyes off them!\x02",
    )

    CloseMessageWindow()

    label("loc_41C9")

    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(130, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #88
        (
            "\x07\x02#40WI commend you for noticing.\x02\x03",

            "#40WStill, your role on this plane is now over.\x02\x03",

            "#40WAdd the wings of white to your number\x01",
            "and journey on deeper into the abyss you\x01",
            "stand inside.\x02\x03",

            "#40WI shall be awaiting our next encounter...\x01",
            "Hahaha...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(800)

    def lambda_4301():
        OP_6D(500, 600, 23720, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4301)

    def lambda_4319():
        OP_67(0, 5780, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4319)

    def lambda_4331():
        OP_6B(2930, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4331)

    def lambda_4341():
        OP_6C(33000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4341)

    def lambda_4351():
        OP_6E(302, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_4351)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_43AA():
        OP_6B(2800, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_43AA)
    OP_0D()
    Sleep(1500)

    def lambda_43C0():
        OP_6D(690, 0, 6750, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_43C0)

    def lambda_43D8():
        OP_67(0, 4230, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43D8)

    def lambda_43F0():
        OP_6B(2930, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_43F0)

    def lambda_4400():
        OP_6C(45000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4400)

    def lambda_4410():
        OP_6E(302, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_4410)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4461")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_44B9")

    label("loc_4461")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4484")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_44B9")

    label("loc_4484")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44A7")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_44B9")

    label("loc_44A7")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_44B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44DC")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_4534")

    label("loc_44DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44FF")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_4534")

    label("loc_44FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4522")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_4534")

    label("loc_4522")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_4534")

    WaitChrThread(0x109, 0x0)
    OP_63(0x109)
    OP_63(0x10F)
    OP_63(0xF0)
    OP_63(0xF1)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #89
        0x109,
        (
            "#1075F#5PPlease. They take their overblown theatrics way\x01",
            "too seriously.\x02\x03",

            "Our resident evildoer's going to have to work\x01",
            "on their act if they want to sound like anything\x01",
            "more than a walking cliche.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #90
        0x10F,
        "#1802F#2PUmm...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4749")

    ChrTalk(    #91
        0x109,
        (
            "#1078F#5PAnyway, we're done here, and we've got ourselves\x01",
            "another sealing stone to open up...\x02\x03",

            "...so let's mosey on back to the base.\x02\x03",

            "I mean, I think we all know who's inside at this\x01",
            "point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x10D,
        "#277F#6PHeh. Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4895")

    label("loc_4749")


    ChrTalk(    #93
        0x109,
        (
            "#1078F#5PAnyway, we're done here, and we've got ourselves\x01",
            "another sealing stone to open up...\x02\x03",

            "...so let's mosey on back to the base.\x02\x03",

            "I think we all know who's inside at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_482A")

    ChrTalk(    #94
        0x102,
        "#1500F#6PYeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4895")

    label("loc_482A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_484F")

    ChrTalk(    #95
        0x107,
        "#560F#6PRight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4895")

    label("loc_484F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4895")

    ChrTalk(    #96
        0x10B,
        "#210F#6PI think it's obvious even to me this time.\x02",
    )

    CloseMessageWindow()

    label("loc_4895")


    ChrTalk(    #97
        0x10E,
        "#170F#6PThank you. I appreciate it.\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_48C9():
        OP_6B(3500, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_48C9)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x2)
    Sleep(2000)
    OP_A2(0x2720)
    OP_AD(0x2400EE, 0x0, 0x0, 0x64)
    OP_F7(0x2, 0x0, 0x0)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x157), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_495B")
    ShowSaveMenu()

    label("loc_495B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0x7D0)
    OP_21()
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x250B)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_2C15 end

    def Function_9_49A4(): pass

    label("Function_9_49A4")

    Sleep(200)
    SetChrFlags(0xFE, 0x800)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 0)
    OP_20(0x0)
    PlayEffect(0x4, 0xFF, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_49FD():
        OP_8F(0xFE, 0x0, 0x3E8, 0x4844, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49FD)

    def lambda_4A18():
        OP_9E(0xFE, 0x1E, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4A18)

    def lambda_4A32():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A32)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4A7C():
        OP_9E(0xFE, 0x1E, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4A7C)

    def lambda_4A96():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A96)
    Sleep(200)
    OP_22(0x22B, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4AE5():
        OP_9E(0xFE, 0x1E, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4AE5)

    def lambda_4AFF():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4AFF)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4B49():
        OP_9E(0xFE, 0x1E, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4B49)

    def lambda_4B63():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4B63)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4BAD():
        OP_9E(0xFE, 0x1E, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4BAD)

    def lambda_4BC7():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BC7)
    WaitChrThread(0xFE, 0x1)
    Sleep(500)

    def lambda_4BE1():
        OP_99(0xFE, 0x8, 0xD, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BE1)
    OP_8F(0xFE, 0x0, 0x258, 0x4844, 0x1388, 0x0)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_9_49A4 end

    def Function_10_4C0F(): pass

    label("Function_10_4C0F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C4B")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_10_4C0F")

    label("loc_4C4B")

    Return()

    # Function_10_4C0F end

    def Function_11_4C4C(): pass

    label("Function_11_4C4C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C8D")
    Sleep(300)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_11_4C4C")

    label("loc_4C8D")

    Return()

    # Function_11_4C4C end

    def Function_12_4C8E(): pass

    label("Function_12_4C8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CCF")
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_12_4C8E")

    label("loc_4CCF")

    Return()

    # Function_12_4C8E end

    def Function_13_4CD0(): pass

    label("Function_13_4CD0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D11")
    Sleep(500)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(800)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_13_4CD0")

    label("loc_4D11")

    Return()

    # Function_13_4CD0 end

    def Function_14_4D12(): pass

    label("Function_14_4D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 1)), scpexpr(EXPR_END)), "loc_4D1A")
    Return()

    label("loc_4D1A")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-30, 600, 21600, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(3970, 0)
    OP_6C(33000, 0)
    OP_6E(212, 0)
    SetChrPos(0x109, -770, 600, 19530, 0)
    SetChrPos(0x10F, 520, 600, 19440, 0)
    SetChrPos(0xF0, -1140, 600, 17900, 0)
    SetChrPos(0xF1, 50, 600, 17850, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #98
        0x109,
        (
            "#1063F#6PWell, this should take us to the third plane.\x02\x03",

            "Funny how this warp ended up being in the\x01",
            "exact spot that device to seal the Aureole was\x01",
            "in the real world.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #99
        0x10F,
        (
            "#1444F#11PDevice?\x02\x03",

            "#1443FAre you referring to the first barrier mentioned\x01",
            "in that report?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #100
        0x109,
        (
            "#1065F#6PYeah. The one designed to temporally freeze it in\x01",
            "another dimensional space.\x02\x03",

            "#1063FAlthough unfortunately for the guys who pulled it\x01",
            "off, it looks like even that wasn't enough to stop\x01",
            "the Gospels being able to influence it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x10F,
        "#1446F#11PI see...\x02",
    )

    CloseMessageWindow()

    def lambda_4FFD():
        OP_67(0, 6500, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4FFD)
    OP_6D(-30, 600, 20600, 1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5178")

    ChrTalk(    #102
        0x107,
        (
            "#561F#6PWe still don't know what happened to the Aureole,\x01",
            "either.\x02\x03",

            "Part of the reason Mom and the army were looking\x01",
            "under the lake was to see if they could find the\x01",
            "Aureole there, but they didn't have any luck.\x02\x03",

            "#063FBut there seem to be plenty who think that the\x01",
            "Liber Ark collapsing means the Aureole itself\x01",
            "is no more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5571")

    label("loc_5178")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52DB")

    ChrTalk(    #103
        0x102,
        (
            "#1503F#6PWe still don't know what happened to the Aureole,\x01",
            "either.\x02\x03",

            "There seem to be many who think that the Liber Ark\x01",
            "collapsing means that the Aureole itself is no more,\x01",
            "too... Which is possible, I suppose.\x02\x03",

            "#1502FAll we really know is that judging by how shaken\x01",
            "Weissmann was, something unexpected happened.\x01",
            "Beyond that, nothing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5571")

    label("loc_52DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53B4")

    ChrTalk(    #104
        0x10E,
        (
            "#176F#6PWe still don't know what happened to the Aureole,\x01",
            "either.\x02\x03",

            "#178FMany seem to believe that the Liber Ark's collapse\x01",
            "means that the Aureole itself is no more, but we\x01",
            "can't say so for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5571")

    label("loc_53B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5493")

    ChrTalk(    #105
        0x10D,
        (
            "#272F#6PWe still don't know what happened to the\x01",
            "Aureole, either.\x02\x03",

            "#270FMany seem to believe that the Liber Ark's\x01",
            "collapse means that the Aureole itself is no\x01",
            "more, but there's no way to say for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5571")

    label("loc_5493")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5571")

    ChrTalk(    #106
        0x105,
        (
            "#1167F#6PWe still don't know what happened to the\x01",
            "Aureole, either.\x02\x03",

            "#1169FMany seem to believe that the Liber Ark's\x01",
            "collapse means that the Aureole itself is no\x01",
            "more, but there's no way to say for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5571")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5649")

    ChrTalk(    #107
        0x10B,
        (
            "#212F#6PDon't think we're ever gonna know for sure\x01",
            "what happened unless someone catches that\x01",
            "sick freak with the glasses and grills him on it.\x02\x03",

            "#416FNot that anyone knows where he is right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59AA")

    label("loc_5649")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_572C")

    ChrTalk(    #108
        0x105,
        (
            "#1163F#6P...I fear Professor Weissmann may be the only one\x01",
            "who knows the truth about exactly what happened.\x02\x03",

            "#1167FAlthough I don't have the faintest idea where he\x01",
            "could be now or what he's doing there...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59AA")

    label("loc_572C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5814")

    ChrTalk(    #109
        0x10D,
        (
            "#270F#6PI imagine the only way to ascertain the truth of\x01",
            "what happened will be to capture Weissmann and\x01",
            "get the answer from him...\x02\x03",

            "#272FAlthough, I can't even imagine where he is or what\x01",
            "he must be doing now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59AA")

    label("loc_5814")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58FC")

    ChrTalk(    #110
        0x10E,
        (
            "#178F#6PI imagine the only way to ascertain the truth of\x01",
            "what happened will be to capture Weissmann and\x01",
            "get the answer from him...\x02\x03",

            "#176FAlthough, I can't even imagine where he is or what\x01",
            "he must be doing now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59AA")

    label("loc_58FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59AA")

    ChrTalk(    #111
        0x102,
        (
            "#1505F#6PMaybe Weissmann is the only one who knows\x01",
            "the truth about what happened.\x02\x03",

            "#1503FI've got no idea what he's been doing since he\x01",
            "escaped, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59AA")

    OP_8C(0x10F, 225, 400)
    Sleep(300)

    ChrTalk(    #112
        0x10F,
        (
            "#1444F#5P...What?\x02\x03",

            "#1802FB-But the report said quite clearly...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B68")
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #113
        0x109,
        (
            "#1065F#5PNo one in the church is sure what happened to him,\x01",
            "either. It's still being looked into.\x02\x03",

            "#1060FStill, I think it's fairly safe to say that Weissmann\x01",
            "isn't involved in what's happening right here.\x02\x03",

            "If he were, I'm sure he'd be openly reveling every\x01",
            "second of this. You all know what kinda guy he is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CAE")

    label("loc_5B68")

    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #114
        0x109,
        (
            "#1065F#5PNo one in the church is sure what happened to him,\x01",
            "either. It's still being looked into.\x02\x03",

            "#1060FStill, I think it's fairly safe to say that Weissmann\x01",
            "isn't involved in what's happening right here.\x02\x03",

            "If he were, I'm sure he'd be openly reveling every\x01",
            "second of this. You all know what kinda guy he is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CDA")

    ChrTalk(    #115
        0x102,
        "#1500F#6PThat's true.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D99")

    label("loc_5CDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D0B")

    ChrTalk(    #116
        0x107,
        "#060F#6PYeah, that's true.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D99")

    label("loc_5D0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D3C")

    ChrTalk(    #117
        0x10B,
        "#210F#6PYeah, that's true.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D99")

    label("loc_5D3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D68")

    ChrTalk(    #118
        0x105,
        "#1160F#6PThat's true.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D99")

    label("loc_5D68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D99")

    ChrTalk(    #119
        0x10E,
        "#170F#6PHmm... A valid point.\x02",
    )

    CloseMessageWindow()

    label("loc_5D99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E00")

    ChrTalk(    #120
        0x10D,
        (
            "#277F#6PHe doesn't have anything to gain by wearing a mask\x01",
            "like that, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FB5")

    label("loc_5E00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E67")

    ChrTalk(    #121
        0x10E,
        (
            "#170F#6PHe doesn't have anything to gain by wearing a mask\x01",
            "like that, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FB5")

    label("loc_5E67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ED8")

    ChrTalk(    #122
        0x105,
        (
            "#1382F#6PHe doesn't really have anything to gain by wearing\x01",
            "a mask like that, I suppose...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FB5")

    label("loc_5ED8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F48")

    ChrTalk(    #123
        0x10B,
        (
            "#210F#6PHe doesn't really have anything to gain by wearing\x01",
            "a mask like that, I suppose...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FB5")

    label("loc_5F48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FB5")

    ChrTalk(    #124
        0x107,
        (
            "#560F#6PHe doesn't really have anything to gain by wearing\x01",
            "a mask like that, I suppose...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FB5")

    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #125
        0x10F,
        "#1443F#11P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_60F2")

    ChrTalk(    #126
        0x109,
        (
            "#1075F#5PWe've got way too many unanswered questions at\x01",
            "this point. All we can do is keep looking for answers.\x02\x03",

            "#1060FThe less we know, the more we have to be on guard,\x01",
            "though. So we'd best be careful. \x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #127
        0x109,
        "#1078F#6PRight, Ries?\x02",
    )

    CloseMessageWindow()
    Jump("loc_61E9")

    label("loc_60F2")


    ChrTalk(    #128
        0x109,
        (
            "#1075F#5PWe've got way too many unanswered questions at\x01",
            "this point. All we can do is keep looking for answers.\x02\x03",

            "#1060FThe less we know, the more we have to be on guard,\x01",
            "though. So we'd best be careful. \x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #129
        0x109,
        "#1078F#6PRight, Ries?\x02",
    )

    CloseMessageWindow()

    label("loc_61E9")


    ChrTalk(    #130
        0x10F,
        "#1446F#11P...I suppose so.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2801)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_14_4D12 end

    def Function_15_6214(): pass

    label("Function_15_6214")

    EventBegin(0x0)
    Fade(500)
    OP_6D(330, 1250, 23660, 0)
    OP_67(0, 6480, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(35000, 0)
    OP_6E(324, 0)
    SetChrPos(0x109, 20, 600, 24220, 0)
    SetChrPos(0x10F, 770, 600, 23280, 0)
    SetChrPos(0xF0, -800, 600, 23250, 0)
    SetChrPos(0xF1, -40, 600, 22450, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 600, 23260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_6322():
        OP_67(0, 8000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6322)

    def lambda_633A():
        OP_6B(3500, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_633A)
    Call(0, 19)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    Sleep(1000)
    NewScene("ED6_DT21/M7100   ._SN", 102, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_15_6214 end

    def Function_16_6374(): pass

    label("Function_16_6374")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -40, 600, 22450, 180)
    SetChrPos(0x1, -800, 600, 23250, 180)
    SetChrPos(0x2, 770, 600, 23280, 180)
    SetChrPos(0x3, 20, 600, 24220, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 600, 23260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 18)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_16_6374 end

    def Function_17_6452(): pass

    label("Function_17_6452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6463")
    Call(0, 15)
    Return()

    label("loc_6463")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -40, 600, 22450, 0)
    SetChrPos(0x2, -800, 600, 23250, 0)
    SetChrPos(0x1, 770, 600, 23280, 0)
    SetChrPos(0x0, 20, 600, 24220, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 600, 23260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 19)
    NewScene("ED6_DT21/M7100   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_17_6452 end

    def Function_18_651F(): pass

    label("Function_18_651F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6548")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_653C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_653C)

    label("loc_6548")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6571")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_6565():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6565)

    label("loc_6571")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_659A")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_658E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_658E)

    label("loc_659A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65C3")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_65B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_65B7)

    label("loc_65C3")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65EF")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_65EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6606")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_6606")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_661D")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_661D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6634")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_6634")

    Return()

    # Function_18_651F end

    def Function_19_6635(): pass

    label("Function_19_6635")


    def lambda_663B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_663B)

    def lambda_664D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_664D)

    def lambda_665F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_665F)

    def lambda_6671():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_6671)
    Sleep(1000)
    Return()

    # Function_19_6635 end

    SaveToFile()

Try(main)
