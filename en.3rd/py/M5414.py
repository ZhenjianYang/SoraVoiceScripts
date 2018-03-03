from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5414   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5414.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60114",
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
        "Function_2_F8",           # 02, 2
        "Function_3_880",          # 03, 3
        "Function_4_970",          # 04, 4
        "Function_5_A36",          # 05, 5
        "Function_6_B4C",          # 06, 6
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_C2"),
        (SWITCH_DEFAULT, "loc_C9"),
    )


    label("loc_C2")

    Event(0, 3)
    Jump("loc_C9")

    label("loc_C9")

    Return()

    # Function_0_AA end

    def Function_1_CA(): pass

    label("Function_1_CA")

    OP_1B(0x0, 0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7")
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_F7")

    Return()

    # Function_1_CA end

    def Function_2_F8(): pass

    label("Function_2_F8")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -850, -3000, -71360, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D")
    SetChrPos(0x102, 370, -3000, -71400, 0)
    SetChrPos(0xF0, -840, -3000, -72800, 0)
    SetChrPos(0xF1, 410, -3000, -72820, 0)
    Jump("loc_1E2")

    label("loc_15D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1")
    SetChrPos(0x102, 370, -3000, -71400, 0)
    SetChrPos(0xEF, -840, -3000, -72800, 0)
    SetChrPos(0xF1, 410, -3000, -72820, 0)
    Jump("loc_1E2")

    label("loc_1A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2")
    SetChrPos(0x102, 370, -3000, -71400, 0)
    SetChrPos(0xEF, -840, -3000, -72800, 0)
    SetChrPos(0xF0, 410, -3000, -72820, 0)

    label("loc_1E2")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-5000, 21350, -30840, 0)
    OP_67(0, 0, -10000, 0)
    OP_6B(5510, 0)
    OP_6C(33000, 0)
    OP_6E(599, 0)

    def lambda_251():
        OP_6D(500, -3000, -71300, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_251)

    def lambda_269():
        OP_67(0, 7300, -10000, 8500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_269)

    def lambda_281():
        OP_6B(4370, 8500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_281)

    def lambda_291():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_291)

    def lambda_2A1():
        OP_6E(613, 8500)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_2A1)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_C8(0x200, 0x46, "C_PLAC41._CH", 0x0, 0x7D0)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    def lambda_2DE():
        OP_6D(500, -3000, -71300, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2DE)

    def lambda_2F6():
        OP_67(0, 7550, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2F6)

    def lambda_30E():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_30E)

    def lambda_31E():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_31E)

    def lambda_32E():
        OP_6E(383, 8000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_32E)
    Sleep(2000)
    Fade(1000)
    OP_44(0xEE, 0x0)
    OP_44(0xEE, 0x2)
    OP_44(0xEE, 0x3)
    OP_44(0xEF, 0x0)
    OP_44(0xEF, 0x2)
    OP_6D(500, -3000, -71300, 0)
    OP_67(0, 7600, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(45000, 0)
    OP_6E(374, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -200, -3000, -71890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3EC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3EC)

    def lambda_3FE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3FE)

    def lambda_410():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_410)

    def lambda_422():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_422)
    Sleep(1500)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_465")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4CC")

    label("loc_465")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48D")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4CC")

    label("loc_48D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B5")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4CC")

    label("loc_4B5")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4CC")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F9")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_560")

    label("loc_4F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_521")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_560")

    label("loc_521")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_549")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_560")

    label("loc_549")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_560")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58D")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5F4")

    label("loc_58D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B5")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5F4")

    label("loc_5B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DD")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5F4")

    label("loc_5DD")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5F4")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_621")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_688")

    label("loc_621")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_649")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_688")

    label("loc_649")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_671")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_688")

    label("loc_671")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_688")

    Sleep(1500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_75C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D7")

    ChrTalk(    #0
        0x101,
        "#1020F#12PWhere are we...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_705")

    label("loc_6D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_705")

    ChrTalk(    #1
        0x10F,
        "#1443F#12PWhere are we...?\x02",
    )

    CloseMessageWindow()

    label("loc_705")


    ChrTalk(    #2
        0x109,
        (
            "#1067F#6PLooks like our friend's prepped an\x01",
            "arena to have our final battle in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C8")

    label("loc_75C")


    ChrTalk(    #3
        0x109,
        (
            "#1079F#6PWhere are we...?\x02\x03",

            "#1067FLooks like our friend's prepped an\x01",
            "arena to have our final battle in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C8")


    ChrTalk(    #4
        0x102,
        (
            "#1505F#5PIt seems that way.\x02\x03",

            "#1502FI can sense someone waiting for us right at the \x01",
            "top of the staircase―someone really powerful.\x02\x03",

            "Let's go.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B2A)
    OP_AA(65282)
    OP_28(0x3B, 0x4, 0x4)
    OP_28(0x3B, 0x4, 0x8)
    OP_28(0x3B, 0x1, 0x1)
    Sleep(300)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_F8 end

    def Function_3_880(): pass

    label("Function_3_880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_891")
    Call(0, 2)
    Return()

    label("loc_891")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -30, -3000, -71200, 0)
    SetChrPos(0x1, 700, -3000, -72200, 0)
    SetChrPos(0x2, -1080, -3000, -71960, 0)
    SetChrPos(0x3, -290, -3000, -72860, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -200, -3000, -71890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 5)
    OP_AA(65282)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_3_880 end

    def Function_4_970(): pass

    label("Function_4_970")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x2000000)
    Fade(500)
    SetChrPos(0x3, -30, -3000, -71200, 180)
    SetChrPos(0x2, 700, -3000, -72200, 180)
    SetChrPos(0x1, -1080, -3000, -71960, 180)
    SetChrPos(0x0, -290, -3000, -72860, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -200, -3000, -71890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 6)
    OP_AA(65281)
    NewScene("ED6_DT21/M5401   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_4_970 end

    def Function_5_A36(): pass

    label("Function_5_A36")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A5F")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_A53():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A53)

    label("loc_A5F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A88")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_A7C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A7C)

    label("loc_A88")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB1")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_AA5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AA5)

    label("loc_AB1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ADA")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_ACE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_ACE)

    label("loc_ADA")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B06")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_B06")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1D")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_B1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B34")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_B34")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4B")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_B4B")

    Return()

    # Function_5_A36 end

    def Function_6_B4C(): pass

    label("Function_6_B4C")


    def lambda_B52():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B52)

    def lambda_B64():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B64)

    def lambda_B76():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B76)

    def lambda_B88():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B88)
    Sleep(1000)
    Return()

    # Function_6_B4C end

    SaveToFile()

Try(main)
