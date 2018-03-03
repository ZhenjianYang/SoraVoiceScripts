from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7006   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7006.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60220",
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_CA",           # 01, 1
        "Function_2_CB",           # 02, 2
        "Function_3_221",          # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_BB")
    OP_A3(0x2504)
    Event(0, 2)
    Jump("loc_C9")

    label("loc_BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_C9")
    OP_A3(0x2505)
    Event(0, 3)

    label("loc_C9")

    Return()

    # Function_0_AA end

    def Function_1_CA(): pass

    label("Function_1_CA")

    Return()

    # Function_1_CA end

    def Function_2_CB(): pass

    label("Function_2_CB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_B0(0x0, 0x3C)
    OP_6F(0x0, 0)
    OP_70(0x0, 0xB4)
    SetChrPos(0x0, 0, 3500, 880, 0)
    SetChrPos(0x1, 900, 3500, -70, 0)
    SetChrPos(0x2, -900, 3500, -20, 0)
    SetChrPos(0x3, 0, 3500, -890, 0)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6D(0, -14000, 30, 0)
    OP_67(0, 7480, -10000, 0)
    OP_6B(4120, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)

    def lambda_17A():
        OP_6D(0, 4000, 30, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_17A)

    def lambda_192():
        OP_67(0, 7800, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_192)

    def lambda_1AA():
        OP_6B(3100, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1AA)
    FadeToBright(1000, 0)
    WaitChrThread(0x0, 0x0)
    Sleep(1000)

    def lambda_1CD():
        OP_6D(-100, 19500, -130, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1CD)

    def lambda_1E5():
        OP_67(0, 12300, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1E5)

    def lambda_1FD():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1FD)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M7005   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_CB end

    def Function_3_221(): pass

    label("Function_3_221")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_B0(0x0, 0x3C)
    OP_6F(0x0, 180)
    OP_70(0x0, 0x0)
    SetChrPos(0x0, 0, 3500, -890, 180)
    SetChrPos(0x1, -900, 3500, -20, 180)
    SetChrPos(0x2, 900, 3500, -70, 180)
    SetChrPos(0x3, 0, 3500, 880, 180)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6D(240, 22150, 20, 0)
    OP_67(0, 11770, -10000, 0)
    OP_6B(4190, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)

    def lambda_2D0():
        OP_6D(140, 4000, 20, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2D0)

    def lambda_2E8():
        OP_67(0, 7800, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2E8)

    def lambda_300():
        OP_6B(3100, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_300)
    FadeToBright(1000, 0)
    WaitChrThread(0x0, 0x0)
    Sleep(1000)

    def lambda_323():
        OP_6D(-100, -12550, -130, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_323)

    def lambda_33B():
        OP_67(0, 5010, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_33B)

    def lambda_353():
        OP_6B(4770, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_353)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M7004   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_3_221 end

    SaveToFile()

Try(main)
