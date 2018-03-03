from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7406   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7406.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        'R-Tycoon',                             # 9
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
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_CA",           # 00, 0
        "Function_1_11E",          # 01, 1
        "Function_2_125",          # 02, 2
        "Function_3_219A",         # 03, 3
        "Function_4_21B6",         # 04, 4
        "Function_5_222B",         # 05, 5
        "Function_6_2460",         # 06, 6
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_E0")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_11D")

    label("loc_E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_FF")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)
    Jump("loc_11D")

    label("loc_FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_11D")

    Return()

    # Function_0_CA end

    def Function_1_11E(): pass

    label("Function_1_11E")

    OP_71(0x408, 0x0)
    ExitThread()
    Return()

    # Function_1_11E end

    def Function_2_125(): pass

    label("Function_2_125")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(246, 0x40, 0x2)
    OP_E0(246, 0x41, 0x3)
    OP_E0(247, 0x42, 0x2)
    OP_E0(247, 0x43, 0x3)
    OP_E0(248, 0x44, 0x2)
    OP_E0(248, 0x45, 0x3)
    OP_E0(249, 0x46, 0x2)
    OP_E0(249, 0x47, 0x3)
    SetChrPos(0xF6, -840, 0, -10480, 0)
    SetChrPos(0xF7, 550, 0, -10450, 0)
    SetChrPos(0xF8, -1260, 0, -12070, 0)
    SetChrPos(0xF9, 610, 0, -12180, 0)
    OP_6D(5130, -28700, 26260, 0)
    OP_67(0, 4490, -10000, 0)
    OP_6B(7270, 0)
    OP_6C(45000, 0)
    OP_6E(672, 0)

    def lambda_1E0():
        OP_6D(5130, -100, 26260, 8000)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_1E0)

    def lambda_1F8():
        OP_67(0, 6470, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1F8)

    def lambda_210():
        OP_8E(0xFE, 0xFFFFFB5A, 0x0, 0x2F9E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF6, 0, lambda_210)
    Sleep(100)

    def lambda_230():
        OP_8E(0xFE, 0x212, 0x0, 0x2FBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_230)
    Sleep(100)

    def lambda_250():
        OP_8E(0xFE, 0xFFFFF948, 0x0, 0x2882, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_250)
    Sleep(100)

    def lambda_270():
        OP_8E(0xFE, 0x1EA, 0x0, 0x2850, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_270)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xF6, 0x1)
    WaitChrThread(0xF7, 0x1)

    def lambda_29F():
        OP_6B(7500, 3000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_29F)

    def lambda_2AF():
        OP_6E(700, 3000)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2AF)
    WaitChrThread(0xF6, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Fade(1000)
    OP_6D(1100, 0, 12850, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(45000, 0)
    OP_6E(275, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37C")

    ChrTalk(    #0
        0x101,
        (
            "#1015F#5PWow... This room's huge.\x02\x03",

            "We must be at the end of this wing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_37C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6")

    ChrTalk(    #1
        0x102,
        (
            "#1505F#5PWe must be at the end of this wing.\x02\x03",

            "#1503FIt certainly is vast, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_3E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_452")

    ChrTalk(    #2
        0x10B,
        (
            "#210F#5PWow... This room's huge.\x02\x03",

            "I'm guessing this is the last part\x01",
            "of the building.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_452")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D2")

    ChrTalk(    #3
        0x110,
        (
            "#261F#5PLooks like we've made it to the end of\x01",
            "this wing.\x02\x03",

            "#265FThis room's suspiciously empty, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_4D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_538")

    ChrTalk(    #4
        0x107,
        (
            "#560F#5PI guess this is the end of this wing?\x02\x03",

            "This room sure is big, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_538")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_596")

    ChrTalk(    #5
        0x10A,
        (
            "#818F#5PWow... This room's huge.\x02\x03",

            "I guess this is the end of this wing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_596")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F5")

    ChrTalk(    #6
        0x105,
        (
            "#1163F#5PThis room is gigantic...\x02\x03",

            "I guess this is the end of this wing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_5F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65A")

    ChrTalk(    #7
        0x103,
        (
            "#1523F#5PWow... This room's huge.\x02\x03",

            "#1522FI guess this is the end of this wing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_65A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B3")

    ChrTalk(    #8
        0x106,
        (
            "#555F#5PThis room's huge...\x02\x03",

            "I guess this is the end of this wing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_6B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71C")

    ChrTalk(    #9
        0x108,
        (
            "#074F#5PWe must be at the end of this wing.\x02\x03",

            "#070FThis room sure is big, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_71C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_782")

    ChrTalk(    #10
        0x10E,
        (
            "#176F#5PThis room certainly is big...\x02\x03",

            "#178FWe must be at the end of this wing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_782")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_802")

    ChrTalk(    #11
        0x104,
        (
            "#1545F#5PWe must be at the end of this wing.\x02\x03",

            "#1540FI'm amazed at how big this room itself is,\x01",
            "however...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_802")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_868")

    ChrTalk(    #12
        0x10D,
        (
            "#272F#5PThis room certainly is big...\x02\x03",

            "#277FWe must be at the end of this wing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_868")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EE")

    ChrTalk(    #13
        0x10C,
        (
            "#119F#5PWe must be at the end of this particular wing.\x02\x03",

            "#110FI'm amazed at how big this room itself is,\x01",
            "however...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_944")

    ChrTalk(    #14
        0x101,
        (
            "#1016F#5PHeehee. I wonder how well my voice would echo\x01",
            "in here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_944")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A1")

    ChrTalk(    #15
        0x102,
        (
            "#1503F#5P(Why is it so vast, though? Surely there must be\x01",
            "a reason...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_9A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EE")

    ChrTalk(    #16
        0x10B,
        "#210F#5PI wonder why it was made to be so big, though?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_9EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A52")

    ChrTalk(    #17
        0x110,
        (
            "#267F#5P(I wonder why it's so vast, though? Surely there\x01",
            "must be a reason...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_A52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8D")

    ChrTalk(    #18
        0x107,
        "#062F#5P(Why is it so vast, though?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_A8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF9")

    ChrTalk(    #19
        0x10A,
        (
            "#819F#5PBeing in a room this wide and open just makes\x01",
            "me want to run around shouting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_AF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B56")

    ChrTalk(    #20
        0x105,
        (
            "#1162F#5P(Why is it so vast, though? Surely there must be\x01",
            "a reason...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_B56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA1")

    ChrTalk(    #21
        0x103,
        "#1522F#5P(Hmm... I wonder why it's so vast, though.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_BA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C00")

    ChrTalk(    #22
        0x106,
        (
            "#552F#5P(You wouldn't make a room this huge without\x01",
            "a reason, though...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_C00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4A")

    ChrTalk(    #23
        0x108,
        "#072F#5P(Hmm... I wonder why it's so vast, though.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_C4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C94")

    ChrTalk(    #24
        0x10E,
        "#178F#5P(Hmm... I wonder why it's so vast, though.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_C94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDF")

    ChrTalk(    #25
        0x104,
        "#1542F#5P(Hmm... I wonder why it's so vast, though.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_CDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D29")

    ChrTalk(    #26
        0x10D,
        "#276F#5P(Hmm... I wonder why it's so vast, though.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8C")

    label("loc_D29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8C")

    ChrTalk(    #27
        0x10C,
        (
            "#112F#5P(Surely one wouldn't make a room this vast\x01",
            "without a reason, though...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8C")

    Sleep(300)
    OP_20(0x7D0)
    OP_22(0x11F, 0x0, 0x50)

    def lambda_DA1():
        OP_7C(0x5, 0x5, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF6, 3, lambda_DA1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE0")
    OP_62(0xF6, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E47")

    label("loc_DE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E08")
    OP_62(0xF6, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E47")

    label("loc_E08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E30")
    OP_62(0xF6, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E47")

    label("loc_E30")

    OP_62(0xF6, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E47")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E74")
    OP_62(0xF7, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EDB")

    label("loc_E74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9C")
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EDB")

    label("loc_E9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC4")
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EDB")

    label("loc_EC4")

    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_EDB")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F08")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F6F")

    label("loc_F08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F30")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F6F")

    label("loc_F30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F58")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F6F")

    label("loc_F58")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F6F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9C")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1003")

    label("loc_F9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC4")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1003")

    label("loc_FC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEC")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1003")

    label("loc_FEC")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1003")

    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0x3)
    Sleep(650)
    OP_B0(0x8, 0xF)
    OP_6F(0x8, 500)
    OP_70(0x8, 0x208)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105E")

    ChrTalk(    #28
        0x101,
        "#1020F#6PTh-That sounded like...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_105E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108D")

    ChrTalk(    #29
        0x102,
        "#1506F#6PWhat was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_108D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D8")

    ChrTalk(    #30
        0x110,
        "#1306F#6POh, my... That was no ordinary monster cry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_10D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1109")

    ChrTalk(    #31
        0x10B,
        "#216F#6PWh-What was THAT?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_1109")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1140")

    ChrTalk(    #32
        0x107,
        "#065F#6PTh-That sounded like...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_1140")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1173")

    ChrTalk(    #33
        0x10A,
        "#1317F#6PThat was a monster!\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_1173")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A6")

    ChrTalk(    #34
        0x105,
        "#1162F#6PThat was a monster!\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_11A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D9")

    ChrTalk(    #35
        0x103,
        "#1523F#6PThat was a monster!\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_11D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1215")

    ChrTalk(    #36
        0x106,
        "#055F#6PYou have gotta be KIDDING me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_1215")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1245")

    ChrTalk(    #37
        0x108,
        "#072F#6PIt couldn't be...\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_1245")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1279")

    ChrTalk(    #38
        0x10E,
        "#173F#6PThat sounded like...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_1279")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C0")

    ChrTalk(    #39
        0x104,
        "#1544F#6PI have a very bad feeling about this...\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_12C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F1")

    ChrTalk(    #40
        0x10D,
        "#273F#6PWhat was that...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_12F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133B")

    ChrTalk(    #41
        0x10C,
        "#112F#6PThat didn't sound like any ordinary monster...\x02",
    )

    CloseMessageWindow()

    label("loc_133B")

    Sleep(300)
    OP_1D(0x9A)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x416, 0x0)
    ExitThread()
    OP_82(0x83, 0x0)
    OP_82(0x85, 0x0)
    OP_6D(-4019, 20000, 30250, 0)
    OP_67(0, 10600, -10000, 0)
    OP_6B(9630, 0)
    OP_6C(134000, 0)
    OP_6E(200, 0)

    def lambda_13B1():
        OP_6D(1680, 1600, 24890, 10000)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_13B1)

    def lambda_13C9():
        OP_67(0, 4030, -10000, 10000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_13C9)

    def lambda_13E1():
        OP_6B(9180, 10000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_13E1)

    def lambda_13F1():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_13F1)

    def lambda_1401():
        OP_6E(186, 10000)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1401)
    SetChrPos(0x10, 0, 30000, 30000, 180)
    OP_A1(0x10, 0x8)
    OP_72(0x408, 0x0)
    ExitThread()

    def lambda_142D():
        OP_8F(0xFE, 0xFFFFF448, 0x1B58, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_142D)
    Sleep(2000)

    def lambda_144D():
        OP_8F(0xFE, 0x7D0, 0x1B58, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_144D)
    WaitChrThread(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_72(0x2008, 0x0)
    ExitThread()
    OP_D8(0x8, 0x3E8)
    OP_6F(0x8, 520)
    OP_70(0x8, 0x212)

    def lambda_1489():
        OP_8C(0xFE, 200, 100)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1489)

    def lambda_1497():
        OP_8F(0xFE, 0x1388, 0x0, 0x7530, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1497)
    WaitChrThread(0x10, 0x1)
    OP_23(0x113)
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0x1388, 0x5DC)
    OP_73(0x8)
    OP_6F(0x8, 530)
    OP_70(0x8, 0x230)
    OP_73(0x8)
    OP_71(0x2008, 0x0)
    ExitThread()
    OP_6F(0x8, 5)
    OP_70(0x8, 0x37)
    WaitChrThread(0xF6, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Fade(500)
    OP_6D(0, 1600, 27240, 0)
    OP_67(0, 1830, -10000, 0)
    OP_6B(5800, 0)
    OP_6C(357000, 0)
    OP_6E(260, 0)

    def lambda_154E():
        OP_6B(6350, 3000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_154E)
    OP_72(0x414, 0x0)
    ExitThread()
    OP_72(0x416, 0x0)
    ExitThread()
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x10, 7000, 0, 30000, 205)
    SetChrPos(0xF6, -570, 0, 12740, 0)
    SetChrPos(0xF7, 640, 0, 12760, 0)
    SetChrPos(0xF8, -900, 0, 10550, 0)
    SetChrPos(0xF9, 1450, 0, 10750, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1652")

    ChrTalk(    #42
        0x101,
        "#1005F#5PWhat...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_1652")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1676")

    ChrTalk(    #43
        0x102,
        "#1502F#5PUgh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_1676")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1698")

    ChrTalk(    #44
        0x110,
        "#264F#5POh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_1698")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BF")

    ChrTalk(    #45
        0x10B,
        "#216F#5PEeeeeek!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_16BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E6")

    ChrTalk(    #46
        0x107,
        "#065F#5PEeeeeek!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_16E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170D")

    ChrTalk(    #47
        0x10A,
        "#1317F#5PWhoooa!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_170D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1731")

    ChrTalk(    #48
        0x105,
        "#1162F#5PUgh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_1731")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1755")

    ChrTalk(    #49
        0x103,
        "#1533F#5PUgh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_1755")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1778")

    ChrTalk(    #50
        0x106,
        "#057F#5PGah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_1778")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179B")

    ChrTalk(    #51
        0x108,
        "#072F#5PUgh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_179B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17BE")

    ChrTalk(    #52
        0x10E,
        "#178F#5PUgh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_17BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E1")

    ChrTalk(    #53
        0x104,
        "#1546F#5POh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_17E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1804")

    ChrTalk(    #54
        0x10D,
        "#270F#5PUgh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1824")

    label("loc_1804")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1824")

    ChrTalk(    #55
        0x10C,
        "#112F#5PUgh!\x02",
    )

    CloseMessageWindow()

    label("loc_1824")

    WaitChrThread(0xF8, 0x1)
    OP_43(0x10, 0x0, 0x0, 0x4)
    Sleep(2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1858")
    OP_62(0xF6, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_18B0")

    label("loc_1858")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187B")
    OP_62(0xF6, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_18B0")

    label("loc_187B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189E")
    OP_62(0xF6, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_18B0")

    label("loc_189E")

    OP_62(0xF6, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_18B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D3")
    OP_62(0xF7, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_192B")

    label("loc_18D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F6")
    OP_62(0xF7, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_192B")

    label("loc_18F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1919")
    OP_62(0xF7, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_192B")

    label("loc_1919")

    OP_62(0xF7, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_192B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_194E")
    OP_62(0xF8, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_19A6")

    label("loc_194E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1971")
    OP_62(0xF8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_19A6")

    label("loc_1971")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1994")
    OP_62(0xF8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_19A6")

    label("loc_1994")

    OP_62(0xF8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_19A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C9")
    OP_62(0xF9, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A21")

    label("loc_19C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19EC")
    OP_62(0xF9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A21")

    label("loc_19EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A0F")
    OP_62(0xF9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A21")

    label("loc_1A0F")

    OP_62(0xF9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1A21")


    def lambda_1A27():
        OP_8F(0xFE, 0x5AA, 0x0, 0x2616, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_1A27)
    Sleep(100)

    def lambda_1A47():
        OP_8F(0xFE, 0xFFFFFC7C, 0x0, 0x254E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_1A47)
    Sleep(100)

    def lambda_1A67():
        OP_8F(0xFE, 0x280, 0x0, 0x2DF0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1A67)
    Sleep(100)

    def lambda_1A87():
        OP_8F(0xFE, 0xFFFFFDC6, 0x0, 0x2DDC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF6, 0, lambda_1A87)
    WaitChrThread(0xF6, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF6, 0)
    SetChrSubChip(0xF6, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF7, 2)
    SetChrSubChip(0xF7, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF8, 4)
    SetChrSubChip(0xF8, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF9, 6)
    SetChrSubChip(0xF9, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x10, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B40")

    ChrTalk(    #56
        0x106,
        "#057F#5PA red...Ragnard?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6A")

    label("loc_1B40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B71")

    ChrTalk(    #57
        0x101,
        "#1020F#5PA-A red Ragnard?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6A")

    label("loc_1B71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B9B")

    ChrTalk(    #58
        0x107,
        "#065F#5PR-Ragnard?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6A")

    label("loc_1B9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BCC")

    ChrTalk(    #59
        0x103,
        "#1533F#5PA red...Ragnard?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6A")

    label("loc_1BCC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BF7")

    ChrTalk(    #60
        0x105,
        "#1163F#5PR-Ragnard?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6A")

    label("loc_1BF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C3E")

    ChrTalk(    #61
        0x10B,
        "#216F#5PI-It's that dragon! Except he's all red!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6A")

    label("loc_1C3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C6E")

    ChrTalk(    #62
        0x108,
        "#072F#5PA red...Ragnard?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6A")

    label("loc_1C6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C98")

    ChrTalk(    #63
        0x10E,
        "#172F#5PR-Ragnard?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6A")

    label("loc_1C98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC9")

    ChrTalk(    #64
        0x104,
        "#1549F#5PA red...Ragnard?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6A")

    label("loc_1CC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D06")

    ChrTalk(    #65
        0x10D,
        "#271F#5PIsn't it that ancient dragon?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6A")

    label("loc_1D06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D3B")

    ChrTalk(    #66
        0x10A,
        "#1317F#5PA-An ancient dragon?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D6A")

    label("loc_1D3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D6A")

    ChrTalk(    #67
        0x10C,
        "#114F#5PAn ancient dragon?!\x02",
    )

    CloseMessageWindow()

    label("loc_1D6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E0A")

    ChrTalk(    #68
        0x110,
        (
            "#265F#5PWow... An ancient dragon!\x02\x03",

            "#261FIt looks like it's been altered from its real life\x01",
            "equivalent like the Black Ark, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E8A")

    label("loc_1E0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E8A")

    ChrTalk(    #69
        0x110,
        (
            "#265F#5PWow... An ancient dragon!\x02\x03",

            "#261FI've never seen one of those before... \x01",
            "It looks so cool!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EFD")

    ChrTalk(    #70
        0x102,
        (
            "#1506F#5PIt looks like it's been altered from its real life\x01",
            "equivalent like the Black Ark, too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFD")

    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_A2(0x2C25)
    OP_E6(0x0, 0x2)
    OP_1D(0xE1)
    Sleep(1000)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #71
        "\x07\x05Select a route.\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2199")
    OP_CC(0x0, 0x0, 0xFFFF, 0xAA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_END)), "loc_1F89")
    OP_CC(0x1, 0x0, "Right Gate Path")
    OP_CC(0x3, 0x0, 0x0)
    Jump("loc_1F9C")

    label("loc_1F89")

    OP_CC(0x1, 0x0, "Right Gate Path")

    label("loc_1F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_END)), "loc_1FBC")
    OP_CC(0x1, 0x0, "Left Gate Path")
    OP_CC(0x3, 0x0, 0x1)
    Jump("loc_1FCE")

    label("loc_1FBC")

    OP_CC(0x1, 0x0, "Left Gate Path")

    label("loc_1FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_END)), "loc_1FEE")
    OP_CC(0x1, 0x0, "Main Gate Path")
    OP_CC(0x3, 0x0, 0x2)
    Jump("loc_2000")

    label("loc_1FEE")

    OP_CC(0x1, 0x0, "Main Gate Path")

    label("loc_2000")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2025")
    OP_CC(0x1, 0x0, "Giant Gate Path")
    Jump("loc_203C")

    label("loc_2025")

    OP_CC(0x1, 0x0, "Giant Gate Path")
    OP_CC(0x3, 0x0, 0x3)

    label("loc_203C")

    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2067"),
        (1, "loc_20BD"),
        (2, "loc_2113"),
        (3, "loc_2169"),
        (SWITCH_DEFAULT, "loc_2196"),
    )


    label("loc_2067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BD")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2089")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20A1")

    label("loc_2089")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A1")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20A1")

    label("loc_20A1")

    OP_DC(0x0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7409   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2196")

    label("loc_20BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2113")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DF")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20F7")

    label("loc_20DF")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20F7")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20F7")

    label("loc_20F7")

    OP_DC(0x0, 0x1)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7413   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2196")

    label("loc_2113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2169")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2135")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_214D")

    label("loc_2135")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_214D")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_214D")

    label("loc_214D")

    OP_DC(0x0, 0x2)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7418   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2196")

    label("loc_2169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2196")
    OP_56(0x0)
    OP_DC(0x0, 0x3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7422   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2196")

    label("loc_2196")

    Jump("loc_1F53")

    label("loc_2199")

    Return()

    # Function_2_125 end

    def Function_3_219A(): pass

    label("Function_3_219A")

    Sleep(400)

    label("loc_219F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21B5")
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    Jump("loc_219F")

    label("loc_21B5")

    Return()

    # Function_3_219A end

    def Function_4_21B6(): pass

    label("Function_4_21B6")

    Fade(500)
    OP_72(0x2008, 0x0)
    ExitThread()
    OP_D8(0x8, 0x3E8)
    OP_6F(0x8, 80)
    OP_70(0x8, 0x78)
    Sleep(1300)

    def lambda_21DE():
        OP_6B(6900, 3000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_21DE)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x258)
    OP_7C(0x12C, 0x12C, 0x1388, 0x258)
    OP_73(0x8)
    OP_D8(0x8, 0x3E8)
    OP_71(0x2008, 0x0)
    ExitThread()
    OP_6F(0x8, 5)
    OP_70(0x8, 0x37)
    Return()

    # Function_4_21B6 end

    def Function_5_222B(): pass

    label("Function_5_222B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(246, 0x40, 0x2)
    OP_E0(246, 0x41, 0x3)
    OP_E0(247, 0x42, 0x2)
    OP_E0(247, 0x43, 0x3)
    OP_E0(248, 0x44, 0x2)
    OP_E0(248, 0x45, 0x3)
    OP_E0(249, 0x46, 0x2)
    OP_E0(249, 0x47, 0x3)
    SetChrPos(0xF6, -570, 0, 12740, 0)
    SetChrPos(0xF7, 640, 0, 12760, 0)
    SetChrPos(0xF8, -1100, 0, 10550, 0)
    SetChrPos(0xF9, 1250, 0, 10750, 0)
    SetChrChipByIndex(0xF6, 0)
    SetChrSubChip(0xF6, 0)
    SetChrChipByIndex(0xF7, 2)
    SetChrSubChip(0xF7, 0)
    SetChrChipByIndex(0xF8, 4)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 6)
    SetChrSubChip(0xF9, 0)
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    SetChrPos(0x10, 7000, 0, 30000, 205)
    OP_A1(0x10, 0x8)
    OP_72(0x408, 0x0)
    ExitThread()
    OP_B0(0x8, 0xF)
    OP_6F(0x8, 5)
    OP_70(0x8, 0x37)
    OP_6D(0, 1600, 30240, 0)
    OP_67(0, 2600, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(20000, 0)
    OP_6E(256, 0)

    def lambda_2348():
        OP_6D(0, 1600, 27240, 3500)
        ExitThread()

    QueueWorkItem(0xF6, 0, lambda_2348)

    def lambda_2360():
        OP_67(0, 1830, -10000, 3500)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_2360)

    def lambda_2378():
        OP_6B(5800, 3500)
        ExitThread()

    QueueWorkItem(0xF6, 2, lambda_2378)

    def lambda_2388():
        OP_6C(357000, 3500)
        ExitThread()

    QueueWorkItem(0xF6, 3, lambda_2388)

    def lambda_2398():
        OP_6E(260, 3500)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2398)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF6, 0x1)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #72 op#A
        (
            "\x07\x02#60W#60AThy very beings shall be devoured by this land,\x01",
            "drawn upon as sustenance!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC(0x0, 0x3)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_222B end

    def Function_6_2460(): pass

    label("Function_6_2460")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(246, 0x40, 0x2)
    OP_E0(246, 0x41, 0x3)
    OP_E0(247, 0x42, 0x2)
    OP_E0(247, 0x43, 0x3)
    OP_E0(248, 0x44, 0x2)
    OP_E0(248, 0x45, 0x3)
    OP_E0(249, 0x46, 0x2)
    OP_E0(249, 0x47, 0x3)
    SetChrPos(0xF6, -570, 0, 12740, 0)
    SetChrPos(0xF7, 640, 0, 12760, 0)
    SetChrPos(0xF8, -1100, 0, 10550, 0)
    SetChrPos(0xF9, 1250, 0, 10750, 0)
    SetChrChipByIndex(0xF6, 0)
    SetChrSubChip(0xF6, 0)
    SetChrChipByIndex(0xF7, 2)
    SetChrSubChip(0xF7, 0)
    SetChrChipByIndex(0xF8, 4)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 6)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0x10, 0, 0, 30000, 180)
    OP_A1(0x10, 0x8)
    OP_72(0x408, 0x0)
    ExitThread()
    OP_B0(0x8, 0xF)
    OP_6F(0x8, 5)
    OP_70(0x8, 0x37)
    OP_6D(0, 1600, 27240, 0)
    OP_67(0, 2410, -10000, 0)
    OP_6B(7000, 0)
    OP_6C(0, 0)
    OP_6E(260, 0)
    FadeToBright(500, 0)
    OP_0D()
    Battle(0x336, 0x0, 0x0, 0x0, 0xFF)
    OP_A2(0x2C2C)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25B2")
    OP_DC(0x0, 0x3)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_267B")

    label("loc_25B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2617")
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25DB")
    OP_DC(0x0, 0x0)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2614")

    label("loc_25DB")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F9")
    OP_DC(0x0, 0x1)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2614")

    label("loc_25F9")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2614")
    OP_DC(0x0, 0x2)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2614")

    Jump("loc_267B")

    label("loc_2617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_267B")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2642")
    OP_DC(0x0, 0x0)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_267B")

    label("loc_2642")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2660")
    OP_DC(0x0, 0x1)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_267B")

    label("loc_2660")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267B")
    OP_DC(0x0, 0x2)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_267B")

    Return()

    # Function_6_2460 end

    SaveToFile()

Try(main)
