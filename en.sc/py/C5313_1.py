from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5313_1 ._SN',
        MapName             = 'Other',
        Location            = 'C5313.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C5313   ._SN',
            'ED6_DT21/C5313_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_23B9",         # 03, 3
        "Function_4_2405",         # 04, 4
        "Function_5_247F",         # 05, 5
        "Function_6_257A",         # 06, 6
        "Function_7_25F3",         # 07, 7
        "Function_8_2626",         # 08, 8
        "Function_9_2695",         # 09, 9
        "Function_10_26B1",        # 0A, 10
        "Function_11_26CD",        # 0B, 11
        "Function_12_26E9",        # 0C, 12
        "Function_13_2705",        # 0D, 13
        "Function_14_2721",        # 0E, 14
        "Function_15_273D",        # 0F, 15
        "Function_16_276D",        # 10, 16
        "Function_17_279D",        # 11, 17
        "Function_18_27F5",        # 12, 18
        "Function_19_2C7B",        # 13, 19
        "Function_20_2CC9",        # 14, 20
        "Function_21_2D17",        # 15, 21
        "Function_22_2D65",        # 16, 22
        "Function_23_2D7B",        # 17, 23
        "Function_24_2DC8",        # 18, 24
        "Function_25_2E7C",        # 19, 25
        "Function_26_2F26",        # 1A, 26
        "Function_27_2F46",        # 1B, 27
        "Function_28_2FB0",        # 1C, 28
        "Function_29_3022",        # 1D, 29
        "Function_30_30B7",        # 1E, 30
        "Function_31_3149",        # 1F, 31
        "Function_32_31A2",        # 20, 32
        "Function_33_31FB",        # 21, 33
        "Function_34_3246",        # 22, 34
        "Function_35_3291",        # 23, 35
        "Function_36_32DC",        # 24, 36
        "Function_37_3327",        # 25, 37
        "Function_38_3372",        # 26, 38
        "Function_39_33B8",        # 27, 39
        "Function_40_3408",        # 28, 40
        "Function_41_3453",        # 29, 41
        "Function_42_349E",        # 2A, 42
        "Function_43_34E9",        # 2B, 43
        "Function_44_3534",        # 2C, 44
        "Function_45_357F",        # 2D, 45
        "Function_46_35C7",        # 2E, 46
        "Function_47_364B",        # 2F, 47
        "Function_48_3693",        # 30, 48
        "Function_49_3715",        # 31, 49
        "Function_50_3767",        # 32, 50
        "Function_51_37AF",        # 33, 51
        "Function_52_382C",        # 34, 52
        "Function_53_3874",        # 35, 53
        "Function_54_38F6",        # 36, 54
        "Function_55_393E",        # 37, 55
        "Function_56_39BB",        # 38, 56
        "Function_57_3A3D",        # 39, 57
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    OP_20(0x3E8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)
    OP_1D(0x23)
    Sleep(500)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 280)
    OP_70(0x2, 0x12C)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 280)
    OP_70(0x3, 0x12C)
    OP_A1(0x19, 0x2)
    OP_A1(0x1A, 0x3)
    SetChrPos(0x19, 7660, 15000, 4860, 245)
    SetChrPos(0x1A, -7660, 15000, 4860, 105)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_D3(0x21)
    Fade(500)
    OP_D2(0x70142, 0x70146, 0x21)
    OP_D2(0x2702C2, 0x2702CC, 0x22)
    OP_D2(0x2702C3, 0x2702CD, 0x23)
    OP_D2(0x2702D6, 0x2702E0, 0x24)
    OP_D2(0x2702D7, 0x2702E1, 0x25)
    OP_D2(0x70298, 0x7029F, 0x26)
    OP_D2(0x70299, 0x702A0, 0x27)
    OP_D2(0x702A6, 0x702AD, 0x28)
    OP_D2(0x702A7, 0x702AE, 0x29)
    OP_D2(0x2702D8, 0x2702E2, 0x0)
    OP_D2(0x7029A, 0x702A1, 0x1)
    OP_D2(0x702A8, 0x702AF, 0x2)
    OP_D2(0x701D2, 0x701DE, 0x3)
    OP_D2(0x701EA, 0x701F6, 0x4)
    OP_D2(0x270370, 0x27037D, 0x8)
    OP_D2(0x7021A, 0x70226, 0x9)
    OP_D2(0x70232, 0x7023E, 0xA)
    OP_D2(0x7024A, 0x70256, 0x1B)
    OP_D2(0x270178, 0x270185, 0x1C)
    OP_D2(0x2601DB, 0x2601E0, 0x1D)
    OP_D2(0x2702C4, 0x2702CE, 0x1F)
    OP_D2(0x2601E2, 0x2601E7, 0x1E)
    OP_D2(0x702B6, 0x702BD, 0x20)
    OP_C0(0x17, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x1E, 29)
    SetChrSubChip(0x1E, 32)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(12200, 0, 9000, 0)
    OP_67(0, 2610, -10000, 0)
    OP_6B(5250, 0)
    OP_6C(45000, 0)
    OP_6E(265, 0)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x2)
    SetChrPos(0x8, -200, -370, 3500, 0)
    SetChrChipByIndex(0x8, 30)
    SetChrSubChip(0x8, 2)
    OP_43(0x19, 0x0, 0x1, 0x1B)
    OP_43(0x19, 0x3, 0x1, 0x1A)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x19, 0x3)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_354")

    label("loc_316")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33D")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_354")

    label("loc_33D")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_354")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3BE")

    label("loc_380")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A7")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3BE")

    label("loc_3A7")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3BE")

    Sleep(1000)

    def lambda_3C9():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3C9)
    Sleep(50)

    def lambda_3DC():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_3DC)
    Sleep(50)

    def lambda_3EF():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_3EF)
    WaitChrThread(0xF9, 0x3)
    Fade(500)
    OP_6D(-12200, 0, 9000, 0)
    OP_67(0, 2610, -10000, 0)
    OP_6B(5250, 0)
    OP_6C(315000, 0)
    OP_6E(265, 0)
    OP_43(0x1A, 0x0, 0x1, 0x1C)
    WaitChrThread(0x1A, 0x0)

    def lambda_450():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_450)
    Sleep(50)

    def lambda_463():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_463)
    Sleep(80)

    def lambda_476():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_476)
    WaitChrThread(0xF9, 0x3)
    Sleep(1000)
    Fade(500)
    OP_6D(0, 0, 7020, 0)
    OP_67(0, 3760, -10000, 0)
    OP_6B(4540, 0)
    OP_6C(0, 0)
    OP_6E(292, 0)
    SetChrPos(0x19, 7660, 0, 4860, 225)
    SetChrPos(0x1A, -7660, 0, 4860, 135)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)

    def lambda_500():
        OP_6B(5000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_500)
    OP_8C(0x101, 45, 0)
    OP_8C(0xF8, 315, 0)
    OP_8C(0xF9, 45, 0)

    def lambda_525():
        OP_96(0xFE, 0x474, 0xFFFFFE8E, 0xFFFFFBF0, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_525)
    Sleep(50)

    def lambda_548():
        OP_96(0xFE, 0xFFFFFC68, 0xFFFFFE8E, 0xFFFFFC68, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_548)
    Sleep(50)

    def lambda_56B():
        OP_96(0xFE, 0x0, 0xFFFFFE8E, 0x5C8, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56B)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x101, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AA")
    SetChrChipByIndex(0x103, 11)

    label("loc_5AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BD")
    SetChrChipByIndex(0x104, 13)

    label("loc_5BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D0")
    SetChrChipByIndex(0x105, 15)

    label("loc_5D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E3")
    SetChrChipByIndex(0x106, 17)

    label("loc_5E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F6")
    SetChrChipByIndex(0x107, 19)

    label("loc_5F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_609")
    SetChrChipByIndex(0x108, 21)

    label("loc_609")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61C")
    SetChrChipByIndex(0x109, 23)

    label("loc_61C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62F")
    SetChrChipByIndex(0x10B, 25)

    label("loc_62F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_642")
    SetChrChipByIndex(0x10F, 36)

    label("loc_642")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_655")
    SetChrChipByIndex(0x110, 34)

    label("loc_655")

    WaitChrThread(0xF8, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A8")

    ChrTalk(    #0
        0x10F,
        (
            "#173FThat's the thing that shot down\x01",
            "the Arseille!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D5")

    label("loc_6A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6ED")

    ChrTalk(    #1
        0x107,
        (
            "#065FAaaah! It's the dragon that shot\x01",
            "us down!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D5")

    label("loc_6ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_719")

    ChrTalk(    #2
        0x10B,
        "#216FWHAT in the...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D5")

    label("loc_719")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76A")

    ChrTalk(    #3
        0x105,
        (
            "#1162FIt's the creature that brought down\x01",
            "the Arseille...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D5")

    label("loc_76A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BB")

    ChrTalk(    #4
        0x103,
        (
            "#024FThat's the thing that brought us\x01",
            "down earlier! Blast!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D5")

    label("loc_7BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_801")

    ChrTalk(    #5
        0x104,
        (
            "#033FIsn't that what brought the\x01",
            "Arseille down?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D5")

    label("loc_801")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_83E")

    ChrTalk(    #6
        0x106,
        "#057FAh, hell. That thing from before!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D5")

    label("loc_83E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_888")

    ChrTalk(    #7
        0x108,
        (
            "#077FIt's the creature that took down\x01",
            "the Arseille!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D5")

    label("loc_888")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D5")

    ChrTalk(    #8
        0x110,
        (
            "#271FMmph! That's the thing that\x01",
            "brought us down earlier!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D5")


    ChrTalk(    #9
        0x8,
        (
            "#121F#5P#30WReverie Dragion...\x02\x03",

            "#124FDamn you, Weissmann. So you DID\x01",
            "have more than just the one I used...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    Sleep(100)
    LoadEffect(0x1, "map\\\\mp009_00.eff")
    LoadEffect(0x2, "battle\\\\btgun00.eff")
    LoadEffect(0x3, "map\\\\mp019_00.eff")
    LoadEffect(0x4, "monster\\\\ms30800a.eff")
    LoadEffect(0x5, "monster\\\\ms30800b.eff")
    LoadEffect(0x6, "monster\\\\ms30800c.eff")

    def lambda_9DA():
        OP_6B(5360, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9DA)
    OP_43(0x19, 0x1, 0x1, 0x18)
    OP_43(0x1A, 0x1, 0x1, 0x19)
    Sleep(5000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A53")

    ChrTalk(    #10
        0x109,
        (
            "#1063FDon't really get the impression they'll\x01",
            "just let us walk on by.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C82")

    label("loc_A53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A8E")

    ChrTalk(    #11
        0x110,
        "#271FSo they want a fight, do they?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C82")

    label("loc_A8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC8")

    ChrTalk(    #12
        0x108,
        "#072FAnother hard battle awaits us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C82")

    label("loc_AC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1F")

    ChrTalk(    #13
        0x106,
        (
            "#057FFigures Weissmann'd throw more\x01",
            "big metal things in our way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C82")

    label("loc_B1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B71")

    ChrTalk(    #14
        0x104,
        (
            "#032FHmm. I doubt they will let us through\x01",
            "without a fight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C82")

    label("loc_B71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC6")

    ChrTalk(    #15
        0x103,
        (
            "#022FAnd I thought we were done fighting\x01",
            "large metal monsters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C82")

    label("loc_BC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C11")

    ChrTalk(    #16
        0x105,
        (
            "#1162FI doubt we will get through\x01",
            "without a fight...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C82")

    label("loc_C11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C64")

    ChrTalk(    #17
        0x10B,
        (
            "#212FKiiinda looks like they want to\x01",
            "give us a huge fight...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C82")

    label("loc_C64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C82")

    ChrTalk(    #18
        0x107,
        "#065FEeep!\x02",
    )

    CloseMessageWindow()

    label("loc_C82")


    ChrTalk(    #19
        0x101,
        "#1020FWe've got to get past them somehow!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D02")
    SetChrPos(0xB, 2800, 0, -16219, 315)

    NpcTalk(    #20
        0xB,
        "Woman's Voice",
        "#5PThen let us handle this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D9F")

    label("loc_D02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D51")
    SetChrPos(0xA, 2800, 0, -16219, 315)

    NpcTalk(    #21
        0xA,
        "Man's Voice",
        "#5PThen let us handle this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D9F")

    label("loc_D51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9F")
    SetChrPos(0x12, 2800, 0, -16219, 315)

    NpcTalk(    #22
        0x12,
        "Girl's Voice",
        "Estelle! Let us handle this!\x02",
    )

    CloseMessageWindow()

    label("loc_D9F")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE2")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E20")

    label("loc_DE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E09")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E20")

    label("loc_E09")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E20")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4C")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E8A")

    label("loc_E4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E73")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E8A")

    label("loc_E73")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E8A")

    Sleep(1000)
    SetChrPos(0x20, 7660, 2720, 3260, 0)
    SetChrPos(0x21, -7660, 3940, 3860, 0)
    OP_43(0x19, 0x1, 0x1, 0x1D)
    Sleep(300)
    OP_43(0x1A, 0x1, 0x1, 0x1E)
    WaitChrThread(0x19, 0x1)
    Sleep(500)

    def lambda_ED4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ED4)
    Sleep(100)

    def lambda_EE7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_EE7)

    def lambda_EF5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_EF5)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #23
        0x101,
        "#1004F#5PAh!\x02",
    )

    CloseMessageWindow()

    def lambda_F1F():
        OP_6D(3180, 0, -4640, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F1F)

    def lambda_F37():
        OP_67(0, 5090, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F37)

    def lambda_F4F():
        OP_6B(3040, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F4F)

    def lambda_F5F():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F5F)

    def lambda_F6F():
        OP_6E(354, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_F6F)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8E")
    OP_43(0xB, 0x1, 0x1, 0x21)

    label("loc_F8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA3")
    OP_43(0xA, 0x1, 0x1, 0x27)

    label("loc_FA3")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBD")
    OP_43(0x14, 0x1, 0x1, 0x26)

    label("loc_FBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD2")
    OP_43(0xF, 0x1, 0x1, 0x2B)

    label("loc_FD2")

    OP_43(0xE, 0x1, 0x1, 0x28)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF3")
    OP_43(0x12, 0x1, 0x1, 0x23)

    label("loc_FF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1008")
    OP_43(0x16, 0x1, 0x1, 0x29)

    label("loc_1008")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1022")
    OP_43(0x10, 0x1, 0x1, 0x2A)

    label("loc_1022")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1037")
    OP_43(0x15, 0x1, 0x1, 0x25)

    label("loc_1037")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104C")
    OP_43(0x11, 0x1, 0x1, 0x24)

    label("loc_104C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1066")
    OP_43(0x13, 0x1, 0x1, 0x2C)

    label("loc_1066")

    OP_43(0xD, 0x1, 0x1, 0x22)
    Sleep(300)
    SetChrChipByIndex(0xC, 33)
    SetChrSubChip(0xC, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3430, 0, -21410, 0)

    def lambda_1098():
        OP_8E(0xFE, 0xB68, 0x0, 0xFFFFD3D2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1098)
    Sleep(900)
    WaitChrThread(0xC, 0x3)
    OP_8C(0xC, 0, 400)
    Sleep(800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_115B")

    ChrTalk(    #24
        0x105,
        "#1164FJulia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x104,
        (
            "#030FAnd my dear Mueller! Your timing\x01",
            "couldn't be more perfect!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1004FWhat are you doing here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_115B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1269")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11CE")

    ChrTalk(    #27
        0x105,
        "#1164FJulia! And Major Vander!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        "#1004FWhat are you doing here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1266")

    label("loc_11CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121B")

    ChrTalk(    #29
        0x105,
        "#1164FJulia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1004FWhat are you guys doing here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1266")

    label("loc_121B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1266")

    ChrTalk(    #31
        0x10F,
        "#173FVander?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1004FWhat are you guys doing here?!\x02",
    )

    CloseMessageWindow()

    label("loc_1266")

    Jump("loc_1822")

    label("loc_1269")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E4")

    ChrTalk(    #33
        0x104,
        "#033FAh, Mueller! And Captain Schwarz!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1004FWhat are you doing here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_13AF")

    label("loc_12E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1332")

    ChrTalk(    #35
        0x110,
        "#273FSchwarz!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1004FWhat are you guys doing here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_13AF")

    label("loc_1332")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AF")

    ChrTalk(    #37
        0x104,
        (
            "#033FAnd my dear Mueller! Your timing\x01",
            "couldn't be more perfect!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1004FWhat are you guys doing here?!\x02",
    )

    CloseMessageWindow()

    label("loc_13AF")

    Jump("loc_1822")

    label("loc_13B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_151E")

    ChrTalk(    #39
        0x101,
        "#1004FJulia? Mueller? Everyone!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1424")

    ChrTalk(    #40
        0x103,
        "#23FWhat are you doing here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_151B")

    label("loc_1424")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1471")

    ChrTalk(    #41
        0x108,
        (
            "#070FHaha! WHEN did you get here\x01",
            "is a better question.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_151B")

    label("loc_1471")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C9")

    ChrTalk(    #42
        0x109,
        (
            "#1064FNot that I'm complaining, but,\x01",
            "yeah, why are you guys here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_151B")

    label("loc_14C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14EE")

    ChrTalk(    #43
        0x106,
        "#051FRight on!\x02",
    )

    CloseMessageWindow()
    Jump("loc_151B")

    label("loc_14EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_151B")

    ChrTalk(    #44
        0x107,
        "#560FEven Grandpa's here!\x02",
    )

    CloseMessageWindow()

    label("loc_151B")

    Jump("loc_1822")

    label("loc_151E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1574")

    ChrTalk(    #45
        0x110,
        "#273FCaptain Schwarz!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1004FWhat are you guys doing here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_1574")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C7")

    ChrTalk(    #47
        0x10F,
        "#173FMajor Vander!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#1004FWhat are you guys doing here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_15C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1621")

    ChrTalk(    #49
        0x10F,
        "#173FYour Highness!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1004FWhat are you doing here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_1621")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_167A")

    ChrTalk(    #51
        0x110,
        "#273FSchwarz!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1004FWhat are you guys doing here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_167A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16D2")

    ChrTalk(    #53
        0x10F,
        "#173FVander!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1004FWhat are you guys doing here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_16D2")


    ChrTalk(    #55
        0x101,
        "#1004FJulia? Mueller? Everyone!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_172B")

    ChrTalk(    #56
        0x103,
        "#23FWhat are you doing here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_172B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1778")

    ChrTalk(    #57
        0x108,
        (
            "#070FHaha! WHEN did you get here\x01",
            "is a better question.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_1778")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17D0")

    ChrTalk(    #58
        0x109,
        (
            "#1064FNot that I'm complaining, but,\x01",
            "yeah, why are you guys here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_17D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F5")

    ChrTalk(    #59
        0x106,
        "#051FRight on!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_17F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1822")

    ChrTalk(    #60
        0x107,
        "#560FEven Grandpa's here!\x02",
    )

    CloseMessageWindow()

    label("loc_1822")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186F")

    ChrTalk(    #61
        0xB,
        (
            "#170FThe repairs to the Arseille are\x01",
            "essentially done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190B")

    label("loc_186F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B6")

    ChrTalk(    #62
        0x12,
        "#1168FHaha! The Arseille is just about repaired.\x02",
    )

    CloseMessageWindow()
    Jump("loc_190B")

    label("loc_18B6")


    ChrTalk(    #63
        0x10,
        (
            "#027FWell, the Arseille's basically repaired.\x01",
            "We thought you might need a hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196B")

    ChrTalk(    #64
        0xA,
        (
            "#277FWe got everyone who could fight\x01",
            "together and came out to assist you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0A")

    label("loc_196B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C6")

    ChrTalk(    #65
        0x10,
        (
            "#526FAnd so everyone who could still\x01",
            "lift a weapon came to help out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0A")

    label("loc_19C6")


    ChrTalk(    #66
        0x12,
        (
            "#1168FEveryone who could still fight\x01",
            "came with us to help you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0A")


    ChrTalk(    #67
        0xC,
        (
            "#103FAdmittedly, I'm just tagging along,\x01",
            "looking at everything in awe. Heh!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B39")

    ChrTalk(    #68
        0x10B,
        "#213FDon?! Kyle?! You, too?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xD,
        "#191FHah! The Bobcat's nearly ready, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xE,
        (
            "#200F#2PSo we thought we'd pop on over and see\x01",
            "how our cute little sister was getting on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10B,
        "#415FAww... You guys...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BF4")

    label("loc_1B39")


    ChrTalk(    #72
        0x16,
        "#210FHeeey, don't forget about us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xD,
        "#490FThe Bobcat's about ready to fly, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xE,
        (
            "#202F#2PWe figured we'd pop on over and\x01",
            "see how you were getting on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1025FThat's great!\x02",
    )

    CloseMessageWindow()

    label("loc_1BF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C66")

    ChrTalk(    #76
        0x15,
        (
            "#1061FAaand I'd say we managed to time\x01",
            "our heroism just right once again!\x01",
            "Please, no applause!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA5")

    ChrTalk(    #77
        0xF,
        "#054FWe'll talk later! Leave this to us!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D7A")

    label("loc_1CA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF7")

    ChrTalk(    #78
        0x10,
        (
            "#024FSo, don't worry about those things!\x01",
            "We'll handle them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7A")

    label("loc_1CF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D38")

    ChrTalk(    #79
        0x14,
        "#076FWe can talk later! Leave those to us!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D7A")

    label("loc_1D38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D7A")

    ChrTalk(    #80
        0xB,
        (
            "#177FWe can talk later!\x01",
            "Go! We'll handle this!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB7")

    ChrTalk(    #81
        0x12,
        "#1162FEstelle, you hurry after Joshua!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E76")

    label("loc_1DB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DFB")

    ChrTalk(    #82
        0x13,
        "#062F#2PEstelle, hurry and save Joshua, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E76")

    label("loc_1DFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E43")

    ChrTalk(    #83
        0x11,
        (
            "#030F#4PEstelle, do not tarry!\x01",
            "Go! Joshua awaits!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E76")

    label("loc_1E43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E76")

    ChrTalk(    #84
        0xA,
        "#271FGo on ahead. We have this!\x02",
    )

    CloseMessageWindow()

    label("loc_1E76")


    ChrTalk(    #85
        0x101,
        "#1025FGuys...thanks!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(2230, -370, 3460, 0)
    OP_67(0, 5090, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(45000, 0)
    OP_6E(354, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #86
        0x8,
        (
            "#121F#5P#30WEstelle...go!\x02\x03",

            "Your light is the only thing\x01",
            "that can save Joshua now!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #87
        0x101,
        "#1006F#2PRight!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(3180, 0, -4640, 0)
    OP_67(0, 5090, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(45000, 0)
    OP_6E(354, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FCD")

    ChrTalk(    #88
        0xB,
        "#177F#4PEveryone, attack!\x02",
    )

    CloseMessageWindow()
    Jump("loc_201A")

    label("loc_1FCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FFB")

    ChrTalk(    #89
        0x12,
        "#1166FReady, everyone?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_201A")

    label("loc_1FFB")


    ChrTalk(    #90
        0x10,
        "#024FLet's do this, then!\x02",
    )

    CloseMessageWindow()

    label("loc_201A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_205F")

    ChrTalk(    #91
        0xA,
        (
            "#271F#5PSplit into two groups!\x01",
            "Rip them apart!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DD")

    label("loc_205F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20AA")

    ChrTalk(    #92
        0x10,
        (
            "#024FLet's split into two groups\x01",
            "and take them down!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DD")

    label("loc_20AA")


    ChrTalk(    #93
        0x12,
        (
            "#1166FSplit into two groups and\x01",
            "destroy them!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DD")

    Sleep(500)
    OP_D7(0x0, 0, 0)
    SetMessageWindowPos(390, 260, -1, -1)
    SetChrName("The Team")

    AnonymousTalk(    #94
        "\x07\x00#5SYeah!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()

    def lambda_212E():
        OP_6D(2460, 0, 6450, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_212E)

    def lambda_2146():
        OP_67(0, 8050, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2146)

    def lambda_215E():
        OP_6B(6690, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_215E)

    def lambda_216E():
        OP_6E(292, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_216E)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_218D")
    OP_43(0xB, 0x1, 0x1, 0x2D)

    label("loc_218D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2F)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21A2")
    OP_43(0xA, 0x1, 0x1, 0x33)

    label("loc_21A2")

    OP_44(0x19, 0x1)
    OP_43(0x19, 0x1, 0x1, 0x1F)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21C7")
    OP_43(0x14, 0x1, 0x1, 0x32)

    label("loc_21C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21DC")
    OP_43(0xF, 0x1, 0x1, 0x37)

    label("loc_21DC")

    OP_43(0xE, 0x1, 0x1, 0x34)
    OP_44(0x1A, 0x1)
    OP_43(0x1A, 0x1, 0x1, 0x20)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2208")
    OP_43(0x12, 0x1, 0x1, 0x2F)

    label("loc_2208")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221D")
    OP_43(0x16, 0x1, 0x1, 0x35)

    label("loc_221D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2237")
    OP_43(0x10, 0x1, 0x1, 0x36)

    label("loc_2237")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_224C")
    OP_43(0x11, 0x1, 0x1, 0x30)

    label("loc_224C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2261")
    OP_43(0x15, 0x1, 0x1, 0x31)

    label("loc_2261")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_227B")
    OP_43(0x13, 0x1, 0x1, 0x38)

    label("loc_227B")

    OP_43(0xD, 0x1, 0x1, 0x2E)
    Sleep(300)
    OP_43(0x101, 0x1, 0x1, 0xF)

    def lambda_2294():
        OP_6D(0, 0, 33380, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2294)
    Sleep(300)

    def lambda_22B1():
        OP_99(0xFE, 0x2, 0x1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_22B1)
    OP_43(0xF8, 0x1, 0x1, 0x10)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x1, 0x11)
    WaitChrThread(0xF9, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0x10, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x16, 0x1)
    Fade(500)
    OP_6D(-1090, 4010, 33290, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_22(0xC8, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x12C)
    Sleep(1000)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_2369():
        OP_6D(240, 4010, 34250, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2369)

    def lambda_2381():
        OP_67(0, 17360, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2381)
    OP_22(0x68, 0x0, 0x64)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    RemoveParty(0x1, 0xFF)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5315   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_AC end

    def Function_3_23B9(): pass

    label("Function_3_23B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2404")
    PlayEffect(0x3, 0xFF, 0x8, -300, 1200, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(100)
    Jump("Function_3_23B9")

    label("loc_2404")

    Return()

    # Function_3_23B9 end

    def Function_4_2405(): pass

    label("Function_4_2405")

    SetChrChipByIndex(0xFE, 32)
    SetChrFlags(0xFE, 0x2)
    SetChrPos(0xFE, 4059, 700, -430, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_242B():

        label("loc_242B")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_242B")

    QueueWorkItem2(0xFE, 2, lambda_242B)

    def lambda_243E():
        OP_96(0xFE, 0x213E, 0x0, 0xFFFFE6E2, 0x1388, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_243E)
    Sleep(2000)
    OP_44(0xFE, 0x2)

    def lambda_2465():
        OP_99(0xFE, 0x18, 0x20, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2465)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_2405 end

    def Function_5_247F(): pass

    label("Function_5_247F")

    OP_D2(0x2601DB, 0x2601E0, 0x1D)
    OP_D2(0x2601E2, 0x2601E7, 0x1E)
    SetChrChipByIndex(0x1E, 29)
    SetChrSubChip(0x1E, 32)
    SetChrChipByIndex(0x8, 30)
    SetChrSubChip(0x8, 2)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x2)
    OP_D2(0x701D0, 0x701DC, 0xB)
    OP_D2(0x701D1, 0x701DD, 0xC)
    OP_D2(0x701E8, 0x701F4, 0xD)
    OP_D2(0x701E9, 0x701F5, 0xE)
    OP_D2(0x27036E, 0x27037B, 0xF)
    OP_D2(0x27036F, 0x27037C, 0x10)
    OP_D2(0x70218, 0x70224, 0x11)
    OP_D2(0x70219, 0x70225, 0x12)
    OP_D2(0x70230, 0x7023C, 0x13)
    OP_D2(0x70231, 0x7023D, 0x14)
    OP_D2(0x70248, 0x70254, 0x15)
    OP_D2(0x70249, 0x70255, 0x16)
    OP_D2(0x270176, 0x270183, 0x17)
    OP_D2(0x270177, 0x270184, 0x18)
    OP_D2(0x702B4, 0x702BB, 0x19)
    OP_D2(0x702B5, 0x702BC, 0x1A)
    OP_D2(0x2702C2, 0x2702CC, 0x22)
    OP_D2(0x2702C3, 0x2702CD, 0x23)
    OP_D2(0x2702D6, 0x2702E0, 0x24)
    OP_D2(0x2702D7, 0x2702E1, 0x25)
    Return()

    # Function_5_247F end

    def Function_6_257A(): pass

    label("Function_6_257A")

    OP_D2(0x2702D8, 0x2702E2, 0x0)
    OP_D2(0x7029A, 0x702A1, 0x1)
    OP_D2(0x702A8, 0x702AF, 0x2)
    OP_D2(0x701D2, 0x701DE, 0x3)
    OP_D2(0x701EA, 0x701F6, 0x4)
    OP_D2(0x270370, 0x27037D, 0x8)
    OP_D2(0x7021A, 0x70226, 0x9)
    OP_D2(0x70232, 0x7023E, 0xA)
    OP_D2(0x7024A, 0x70256, 0x1B)
    OP_D2(0x270178, 0x270185, 0x1C)
    OP_D2(0x2702C4, 0x2702CE, 0x1F)
    OP_D2(0x702B6, 0x702BD, 0x20)
    Return()

    # Function_6_257A end

    def Function_7_25F3(): pass

    label("Function_7_25F3")

    OP_D2(0x70142, 0x70146, 0x21)
    OP_D2(0x70298, 0x7029F, 0x26)
    OP_D2(0x70299, 0x702A0, 0x27)
    OP_D2(0x702A6, 0x702AD, 0x28)
    OP_D2(0x702A7, 0x702AE, 0x29)
    Return()

    # Function_7_25F3 end

    def Function_8_2626(): pass

    label("Function_8_2626")

    LoadEffect(0x1, "map\\\\mp009_00.eff")
    LoadEffect(0x2, "battle\\\\btgun00.eff")
    LoadEffect(0x3, "map\\\\mp019_00.eff")
    LoadEffect(0x4, "monster\\\\ms30800a.eff")
    LoadEffect(0x5, "monster\\\\ms30800b.eff")
    Return()

    # Function_8_2626 end

    def Function_9_2695(): pass

    label("Function_9_2695")

    OP_8C(0xFE, 35, 0)
    OP_8F(0xFE, 0x280, 0xFFFFFE8E, 0x280, 0x1388, 0x0)
    Return()

    # Function_9_2695 end

    def Function_10_26B1(): pass

    label("Function_10_26B1")

    OP_8C(0xFE, 35, 0)
    OP_8F(0xFE, 0xFFFFFC2C, 0xFFFFFE8E, 0xFFFFFF10, 0x1388, 0x0)
    Return()

    # Function_10_26B1 end

    def Function_11_26CD(): pass

    label("Function_11_26CD")

    OP_8C(0xFE, 35, 0)
    OP_8F(0xFE, 0x208, 0xFFFFFE8E, 0xFFFFFCE0, 0x1388, 0x0)
    Return()

    # Function_11_26CD end

    def Function_12_26E9(): pass

    label("Function_12_26E9")

    OP_8E(0xFE, 0xC8, 0xFFFFFE8E, 0x870, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_26E9 end

    def Function_13_2705(): pass

    label("Function_13_2705")

    OP_8E(0xFE, 0xFFFFFD30, 0xFFFFFE8E, 0x258, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_2705 end

    def Function_14_2721(): pass

    label("Function_14_2721")

    OP_8E(0xFE, 0x2B2, 0xFFFFFE8E, 0x32A, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_2721 end

    def Function_15_273D(): pass

    label("Function_15_273D")

    OP_8E(0xFE, 0x3DE, 0xFFFFFE8E, 0xD66, 0x1770, 0x0)
    OP_8E(0xFE, 0x0, 0xFAA, 0x858E, 0x1770, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_273D end

    def Function_16_276D(): pass

    label("Function_16_276D")

    OP_8E(0xFE, 0xFFFFF8F8, 0xFFFFFE8E, 0xC80, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFFBC8, 0xFAA, 0x7EF4, 0x1770, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_16_276D end

    def Function_17_279D(): pass

    label("Function_17_279D")

    OP_8E(0xFE, 0xFFFFF8F8, 0xFFFFFE8E, 0xE42, 0x1770, 0x0)
    OP_8E(0xFE, 0xDC, 0x0, 0x319C, 0x1770, 0x0)
    OP_8E(0xFE, 0x0, 0xFAA, 0x63BA, 0x1770, 0x0)
    OP_8E(0xFE, 0x438, 0xFAA, 0x7EF4, 0x1770, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_17_279D end

    def Function_18_27F5(): pass

    label("Function_18_27F5")

    Sleep(500)
    ClearChrFlags(0x102, 0x2)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 9)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 29)

    def lambda_2819():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2819)

    def lambda_2829():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2829)
    OP_22(0xD6, 0x0, 0x46)

    def lambda_283E():
        OP_8F(0xFE, 0x154, 0xFFFFFE8E, 0xFFFFF97A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_283E)
    OP_8F(0x102, 0xFFFFFE66, 0xFFFFFE8E, 0x852, 0x4E20, 0x0)
    Sleep(500)

    def lambda_2872():

        label("loc_2872")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2872")

    QueueWorkItem2(0x102, 3, lambda_2872)

    def lambda_2883():

        label("loc_2883")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2883")

    QueueWorkItem2(0x8, 3, lambda_2883)

    def lambda_2894():
        OP_96(0xFE, 0x9F6, 0xFFFFFE8E, 0xD0C, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2894)
    OP_96(0x102, 0x15E, 0xFFFFFE8E, 0xD48, 0x1F4, 0x2710)

    label("loc_28C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2AE7")

    def lambda_28D0():
        OP_99(0xFE, 0x0, 0x5, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28D0)

    def lambda_28E0():
        OP_99(0xFE, 0x0, 0x5, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_28E0)
    OP_22(0xD6, 0x0, 0x46)

    def lambda_28F5():
        OP_96(0xFE, 0xFFFFFA6A, 0xFFFFFE8E, 0xFFFFF588, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_28F5)
    OP_96(0x102, 0xFFFFFF10, 0xFFFFFE8E, 0xFFFFF452, 0x1F4, 0x2710)

    def lambda_292A():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_292A)

    def lambda_293A():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_293A)
    OP_22(0xD6, 0x0, 0x46)

    def lambda_294F():
        OP_8F(0xFE, 0xFFFFFF10, 0xFFFFFE8E, 0xFFFFF452, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_294F)
    OP_8F(0x102, 0xFFFFFA6A, 0xFFFFFE8E, 0xFFFFF588, 0x4E20, 0x0)

    def lambda_297E():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_297E)

    def lambda_298E():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_298E)
    OP_22(0xD6, 0x0, 0x46)

    def lambda_29A3():
        OP_96(0xFE, 0x74E, 0xFFFFFE8E, 0xFFFFFBDC, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_29A3)
    OP_96(0x102, 0x78A, 0xFFFFFE8E, 0xFFFFF876, 0x1F4, 0x2710)
    Sleep(500)

    def lambda_29DD():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29DD)

    def lambda_29ED():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29ED)
    OP_22(0xD6, 0x0, 0x46)

    def lambda_2A02():
        OP_8F(0xFE, 0xFFFFFF10, 0xFFFFFE8E, 0xFFFFF452, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2A02)
    OP_8F(0x102, 0xFFFFFA6A, 0xFFFFFE8E, 0xFFFFF588, 0x4E20, 0x0)

    def lambda_2A31():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A31)

    def lambda_2A41():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A41)
    OP_22(0xD6, 0x0, 0x46)

    def lambda_2A56():
        OP_96(0xFE, 0x884, 0xFFFFFE8E, 0x41A, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2A56)
    OP_96(0x102, 0x3C0, 0xFFFFFE8E, 0x442, 0x1F4, 0x2710)

    def lambda_2A8B():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A8B)

    def lambda_2A9B():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A9B)
    OP_22(0xD6, 0x0, 0x46)

    def lambda_2AB0():
        OP_96(0xFE, 0xFFFFF89E, 0xFFFFFE8E, 0xFFFFFE20, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2AB0)
    OP_96(0x102, 0xFFFFF722, 0xFFFFFE8E, 0x316, 0x1F4, 0x2710)
    Sleep(500)
    Jump("loc_28C3")

    label("loc_2AE7")


    def lambda_2AED():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2AED)

    def lambda_2AFD():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2AFD)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_2B12():
        OP_96(0xFE, 0x74E, 0xFFFFFE8E, 0xFFFFFBDC, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2B12)
    OP_96(0x102, 0x78A, 0xFFFFFE8E, 0xFFFFF876, 0x1F4, 0x2710)

    def lambda_2B47():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B47)

    def lambda_2B57():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B57)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_2B6C():
        OP_96(0xFE, 0x884, 0xFFFFFE8E, 0x41A, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2B6C)
    OP_96(0x102, 0x3C0, 0xFFFFFE8E, 0x442, 0x1F4, 0x2710)

    def lambda_2BA1():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BA1)

    def lambda_2BB1():
        OP_99(0xFE, 0x0, 0x5, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2BB1)
    OP_22(0xD6, 0x0, 0x64)

    QueueWorkItem(0x8, 2, None)
    OP_8F(0x102, 0xFFFFFDBC, 0xFFFFFE8E, 0x366, 0x4E20, 0x0)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 8)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 28)

    def lambda_2BF4():
        OP_96(0xFE, 0xFFFFF36C, 0xFFFFFE8E, 0x0, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BF4)
    OP_96(0x8, 0xC94, 0xFFFFFE8E, 0x0, 0x1F4, 0x2710)
    Sleep(1000)

    def lambda_2C2E():
        OP_8F(0xFE, 0x0, 0xFFFFFE8E, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C2E)
    OP_8F(0x102, 0x64, 0xFFFFFE8E, 0x0, 0x4E20, 0x0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 3)
    OP_43(0x101, 0x2, 0x0, 0x16)
    Sleep(1000)
    OP_A2(0x1)
    Return()

    # Function_18_27F5 end

    def Function_19_2C7B(): pass

    label("Function_19_2C7B")

    SetChrSubChip(0x1B, 23)
    SetChrChipByIndex(0x1B, 1)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -560, -370, 2940, 0)
    OP_8F(0x1B, 0x154, 0x0, 0xFFFFF182, 0x61A8, 0x0)
    OP_8F(0x1B, 0x154, 0x2710, 0xFFFFF182, 0x61A8, 0x0)
    SetChrFlags(0x1B, 0x80)
    Return()

    # Function_19_2C7B end

    def Function_20_2CC9(): pass

    label("Function_20_2CC9")

    SetChrSubChip(0x1C, 23)
    SetChrChipByIndex(0x1C, 1)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -560, -370, 2940, 0)
    OP_8F(0x1C, 0x154, 0x0, 0xFFFFF182, 0x61A8, 0x0)
    OP_8F(0x1C, 0x4F74, 0xFA0, 0xFFFFF182, 0x61A8, 0x0)
    SetChrFlags(0x1C, 0x80)
    Return()

    # Function_20_2CC9 end

    def Function_21_2D17(): pass

    label("Function_21_2D17")

    SetChrSubChip(0x1D, 23)
    SetChrChipByIndex(0x1D, 1)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -560, -370, 2940, 0)
    OP_8F(0x1D, 0x154, 0x0, 0xFFFFF182, 0x61A8, 0x0)
    OP_8F(0x1D, 0xFFFFB08C, 0x1388, 0xFFFFF182, 0x61A8, 0x0)
    SetChrFlags(0x1D, 0x80)
    Return()

    # Function_21_2D17 end

    def Function_22_2D65(): pass

    label("Function_22_2D65")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D7A")
    OP_99(0x8, 0x0, 0x7, 0x9C4)
    Jump("Function_22_2D65")

    label("loc_2D7A")

    Return()

    # Function_22_2D65 end

    def Function_23_2D7B(): pass

    label("Function_23_2D7B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DC7")
    OP_51(0x1F, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_23_2D7B")

    label("loc_2DC7")

    Return()

    # Function_23_2D7B end

    def Function_24_2DC8(): pass

    label("Function_24_2DC8")

    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 880)
    OP_70(0x2, 0x3AC)
    OP_22(0x142, 0x0, 0x64)
    Sleep(2000)
    Play3DEffect(0x4, 0x1, 0x2, "Frame34_Bone__33_", 0x0, 0x0, 0x0, 0x37, 0xBE, 0xA5, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(50)
    OP_22(0x143, 0x0, 0x64)
    Play3DEffect(0x5, 0x2, 0x2, "Frame26_Bone__25_", 0x0, 0x0, 0x0, 0x37, 0xAA, 0xA5, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 950)
    OP_70(0x2, 0x3CA)
    Return()

    # Function_24_2DC8 end

    def Function_25_2E7C(): pass

    label("Function_25_2E7C")

    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 880)
    OP_70(0x3, 0x3AC)
    Sleep(2000)
    Play3DEffect(0x4, 0x3, 0x3, "Frame34_Bone__33_", 0x0, 0x0, 0x0, 0x13B, 0xBE, 0xA5, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(50)
    Play3DEffect(0x5, 0x4, 0x3, "Frame26_Bone__25_", 0x0, 0x0, 0x0, 0x13B, 0xAA, 0xA5, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_73(0x3)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 950)
    OP_70(0x3, 0x3CA)
    Return()

    # Function_25_2E7C end

    def Function_26_2F26(): pass

    label("Function_26_2F26")

    OP_24(0x158, 0x55)
    Sleep(100)
    OP_24(0x158, 0x5A)
    Sleep(100)
    OP_24(0x158, 0x5F)
    Sleep(100)
    OP_24(0x158, 0x64)
    Return()

    # Function_26_2F26 end

    def Function_27_2F46(): pass

    label("Function_27_2F46")


    def lambda_2F4C():
        OP_8F(0xFE, 0x1DEC, 0x0, 0x12FC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2F4C)
    WaitChrThread(0x19, 0x1)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 300)
    OP_70(0x2, 0x136)
    Sleep(200)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0x1388, 0x5DC)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x14)
    Return()

    # Function_27_2F46 end

    def Function_28_2FB0(): pass

    label("Function_28_2FB0")

    Sleep(200)

    def lambda_2FBB():
        OP_8F(0xFE, 0xFFFFE214, 0x0, 0x12FC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2FBB)
    WaitChrThread(0x1A, 0x1)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 300)
    OP_70(0x3, 0x136)
    Sleep(200)
    OP_23(0x158)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0x1388, 0x5DC)
    OP_73(0x3)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x14)
    Return()

    # Function_28_2FB0 end

    def Function_29_3022(): pass

    label("Function_29_3022")

    OP_22(0x1FA, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0xFF, 4280, 2240, -14080, 0, 0, 0, 1000, 1000, 1000, 0x20, 0, 0, 0, 0)
    Sleep(1000)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 110)
    OP_70(0x2, 0x8C)
    OP_23(0x143)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_73(0x2)
    Sleep(100)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 210)
    OP_70(0x2, 0xE6)
    OP_8C(0x19, 195, 50)
    OP_D8(0x2, 0x1F4)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x14)
    OP_22(0xEC, 0x0, 0x64)
    Return()

    # Function_29_3022 end

    def Function_30_30B7(): pass

    label("Function_30_30B7")

    OP_22(0x1FA, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0xFF, -3400, 2740, -14080, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(1000)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 110)
    OP_70(0x3, 0x8C)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_73(0x3)
    OP_71(0x3, 0x20)
    Sleep(100)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 240)
    OP_70(0x3, 0x104)
    OP_8C(0x1A, 165, 50)
    OP_D8(0x3, 0x1F4)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x14)
    Return()

    # Function_30_30B7 end

    def Function_31_3149(): pass

    label("Function_31_3149")

    OP_6F(0x2, 210)
    OP_70(0x2, 0xE6)
    OP_8C(0x19, 180, 50)
    OP_D8(0x2, 0x1F4)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x14)
    Sleep(1000)

    label("loc_317A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31A1")
    OP_72(0x2, 0x20)
    OP_6F(0x2, 110)
    OP_70(0x2, 0x8C)
    OP_73(0x2)
    Sleep(100)
    Jump("loc_317A")

    label("loc_31A1")

    Return()

    # Function_31_3149 end

    def Function_32_31A2(): pass

    label("Function_32_31A2")

    OP_6F(0x3, 240)
    OP_70(0x3, 0x104)
    OP_8C(0x1A, 180, 50)
    OP_D8(0x3, 0x1F4)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x14)
    Sleep(1000)

    label("loc_31D3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31FA")
    OP_72(0x3, 0x20)
    OP_6F(0x3, 110)
    OP_70(0x3, 0x8C)
    OP_73(0x3)
    Sleep(100)
    Jump("loc_31D3")

    label("loc_31FA")

    Return()

    # Function_32_31A2 end

    def Function_33_31FB(): pass

    label("Function_33_31FB")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xB, 37)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2800, 0, -16219, 315)
    OP_8E(0xB, 0xB2C, 0x0, 0xFFFFE6E2, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xB, 36)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_33_31FB end

    def Function_34_3246(): pass

    label("Function_34_3246")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xD, 39)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1290, 0, -21350, 315)
    OP_8E(0xD, 0x186, 0x0, 0xFFFFD3D2, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xD, 38)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_34_3246 end

    def Function_35_3291(): pass

    label("Function_35_3291")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0x12, 16)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 4710, 0, -17770, 315)
    OP_8E(0x12, 0xFE6, 0x0, 0xFFFFE278, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    SetChrChipByIndex(0x12, 15)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_35_3291 end

    def Function_36_32DC(): pass

    label("Function_36_32DC")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0x11, 14)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 6070, 0, -19890, 315)
    OP_8E(0x11, 0x173E, 0x0, 0xFFFFE32C, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    SetChrChipByIndex(0x11, 13)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_36_32DC end

    def Function_37_3327(): pass

    label("Function_37_3327")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0x15, 24)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 5800, 0, -18920, 315)
    OP_8E(0x15, 0xD5C, 0x0, 0xFFFFDB34, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0x15, 23)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_37_3327 end

    def Function_38_3372(): pass

    label("Function_38_3372")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0x14, 22)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 3830, 0, -16930, 315)
    OP_8E(0x14, 0x12DE, 0x0, 0xFFFFE822, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0x14, 21)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_38_3372 end

    def Function_39_33B8(): pass

    label("Function_39_33B8")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xA, 0x1000)
    SetChrChipByIndex(0xA, 35)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -100, 0, -17210, 0)
    OP_8E(0xA, 0xFFFFFF9C, 0x0, 0xFFFFE3D6, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xA, 34)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_39_33B8 end

    def Function_40_3408(): pass

    label("Function_40_3408")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xE, 41)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 30, 0, -18260, 0)
    OP_8E(0xE, 0xFFFFFA74, 0x0, 0xFFFFDBB6, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xE, 40)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_40_3408 end

    def Function_41_3453(): pass

    label("Function_41_3453")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0x16, 26)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 20, 0, -19250, 0)
    OP_8E(0x16, 0x14, 0x0, 0xFFFFDBDE, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0x16, 25)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_41_3453 end

    def Function_42_349E(): pass

    label("Function_42_349E")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1370, 0, -20350, 0)
    OP_8E(0x10, 0x6B8, 0x0, 0xFFFFDA6C, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0x10, 11)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_42_349E end

    def Function_43_34E9(): pass

    label("Function_43_34E9")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0xF, 18)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 590, 0, -20100, 0)
    OP_8E(0xF, 0x546, 0x0, 0xFFFFDF1C, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xF, 17)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_43_34E9 end

    def Function_44_3534(): pass

    label("Function_44_3534")

    SetChrFlags(0xFE, 0x40)
    SetChrChipByIndex(0x13, 20)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 5950, 0, -19260, 0)
    OP_8E(0x13, 0x13BA, 0x0, 0xFFFFDAD0, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_44_3534 end

    def Function_45_357F(): pass

    label("Function_45_357F")

    SetChrChipByIndex(0xB, 37)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xB, 0x1D2E, 0x0, 0xCF8, 0x1B58, 0x0)
    OP_8C(0xB, 0, 0)
    SetChrChipByIndex(0xB, 0)
    SetChrSubChip(0xFE, 0)

    label("loc_35AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35C6")
    OP_A2(0x8)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("loc_35AE")

    label("loc_35C6")

    Return()

    # Function_45_357F end

    def Function_46_35C7(): pass

    label("Function_46_35C7")

    SetChrChipByIndex(0xD, 39)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xD, 0xFFFFE7BE, 0x0, 0xFFFFF736, 0x1B58, 0x0)
    OP_8C(0xD, 0, 0)
    SetChrChipByIndex(0xD, 1)
    SetChrSubChip(0xFE, 0)

    label("loc_35F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_364A")
    OP_22(0x1FA, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0xD, 1000, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(3000)
    Jump("loc_35F6")

    label("loc_364A")

    Return()

    # Function_46_35C7 end

    def Function_47_364B(): pass

    label("Function_47_364B")

    SetChrChipByIndex(0x12, 16)
    SetChrSubChip(0xFE, 0)
    OP_8E(0x12, 0x1716, 0xFFFFFF92, 0x8D4, 0x1B58, 0x0)
    OP_8C(0x12, 0, 0)
    SetChrChipByIndex(0x12, 8)
    SetChrSubChip(0xFE, 0)

    label("loc_367A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3692")
    OP_A2(0x8)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("loc_367A")

    label("loc_3692")

    Return()

    # Function_47_364B end

    def Function_48_3693(): pass

    label("Function_48_3693")

    SetChrChipByIndex(0x11, 14)
    SetChrSubChip(0xFE, 0)
    OP_8E(0x11, 0x204E, 0x0, 0xFFFFF3C6, 0x1B58, 0x0)
    OP_8C(0x11, 0, 0)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0xFE, 0)

    label("loc_36C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3714")
    OP_A2(0x5)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("loc_36C2")

    label("loc_3714")

    Return()

    # Function_48_3693 end

    def Function_49_3715(): pass

    label("Function_49_3715")

    SetChrChipByIndex(0x15, 24)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0x15, 0x80)
    OP_8E(0x15, 0x1D42, 0x0, 0xFFFFEE80, 0x1B58, 0x0)
    OP_8C(0x15, 0, 0)
    SetChrChipByIndex(0x15, 28)
    SetChrSubChip(0xFE, 0)

    label("loc_3749")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3766")
    OP_A2(0x4)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("loc_3749")

    label("loc_3766")

    Return()

    # Function_49_3715 end

    def Function_50_3767(): pass

    label("Function_50_3767")

    SetChrChipByIndex(0x14, 22)
    SetChrSubChip(0xFE, 0)
    OP_8E(0x14, 0x2454, 0x0, 0x8D4, 0x1B58, 0x0)
    OP_8C(0x14, 0, 0)
    SetChrChipByIndex(0x14, 27)
    SetChrSubChip(0xFE, 0)

    label("loc_3796")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37AE")
    OP_A2(0x7)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("loc_3796")

    label("loc_37AE")

    Return()

    # Function_50_3767 end

    def Function_51_37AF(): pass

    label("Function_51_37AF")

    SetChrChipByIndex(0xA, 35)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xA, 0xFFFFE1E2, 0x0, 0xB36, 0x1B58, 0x0)
    OP_8C(0xA, 0, 0)
    SetChrChipByIndex(0xA, 31)
    SetChrSubChip(0xFE, 0)

    label("loc_37DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_382B")
    OP_A2(0x2)
    PlayEffect(0x1, 0xFF, 0xFE, 0, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("loc_37DE")

    label("loc_382B")

    Return()

    # Function_51_37AF end

    def Function_52_382C(): pass

    label("Function_52_382C")

    SetChrChipByIndex(0xE, 41)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xE, 0xFFFFDB66, 0x0, 0x8AC, 0x1B58, 0x0)
    OP_8C(0xE, 0, 0)
    SetChrChipByIndex(0xE, 2)
    SetChrSubChip(0xFE, 0)

    label("loc_385B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3873")
    OP_A2(0x6)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("loc_385B")

    label("loc_3873")

    Return()

    # Function_52_382C end

    def Function_53_3874(): pass

    label("Function_53_3874")

    SetChrChipByIndex(0x16, 26)
    SetChrSubChip(0xFE, 0)
    OP_8E(0x16, 0xFFFFE2AA, 0x0, 0xFFFFF920, 0x1B58, 0x0)
    OP_8C(0x16, 0, 0)
    SetChrChipByIndex(0x16, 32)
    SetChrSubChip(0xFE, 0)

    label("loc_38A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38F5")
    OP_A2(0x5)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("loc_38A3")

    label("loc_38F5")

    Return()

    # Function_53_3874 end

    def Function_54_38F6(): pass

    label("Function_54_38F6")

    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0xFE, 0)
    OP_8E(0x10, 0xFFFFDF80, 0x0, 0x7C6, 0x1B58, 0x0)
    OP_8C(0x10, 0, 0)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0xFE, 0)

    label("loc_3925")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_393D")
    OP_A2(0x4)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("loc_3925")

    label("loc_393D")

    Return()

    # Function_54_38F6 end

    def Function_55_393E(): pass

    label("Function_55_393E")

    SetChrChipByIndex(0xF, 18)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xF, 0xFFFFE9EE, 0xFFFFFFC4, 0xBCC, 0x1B58, 0x0)
    OP_8C(0xF, 0, 0)
    SetChrChipByIndex(0xF, 9)
    SetChrSubChip(0xFE, 0)

    label("loc_396D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39BA")
    OP_A2(0x2)
    PlayEffect(0x1, 0xFF, 0xFE, 0, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("loc_396D")

    label("loc_39BA")

    Return()

    # Function_55_393E end

    def Function_56_39BB(): pass

    label("Function_56_39BB")

    SetChrChipByIndex(0x13, 20)
    SetChrSubChip(0xFE, 0)
    OP_8E(0x13, 0x27CE, 0x0, 0xFFFFF088, 0x1B58, 0x0)
    OP_8C(0x13, 0, 0)
    SetChrChipByIndex(0x13, 10)
    SetChrSubChip(0xFE, 0)

    label("loc_39EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A3C")
    OP_A2(0x3)
    PlayEffect(0x3, 0xFF, 0x13, 1000, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x19, 0, 0, 0, 0)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(3000)
    Jump("loc_39EA")

    label("loc_3A3C")

    Return()

    # Function_56_39BB end

    def Function_57_3A3D(): pass

    label("Function_57_3A3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3A55")
    OP_22(0x1FA, 0x0, 0x64)
    OP_A3(0x3)

    label("loc_3A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3A64")
    OP_22(0x1F9, 0x0, 0x64)
    OP_A3(0x2)

    label("loc_3A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3A73")
    OP_22(0x1F6, 0x0, 0x64)
    OP_A3(0x4)

    label("loc_3A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3A82")
    OP_22(0x1F7, 0x0, 0x64)
    OP_A3(0x5)

    label("loc_3A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3A91")
    OP_22(0x1FC, 0x0, 0x64)
    OP_A3(0x6)

    label("loc_3A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3AA0")
    OP_22(0x1FB, 0x0, 0x64)
    OP_A3(0x7)

    label("loc_3AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3AAF")
    OP_22(0x1F8, 0x0, 0x64)
    OP_A3(0x8)

    label("loc_3AAF")

    OP_48()
    Jump("Function_57_3A3D")

    label("loc_3AB3")

    Return()

    # Function_57_3A3D end

    SaveToFile()

Try(main)
