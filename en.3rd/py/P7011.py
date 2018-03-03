from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'P7011   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P7011.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60211",
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
        "Function_1_14E",          # 01, 1
        "Function_2_14F",          # 02, 2
        "Function_3_DF0",          # 03, 3
        "Function_4_E32",          # 04, 4
        "Function_5_E74",          # 05, 5
        "Function_6_EB6",          # 06, 6
        "Function_7_EF8",          # 07, 7
        "Function_8_1BB4",         # 08, 8
        "Function_9_1BC9",         # 09, 9
        "Function_10_1BF2",        # 0A, 10
        "Function_11_1C1B",        # 0B, 11
        "Function_12_1C44",        # 0C, 12
        "Function_13_2BC9",        # 0D, 13
        "Function_14_2C12",        # 0E, 14
        "Function_15_2C54",        # 0F, 15
        "Function_16_2C9D",        # 10, 16
        "Function_17_2CDF",        # 11, 17
        "Function_18_3083",        # 12, 18
        "Function_19_30B1",        # 13, 19
        "Function_20_30D8",        # 14, 20
        "Function_21_3109",        # 15, 21
        "Function_22_313A",        # 16, 22
        "Function_23_38B9",        # 17, 23
        "Function_24_38D5",        # 18, 24
        "Function_25_38EA",        # 19, 25
        "Function_26_38FF",        # 1A, 26
        "Function_27_3914",        # 1B, 27
        "Function_28_3E0B",        # 1C, 28
        "Function_29_3E39",        # 1D, 29
        "Function_30_3E82",        # 1E, 30
        "Function_31_3EB0",        # 1F, 31
        "Function_32_3ED7",        # 20, 32
        "Function_33_438F",        # 21, 33
        "Function_34_43AB",        # 22, 34
        "Function_35_43C0",        # 23, 35
        "Function_36_43E9",        # 24, 36
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5")
    Event(0, 2)
    Jump("loc_D5")

    label("loc_C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5")
    Event(0, 7)

    label("loc_D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED")
    Event(0, 12)

    label("loc_ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105")
    Event(0, 17)

    label("loc_105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D")
    Event(0, 22)

    label("loc_11D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135")
    Event(0, 27)

    label("loc_135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D")
    Event(0, 32)

    label("loc_14D")

    Return()

    # Function_0_AA end

    def Function_1_14E(): pass

    label("Function_1_14E")

    Return()

    # Function_1_14E end

    def Function_2_14F(): pass

    label("Function_2_14F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 2470, 0, -170, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0")
    SetChrPos(0xEF, 2470, 0, -170, 270)
    SetChrPos(0xF0, 2470, 0, -170, 270)
    SetChrPos(0xF1, 2470, 0, -170, 270)
    Jump("loc_235")

    label("loc_1B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F4")
    SetChrPos(0xF0, 2470, 0, -170, 270)
    SetChrPos(0xEF, 2470, 0, -170, 270)
    SetChrPos(0xF1, 2470, 0, -170, 270)
    Jump("loc_235")

    label("loc_1F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235")
    SetChrPos(0xF1, 2470, 0, -170, 270)
    SetChrPos(0xEF, 2470, 0, -170, 270)
    SetChrPos(0xF0, 2470, 0, -170, 270)

    label("loc_235")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(840, 0, 410, 0)
    OP_67(0, 7060, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(250, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_2BD():
        OP_6D(-3510, 0, 3170, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2BD)
    OP_43(0x109, 0x0, 0x0, 0x3)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30B")
    OP_43(0xEF, 0x0, 0x0, 0x4)
    Sleep(600)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    Jump("loc_368")

    label("loc_30B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33B")
    OP_43(0xF0, 0x0, 0x0, 0x4)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    Jump("loc_368")

    label("loc_33B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_368")
    OP_43(0xF1, 0x0, 0x0, 0x4)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0x5)
    Sleep(500)
    OP_43(0xF0, 0x0, 0x0, 0x6)

    label("loc_368")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x3)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B7")

    ChrTalk(    #0
        0x105,
        "#1168F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_3B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E8")

    ChrTalk(    #1
        0x103,
        "#1527F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_3E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_419")

    ChrTalk(    #2
        0x101,
        "#1011F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_419")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44A")

    ChrTalk(    #3
        0x102,
        "#1500F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_44A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47A")

    ChrTalk(    #4
        0x10B,
        "#210F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_47A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AB")

    ChrTalk(    #5
        0x110,
        "#264F#6PThis room's big...\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_4AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DB")

    ChrTalk(    #6
        0x107,
        "#560F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_4DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50C")

    ChrTalk(    #7
        0x10A,
        "#1310F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_50C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53C")

    ChrTalk(    #8
        0x106,
        "#051F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_53C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56C")

    ChrTalk(    #9
        0x108,
        "#070F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_56C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59C")

    ChrTalk(    #10
        0x10E,
        "#171F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_59C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CD")

    ChrTalk(    #11
        0x104,
        "#1540F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_5CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FD")

    ChrTalk(    #12
        0x10D,
        "#275F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_5FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62A")

    ChrTalk(    #13
        0x10C,
        "#111F#6PWhat's this room?\x02",
    )

    CloseMessageWindow()

    label("loc_62A")


    def lambda_630():
        OP_6D(-4070, 0, 11330, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_630)

    def lambda_648():
        OP_67(0, 7690, -10000, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_648)

    def lambda_660():
        OP_6B(2650, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_660)

    def lambda_670():
        OP_6E(290, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_670)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #14
        0x10F,
        (
            "#1447F#2PThis is the living room, where we used to have all\x01",
            "of our meals.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-4100, 0, 3780, 0)
    OP_67(0, 5630, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(278, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #15
        0x109,
        (
            "#1068F#11PJust don't make the mistake of thinking it was\x01",
            "a warm place like Mercia Orphanage.\x02\x03",

            "#1840FThe matron here was a stubborn old sister who\x01",
            "was strict as could be.\x02\x03",

            "Every mealtime we had to pray so much that our\x01",
            "stomachs had given up on getting fed by the end \x01",
            "of it, and we got yelled at for the tiniest thing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89B")

    ChrTalk(    #16
        0x105,
        "#1165F#6POh, I see...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C2")

    label("loc_89B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C2")

    ChrTalk(    #17
        0x10A,
        "#819F#6POh, really?\x02",
    )

    CloseMessageWindow()

    label("loc_8C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_993")

    ChrTalk(    #18
        0x104,
        (
            "#1541F#6P...That sounds like it must have been\x01",
            "a rather unpleasant upbringing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_990")

    ChrTalk(    #19
        0x10D,
        (
            "#278F#6PHeh. I can easily see you getting yelled at a\x01",
            "LOT under the same circumstances. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_990")

    Jump("loc_A0B")

    label("loc_993")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D1")

    ChrTalk(    #20
        0x101,
        "#1016F#6POuch... That does sound harsh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A0B")

    label("loc_9D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A0B")

    ChrTalk(    #21
        0x10B,
        "#210F#6PWow... That does sound strict.\x02",
    )

    CloseMessageWindow()

    label("loc_A0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A83")

    ChrTalk(    #22
        0x103,
        (
            "#1521F#6PThat sounds like about what you'd expect from\x01",
            "a church-run orphanage, though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF6")

    label("loc_A83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF6")

    ChrTalk(    #23
        0x106,
        (
            "#051F#6PSounds like about what you'd expect from a \x01",
            "church-run orphanage, though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF6")

    label("loc_AF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6D")

    ChrTalk(    #24
        0x108,
        (
            "#070F#6PThat sounds like about what you'd expect from\x01",
            "a church-run orphanage, though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF6")

    label("loc_B6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE5")

    ChrTalk(    #25
        0x102,
        (
            "#1513F#6PThat sounds like about what you'd expect from\x01",
            "a church-run orphanage, though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF6")

    label("loc_BE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6F")

    ChrTalk(    #26
        0x10E,
        (
            "#179F#6PThat is in keeping with the kind of image one \x01",
            "would expect from a church-run orphanage,\x01",
            "though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF6")

    label("loc_C6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF6")

    ChrTalk(    #27
        0x10C,
        (
            "#119F#6PThat is in keeping with the kind of image one \x01",
            "would expect from a church-run orphanage,\x01",
            "though, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D16")

    ChrTalk(    #28
        0x110,
        "#1300F#6P...\x02",
    )

    CloseMessageWindow()

    label("loc_D16")


    ChrTalk(    #29
        0x10F,
        (
            "#1446F#6PYou deserved it all, in my opinion.\x02\x03",

            "#1801FYou never did as you were told and caused\x01",
            "her nothing but grief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        (
            "#1066F#11PEheheh... Okay, I'll admit that's PROBABLY\x01",
            "accurate, but still!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C04)
    OP_28(0x3C, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_14F end

    def Function_3_DF0(): pass

    label("Function_3_DF0")


    def lambda_DF6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF6)
    OP_8E(0xFE, 0x136, 0x0, 0xFFFFFF74, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF4D4, 0x0, 0xE7E, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_DF0 end

    def Function_4_E32(): pass

    label("Function_4_E32")


    def lambda_E38():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E38)
    OP_8E(0xFE, 0x14A, 0x0, 0x10E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF39E, 0x0, 0x88E, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_E32 end

    def Function_5_E74(): pass

    label("Function_5_E74")


    def lambda_E7A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E7A)
    OP_8E(0xFE, 0x136, 0x0, 0xFFFFFF74, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF394, 0x0, 0x2A8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_5_E74 end

    def Function_6_EB6(): pass

    label("Function_6_EB6")


    def lambda_EBC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EBC)
    OP_8E(0xFE, 0x14A, 0x0, 0x10E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF970, 0x0, 0x44C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_EB6 end

    def Function_7_EF8(): pass

    label("Function_7_EF8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -3160, 0, 21490, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F59")
    SetChrPos(0xEF, -3160, 0, 21490, 180)
    SetChrPos(0xF0, -3160, 0, 21490, 180)
    SetChrPos(0xF1, -3160, 0, 21490, 180)
    Jump("loc_FDE")

    label("loc_F59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9D")
    SetChrPos(0xF0, -3160, 0, 21490, 180)
    SetChrPos(0xEF, -3160, 0, 21490, 180)
    SetChrPos(0xF1, -3160, 0, 21490, 180)
    Jump("loc_FDE")

    label("loc_F9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDE")
    SetChrPos(0xF1, -3160, 0, 21490, 180)
    SetChrPos(0xEF, -3160, 0, 21490, 180)
    SetChrPos(0xF0, -3160, 0, 21490, 180)

    label("loc_FDE")

    OP_6D(-4250, 0, 20950, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(315000, 0)
    OP_6E(267, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_70(0x1, 0xF)
    OP_73(0x1)

    def lambda_1047():
        OP_6D(-4110, 0, 18840, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1047)
    OP_43(0x109, 0x0, 0x0, 0x8)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1095")
    OP_43(0xEF, 0x0, 0x0, 0x9)
    Sleep(600)
    OP_43(0xF0, 0x0, 0x0, 0xA)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0xB)
    Jump("loc_10F2")

    label("loc_1095")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C5")
    OP_43(0xF0, 0x0, 0x0, 0x9)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0xA)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0xB)
    Jump("loc_10F2")

    label("loc_10C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F2")
    OP_43(0xF1, 0x0, 0x0, 0x9)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0xA)
    Sleep(500)
    OP_43(0xF0, 0x0, 0x0, 0xB)

    label("loc_10F2")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_72(0x1, 0x8)
    ExitThread()
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x1, 15)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_71(0x1001, 0x0)
    ExitThread()
    WaitChrThread(0xEE, 0x3)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1164")

    ChrTalk(    #31
        0x105,
        "#1168F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_1164")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1196")

    ChrTalk(    #32
        0x103,
        "#1527F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_1196")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C8")

    ChrTalk(    #33
        0x101,
        "#1011F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_11C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11FA")

    ChrTalk(    #34
        0x102,
        "#1500F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_11FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_122B")

    ChrTalk(    #35
        0x10B,
        "#210F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_122B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125D")

    ChrTalk(    #36
        0x110,
        "#264F#11PThis room's big...\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_125D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_128E")

    ChrTalk(    #37
        0x107,
        "#560F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_128E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C0")

    ChrTalk(    #38
        0x10A,
        "#1310F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_12C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F1")

    ChrTalk(    #39
        0x106,
        "#051F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_12F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1322")

    ChrTalk(    #40
        0x108,
        "#070F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_1322")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1353")

    ChrTalk(    #41
        0x10E,
        "#171F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_1353")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1385")

    ChrTalk(    #42
        0x104,
        "#1540F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_1385")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B6")

    ChrTalk(    #43
        0x10D,
        "#275F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_13B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E4")

    ChrTalk(    #44
        0x10C,
        "#111F#11PWhat's this room?\x02",
    )

    CloseMessageWindow()

    label("loc_13E4")

    Sleep(150)
    Fade(500)
    OP_6D(-4790, 0, 4000, 0)
    OP_67(0, 7690, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(315000, 0)
    OP_6E(290, 0)
    OP_6D(-4070, 0, 11330, 4000)
    Sleep(500)

    ChrTalk(    #45
        0x10F,
        (
            "#1447F#3PThis is the living room, where we used to have all\x01",
            "of our meals.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-4100, 0, 18800, 0)
    OP_67(0, 5590, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(315000, 0)
    OP_6E(268, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #46
        0x109,
        (
            "#1068F#6PJust don't make the mistake of thinking it was\x01",
            "a warm place like Mercia Orphanage.\x02\x03",

            "#1840FThe matron here was a stubborn old sister who\x01",
            "was strict as could be.\x02\x03",

            "Every mealtime, we had to pray so much that our\x01",
            "stomachs had given up on getting fed by the end \x01",
            "of it, and we got yelled at for the tiniest thing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1659")

    ChrTalk(    #47
        0x105,
        "#1165F#11POh, I see...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1681")

    label("loc_1659")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1681")

    ChrTalk(    #48
        0x10A,
        "#819F#11POh, really?\x02",
    )

    CloseMessageWindow()

    label("loc_1681")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1754")

    ChrTalk(    #49
        0x104,
        (
            "#1541F#11P...That sounds like it must have been\x01",
            "a rather unpleasant upbringing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1751")

    ChrTalk(    #50
        0x10D,
        (
            "#278F#11PHeh. I can easily see you getting yelled at a\x01",
            "LOT under the same circumstances. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_1751")

    Jump("loc_17CE")

    label("loc_1754")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1793")

    ChrTalk(    #51
        0x101,
        "#1016F#11POuch... That does sound harsh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17CE")

    label("loc_1793")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17CE")

    ChrTalk(    #52
        0x10B,
        "#210F#11PWow... That does sound strict.\x02",
    )

    CloseMessageWindow()

    label("loc_17CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1847")

    ChrTalk(    #53
        0x103,
        (
            "#1521F#11PThat sounds like about what you'd expect from\x01",
            "a church-run orphanage, though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABF")

    label("loc_1847")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18BB")

    ChrTalk(    #54
        0x106,
        (
            "#051F#11PSounds like about what you'd expect from a \x01",
            "church-run orphanage, though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABF")

    label("loc_18BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1933")

    ChrTalk(    #55
        0x108,
        (
            "#070F#11PThat sounds like about what you'd expect from\x01",
            "a church-run orphanage, though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABF")

    label("loc_1933")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19AC")

    ChrTalk(    #56
        0x102,
        (
            "#1513F#11PThat sounds like about what you'd expect from\x01",
            "a church-run orphanage, though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABF")

    label("loc_19AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A37")

    ChrTalk(    #57
        0x10E,
        (
            "#179F#11PThat is in keeping with the kind of image one \x01",
            "would expect from a church-run orphanage,\x01",
            "though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABF")

    label("loc_1A37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ABF")

    ChrTalk(    #58
        0x10C,
        (
            "#119F#11PThat is in keeping with the kind of image one \x01",
            "would expect from a church-run orphanage,\x01",
            "though, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ABF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AE0")

    ChrTalk(    #59
        0x110,
        "#1300F#11P...\x02",
    )

    CloseMessageWindow()

    label("loc_1AE0")


    ChrTalk(    #60
        0x10F,
        (
            "#1446F#11PYou deserved it all, too.\x02\x03",

            "#1801FYou never did as you were told and caused\x01",
            "her nothing but trouble. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x109,
        (
            "#1066F#6PEeheheh... Okay, I'll admit that's PROBABLY\x01",
            "accurate, but still!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C04)
    OP_28(0x3C, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_7_EF8 end

    def Function_8_1BB4(): pass

    label("Function_8_1BB4")

    OP_8F(0xFE, 0xFFFFF56A, 0x0, 0x3E9E, 0x7D0, 0x0)
    Return()

    # Function_8_1BB4 end

    def Function_9_1BC9(): pass

    label("Function_9_1BC9")

    OP_8F(0xFE, 0xFFFFF506, 0x0, 0x4E02, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFF6C8, 0x0, 0x431C, 0x7D0, 0x0)
    Return()

    # Function_9_1BC9 end

    def Function_10_1BF2(): pass

    label("Function_10_1BF2")

    OP_8F(0xFE, 0xFFFFF506, 0x0, 0x4E02, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFF164, 0x0, 0x470E, 0x7D0, 0x0)
    Return()

    # Function_10_1BF2 end

    def Function_11_1C1B(): pass

    label("Function_11_1C1B")

    OP_8F(0xFE, 0xFFFFF506, 0x0, 0x4E02, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFF7B8, 0x0, 0x47AE, 0x7D0, 0x0)
    Return()

    # Function_11_1C1B end

    def Function_12_1C44(): pass

    label("Function_12_1C44")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 2500, 0, -22240, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA5")
    SetChrPos(0xEF, 2500, 0, -22240, 270)
    SetChrPos(0xF0, 2500, 0, -22240, 270)
    SetChrPos(0xF1, 2500, 0, -22240, 270)
    Jump("loc_1D2A")

    label("loc_1CA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE9")
    SetChrPos(0xF0, 2500, 0, -22240, 270)
    SetChrPos(0xEF, 2500, 0, -22240, 270)
    SetChrPos(0xF1, 2500, 0, -22240, 270)
    Jump("loc_1D2A")

    label("loc_1CE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D2A")
    SetChrPos(0xF1, 2500, 0, -22240, 270)
    SetChrPos(0xEF, 2500, 0, -22240, 270)
    SetChrPos(0xF0, 2500, 0, -22240, 270)

    label("loc_1D2A")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-3060, 0, -16110, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(315000, 0)
    OP_6E(245, 0)

    def lambda_1D99():
        OP_6D(-2240, 0, -23650, 5500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1D99)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)
    OP_43(0x109, 0x0, 0x0, 0xD)
    Sleep(800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E00")
    OP_43(0xEF, 0x0, 0x0, 0xE)
    Sleep(900)
    OP_43(0xF0, 0x0, 0x0, 0xF)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x10)
    Jump("loc_1E5D")

    label("loc_1E00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E30")
    OP_43(0xF0, 0x0, 0x0, 0xE)
    Sleep(900)
    OP_43(0xEF, 0x0, 0x0, 0xF)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x10)
    Jump("loc_1E5D")

    label("loc_1E30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E5D")
    OP_43(0xF1, 0x0, 0x0, 0xE)
    Sleep(900)
    OP_43(0xEF, 0x0, 0x0, 0xF)
    Sleep(800)
    OP_43(0xF0, 0x0, 0x0, 0x10)

    label("loc_1E5D")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x3)
    Sleep(300)

    ChrTalk(    #62
        0x109,
        (
            "#1060F#6PAs you can probably guess, this right here's\x01",
            "the kitchen. This is where the older children\x01",
            "of the facility did the cooking.\x02\x03",

            "It was also Ries' favorite place to sneak into \x01",
            "whenever she had a hankerin' for some food.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0x10F,
        "#1441F#11PKevin!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FEB")

    ChrTalk(    #64
        0x101,
        (
            "#1016F#11PAhaha. She did, huh?\x02\x03",

            "#1008FThat makes sense knowing you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_208A")

    ChrTalk(    #65
        0x105,
        (
            "#1165F#11PThat brings back memories of \x01",
            "Matron Theresia's orphanage.\x02\x03",

            "#1168FDaniel and Polly used to do that,\x01",
            "too... Perhaps they still do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_208A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20DE")

    ChrTalk(    #66
        0x10B,
        (
            "#211F#11PRies was a kitchen thief, huh?\x02\x03",

            "#210FThat's kinda cute.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_212C")

    ChrTalk(    #67
        0x102,
        "#1501F#11PHaha... There's a sight I can hardly imagine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_220D")

    label("loc_212C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2179")

    ChrTalk(    #68
        0x10E,
        "#171F#11PHaha... There's a sight I can hardly imagine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_220D")

    label("loc_2179")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21C3")

    ChrTalk(    #69
        0x10D,
        "#275F#11PHeh. There's a sight I can hardly imagine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_220D")

    label("loc_21C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_220D")

    ChrTalk(    #70
        0x10C,
        "#111F#11PHaha... There's a sight I can hardly imagine.\x02",
    )

    CloseMessageWindow()

    label("loc_220D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B6")

    ChrTalk(    #71
        0x10A,
        (
            "#1317F#11PR-Ries used to sneak into the kitchen when\x01",
            "she was a kid?\x02\x03",

            "#1311FThe mental image I'm getting is so darn cute,\x01",
            "I think I'm gonna melt...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2347")

    label("loc_22B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2347")

    ChrTalk(    #72
        0x104,
        (
            "#1545F#11PRies used to sneak into the kitchen when she\x01",
            "was younger, did she?\x02\x03",

            "#1547FNow, that's a mental image like no other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2376")

    ChrTalk(    #73
        0x107,
        "#067F#11PThat's so sweet...\x02",
    )

    CloseMessageWindow()

    label("loc_2376")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23A4")

    ChrTalk(    #74
        0x110,
        "#261F#11PHeehee. How cute.\x02",
    )

    CloseMessageWindow()

    label("loc_23A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C1")

    ChrTalk(    #75
        0x103,
        (
            "#1521F#11PHaha... I feel we're kindred spirits all of a sudden.\x02\x03",

            "#1527FI used to get in trouble with Luci for...borrowing\x01",
            "the troupe leader's liquor and drinking it, too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2492")

    ChrTalk(    #76
        0x101,
        "#1016F#11PY-You did what?\x02",
    )

    CloseMessageWindow()
    Jump("loc_24BE")

    label("loc_2492")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24BE")

    ChrTalk(    #77
        0x104,
        "#1544F#11PWhat was that?\x02",
    )

    CloseMessageWindow()

    label("loc_24BE")

    Jump("loc_2622")

    label("loc_24C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_257C")

    ChrTalk(    #78
        0x108,
        (
            "#071F#11PHaha... Great minds think alike, don't they?\x02\x03",

            "#070FI used to do something pretty similar when I was\x01",
            "younger. Got hell from Kilika a lot because of it,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2622")

    label("loc_257C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2622")

    ChrTalk(    #79
        0x106,
        (
            "#556F#11PHeh. Maybe you're more like me than I thought.\x02\x03",

            "I used to do the same kinda thing when I was a\x01",
            "kid. Got yelled at by Mischa a lot for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2622")

    OP_62(0x10F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #80
        0x10F,
        (
            "#1800F#11PP-Please don't take everything he says at face\x01",
            "value.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x109,
        (
            "#1077F#6PHaha... Well, anyway...\x02\x03",

            "#1840FThis was always Rufina's turf back when she was\x01",
            "still here.\x02\x03",

            "She was always out here around mealtime making\x01",
            "food for me, Ries, and the other kids.\x02\x03",

            "#1075FAfter she left, Ries and I took over her position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10F,
        (
            "#1447F#11PThat brings back memories...\x02\x03",

            "#1801FOf course, then you left, too, leaving me to\x01",
            "handle it all alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x109,
        "#1064F#6PErk...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10F,
        (
            "#1801F#11PThe mere thought aggravates me.\x02\x03",

            "In fact, I think you should whip up something\x01",
            "right now to make up for your selfishness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x109,
        (
            "#1841F#6PYes, ma'am...\x02\x03",

            "#1066FI'll make you something...later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x10F,
        (
            "#1446F#11PThe only thing less reliable than a promise with\x01",
            "'later' attached to the end is one said by you.\x02\x03",

            "#1448FI'm not going to get my hopes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x109,
        "#1840F#6P*sigh* Man, no faith in me, huh?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C0")

    ChrTalk(    #88
        0x101,
        "#1016F#11PAhaha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_29E5")

    label("loc_29C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29E5")

    ChrTalk(    #89
        0x10B,
        "#211F#11PAhaha...\x02",
    )

    CloseMessageWindow()

    label("loc_29E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A0E")

    ChrTalk(    #90
        0x107,
        "#061F#11PHeehee...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A35")

    label("loc_2A0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A35")

    ChrTalk(    #91
        0x105,
        "#1165F#11PHeehee...\x02",
    )

    CloseMessageWindow()

    label("loc_2A35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A5C")

    ChrTalk(    #92
        0x110,
        "#1306F#11PHeehee...\x02",
    )

    CloseMessageWindow()

    label("loc_2A5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A7E")

    ChrTalk(    #93
        0x104,
        "#1541F#11PHeh.\x02",
    )

    CloseMessageWindow()

    label("loc_2A7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AA6")

    ChrTalk(    #94
        0x102,
        "#1501F#11PHaha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ACA")

    label("loc_2AA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ACA")

    ChrTalk(    #95
        0x10A,
        "#811F#11PHaha...\x02",
    )

    CloseMessageWindow()

    label("loc_2ACA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AF1")

    ChrTalk(    #96
        0x108,
        "#071F#11PHaha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B3C")

    label("loc_2AF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B18")

    ChrTalk(    #97
        0x10E,
        "#171F#11PHaha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B3C")

    label("loc_2B18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B3C")

    ChrTalk(    #98
        0x10C,
        "#111F#11PHaha...\x02",
    )

    CloseMessageWindow()

    label("loc_2B3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B67")

    ChrTalk(    #99
        0x103,
        "#1527F#11POh, boy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BB8")

    label("loc_2B67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B91")

    ChrTalk(    #100
        0x106,
        "#556F#11POh, boy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BB8")

    label("loc_2B91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BB8")

    ChrTalk(    #101
        0x10D,
        "#277F#11POh, boy...\x02",
    )

    CloseMessageWindow()

    label("loc_2BB8")

    OP_A2(0x2C05)
    OP_28(0x3C, 0x1, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_12_1C44 end

    def Function_13_2BC9(): pass

    label("Function_13_2BC9")


    def lambda_2BCF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BCF)
    OP_8F(0xFE, 0x1CC, 0x0, 0xFFFFA894, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_8F(0xFE, 0xFFFFFB32, 0x0, 0xFFFF9872, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_2BC9 end

    def Function_14_2C12(): pass

    label("Function_14_2C12")


    def lambda_2C18():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C18)
    OP_8F(0xFE, 0x1CC, 0x0, 0xFFFFA894, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_8F(0xFE, 0xFFFFFC9A, 0x0, 0xFFFF9E30, 0x7D0, 0x0)
    Return()

    # Function_14_2C12 end

    def Function_15_2C54(): pass

    label("Function_15_2C54")


    def lambda_2C5A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C5A)
    OP_8F(0xFE, 0x1CC, 0x0, 0xFFFFA894, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 0)
    OP_8F(0xFE, 0xFFFFF8C6, 0x0, 0xFFFFA40C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_15_2C54 end

    def Function_16_2C9D(): pass

    label("Function_16_2C9D")


    def lambda_2CA3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CA3)
    OP_8F(0xFE, 0x1CC, 0x0, 0xFFFFA894, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_8F(0xFE, 0xFFFFFF56, 0x0, 0xFFFFA272, 0x7D0, 0x0)
    Return()

    # Function_16_2C9D end

    def Function_17_2CDF(): pass

    label("Function_17_2CDF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -31690, 0, 6820, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D40")
    SetChrPos(0xEF, -31690, 0, 6820, 270)
    SetChrPos(0xF0, -31690, 0, 6820, 270)
    SetChrPos(0xF1, -31690, 0, 6820, 270)
    Jump("loc_2DC5")

    label("loc_2D40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D84")
    SetChrPos(0xF0, -31690, 0, 6820, 270)
    SetChrPos(0xEF, -31690, 0, 6820, 270)
    SetChrPos(0xF1, -31690, 0, 6820, 270)
    Jump("loc_2DC5")

    label("loc_2D84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC5")
    SetChrPos(0xF1, -31690, 0, 6820, 270)
    SetChrPos(0xEF, -31690, 0, 6820, 270)
    SetChrPos(0xF0, -31690, 0, 6820, 270)

    label("loc_2DC5")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-36680, 0, 8370, 0)
    OP_67(0, 6010, -10000, 0)
    OP_6B(2660, 0)
    OP_6C(315000, 0)
    OP_6E(257, 0)
    FadeToBright(1000, 0)
    Sleep(300)
    OP_43(0x109, 0x0, 0x0, 0x12)
    Sleep(800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E78")
    OP_43(0xEF, 0x0, 0x0, 0x13)
    Sleep(900)
    OP_43(0xF0, 0x0, 0x0, 0x14)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x15)
    Jump("loc_2ED5")

    label("loc_2E78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EA8")
    OP_43(0xF0, 0x0, 0x0, 0x13)
    Sleep(900)
    OP_43(0xEF, 0x0, 0x0, 0x14)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x15)
    Jump("loc_2ED5")

    label("loc_2EA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED5")
    OP_43(0xF1, 0x0, 0x0, 0x13)
    Sleep(900)
    OP_43(0xEF, 0x0, 0x0, 0x14)
    Sleep(800)
    OP_43(0xF0, 0x0, 0x0, 0x15)

    label("loc_2ED5")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #102
        0x10F,
        (
            "#1445F#6PThis was the matron's room...\x01",
            "No one's here now, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x109,
        "#1065F#5PYeah...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(500)

    ChrTalk(    #104
        0x109,
        (
            "#1060F#5PBy the way, Ries...\x02\x03",

            "How is the matron these days?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10F,
        (
            "#1447F#6PShe's fine... Her injuries weren't lasting.\x02\x03",

            "#1445FShe hasn't had the energy she used to ever\x01",
            "since retiring, unfortunately.\x02\x03",

            "#1802FShe really wanted to see you again, Kevin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x109,
        "#1067F#5PShe did, huh?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C06)
    OP_28(0x3C, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_17_2CDF end

    def Function_18_3083(): pass

    label("Function_18_3083")


    def lambda_3089():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3089)
    OP_8F(0xFE, 0xFFFF7068, 0x0, 0x1BA8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_3083 end

    def Function_19_30B1(): pass

    label("Function_19_30B1")


    def lambda_30B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30B7)
    OP_8F(0xFE, 0xFFFF769E, 0x0, 0x1C84, 0x7D0, 0x0)
    Return()

    # Function_19_30B1 end

    def Function_20_30D8(): pass

    label("Function_20_30D8")

    SetChrFlags(0xFE, 0x4)

    def lambda_30E3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30E3)
    OP_8F(0xFE, 0xFFFF7C34, 0x0, 0x1856, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_20_30D8 end

    def Function_21_3109(): pass

    label("Function_21_3109")

    SetChrFlags(0xFE, 0x4)

    def lambda_3114():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3114)
    OP_8F(0xFE, 0xFFFF7CCA, 0x0, 0x1D88, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_21_3109 end

    def Function_22_313A(): pass

    label("Function_22_313A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -70500, 0, 8010, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_319B")
    SetChrPos(0xEF, -70500, 0, 8010, 90)
    SetChrPos(0xF0, -70500, 0, 8010, 90)
    SetChrPos(0xF1, -70500, 0, 8010, 90)
    Jump("loc_3220")

    label("loc_319B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31DF")
    SetChrPos(0xF0, -70500, 0, 8010, 90)
    SetChrPos(0xEF, -70500, 0, 8010, 90)
    SetChrPos(0xF1, -70500, 0, 8010, 90)
    Jump("loc_3220")

    label("loc_31DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3220")
    SetChrPos(0xF1, -70500, 0, 8010, 90)
    SetChrPos(0xEF, -70500, 0, 8010, 90)
    SetChrPos(0xF0, -70500, 0, 8010, 90)

    label("loc_3220")

    OP_6D(-69000, 0, 8800, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(256, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_70(0x4, 0xF)
    OP_73(0x1)
    Sleep(300)

    def lambda_328D():
        OP_6D(-66580, 0, 8800, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_328D)
    OP_43(0x109, 0x0, 0x0, 0x17)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32DB")
    OP_43(0xEF, 0x0, 0x0, 0x18)
    Sleep(600)
    OP_43(0xF0, 0x0, 0x0, 0x19)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0x1A)
    Jump("loc_3338")

    label("loc_32DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_330B")
    OP_43(0xF0, 0x0, 0x0, 0x18)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0x19)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0x1A)
    Jump("loc_3338")

    label("loc_330B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3338")
    OP_43(0xF1, 0x0, 0x0, 0x18)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0x19)
    Sleep(500)
    OP_43(0xF0, 0x0, 0x0, 0x1A)

    label("loc_3338")

    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    OP_23(0x6)
    OP_6F(0x4, 15)
    OP_70(0x4, 0x0)
    OP_23(0x6)
    OP_73(0x4)
    OP_71(0x1004, 0x0)
    ExitThread()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x3)
    Sleep(300)

    ChrTalk(    #107
        0x109,
        (
            "#1060F#12PThis here's the kids' bedroom.\x02\x03",

            "I slept here back when I was first taken in\x01",
            "before graduating to the boys' bedroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10F,
        (
            "#1447F#5PYou never really did mix well with the other\x01",
            "children.\x02\x03",

            "#1806FRufina had such a hard time trying to get you to\x01",
            "make friends with them... It was a real ordeal\x01",
            "for her, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x109,
        (
            "#1067F#12PYeah. I know...\x02\x03",

            "#1841FI was like a little hedgehog who didn't want to\x01",
            "let anyone get near back then... I feel sorry for\x01",
            "everyone who had to put up with me.\x02\x03",

            "#1840FI'm still amazed you even bothered trying to be\x01",
            "friendly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x10F,
        (
            "#1447F#5PWell, I knew you were only playing tough.\x02\x03",

            "#1442FLike that time with Rufina and the chocolate.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #111
        0x109,
        "#1069F#12P#3SStop! We're not hearing that story here!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36BC")

    ChrTalk(    #112
        0x101,
        "#1016F#5P(Now I'm really curious...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F3")

    label("loc_36BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36F3")

    ChrTalk(    #113
        0x10B,
        "#210F#5P(Now I'm really curious...)\x02",
    )

    CloseMessageWindow()

    label("loc_36F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_372D")

    ChrTalk(    #114
        0x107,
        "#067F#5P(I-I wonder what happened?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3854")

    label("loc_372D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3770")

    ChrTalk(    #115
        0x110,
        "#1306F#5P(Heehee... Now I'm really curious.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3854")

    label("loc_3770")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37A9")

    ChrTalk(    #116
        0x102,
        "#1504F#5P(I wonder what happened?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3854")

    label("loc_37A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37E5")

    ChrTalk(    #117
        0x10A,
        "#819F#5P(N-Now I'm really curious...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3854")

    label("loc_37E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_381E")

    ChrTalk(    #118
        0x105,
        "#1165F#5P(I wonder what happened?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3854")

    label("loc_381E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3854")

    ChrTalk(    #119
        0x103,
        "#1527F#5P(I wonder what happened?)\x02",
    )

    CloseMessageWindow()

    label("loc_3854")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38A8")

    ChrTalk(    #120
        0x104,
        (
            "#1547F#5P(Well, he certainly knows how to pique\x01",
            "my curiosity...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A8")

    OP_A2(0x2C07)
    OP_28(0x3C, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_22_313A end

    def Function_23_38B9(): pass

    label("Function_23_38B9")

    OP_8F(0xFE, 0xFFFF07F4, 0x0, 0x1D7E, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_23_38B9 end

    def Function_24_38D5(): pass

    label("Function_24_38D5")

    OP_8F(0xFE, 0xFFFF01A0, 0x0, 0x1CC0, 0x7D0, 0x0)
    Return()

    # Function_24_38D5 end

    def Function_25_38EA(): pass

    label("Function_25_38EA")

    OP_8F(0xFE, 0xFFFEFC50, 0x0, 0x1B80, 0x7D0, 0x0)
    Return()

    # Function_25_38EA end

    def Function_26_38FF(): pass

    label("Function_26_38FF")

    OP_8F(0xFE, 0xFFFEFC8C, 0x0, 0x20BC, 0x7D0, 0x0)
    Return()

    # Function_26_38FF end

    def Function_27_3914(): pass

    label("Function_27_3914")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -31770, 0, -21180, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3975")
    SetChrPos(0xEF, -31770, 0, -21180, 270)
    SetChrPos(0xF0, -31770, 0, -21180, 270)
    SetChrPos(0xF1, -31770, 0, -21180, 270)
    Jump("loc_39FA")

    label("loc_3975")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B9")
    SetChrPos(0xF0, -31770, 0, -21180, 270)
    SetChrPos(0xEF, -31770, 0, -21180, 270)
    SetChrPos(0xF1, -31770, 0, -21180, 270)
    Jump("loc_39FA")

    label("loc_39B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39FA")
    SetChrPos(0xF1, -31770, 0, -21180, 270)
    SetChrPos(0xEF, -31770, 0, -21180, 270)
    SetChrPos(0xF0, -31770, 0, -21180, 270)

    label("loc_39FA")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-36130, 0, -20170, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(315000, 0)
    OP_6E(264, 0)
    FadeToBright(1000, 0)
    Sleep(300)
    OP_43(0x109, 0x0, 0x0, 0x1C)
    Sleep(800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AAD")
    OP_43(0xEF, 0x0, 0x0, 0x1D)
    Sleep(900)
    OP_43(0xF0, 0x0, 0x0, 0x1E)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x1F)
    Jump("loc_3B0A")

    label("loc_3AAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ADD")
    OP_43(0xF0, 0x0, 0x0, 0x1D)
    Sleep(900)
    OP_43(0xEF, 0x0, 0x0, 0x1E)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x1F)
    Jump("loc_3B0A")

    label("loc_3ADD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B0A")
    OP_43(0xF1, 0x0, 0x0, 0x1D)
    Sleep(900)
    OP_43(0xEF, 0x0, 0x0, 0x1E)
    Sleep(800)
    OP_43(0xF0, 0x0, 0x0, 0x1F)

    label("loc_3B0A")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #121
        0x109,
        (
            "#1065F#5PThis is the boys' bedroom, where I slept until\x01",
            "I was about ten years old.\x02\x03",

            "#1840FTechnically, the boys and girls weren't supposed\x01",
            "to enter one another's bedrooms...\x02\x03",

            "That never stopped Ries here from doing it all the\x01",
            "time, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x10F,
        (
            "#1801F#6PWhat he neglects to mention is that it was\x01",
            "his fault I did so.\x02\x03",

            "What else was I supposed to do when he\x01",
            "slept in every morning he was on cleaning\x01",
            "duty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x109,
        (
            "#1079F#5PW-Well, you could've just knocked on the door \x01",
            "until I got up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x10F,
        (
            "#1443F#6PBut then I'd disturb the other boys who were\x01",
            "sleeping, which would have been unfair.\x01",
            "They weren't the ones shirking their duties.\x02\x03",

            "#1446FIt was one hundred percent your fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x109,
        "#1840F#5P...Fine, fine. Whatever you say.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C08)
    OP_28(0x3C, 0x1, 0x40)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_27_3914 end

    def Function_28_3E0B(): pass

    label("Function_28_3E0B")


    def lambda_3E11():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E11)
    OP_8F(0xFE, 0xFFFF72DE, 0x0, 0xFFFFAAD8, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_28_3E0B end

    def Function_29_3E39(): pass

    label("Function_29_3E39")


    def lambda_3E3F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E3F)
    OP_8F(0xFE, 0xFFFF7E14, 0x0, 0xFFFFACFE, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 0)
    OP_8F(0xFE, 0xFFFF7982, 0x0, 0xFFFFA8D0, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_29_3E39 end

    def Function_30_3E82(): pass

    label("Function_30_3E82")


    def lambda_3E88():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E88)
    OP_8F(0xFE, 0xFFFF782E, 0x0, 0xFFFFAFD8, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_30_3E82 end

    def Function_31_3EB0(): pass

    label("Function_31_3EB0")


    def lambda_3EB6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EB6)
    OP_8F(0xFE, 0xFFFF7CAC, 0x0, 0xFFFFAB6E, 0x7D0, 0x0)
    Return()

    # Function_31_3EB0 end

    def Function_32_3ED7(): pass

    label("Function_32_3ED7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -70500, 0, -22050, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F38")
    SetChrPos(0xEF, -70500, 0, -22050, 90)
    SetChrPos(0xF0, -70500, 0, -22050, 90)
    SetChrPos(0xF1, -70500, 0, -22050, 90)
    Jump("loc_3FBD")

    label("loc_3F38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F7C")
    SetChrPos(0xF0, -70500, 0, -22050, 90)
    SetChrPos(0xEF, -70500, 0, -22050, 90)
    SetChrPos(0xF1, -70500, 0, -22050, 90)
    Jump("loc_3FBD")

    label("loc_3F7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FBD")
    SetChrPos(0xF1, -70500, 0, -22050, 90)
    SetChrPos(0xEF, -70500, 0, -22050, 90)
    SetChrPos(0xF0, -70500, 0, -22050, 90)

    label("loc_3FBD")

    OP_6D(-69000, 0, -21100, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(263, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_72(0x1005, 0x0)
    ExitThread()
    OP_6F(0x5, 0)
    OP_70(0x5, 0xF)
    OP_73(0x5)
    Sleep(300)

    def lambda_402A():
        OP_6D(-66970, 0, -21510, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_402A)
    OP_43(0x109, 0x0, 0x0, 0x21)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4078")
    OP_43(0xEF, 0x0, 0x0, 0x22)
    Sleep(600)
    OP_43(0xF0, 0x0, 0x0, 0x23)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0x24)
    Jump("loc_40D5")

    label("loc_4078")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40A8")
    OP_43(0xF0, 0x0, 0x0, 0x22)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0x23)
    Sleep(500)
    OP_43(0xF1, 0x0, 0x0, 0x24)
    Jump("loc_40D5")

    label("loc_40A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40D5")
    OP_43(0xF1, 0x0, 0x0, 0x22)
    Sleep(600)
    OP_43(0xEF, 0x0, 0x0, 0x23)
    Sleep(500)
    OP_43(0xF0, 0x0, 0x0, 0x24)

    label("loc_40D5")

    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    OP_23(0x6)
    OP_6F(0x5, 15)
    OP_70(0x5, 0x0)
    OP_23(0x6)
    OP_73(0x5)
    OP_71(0x1005, 0x0)
    ExitThread()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x3)
    Sleep(300)

    ChrTalk(    #126
        0x109,
        (
            "#1840F#12PThis here's the girls' bedroom.\x02\x03",

            "The place where Rufina spent her nights.\x01",
            "Same for you eventually, too, Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x10F,
        (
            "#1442F#5PI even used to sleep with her from time to time.\x02\x03",

            "#1447FHer bed was always cozy and smelled really nice.\x01",
            "It was much nicer than sleeping in my own.\x02\x03",

            "After she left here, her bed became mine.\x02\x03",

            "#1448FI bet you were jealous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x109,
        (
            "#1077F#12PHaha. You bet.\x02\x03",

            "#1078FI was at the time, I'll admit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x10F,
        (
            "#1803F#5POh... I thought you'd be a bit more flustered\x01",
            "than that.\x02\x03",

            "#1446FI shouldn't have bothered saying anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #130
        0x109,
        "#1068F#12PGive me a break...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C09)
    OP_28(0x3C, 0x1, 0x80)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_32_3ED7 end

    def Function_33_438F(): pass

    label("Function_33_438F")

    OP_8F(0xFE, 0xFFFF0650, 0x0, 0xFFFFA6B4, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_33_438F end

    def Function_34_43AB(): pass

    label("Function_34_43AB")

    OP_8F(0xFE, 0xFFFEFF98, 0x0, 0xFFFFA6DC, 0x7D0, 0x0)
    Return()

    # Function_34_43AB end

    def Function_35_43C0(): pass

    label("Function_35_43C0")

    OP_8F(0xFE, 0xFFFEF462, 0x0, 0xFFFFA90C, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFEFBC4, 0x0, 0xFFFFA448, 0x7D0, 0x0)
    Return()

    # Function_35_43C0 end

    def Function_36_43E9(): pass

    label("Function_36_43E9")

    OP_8F(0xFE, 0xFFFEFA98, 0x0, 0xFFFFA9B6, 0x7D0, 0x0)
    Return()

    # Function_36_43E9 end

    SaveToFile()

Try(main)
