from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T5200   ._SN',
        MapName             = 'Other',
        Location            = 'T5200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60117",
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
        'Josette',                              # 9
        'Kyle',                                 # 10
        'Don',                                  # 11
        'Camera Control',                       # 12
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
        'ED6_DT27/CH03100 ._CH',             # 00
        'ED6_DT27/CH03770 ._CH',             # 01
        'ED6_DT27/CH03760 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT27/CH03100P._CP',             # 00
        'ED6_DT27/CH03770P._CP',             # 01
        'ED6_DT27/CH03760P._CP',             # 02
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        NpcIndex            = 0x1CC,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_142",          # 00, 0
        "Function_1_161",          # 01, 1
        "Function_2_162",          # 02, 2
        "Function_3_5B1",          # 03, 3
        "Function_4_636",          # 04, 4
        "Function_5_67A",          # 05, 5
    )


    def Function_0_142(): pass

    label("Function_0_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_153")
    OP_A3(0x10F0)
    Event(0, 5)
    Jump("loc_160")

    label("loc_153")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_160")

    Return()

    # Function_0_142 end

    def Function_1_161(): pass

    label("Function_1_161")

    Return()

    # Function_1_161 end

    def Function_2_162(): pass

    label("Function_2_162")

    EventBegin(0x0)
    ClearMapFlags(0x2000000)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x10A, 0x80)
    OP_22(0x1C3, 0x0, 0x64)
    OP_6D(2080, 0, -12200, 0)
    OP_67(0, 12390, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 7740, 3130, 48960, 90)
    SetChrPos(0x9, 2670, 0, 21830, 0)
    SetChrPos(0xA, -8320, 0, 15250, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_208():
        OP_6D(-2040, 0, 18280, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_208)

    def lambda_220():
        OP_6B(6500, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_220)
    Sleep(500)
    FadeToBright(2000, 0)
    Sleep(2000)
    OP_43(0x10A, 0x1, 0x0, 0x3)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Fade(500)
    OP_6D(5010, 0, 25180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3440, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x9, 90, 400)
    Sleep(500)
    OP_8C(0x9, 0, 400)
    Sleep(1000)
    OP_8C(0x9, 270, 400)

    def lambda_2A9():
        OP_8E(0xFE, 0xFFFFF614, 0x0, 0x497A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2A9)
    Sleep(1000)
    Fade(500)
    OP_6D(-13540, 10, 15940, 0)
    OP_6C(315000, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0xA, 225, 400)
    Sleep(500)
    OP_8C(0xA, 315, 400)
    Sleep(1000)
    OP_8C(0xA, 90, 400)
    SetChrPos(0x9, -2500, 0, 17010, 254)

    def lambda_31E():
        OP_8E(0xFE, 0xFFFFEEE4, 0x0, 0x40E2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_31E)

    def lambda_339():
        OP_6D(-3510, 0, 16860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_339)

    def lambda_351():
        OP_6B(4440, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_351)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)

    def lambda_370():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_370)
    Sleep(500)

    def lambda_383():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_383)
    Sleep(500)

    def lambda_396():
        OP_8E(0xFE, 0xFFFFEE44, 0x3E8, 0x8AB6, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_396)
    Sleep(400)

    def lambda_3B6():
        OP_8E(0xFE, 0xFFFFE85E, 0x3E8, 0x8B4C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3B6)
    Sleep(1000)
    Fade(500)
    OP_6D(-2940, 2000, 57100, 0)
    OP_6B(5240, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_407():
        OP_6D(11400, 2000, 42760, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_407)
    OP_43(0x8, 0x0, 0x0, 0x4)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    SetChrPos(0x9, -2540, 1000, 40650, 90)
    SetChrPos(0xA, -3500, 1000, 42410, 90)

    def lambda_450():
        OP_8E(0xFE, 0x2BF2, 0x7D0, 0xA2B2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_450)
    Sleep(500)

    def lambda_470():
        OP_8E(0xFE, 0x28F0, 0x7D0, 0xA992, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_470)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x9, 0x0)

    def lambda_495():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_495)
    WaitChrThread(0xA, 0x0)

    def lambda_4A8():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_4A8)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 90, 400)

    def lambda_4E3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_4E3)
    Sleep(150)

    def lambda_4F6():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_4F6)
    Sleep(1500)

    def lambda_509():
        OP_6D(51590, -1000, 43830, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_509)

    def lambda_521():
        OP_67(0, 10550, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_521)

    def lambda_539():
        OP_8E(0xFE, 0x55F0, 0x76C, 0xA74E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_539)
    Sleep(400)

    def lambda_559():
        OP_8E(0xFE, 0x55F0, 0x7D0, 0xA2C6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_559)
    Sleep(400)

    def lambda_579():
        OP_8E(0xFE, 0x55F0, 0x7D0, 0xA99C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_579)
    Sleep(3200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T5201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_162 end

    def Function_3_5B1(): pass

    label("Function_3_5B1")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0 op#A
        "\x07\x05#50AMeanwhile... Erebonian Empire, Southern Regions\x02",
    )

    Sleep(3000)
    OP_56(0x0)

    AnonymousTalk(    #1 op#A
        "\x07\x05#50A120 selge from the Liberlian Border\x02",
    )

    Sleep(3000)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_3_5B1 end

    def Function_4_636(): pass

    label("Function_4_636")

    OP_8E(0x8, 0x2A12, 0x7D0, 0xBF40, 0x7D0, 0x0)
    OP_8E(0x8, 0x31E2, 0x7D0, 0xB50E, 0x7D0, 0x0)
    OP_8E(0x8, 0x31E2, 0x7D0, 0xA780, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Return()

    # Function_4_636 end

    def Function_5_67A(): pass

    label("Function_5_67A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(1050, 50, 6880, 0)
    OP_67(0, 10400, -10000, 0)
    OP_6B(5830, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C2, 0x0, 0x64)
    FadeToBright(1000, 0)

    def lambda_6EC():
        OP_6D(-2970, 870, 30980, 10000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6EC)

    def lambda_704():
        OP_67(0, 15430, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_704)
    OP_C8(0x200, 0x46, "C_PLAC28._CH", 0x1, 0x7D0)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T5201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_67A end

    SaveToFile()

Try(main)
