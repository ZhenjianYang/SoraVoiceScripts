from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3103   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3103.x',
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
        ' ',                                    # 9
        '目标用照相机',                         # 10
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_EA",           # 00, 0
        "Function_1_11A",          # 01, 1
        "Function_2_122",          # 02, 2
        "Function_3_15A",          # 03, 3
        "Function_4_28B",          # 04, 4
        "Function_5_2A0",          # 05, 5
        "Function_6_376",          # 06, 6
    )


    def Function_0_EA(): pass

    label("Function_0_EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_FD")
    OP_A3(0x2508)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_119")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_119")

    Return()

    # Function_0_EA end

    def Function_1_11A(): pass

    label("Function_1_11A")

    OP_43(0x10, 0x0, 0x0, 0x2)
    Return()

    # Function_1_11A end

    def Function_2_122(): pass

    label("Function_2_122")

    OP_72(0x2010, 0x0)
    ExitThread()
    OP_72(0x200E, 0x0)
    ExitThread()

    label("loc_12E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_159")
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    OP_6F(0xE, 0)
    OP_70(0xE, 0x28)
    OP_73(0x10)
    Jump("loc_12E")

    label("loc_159")

    Return()

    # Function_2_122 end

    def Function_3_15A(): pass

    label("Function_3_15A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x106, 25470, 0, 59050, 90)
    OP_6D(25030, 3200, 74910, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(4370, 0)
    OP_6C(318000, 0)
    OP_6E(328, 0)
    FadeToBright(2000, 0)
    OP_43(0x106, 0x0, 0x0, 0x4)

    def lambda_1CA():
        OP_6D(46980, 3200, 59210, 6000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1CA)

    def lambda_1E2():
        OP_67(0, 7340, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E2)

    def lambda_1FA():
        OP_6B(4370, 6000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1FA)

    def lambda_20A():
        OP_6C(221000, 12000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_20A)

    def lambda_21A():
        OP_6E(305, 6000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_21A)
    Sleep(5000)

    def lambda_22F():
        OP_6D(56530, 3200, 24210, 8000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_22F)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x11, 0x2)
    WaitChrThread(0x11, 0x3)

    def lambda_25B():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_25B)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x11, 0x2)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3172   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_15A end

    def Function_4_28B(): pass

    label("Function_4_28B")

    OP_8E(0xFE, 0xE5EC, 0x0, 0xE5CE, 0x7D0, 0x0)
    Return()

    # Function_4_28B end

    def Function_5_2A0(): pass

    label("Function_5_2A0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x107, 0x80)
    OP_6D(53060, 0, 18180, 0)
    OP_67(0, 7870, -10000, 0)
    OP_6B(4040, 0)
    OP_6C(224000, 0)
    OP_6E(362, 0)

    def lambda_2F4():
        OP_6D(55050, 0, 14970, 5000)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2F4)

    def lambda_30C():
        OP_67(0, 7920, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_30C)

    def lambda_324():
        OP_6B(4180, 5000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_324)

    def lambda_334():
        OP_6C(188000, 5000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_334)
    OP_22(0xE0, 0x1, 0x46)
    OP_43(0x10, 0x0, 0x0, 0x6)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x107, 0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2509)
    NewScene("ED6_DT21/T3172   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_2A0 end

    def Function_6_376(): pass

    label("Function_6_376")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CA")
    OP_22(0x9F, 0x0, 0x32)
    Sleep(800)
    OP_23(0x9F)
    Sleep(500)
    OP_22(0x9F, 0x0, 0x32)
    Sleep(1000)
    OP_23(0x9F)
    Sleep(500)
    OP_22(0x9F, 0x0, 0x32)
    Sleep(600)
    OP_23(0x9F)
    Sleep(500)
    OP_22(0x9F, 0x0, 0x32)
    Sleep(1500)
    OP_23(0x9F)
    Sleep(500)
    Jump("Function_6_376")

    label("loc_3CA")

    Return()

    # Function_6_376 end

    SaveToFile()

Try(main)
