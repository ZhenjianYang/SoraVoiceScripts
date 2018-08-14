from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'P9001   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P9001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        '守护兽',                               # 9
        '事件用照相机',                         # 10
        '',                                     # 11
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
        'ED6_DT29/CH15230 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT29/CH15230P._CP',             # 00
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
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_3BA",          # 01, 1
        "Function_2_3BB",          # 02, 2
        "Function_3_3EC",          # 03, 3
        "Function_4_41D",          # 04, 4
        "Function_5_44E",          # 05, 5
        "Function_6_47F",          # 06, 6
        "Function_7_4B0",          # 07, 7
        "Function_8_55E",          # 08, 8
        "Function_9_65C",          # 09, 9
        "Function_10_6B6",         # 0A, 10
        "Function_11_6FB",         # 0B, 11
        "Function_12_762",         # 0C, 12
        "Function_13_7E4",         # 0D, 13
        "Function_14_880",         # 0E, 14
        "Function_15_91A",         # 0F, 15
        "Function_16_9B0",         # 10, 16
        "Function_17_A28",         # 11, 17
        "Function_18_C27",         # 12, 18
        "Function_19_CB2",         # 13, 19
        "Function_20_D4E",         # 14, 20
        "Function_21_E11",         # 15, 21
        "Function_22_EA6",         # 16, 22
        "Function_23_F3F",         # 17, 23
        "Function_24_FDD",         # 18, 24
        "Function_25_1074",        # 19, 25
        "Function_26_1112",        # 1A, 26
        "Function_27_130C",        # 1B, 27
        "Function_28_13CC",        # 1C, 28
        "Function_29_14B6",        # 1D, 29
        "Function_30_154D",        # 1E, 30
        "Function_31_1739",        # 1F, 31
        "Function_32_17BC",        # 20, 32
        "Function_33_1850",        # 21, 33
        "Function_34_1A4A",        # 22, 34
        "Function_35_1ACD",        # 23, 35
        "Function_36_1B61",        # 24, 36
        "Function_37_1D5B",        # 25, 37
        "Function_38_1DDE",        # 26, 38
        "Function_39_1E72",        # 27, 39
        "Function_40_206C",        # 28, 40
        "Function_41_20EF",        # 29, 41
        "Function_42_2183",        # 2A, 42
        "Function_43_2374",        # 2B, 43
        "Function_44_2405",        # 2C, 44
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_111")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_111")

    Event(0, 14)
    Jump("loc_3B9")

    label("loc_118")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_137")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_137")

    Event(0, 15)
    Jump("loc_3B9")

    label("loc_13E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_15D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15D")

    Event(0, 16)
    Jump("loc_3B9")

    label("loc_164")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_194")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_18D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18D")

    Event(0, 19)
    Jump("loc_198")

    label("loc_194")

    Event(0, 17)

    label("loc_198")

    Jump("loc_3B9")

    label("loc_19B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1BA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BA")

    Event(0, 20)
    Jump("loc_3B9")

    label("loc_1C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1E0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E0")

    Event(0, 21)
    Jump("loc_3B9")

    label("loc_1E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_206")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_206")

    Event(0, 28)
    Jump("loc_3B9")

    label("loc_20D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_233")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_22C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22C")

    Event(0, 22)
    Jump("loc_3B9")

    label("loc_233")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_259")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_252")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_252")

    Event(0, 23)
    Jump("loc_3B9")

    label("loc_259")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xB, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_278")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_278")

    Event(0, 24)
    Jump("loc_3B9")

    label("loc_27F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_29E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29E")

    Event(0, 25)
    Jump("loc_3B9")

    label("loc_2A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_2C4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C4")

    Event(0, 29)
    Jump("loc_3B9")

    label("loc_2CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_2EA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EA")

    Event(0, 32)
    Jump("loc_3B9")

    label("loc_2F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_321")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_31A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31A")

    Event(0, 35)
    Jump("loc_325")

    label("loc_321")

    Event(0, 33)

    label("loc_325")

    Jump("loc_3B9")

    label("loc_328")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_358")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_351")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_351")

    Event(0, 38)
    Jump("loc_35C")

    label("loc_358")

    Event(0, 36)

    label("loc_35C")

    Jump("loc_3B9")

    label("loc_35F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x16, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_37E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37E")

    Event(0, 41)
    Jump("loc_3B9")

    label("loc_385")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_3AE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AE")

    Event(0, 44)
    Jump("loc_3B9")

    label("loc_3B5")

    Event(0, 42)

    label("loc_3B9")

    Return()

    # Function_0_F2 end

    def Function_1_3BA(): pass

    label("Function_1_3BA")

    Return()

    # Function_1_3BA end

    def Function_2_3BB(): pass

    label("Function_2_3BB")

    Sleep(4000)

    def lambda_3C6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C6)
    OP_8E(0xFE, 0x258, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_2_3BB end

    def Function_3_3EC(): pass

    label("Function_3_3EC")

    Sleep(4000)

    def lambda_3F7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F7)
    OP_8E(0xFE, 0xFFFFFF38, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_3_3EC end

    def Function_4_41D(): pass

    label("Function_4_41D")

    Sleep(4000)

    def lambda_428():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_428)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_4_41D end

    def Function_5_44E(): pass

    label("Function_5_44E")

    Sleep(4000)

    def lambda_459():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_459)
    OP_8E(0xFE, 0x258, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_5_44E end

    def Function_6_47F(): pass

    label("Function_6_47F")

    Sleep(4000)

    def lambda_48A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48A)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_47F end

    def Function_7_4B0(): pass

    label("Function_7_4B0")

    SetChrPos(0x0, 600, 0, -16500, 0)
    SetChrPos(0x1, -1000, 0, -16500, 0)
    SetChrPos(0x2, 600, 0, -18500, 0)
    SetChrPos(0x3, -1000, 0, -18500, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(440, 9760, 12190, 0)
    OP_67(0, 2440, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(397, 0)
    Return()

    # Function_7_4B0 end

    def Function_8_55E(): pass

    label("Function_8_55E")

    Fade(1000)
    OP_44(0x11, 0x0)
    OP_6D(2140, 5910, 10240, 0)
    OP_67(0, 3590, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(45000, 0)
    OP_6E(478, 0)

    def lambda_5AA():
        OP_6D(5340, 3360, 4440, 6000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_5AA)

    def lambda_5C2():
        OP_67(0, 1910, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5C2)

    def lambda_5DA():
        OP_6B(4100, 6000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5DA)

    def lambda_5EA():
        OP_6E(571, 6000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_5EA)
    OP_C8(0x200, 0x46, "C_PLAC42._CH", 0x1, 0x3E8)
    WaitChrThread(0x11, 0x0)
    Sleep(2000)
    Fade(500)
    OP_6D(890, 110, -4660, 0)
    OP_67(0, 5970, -10000, 0)
    OP_6B(2210, 0)
    OP_6C(45000, 0)
    OP_6E(384, 0)
    OP_0D()
    Sleep(300)
    Return()

    # Function_8_55E end

    def Function_9_65C(): pass

    label("Function_9_65C")


    def lambda_662():
        OP_D0(-270000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_662)

    def lambda_672():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_672)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    OP_44(0x0, 0x2)
    OP_44(0x0, 0x3)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    Return()

    # Function_9_65C end

    def Function_10_6B6(): pass

    label("Function_10_6B6")

    SetChrPos(0x0, 600, 0, -6500, 0)
    SetChrPos(0x1, -1000, 0, -6500, 0)
    SetChrPos(0x2, 600, 0, -8000, 0)
    SetChrPos(0x3, -1000, 0, -8000, 0)
    Return()

    # Function_10_6B6 end

    def Function_11_6FB(): pass

    label("Function_11_6FB")

    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 128, -1, -1)

    AnonymousTalk(    #0
        "\x07\x05\x18#2S#40W在此赠予记忆碎片……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Return()

    # Function_11_6FB end

    def Function_12_762(): pass

    label("Function_12_762")

    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x05#2S#40W祝贺通过试炼。\x01",
            "#500W \x01",
            "#40W在此赠予记忆碎片……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Return()

    # Function_12_762 end

    def Function_13_7E4(): pass

    label("Function_13_7E4")

    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 90, -1, -1)

    AnonymousTalk(    #2
        (
            "\x07\x05#40W    请攻克吾之试炼……\x01",
            "#500W \x01",
            "#40W     如是，则赠予汝\x01",
            "     记忆碎片与祝福。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Return()

    # Function_13_7E4 end

    def Function_14_880(): pass

    label("Function_14_880")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x0, 0, 0x0)
    ClearParty()
    AddParty(0xD, 0xEE, 0xFF)
    AddParty(0xC, 0xEE, 0xFF)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F4")

    def lambda_8B2():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_8B2)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x10E, 0x0, 0x0, 0x2)
    OP_43(0x10D, 0x0, 0x0, 0x4)
    Call(0, 8)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x10D, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_8F4")

    OP_D6(0x0)
    OP_E3(0x0, 0x0, 12288, 0x2)
    ClearParty()
    AddParty(0xD, 0xEE, 0xFF)
    OP_E6(0x0, 0x0)
    OP_E6(0x2)
    OP_28(0xD, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_880 end

    def Function_15_91A(): pass

    label("Function_15_91A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x2, 0, 0x0)
    ClearParty()
    AddParty(0x7, 0xEE, 0xFF)
    Call(0, 7)
    SetChrPos(0x108, 0, 0, -16000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98F")

    def lambda_959():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_959)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x108, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x108, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_98F")

    OP_D6(0x0)
    OP_E3(0x0, 0x2, 128, 0x2)
    ClearParty()
    AddParty(0x7, 0xEE, 0xFF)
    OP_28(0x9, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_91A end

    def Function_16_9B0(): pass

    label("Function_16_9B0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x3, 0, 0x0)
    ClearParty()
    AddParty(0xF, 0xEE, 0xFF)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A14")

    def lambda_9DE():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_9DE)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x110, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x110, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_A14")

    OP_D6(0x0)
    OP_28(0xF, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_9B0 end

    def Function_17_A28(): pass

    label("Function_17_A28")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x4, 0, 0x0)
    Call(0, 7)

    def lambda_A46():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_A46)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(2000)
    Fade(1000)
    LoadEffect(0x0, "map\\mp250_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x222, 0x0, 0x64)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 0, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_B27():

        label("loc_B27")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B27")

    QueueWorkItem2(0x10, 3, lambda_B27)

    def lambda_B3A():
        OP_6D(1120, 110, -2080, 1500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_B3A)

    def lambda_B52():
        OP_67(0, 4750, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B52)

    def lambda_B6A():
        OP_6B(2350, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_B6A)

    def lambda_B7A():
        OP_6E(406, 1500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_B7A)
    WaitChrThread(0x11, 0x0)
    LoadEffect(0x1, "map\\mp250_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_BE1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_BE1)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    WaitChrThread(0x10, 0x0)
    Sleep(500)
    Fade(250)
    ClearMapFlags(0x10)
    Sleep(300)
    Call(0, 13)
    Battle(0x385, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 18)
    Return()

    # Function_17_A28 end

    def Function_18_C27(): pass

    label("Function_18_C27")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapFlags(0x10)
    SetChrFlags(0x10, 0x80)
    OP_44(0x10, 0x3)
    Call(0, 10)
    OP_6D(100, 0, -7160, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)
    Call(0, 12)
    Call(0, 9)
    OP_D6(0x0)
    ClearParty()
    AddParty(0x23, 0xEE, 0xFF)
    OP_28(0x10, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C5400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_C27 end

    def Function_19_CB2(): pass

    label("Function_19_CB2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x4, 0, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D35")

    def lambda_CDB():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_CDB)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_D35")

    OP_D6(0x0)
    ClearParty()
    AddParty(0x23, 0xEE, 0xFF)
    OP_28(0x10, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C5400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_CB2 end

    def Function_20_D4E(): pass

    label("Function_20_D4E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x5, 0, 0x0)
    ClearParty()
    AddParty(0x1, 0xEE, 0xFF)
    AddParty(0x4, 0xEE, 0xFF)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC2")

    def lambda_D80():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_D80)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x102, 0x0, 0x0, 0x2)
    OP_43(0x105, 0x0, 0x0, 0x4)
    Call(0, 8)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x105, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_DC2")

    OP_D6(0x0)
    OP_E3(0x0, 0x5, 2, 0x2)
    ClearParty()
    AddParty(0x1, 0xEE, 0xFF)
    OP_BB(0x1, 0x1, 0x1C)
    OP_BD()
    OP_31(0x1, 0x10, 0x5A)
    OP_C2(0x1, 0x1F)
    OP_28(0x7, 0x4, 0x8)
    OP_A3(0x2F9A)
    OP_A3(0x2F9B)
    OP_A3(0x2F9C)
    OP_A3(0x2F9D)
    OP_A3(0x2F9E)
    OP_A3(0x2F9F)
    OP_A3(0x2FA0)
    OP_A3(0x2FA1)
    OP_A3(0x2FA2)
    OP_A3(0x2FA3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4203   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_D4E end

    def Function_21_E11(): pass

    label("Function_21_E11")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x6, 0, 0x0)
    ClearParty()
    AddParty(0x3, 0xEE, 0xFF)
    AddParty(0xC, 0xEF, 0xFF)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E85")

    def lambda_E43():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_E43)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x104, 0x0, 0x0, 0x2)
    OP_43(0x10D, 0x0, 0x0, 0x4)
    Call(0, 8)
    WaitChrThread(0x104, 0x0)
    WaitChrThread(0x10D, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_E85")

    OP_D6(0x0)
    OP_E3(0x0, 0x6, 8, 0x2)
    ClearParty()
    AddParty(0x3, 0xEE, 0xFF)
    OP_28(0x8, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4163   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_E11 end

    def Function_22_EA6(): pass

    label("Function_22_EA6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0xE, 0, 0x0)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    AddParty(0xE, 0xEF, 0xFF)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1A")

    def lambda_ED8():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_ED8)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x109, 0x0, 0x0, 0x2)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    Call(0, 8)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_F1A")

    OP_D6(0x0)
    OP_E3(0x0, 0xE, 16640, 0x2)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    AddParty(0xE, 0xEF, 0xFF)
    OP_28(0x11, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_EA6 end

    def Function_23_F3F(): pass

    label("Function_23_F3F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x12, 0, 0x0)
    ClearParty()
    AddParty(0x9, 0xEE, 0xFF)
    Call(0, 7)
    SetChrPos(0x10A, 0, 0, -16000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB4")

    def lambda_F7E():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_F7E)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x10A, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x10A, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_FB4")

    OP_D6(0x0)
    OP_E3(0x0, 0x12, 512, 0x2)
    ClearParty()
    AddParty(0x9, 0xEE, 0xFF)
    OP_E6(0x0, 0x0)
    OP_E6(0x2)
    OP_28(0xA, 0x4, 0x8)
    OP_A3(0x2FA6)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_F3F end

    def Function_24_FDD(): pass

    label("Function_24_FDD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x13, 0, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xB, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1060")

    def lambda_1006():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1006)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_1060")

    OP_D6(0x0)
    OP_28(0xB, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_FDD end

    def Function_25_1074(): pass

    label("Function_25_1074")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x14, 0, 0x0)
    ClearParty()
    AddParty(0xB, 0xEE, 0xFF)
    Call(0, 7)
    SetChrPos(0x10C, 0, 0, -16000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E9")

    def lambda_10B3():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_10B3)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x10C, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x10C, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_10E9")

    OP_D6(0x0)
    OP_E3(0x0, 0x14, 2048, 0x2)
    ClearParty()
    AddParty(0xB, 0xEE, 0xFF)
    OP_BB(0xB, 0x1, 0x53)
    OP_BD()
    OP_28(0xE, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_1074 end

    def Function_26_1112(): pass

    label("Function_26_1112")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0xD, 0, 0x0)
    Call(0, 7)

    def lambda_1130():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1130)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(2000)
    Fade(1000)
    LoadEffect(0x0, "map\\mp250_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x222, 0x0, 0x64)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 0, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1211():

        label("loc_1211")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1211")

    QueueWorkItem2(0x10, 3, lambda_1211)

    def lambda_1224():
        OP_6D(1120, 110, -2080, 1500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1224)

    def lambda_123C():
        OP_67(0, 4750, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_123C)

    def lambda_1254():
        OP_6B(2350, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1254)

    def lambda_1264():
        OP_6E(406, 1500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1264)
    WaitChrThread(0x11, 0x0)
    LoadEffect(0x1, "map\\mp250_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_12CB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_12CB)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    WaitChrThread(0x10, 0x0)
    Fade(250)
    ClearMapFlags(0x10)
    Sleep(300)
    Call(0, 13)
    Battle(0x386, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 27)
    Return()

    # Function_26_1112 end

    def Function_27_130C(): pass

    label("Function_27_130C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapFlags(0x10)
    SetChrFlags(0x10, 0x80)
    OP_44(0x10, 0x3)
    Call(0, 10)
    OP_6D(100, 0, -7160, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)
    Call(0, 12)
    Call(0, 9)
    OP_D6(0x0)
    OP_3E(0x32B, 1)
    OP_E3(0x0, 0xD, 0, 0x0)
    ClearParty()
    AddParty(0x12, 0xF0, 0xFF)
    AddParty(0x10, 0xEE, 0xFF)
    AddParty(0x11, 0xEF, 0xFF)
    OP_E6(0x0, 0x0)
    OP_E6(0x2)
    OP_C2(0x1, 0x4)
    OP_28(0xC, 0x4, 0x8)
    OP_A3(0x2F90)
    OP_A3(0x2F91)
    OP_A3(0x2F92)
    OP_A3(0x2F93)
    OP_A3(0x2F94)
    OP_A3(0x2F95)
    OP_A3(0x2F96)
    OP_A3(0x2F97)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C1401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_27_130C end

    def Function_28_13CC(): pass

    label("Function_28_13CC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0xD, 0, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144F")

    def lambda_13F5():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_13F5)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_144F")

    OP_D6(0x0)
    OP_3E(0x32B, 1)
    ClearParty()
    AddParty(0x12, 0xF0, 0xFF)
    AddParty(0x10, 0xEE, 0xFF)
    AddParty(0x11, 0xEF, 0xFF)
    OP_E6(0x0, 0x0)
    OP_E6(0x2)
    OP_C2(0x1, 0x4)
    OP_28(0xC, 0x4, 0x8)
    OP_A3(0x2F90)
    OP_A3(0x2F91)
    OP_A3(0x2F92)
    OP_A3(0x2F93)
    OP_A3(0x2F94)
    OP_A3(0x2F95)
    OP_A3(0x2F96)
    OP_A3(0x2F97)
    OP_A3(0x2FE0)
    OP_A3(0x2FE1)
    OP_A3(0x2FE2)
    OP_A3(0x2FE3)
    OP_A3(0x2FE4)
    OP_A3(0x2FE5)
    OP_A3(0x2FE6)
    OP_A3(0x2FE8)
    OP_A3(0x2FE9)
    OP_A3(0x2FEA)
    OP_A3(0x2FEB)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C1401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_28_13CC end

    def Function_29_14B6(): pass

    label("Function_29_14B6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x1D, 0, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1539")

    def lambda_14DF():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_14DF)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_1539")

    OP_D6(0x0)
    OP_28(0x12, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_14B6 end

    def Function_30_154D(): pass

    label("Function_30_154D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x1E, 0, 0x0)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    Call(0, 7)
    SetChrPos(0x109, 0, 0, -16000, 0)

    def lambda_1581():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1581)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x109, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x109, 0x0)
    Sleep(2000)
    Fade(1000)
    LoadEffect(0x0, "map\\mp250_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x222, 0x0, 0x64)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 0, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_163E():

        label("loc_163E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_163E")

    QueueWorkItem2(0x10, 3, lambda_163E)

    def lambda_1651():
        OP_6D(1120, 110, -2080, 1500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1651)

    def lambda_1669():
        OP_67(0, 4750, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1669)

    def lambda_1681():
        OP_6B(2350, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1681)

    def lambda_1691():
        OP_6E(406, 1500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1691)
    WaitChrThread(0x11, 0x0)
    LoadEffect(0x1, "map\\mp250_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_16F8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_16F8)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    WaitChrThread(0x10, 0x0)
    Fade(250)
    ClearMapFlags(0x10)
    Sleep(300)
    Call(0, 13)
    Battle(0x387, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 31)
    Return()

    # Function_30_154D end

    def Function_31_1739(): pass

    label("Function_31_1739")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapFlags(0x10)
    SetChrFlags(0x10, 0x80)
    OP_44(0x10, 0x3)
    Call(0, 10)
    OP_6D(100, 0, -7160, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)
    Call(0, 12)
    Call(0, 9)
    OP_D6(0x0)
    OP_28(0x13, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_1739 end

    def Function_32_17BC(): pass

    label("Function_32_17BC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x1E, 0, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183F")

    def lambda_17E5():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_17E5)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_183F")

    OP_D6(0x0)
    OP_28(0x13, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_32_17BC end

    def Function_33_1850(): pass

    label("Function_33_1850")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x1F, 0, 0x0)
    Call(0, 7)

    def lambda_186E():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_186E)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(2000)
    Fade(1000)
    LoadEffect(0x0, "map\\mp250_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x222, 0x0, 0x64)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 0, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_194F():

        label("loc_194F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_194F")

    QueueWorkItem2(0x10, 3, lambda_194F)

    def lambda_1962():
        OP_6D(1120, 110, -2080, 1500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1962)

    def lambda_197A():
        OP_67(0, 4750, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_197A)

    def lambda_1992():
        OP_6B(2350, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1992)

    def lambda_19A2():
        OP_6E(406, 1500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_19A2)
    WaitChrThread(0x11, 0x0)
    LoadEffect(0x1, "map\\mp250_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1A09():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A09)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    WaitChrThread(0x10, 0x0)
    Fade(250)
    ClearMapFlags(0x10)
    Sleep(300)
    Call(0, 13)
    Battle(0x388, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 34)
    Return()

    # Function_33_1850 end

    def Function_34_1A4A(): pass

    label("Function_34_1A4A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapFlags(0x10)
    SetChrFlags(0x10, 0x80)
    OP_44(0x10, 0x3)
    Call(0, 10)
    OP_6D(100, 0, -7160, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)
    Call(0, 12)
    Call(0, 9)
    OP_D6(0x0)
    OP_28(0x14, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_34_1A4A end

    def Function_35_1ACD(): pass

    label("Function_35_1ACD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x1F, 0, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B50")

    def lambda_1AF6():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1AF6)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_1B50")

    OP_D6(0x0)
    OP_28(0x14, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_35_1ACD end

    def Function_36_1B61(): pass

    label("Function_36_1B61")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x20, 0, 0x0)
    Call(0, 7)

    def lambda_1B7F():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1B7F)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(2000)
    Fade(1000)
    LoadEffect(0x0, "map\\mp250_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x222, 0x0, 0x64)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 0, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1C60():

        label("loc_1C60")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1C60")

    QueueWorkItem2(0x10, 3, lambda_1C60)

    def lambda_1C73():
        OP_6D(1120, 110, -2080, 1500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1C73)

    def lambda_1C8B():
        OP_67(0, 4750, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C8B)

    def lambda_1CA3():
        OP_6B(2350, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1CA3)

    def lambda_1CB3():
        OP_6E(406, 1500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1CB3)
    WaitChrThread(0x11, 0x0)
    LoadEffect(0x1, "map\\mp250_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1D1A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1D1A)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    WaitChrThread(0x10, 0x0)
    Fade(250)
    ClearMapFlags(0x10)
    Sleep(300)
    Call(0, 13)
    Battle(0x389, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 37)
    Return()

    # Function_36_1B61 end

    def Function_37_1D5B(): pass

    label("Function_37_1D5B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapFlags(0x10)
    SetChrFlags(0x10, 0x80)
    OP_44(0x10, 0x3)
    Call(0, 10)
    OP_6D(100, 0, -7160, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)
    Call(0, 12)
    Call(0, 9)
    OP_D6(0x0)
    OP_28(0x15, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_37_1D5B end

    def Function_38_1DDE(): pass

    label("Function_38_1DDE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x20, 0, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E61")

    def lambda_1E07():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1E07)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_1E61")

    OP_D6(0x0)
    OP_28(0x15, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_38_1DDE end

    def Function_39_1E72(): pass

    label("Function_39_1E72")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x21, 0, 0x0)
    Call(0, 7)

    def lambda_1E90():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1E90)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(2000)
    Fade(1000)
    LoadEffect(0x0, "map\\mp250_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x222, 0x0, 0x64)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 0, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1F71():

        label("loc_1F71")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1F71")

    QueueWorkItem2(0x10, 3, lambda_1F71)

    def lambda_1F84():
        OP_6D(1120, 110, -2080, 1500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1F84)

    def lambda_1F9C():
        OP_67(0, 4750, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F9C)

    def lambda_1FB4():
        OP_6B(2350, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1FB4)

    def lambda_1FC4():
        OP_6E(406, 1500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1FC4)
    WaitChrThread(0x11, 0x0)
    LoadEffect(0x1, "map\\mp250_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_202B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_202B)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    WaitChrThread(0x10, 0x0)
    Fade(250)
    ClearMapFlags(0x10)
    Sleep(300)
    Call(0, 13)
    Battle(0x38A, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 40)
    Return()

    # Function_39_1E72 end

    def Function_40_206C(): pass

    label("Function_40_206C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapFlags(0x10)
    SetChrFlags(0x10, 0x80)
    OP_44(0x10, 0x3)
    Call(0, 10)
    OP_6D(100, 0, -7160, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)
    Call(0, 12)
    Call(0, 9)
    OP_D6(0x0)
    OP_28(0x16, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_40_206C end

    def Function_41_20EF(): pass

    label("Function_41_20EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x21, 0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x16, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2172")
    Call(0, 7)

    def lambda_2118():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2118)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_2172")

    OP_D6(0x0)
    OP_28(0x16, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_41_20EF end

    def Function_42_2183(): pass

    label("Function_42_2183")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x22, 0, 0x0)
    ClearParty()
    AddParty(0xF, 0xEE, 0xFF)
    OP_31(0xF, 0xFA, 0x0)
    Call(0, 7)
    SetChrPos(0x110, 0, 0, -16000, 0)

    def lambda_21BC():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_21BC)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x110, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x110, 0x0)
    Sleep(2000)
    Fade(1000)
    LoadEffect(0x0, "map\\mp250_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x222, 0x0, 0x64)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 0, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2279():

        label("loc_2279")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2279")

    QueueWorkItem2(0x10, 3, lambda_2279)

    def lambda_228C():
        OP_6D(1120, 110, -2080, 1500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_228C)

    def lambda_22A4():
        OP_67(0, 4750, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_22A4)

    def lambda_22BC():
        OP_6B(2350, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_22BC)

    def lambda_22CC():
        OP_6E(406, 1500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_22CC)
    WaitChrThread(0x11, 0x0)
    LoadEffect(0x1, "map\\mp250_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_2333():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2333)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    WaitChrThread(0x10, 0x0)
    Fade(250)
    ClearMapFlags(0x10)
    Sleep(300)
    Call(0, 13)
    Battle(0x38B, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 43)
    Return()

    # Function_42_2183 end

    def Function_43_2374(): pass

    label("Function_43_2374")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapFlags(0x10)
    SetChrFlags(0x10, 0x80)
    OP_44(0x10, 0x3)
    OP_6D(1190, 110, -4250, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(1000)
    Sleep(500)
    Call(0, 12)
    Call(0, 9)
    OP_D6(0x0)
    OP_E3(0x0, 0x22, 32768, 0x2)
    ClearParty()
    AddParty(0xF, 0xEE, 0xFF)
    OP_28(0x17, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_43_2374 end

    def Function_44_2405(): pass

    label("Function_44_2405")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x22, 0, 0x0)
    ClearParty()
    AddParty(0xF, 0xEE, 0xFF)
    Call(0, 7)
    SetChrPos(0x110, 0, 0, -16000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247A")

    def lambda_2444():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2444)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x110, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x110, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_247A")

    OP_D6(0x0)
    OP_E3(0x0, 0x22, 32768, 0x2)
    ClearParty()
    AddParty(0xF, 0xEE, 0xFF)
    OP_28(0x17, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_44_2405 end

    SaveToFile()

Try(main)
