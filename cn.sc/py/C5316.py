from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5316   ._SN',
        MapName             = 'Other',
        Location            = 'C5316.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60064",
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
        "Function_1_D1",           # 01, 1
        "Function_2_D2",           # 02, 2
        "Function_3_281",          # 03, 3
        "Function_4_3E8",          # 04, 4
        "Function_5_4E6",          # 05, 5
        "Function_6_5E4",          # 06, 6
        "Function_7_66B",          # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_BB")
    OP_A3(0x10F0)
    Event(0, 3)
    Jump("loc_D0")

    label("loc_BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_D0")

    Return()

    # Function_0_AA end

    def Function_1_D1(): pass

    label("Function_1_D1")

    Return()

    # Function_1_D1 end

    def Function_2_D2(): pass

    label("Function_2_D2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E9")
    Call(0, 6)
    Call(0, 7)

    label("loc_E9")

    OP_6D(-90, 13760, -140, 0)
    OP_67(0, 7950, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 0, 1760, 1000, 0)
    SetChrPos(0x102, 1000, 1760, 0, 90)
    SetChrPos(0xF8, -1000, 1760, 0, 270)
    SetChrPos(0xF9, 0, 1760, -1000, 180)
    OP_B0(0x0, 0x8C)
    OP_6F(0x0, 230)
    OP_70(0x0, 0x1E)
    ClearMapFlags(0x100000)
    OP_22(0xEB, 0x1, 0x64)

    def lambda_18C():
        OP_6D(-90, 3000, -140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18C)

    def lambda_1A4():
        OP_67(0, 6470, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A4)

    def lambda_1BC():
        OP_6B(3680, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BC)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Sleep(2000)

    def lambda_1E0():
        OP_6D(-90, 2000, -140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E0)

    def lambda_1F8():
        OP_67(0, 5000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F8)

    def lambda_210():
        OP_6B(3900, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_210)
    Sleep(2000)
    Sleep(2000)

    def lambda_22A():
        OP_6D(-90, -9740, -140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22A)

    def lambda_242():
        OP_67(0, 2180, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_242)

    def lambda_25A():
        OP_6B(4320, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25A)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5313   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_D2 end

    def Function_3_281(): pass

    label("Function_3_281")

    EventBegin(0x0)
    OP_6D(0, 1760, 0, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1000, 1760, 0, 90)
    SetChrPos(0x1, 0, 1760, -1000, 180)
    SetChrPos(0x2, 0, 1760, 1000, 0)
    SetChrPos(0x3, -1000, 1760, 0, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 4)), scpexpr(EXPR_END)), "loc_31B")
    Call(0, 4)
    NewScene("ED6_DT21/C5301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3E7")

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 5)), scpexpr(EXPR_END)), "loc_332")
    Call(0, 5)
    NewScene("ED6_DT21/C5300   ._SN", 119, 0, 0)
    IdleLoop()
    Jump("loc_3E7")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 6)), scpexpr(EXPR_END)), "loc_349")
    Call(0, 4)
    NewScene("ED6_DT21/C5303   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3E7")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 7)), scpexpr(EXPR_END)), "loc_360")
    Call(0, 5)
    NewScene("ED6_DT21/C5302   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3E7")

    label("loc_360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 0)), scpexpr(EXPR_END)), "loc_377")
    Call(0, 4)
    NewScene("ED6_DT21/C5304   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3E7")

    label("loc_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 1)), scpexpr(EXPR_END)), "loc_38E")
    Call(0, 5)
    NewScene("ED6_DT21/C5303   ._SN", 114, 0, 0)
    IdleLoop()
    Jump("loc_3E7")

    label("loc_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 2)), scpexpr(EXPR_END)), "loc_3A5")
    Call(0, 4)
    NewScene("ED6_DT21/C5306   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3E7")

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 3)), scpexpr(EXPR_END)), "loc_3BC")
    Call(0, 5)
    NewScene("ED6_DT21/C5305   ._SN", 114, 0, 0)
    IdleLoop()
    Jump("loc_3E7")

    label("loc_3BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 4)), scpexpr(EXPR_END)), "loc_3D3")
    Call(0, 4)
    NewScene("ED6_DT21/C5307   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3E7")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 5)), scpexpr(EXPR_END)), "loc_3E7")
    Call(0, 5)
    NewScene("ED6_DT21/C5306   ._SN", 122, 0, 0)
    IdleLoop()

    label("loc_3E7")

    Return()

    # Function_3_281 end

    def Function_4_3E8(): pass

    label("Function_4_3E8")

    OP_B0(0x0, 0x78)
    OP_6F(0x0, 230)
    OP_70(0x0, 0x1E)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6D(-90, 13760, -140, 0)
    OP_67(0, 7950, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_447():
        OP_6D(-90, 2360, -140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_447)

    def lambda_45F():
        OP_67(0, 6470, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45F)

    def lambda_477():
        OP_6B(3680, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_477)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Sleep(2000)

    def lambda_49B():
        OP_6D(-90, -9740, -140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_49B)

    def lambda_4B3():
        OP_67(0, 2180, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B3)

    def lambda_4CB():
        OP_6B(4320, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4CB)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_4_3E8 end

    def Function_5_4E6(): pass

    label("Function_5_4E6")

    OP_B0(0x0, 0x78)
    OP_6F(0x0, 30)
    OP_70(0x0, 0xE6)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6D(-90, -9740, -140, 0)
    OP_67(0, 2180, -10000, 0)
    OP_6B(4320, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_545():
        OP_6D(-90, 2360, -140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_545)

    def lambda_55D():
        OP_67(0, 6470, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55D)

    def lambda_575():
        OP_6B(3680, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_575)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Sleep(2000)

    def lambda_599():
        OP_6D(-90, 13760, -140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_599)

    def lambda_5B1():
        OP_67(0, 7950, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B1)

    def lambda_5C9():
        OP_6B(3620, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C9)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_5_4E6 end

    def Function_6_5E4(): pass

    label("Function_6_5E4")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_65E"),
        (1, "loc_664"),
        (SWITCH_DEFAULT, "loc_66A"),
    )


    label("loc_65E")

    OP_A2(0x1200)
    Jump("loc_66A")

    label("loc_664")

    OP_A2(0x1201)
    Jump("loc_66A")

    label("loc_66A")

    Return()

    # Function_6_5E4 end

    def Function_7_66B(): pass

    label("Function_7_66B")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
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

    # Function_7_66B end

    SaveToFile()

Try(main)
