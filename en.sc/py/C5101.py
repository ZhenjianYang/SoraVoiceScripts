from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5101   ._SN',
        MapName             = 'Other',
        Location            = 'C5101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        'Riot Arms （黒）',                     # 9
        'Port Seeker',                          # 10
        'Port Seeker',                          # 11
        'Axis Pillar Station',                  # 12
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
        'ED6_DT29/CH12520 ._CH',             # 00
        'ED6_DT29/CH12521 ._CH',             # 01
        'ED6_DT29/CH12522 ._CH',             # 02
        'ED6_DT29/CH13080 ._CH',             # 03
        'ED6_DT29/CH13081 ._CH',             # 04
        'ED6_DT27/CH04000 ._CH',             # 05
        'ED6_DT27/CH04010 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT29/CH12520P._CP',             # 00
        'ED6_DT29/CH12521P._CP',             # 01
        'ED6_DT29/CH12522P._CP',             # 02
        'ED6_DT29/CH13080P._CP',             # 03
        'ED6_DT29/CH13081P._CP',             # 04
        'ED6_DT27/CH04000P._CP',             # 05
        'ED6_DT27/CH04010P._CP',             # 06
    )

    DeclNpc(
        X                   = 0,
        Z                   = 4000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 4000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 4000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 80,
        Z                   = 4000,
        Y                   = 65129,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -6540,
        Y                   = 4000,
        Z                   = 101490,
        Range               = 6540,
        Unknown_10          = 0x1770,
        Unknown_14          = 0x19456,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -6540,
        Y                   = 4000,
        Z                   = 101490,
        Range               = 6540,
        Unknown_10          = 0x1770,
        Unknown_14          = 0x19456,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_22F",          # 01, 1
        "Function_2_277",          # 02, 2
        "Function_3_28D",          # 03, 3
        "Function_4_3F4",          # 04, 4
        "Function_5_4A0",          # 05, 5
        "Function_6_580",          # 06, 6
        "Function_7_9CD",          # 07, 7
        "Function_8_C1E",          # 08, 8
        "Function_9_C73",          # 09, 9
        "Function_10_CAD",         # 0A, 10
        "Function_11_D96",         # 0B, 11
        "Function_12_ECA",         # 0C, 12
        "Function_13_F50",         # 0D, 13
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45F, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20F")
    SetChrPos(0x8, 0, 8800, 112340, 180)
    SetChrPos(0x9, -3880, 8000, 111800, 180)
    SetChrPos(0xA, 3880, 8000, 111800, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)

    label("loc_20F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_220")
    OP_A3(0x10F0)
    Event(0, 4)
    Jump("loc_22E")

    label("loc_220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_22E")
    OP_A3(0x10F1)
    Event(0, 5)

    label("loc_22E")

    Return()

    # Function_0_1A2 end

    def Function_1_22F(): pass

    label("Function_1_22F")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFF8AD0, 0x230072)
    Call(0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_END)), "loc_25D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x42), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x85, 0x1, 0x5A)
    Jump("loc_262")

    label("loc_25D")

    OP_22(0x1C7, 0x1, 0x5A)

    label("loc_262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45F, 3)), scpexpr(EXPR_END)), "loc_271")
    OP_B2(0x0, 0x0, 0x80)
    Jump("loc_276")

    label("loc_271")

    OP_B2(0x0, 0x1, 0x80)

    label("loc_276")

    Return()

    # Function_1_22F end

    def Function_2_277(): pass

    label("Function_2_277")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_277")

    label("loc_28C")

    Return()

    # Function_2_277 end

    def Function_3_28D(): pass

    label("Function_3_28D")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_2BE"),
        (3, "loc_2CB"),
        (4, "loc_2D8"),
        (5, "loc_2E5"),
        (6, "loc_2F2"),
        (7, "loc_2FF"),
        (8, "loc_30C"),
        (10, "loc_319"),
        (14, "loc_326"),
        (15, "loc_333"),
        (SWITCH_DEFAULT, "loc_340"),
    )


    label("loc_2BE")

    OP_D2(0x701D0, 0x701DC, 0x7)
    Jump("loc_340")

    label("loc_2CB")

    OP_D2(0x701E8, 0x701F4, 0x7)
    Jump("loc_340")

    label("loc_2D8")

    OP_D2(0x27036E, 0x27037B, 0x7)
    Jump("loc_340")

    label("loc_2E5")

    OP_D2(0x70218, 0x70224, 0x7)
    Jump("loc_340")

    label("loc_2F2")

    OP_D2(0x70230, 0x7023C, 0x7)
    Jump("loc_340")

    label("loc_2FF")

    OP_D2(0x70248, 0x70254, 0x7)
    Jump("loc_340")

    label("loc_30C")

    OP_D2(0x270176, 0x270183, 0x7)
    Jump("loc_340")

    label("loc_319")

    OP_D2(0x702B4, 0x702BB, 0x7)
    Jump("loc_340")

    label("loc_326")

    OP_D2(0x2702D6, 0x2702E0, 0x7)
    Jump("loc_340")

    label("loc_333")

    OP_D2(0x2702C2, 0x2702CC, 0x7)
    Jump("loc_340")

    label("loc_340")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_371"),
        (3, "loc_37E"),
        (4, "loc_38B"),
        (5, "loc_398"),
        (6, "loc_3A5"),
        (7, "loc_3B2"),
        (8, "loc_3BF"),
        (10, "loc_3CC"),
        (14, "loc_3D9"),
        (15, "loc_3E6"),
        (SWITCH_DEFAULT, "loc_3F3"),
    )


    label("loc_371")

    OP_D2(0x701D0, 0x701DC, 0x8)
    Jump("loc_3F3")

    label("loc_37E")

    OP_D2(0x701E8, 0x701F4, 0x8)
    Jump("loc_3F3")

    label("loc_38B")

    OP_D2(0x27036E, 0x27037B, 0x8)
    Jump("loc_3F3")

    label("loc_398")

    OP_D2(0x70218, 0x70224, 0x8)
    Jump("loc_3F3")

    label("loc_3A5")

    OP_D2(0x70230, 0x7023C, 0x8)
    Jump("loc_3F3")

    label("loc_3B2")

    OP_D2(0x70248, 0x70254, 0x8)
    Jump("loc_3F3")

    label("loc_3BF")

    OP_D2(0x270176, 0x270183, 0x8)
    Jump("loc_3F3")

    label("loc_3CC")

    OP_D2(0x702B4, 0x702BB, 0x8)
    Jump("loc_3F3")

    label("loc_3D9")

    OP_D2(0x2702D6, 0x2702E0, 0x8)
    Jump("loc_3F3")

    label("loc_3E6")

    OP_D2(0x2702C2, 0x2702CC, 0x8)
    Jump("loc_3F3")

    label("loc_3F3")

    Return()

    # Function_3_28D end

    def Function_4_3F4(): pass

    label("Function_4_3F4")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-200, 12000, 148580, 0)
    OP_67(0, -840, -10000, 0)
    OP_6B(5800, 0)
    OP_6C(359000, 0)
    OP_6E(1276, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(    #0
        "\x07\x00Goddess...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0110   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_4_3F4 end

    def Function_5_4A0(): pass

    label("Function_5_4A0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-200, 12000, 148580, 0)
    OP_67(0, -840, -10000, 0)
    OP_6B(5800, 0)
    OP_6C(359000, 0)
    OP_6E(1276, 0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x400, 0x0, 0xFDE4, 0x400, 0x400, 0x0, 0x0, 0x280, 0x400, 0xFFFFFF, 0x0, "C_VIS189._CH")
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x7, 0, 0, 7000)
    OP_C7(0x0, 0x0, 0x0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    Sleep(2000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5100   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_5_4A0 end

    def Function_6_580(): pass

    label("Function_6_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45F, 4)), scpexpr(EXPR_END)), "loc_588")
    Return()

    label("loc_588")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AD")
    Call(0, 12)
    Call(0, 13)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_5AD")

    SetChrPos(0x8, 0, 12800, 172800, 180)
    SetChrPos(0x9, -3880, 18000, 111800, 180)
    SetChrPos(0xA, 3880, 21000, 111800, 180)
    ClearChrFlags(0x8, 0x80)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(1140, 4170, 102820, 0)
    OP_67(0, 9410, -10000, 0)
    OP_6B(4240, 0)
    OP_6C(43000, 0)

    def lambda_657():
        OP_6D(1140, 4170, 102820, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_657)

    def lambda_66F():
        OP_6C(43000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_66F)

    def lambda_67F():
        OP_67(0, 9410, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67F)

    def lambda_697():
        OP_6B(4240, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_697)
    WaitChrThread(0x101, 0x0)

    def lambda_6AC():
        OP_6D(-1050, 12000, 161650, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6AC)

    def lambda_6C4():
        OP_6C(334000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C4)

    def lambda_6D4():
        OP_67(0, 5260, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6D4)

    def lambda_6EC():
        OP_6B(6800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6EC)
    WaitChrThread(0x101, 0x3)

    def lambda_701():
        OP_6B(3930, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_701)
    WaitChrThread(0x101, 0x0)
    SetChrPos(0x101, -1830, 4000, 102580, 0)
    SetChrPos(0x102, -490, 4000, 102010, 0)
    SetChrPos(0xF8, -2820, 4000, 101160, 0)
    SetChrPos(0xF9, -1540, 4000, 100700, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 6)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 7)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 8)
    SetChrSubChip(0xF9, 0)
    ClearMapFlags(0x10)
    OP_22(0x193, 0x0, 0x64)
    Sleep(1200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_79A():
        OP_6D(-930, 8000, 114170, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_79A)

    def lambda_7B2():
        OP_6C(330000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B2)

    def lambda_7C2():
        OP_6B(2650, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7C2)
    OP_43(0x8, 0x0, 0x0, 0x8)
    OP_43(0x8, 0x3, 0x0, 0x9)
    WaitChrThread(0x8, 0x0)
    OP_7C(0x0, 0x1F4, 0x1388, 0x1F4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_81A():
        OP_8F(0xFE, 0xFFFFF0D8, 0x1F40, 0x1B4B8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_81A)

    def lambda_835():
        OP_8F(0xFE, 0xF28, 0x1F40, 0x1B4B8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_835)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_6D(-330, 6800, 107210, 0)
    OP_67(0, 7780, -10000, 0)
    OP_6B(4550, 0)
    OP_6C(328000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)

    def lambda_8B5():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8B5)
    WaitChrThread(0x8, 0x2)
    OP_22(0x193, 0x0, 0x64)
    Sleep(1000)

    def lambda_8D4():
        OP_6D(-1890, 5200, 105220, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8D4)

    def lambda_8EC():
        OP_6B(3530, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8EC)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_901():
        OP_96(0xFE, 0xFFFFFBF0, 0x12C0, 0x18DEE, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_901)

    def lambda_91F():
        OP_99(0xFE, 0x4, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_91F)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x4)

    def lambda_939():
        OP_8F(0xFE, 0xFFFFF420, 0x12C0, 0x18DEE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_939)

    def lambda_954():
        OP_8F(0xFE, 0x410, 0x12C0, 0x18DEE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_954)
    WaitChrThread(0x101, 0x0)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x525, 0x0, 0x0, 0x0, 0xFF)
    OP_44(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_9B9"),
        (0, "loc_9BE"),
        (2, "loc_9C5"),
        (SWITCH_DEFAULT, "loc_9CC"),
    )


    label("loc_9B9")

    OP_B4(0x0)
    Jump("loc_9CC")

    label("loc_9BE")

    Call(0, 10)
    Jump("loc_9CC")

    label("loc_9C5")

    Call(0, 11)
    Jump("loc_9CC")

    label("loc_9CC")

    Return()

    # Function_6_580 end

    def Function_7_9CD(): pass

    label("Function_7_9CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45F, 4)), scpexpr(EXPR_END)), "loc_9D5")
    Return()

    label("loc_9D5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9FA")
    Call(0, 12)
    Call(0, 13)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_9FA")

    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(-330, 6800, 107210, 0)
    OP_67(0, 7780, -10000, 0)
    OP_6B(4550, 0)
    OP_6C(328000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1830, 4000, 102580, 0)
    SetChrPos(0x102, -490, 4000, 102010, 0)
    SetChrPos(0xF8, -2820, 4000, 101160, 0)
    SetChrPos(0xF9, -1540, 4000, 100700, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 6)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 7)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 8)
    SetChrSubChip(0xF9, 0)
    OP_0D()
    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)

    def lambda_B06():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B06)
    WaitChrThread(0x8, 0x2)
    OP_22(0x193, 0x0, 0x64)
    Sleep(1000)

    def lambda_B25():
        OP_6D(-1890, 5200, 105220, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B25)

    def lambda_B3D():
        OP_6B(3530, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B3D)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_B52():
        OP_96(0xFE, 0xFFFFFBF0, 0x12C0, 0x18DEE, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B52)

    def lambda_B70():
        OP_99(0xFE, 0x4, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B70)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x4)

    def lambda_B8A():
        OP_8F(0xFE, 0xFFFFF420, 0x12C0, 0x18DEE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B8A)

    def lambda_BA5():
        OP_8F(0xFE, 0x410, 0x12C0, 0x18DEE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BA5)
    WaitChrThread(0x101, 0x0)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x525, 0x0, 0x0, 0x0, 0xFF)
    OP_44(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_C0A"),
        (0, "loc_C0F"),
        (2, "loc_C16"),
        (SWITCH_DEFAULT, "loc_C1D"),
    )


    label("loc_C0A")

    OP_B4(0x0)
    Jump("loc_C1D")

    label("loc_C0F")

    Call(0, 10)
    Jump("loc_C1D")

    label("loc_C16")

    Call(0, 11)
    Jump("loc_C1D")

    label("loc_C1D")

    Return()

    # Function_7_9CD end

    def Function_8_C1E(): pass

    label("Function_8_C1E")


    def lambda_C24():
        OP_8F(0xFE, 0x0, 0x3200, 0x2079C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C24)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x3)
    OP_23(0x13F)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_C50():
        OP_96(0xFE, 0x0, 0x2260, 0x1B6D4, 0x1F40, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C50)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    Return()

    # Function_8_C1E end

    def Function_9_C73(): pass

    label("Function_9_C73")

    Sleep(200)
    OP_22(0x13F, 0x0, 0x46)
    Sleep(500)
    OP_22(0x13F, 0x0, 0x50)
    Sleep(500)
    OP_22(0x13F, 0x0, 0x5A)
    Sleep(500)

    label("loc_C96")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CAC")
    OP_22(0x13F, 0x0, 0x64)
    Sleep(500)
    Jump("loc_C96")

    label("loc_CAC")

    Return()

    # Function_9_C73 end

    def Function_10_CAD(): pass

    label("Function_10_CAD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_6D(-120, 4000, 100630, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -120, 4000, 100630, 0)
    SetChrPos(0x1, -120, 4000, 100630, 0)
    SetChrPos(0x2, -120, 4000, 100630, 0)
    SetChrPos(0x3, -120, 4000, 100630, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    OP_A2(0x22FC)
    OP_B2(0x0, 0x0, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_CAD end

    def Function_11_D96(): pass

    label("Function_11_D96")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x8, 0, 8800, 112340, 180)
    SetChrPos(0x9, -3880, 8000, 111800, 180)
    SetChrPos(0xA, 3880, 8000, 111800, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_6D(-120, 4000, 100630, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -120, 4000, 98630, 180)
    SetChrPos(0x1, -120, 4000, 98630, 180)
    SetChrPos(0x2, -120, 4000, 98630, 180)
    SetChrPos(0x3, -120, 4000, 98630, 180)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    OP_A2(0x22FB)
    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_11_D96 end

    def Function_12_ECA(): pass

    label("Function_12_ECA")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
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
        (0, "loc_F43"),
        (1, "loc_F49"),
        (SWITCH_DEFAULT, "loc_F4F"),
    )


    label("loc_F43")

    OP_A2(0x1200)
    Jump("loc_F4F")

    label("loc_F49")

    OP_A2(0x1201)
    Jump("loc_F4F")

    label("loc_F4F")

    Return()

    # Function_12_ECA end

    def Function_13_F50(): pass

    label("Function_13_F50")

    FadeToDark(0, 0, -1)
    OP_6D(-27650, 0, -3680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_13_F50 end

    SaveToFile()

Try(main)
