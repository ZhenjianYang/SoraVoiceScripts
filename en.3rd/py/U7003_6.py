from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7003_6 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7003.x',
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
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_4301",         # 03, 3
        "Function_4_434F",         # 04, 4
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17A")
    TalkBegin(0xFE)

    ChrTalk(    #0
        0x20,
        (
            "#265FThe Arseille's that really pretty white ship,\x01",
            "right?\x02\x03",

            "#261FHeehee. I've wanted to have a ride on it for \x01",
            "ages.\x02\x03",

            "The view from the deck sounds like it's amazing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3")

    label("loc_17A")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x11, 400)
    Sleep(300)

    ChrTalk(    #1
        0x20,
        (
            "#264FOh, dear! Are you being naughty again, Ries?\x02\x03",

            "#260FYou're supposed to be getting ready, not stuffing\x01",
            "yourself full of food when you think no one's looking.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x11, 255)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(200)
    TurnDirection(0x11, 0x20, 600)
    Sleep(200)

    ChrTalk(    #2
        0x11,
        (
            "#1933FI-I'm doing no such thing!\x02\x03",

            "#1940FThis is purely a taste-testing exercise.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 0)
    OP_4B(0x11, 255)

    label("loc_2D3")

    OP_A2(0x6)
    Jump("loc_387")

    label("loc_2D9")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0x20,
        (
            "#265FI can't wait to ride on the Arseille!\x02\x03",

            "#261FTeehee. This is going to be such a wonderful trip.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_387")

    ChrTalk(    #4
        0x109,
        "#1066FWe're not going on a picnic, you know...\x02",
    )

    CloseMessageWindow()

    label("loc_387")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_4300")

    label("loc_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_3013")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0B")
    EventBegin(0x0)
    OP_4A(0x20, 255)
    OP_4A(0x11, 255)
    OP_4A(0x1E, 255)
    SetChrPos(0x11, 93410, -14000, -52280, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E6")
    Fade(500)
    OP_6D(97110, -14000, -51710, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(1920, 0)
    OP_6C(48000, 0)
    OP_6E(476, 0)
    SetChrPos(0xEE, 95350, -14000, -52580, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_465")
    SetChrPos(0xEF, 94630, -14000, -54700, 45)
    SetChrPos(0xF0, 94280, -14000, -51660, 90)
    SetChrPos(0xF1, 93340, -14000, -53740, 90)
    Jump("loc_4EA")

    label("loc_465")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A9")
    SetChrPos(0xF0, 94630, -14000, -54700, 45)
    SetChrPos(0xEF, 94280, -14000, -51660, 90)
    SetChrPos(0xF1, 93340, -14000, -53740, 90)
    Jump("loc_4EA")

    label("loc_4A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EA")
    SetChrPos(0xF1, 94630, -14000, -54700, 45)
    SetChrPos(0xEF, 94280, -14000, -51660, 90)
    SetChrPos(0xF0, 93340, -14000, -53740, 90)

    label("loc_4EA")

    TurnDirection(0x20, 0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #5
        0x109,
        (
            "#1079F#6PHuh? What're you doing here, Renne?\x02\x03",

            "#1066FTrying to guess who the next guardian will be\x01",
            "or something?\x02\x03",

            "#1068FIt'd sure help if we knew how they fought before\x01",
            "we actually ended up in battle with them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x20,
        (
            "#263F#11PI suppose it would.\x02\x03",

            "#269FThe Lord of Phantasma always picks really exciting\x01",
            "people for us to fight, don't they?\x02\x03",

            "#265FI can hardly wait to see who makes an appearance\x01",
            "in our fairy tale next.\x02\x03",

            "#261FWhoever will it be? ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1061F#6PU-Umm... You're looking forward to the next fight?\x02\x03",

            "#1066FSo you're not trying to work out who it'll be against,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x20,
        (
            "#264F#11PWhy would I want to do that?\x02\x03",

            "#1305FFairy tales are always more exciting when you\x01",
            "don't know what's going to happen.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(2000)

    ChrTalk(    #9
        0x10F,
        (
            "#1446F#12P...I was reluctant to comment at first, but now\x01",
            "I feel obliged to do so.\x02\x03",

            "#1805FDo you not find such remarks a little imprudent?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x20, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_88C():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_88C)

    def lambda_89A():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_89A)

    def lambda_8A8():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8A8)

    def lambda_8B6():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_8B6)
    TurnDirection(0x20, 0x10F, 400)
    Sleep(200)

    ChrTalk(    #10
        0x20,
        "#264F#11PImprudent?\x02",
    )

    CloseMessageWindow()
    Jump("loc_14F8")

    label("loc_8E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_C74")
    Fade(500)
    OP_6D(88090, -14000, -51890, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2070, 0)
    OP_6C(47000, 0)
    OP_6E(512, 0)
    SetChrPos(0xEE, 84050, -14000, -53200, 90)
    SetChrPos(0xEF, 84000, -14000, -51820, 90)
    SetChrPos(0xF0, 82700, -14000, -53630, 90)
    SetChrPos(0xF1, 82660, -14000, -51800, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #11
        0x11,
        (
            "#1446F#6P...I was reluctant to comment at first, but now\x01",
            "I feel obliged to do so.\x02\x03",

            "#1805FDo you not find such remarks a little imprudent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x20,
        "#264F#12PImprudent?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A49")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_AB0")

    label("loc_A49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A71")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_AB0")

    label("loc_A71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A99")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_AB0")

    label("loc_A99")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_AB0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADD")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_B44")

    label("loc_ADD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B05")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_B44")

    label("loc_B05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2D")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_B44")

    label("loc_B2D")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_B44")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B71")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_BD8")

    label("loc_B71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B99")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_BD8")

    label("loc_B99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC1")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_BD8")

    label("loc_BC1")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_BD8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C05")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C6C")

    label("loc_C05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2D")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C6C")

    label("loc_C2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C55")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_C6C")

    label("loc_C55")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_C6C")

    Sleep(1000)
    Jump("loc_14F8")

    label("loc_C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_1047")
    Fade(500)
    OP_6D(93730, -14000, -51100, 0)
    OP_67(0, 5330, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(51000, 0)
    OP_6E(394, 0)
    SetChrPos(0xEE, 87290, -14000, -53260, 270)
    SetChrPos(0xEF, 87420, -14000, -51850, 270)
    SetChrPos(0xF0, 88980, -14000, -53460, 270)
    SetChrPos(0xF1, 89350, -14000, -52010, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #13
        0x11,
        (
            "#1446F#6P...I was reluctant to comment at first, but now\x01",
            "I feel obliged to do so.\x02\x03",

            "#1805FDo you not find such remarks a little imprudent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x20,
        "#264F#11PImprudent?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD7")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_E3E")

    label("loc_DD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFF")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_E3E")

    label("loc_DFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E27")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_E3E")

    label("loc_E27")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_E3E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6B")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_ED2")

    label("loc_E6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E93")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_ED2")

    label("loc_E93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBB")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_ED2")

    label("loc_EBB")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_ED2")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EFF")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_F66")

    label("loc_EFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F27")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_F66")

    label("loc_F27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4F")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_F66")

    label("loc_F4F")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_F66")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F93")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_FFA")

    label("loc_F93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBB")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_FFA")

    label("loc_FBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE3")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_FFA")

    label("loc_FE3")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_FFA")

    Sleep(1000)

    def lambda_1005():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1005)
    Sleep(50)

    def lambda_1018():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1018)
    Sleep(50)

    def lambda_102B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_102B)
    Sleep(50)
    OP_8C(0xF1, 90, 400)
    Sleep(300)
    Jump("loc_14F8")

    label("loc_1047")

    Fade(500)
    OP_6D(97110, -14000, -51710, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(1920, 0)
    OP_6C(48000, 0)
    OP_6E(476, 0)
    SetChrPos(0xEE, 95350, -14000, -52580, 90)
    SetChrPos(0xEF, 94480, -14000, -51660, 90)
    SetChrPos(0xF0, 94630, -14000, -54700, 45)
    SetChrPos(0xF1, 93370, -14000, -53970, 90)
    SetChrPos(0x11, 93000, -14000, -52320, 90)
    TurnDirection(0x20, 0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #15
        0x109,
        (
            "#1079F#6PHuh? What're you doing here, Renne?\x02\x03",

            "#1066FTrying to guess who the next guardian will be\x01",
            "or something?\x02\x03",

            "#1068FIt'd sure help if we knew how they fought before\x01",
            "we actually ended up in battle with them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x20,
        (
            "#263F#11PI suppose it would.\x02\x03",

            "#269FThe Lord of Phantasma always picks really exciting\x01",
            "people for us to fight, don't they?\x02\x03",

            "#265FI can hardly wait to see who makes an appearance\x01",
            "in our fairy tale next.\x02\x03",

            "#261FWhoever will it be? ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x109,
        (
            "#1061F#6PU-Umm... You're looking forward to the next fight?\x02\x03",

            "#1066FSo you're not trying to work out who it'll be against,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x20,
        (
            "#264F#11PWhy would I want to do that?\x02\x03",

            "#1305FFairy tales are always more exciting when you\x01",
            "don't know what's going to happen.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13BD():
        OP_6D(96000, -14000, -51710, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_13BD)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(2000)
    WaitChrThread(0xEE, 0x3)

    ChrTalk(    #19
        0x11,
        (
            "#1446F#6P...I was reluctant to comment at first, but now\x01",
            "I feel obliged to do so.\x02\x03",

            "#1805FDo you not find such remarks a little imprudent?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x20, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_149C():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_149C)

    def lambda_14AA():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_14AA)

    def lambda_14B8():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_14B8)

    def lambda_14C6():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_14C6)
    TurnDirection(0x20, 0x11, 400)
    Sleep(400)

    ChrTalk(    #20
        0x20,
        "#264F#11PImprudent?\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    label("loc_14F8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_8C(0x20, 270, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1522")
    SetChrFlags(0x10F, 0x8)
    ClearChrFlags(0x11, 0x80)

    label("loc_1522")

    SetChrPos(0x11, 94850, -14000, -52390, 90)
    SetChrPos(0xEE, 93550, -14000, -53440, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EE")
    SetChrPos(0xEF, 94850, -14000, -52390, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1596")
    SetChrPos(0xF0, 92780, -14000, -51830, 90)
    SetChrPos(0xF1, 92390, -14000, -54300, 90)
    Jump("loc_15EB")

    label("loc_1596")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C9")
    SetChrPos(0xF1, 92780, -14000, -51830, 90)
    SetChrPos(0xF0, 92390, -14000, -54300, 90)
    Jump("loc_15EB")

    label("loc_15C9")

    SetChrPos(0xF0, 91700, -14000, -52850, 90)
    SetChrPos(0xF1, 92390, -14000, -54300, 90)

    label("loc_15EB")

    Jump("loc_1841")

    label("loc_15EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1698")
    SetChrPos(0xF0, 94630, -14000, -54700, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1640")
    SetChrPos(0xEF, 92780, -14000, -51830, 90)
    SetChrPos(0xF1, 92390, -14000, -54300, 90)
    Jump("loc_1695")

    label("loc_1640")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1673")
    SetChrPos(0xF1, 92780, -14000, -51830, 90)
    SetChrPos(0xEF, 92390, -14000, -54300, 90)
    Jump("loc_1695")

    label("loc_1673")

    SetChrPos(0xEF, 91700, -14000, -52850, 90)
    SetChrPos(0xF1, 92390, -14000, -54300, 90)

    label("loc_1695")

    Jump("loc_1841")

    label("loc_1698")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1742")
    SetChrPos(0xF1, 94630, -14000, -54700, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16EA")
    SetChrPos(0xEF, 92780, -14000, -51830, 90)
    SetChrPos(0xF0, 92390, -14000, -54300, 90)
    Jump("loc_173F")

    label("loc_16EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_171D")
    SetChrPos(0xF0, 92780, -14000, -51830, 90)
    SetChrPos(0xEF, 92390, -14000, -54300, 90)
    Jump("loc_173F")

    label("loc_171D")

    SetChrPos(0xEF, 91700, -14000, -52850, 90)
    SetChrPos(0xF0, 92390, -14000, -54300, 90)

    label("loc_173F")

    Jump("loc_1841")

    label("loc_1742")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1786")
    SetChrPos(0xEF, 92780, -14000, -51830, 90)
    SetChrPos(0xF0, 92390, -14000, -54300, 90)
    SetChrPos(0xF1, 91700, -14000, -52850, 90)
    Jump("loc_1841")

    label("loc_1786")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CA")
    SetChrPos(0xF0, 92780, -14000, -51830, 90)
    SetChrPos(0xEF, 92390, -14000, -54300, 90)
    SetChrPos(0xF1, 91700, -14000, -52850, 90)
    Jump("loc_1841")

    label("loc_17CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_180E")
    SetChrPos(0xF1, 92780, -14000, -51830, 90)
    SetChrPos(0xEF, 92390, -14000, -54300, 90)
    SetChrPos(0xF0, 91700, -14000, -52850, 90)
    Jump("loc_1841")

    label("loc_180E")

    SetChrPos(0xEF, 92780, -14000, -51830, 90)
    SetChrPos(0xF0, 92390, -14000, -54300, 90)
    SetChrPos(0xF1, 91700, -14000, -52850, 90)

    label("loc_1841")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1871")
    SetChrFlags(0x101, 0x8)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 92780, -14000, -51830, 90)
    OP_44(0x1E, 0xFF)
    Jump("loc_1882")

    label("loc_1871")

    SetChrPos(0x1E, 80540, -13100, -52040, 90)

    label("loc_1882")

    OP_6D(94920, -14000, -51020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(315000, 0)
    OP_6E(406, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #21
        0x11,
        (
            "#1446F#5PIt's clear from all they've done so far that the\x01",
            "Lord of Phantasma is our enemy.\x02\x03",

            "Furthermore, while the guardians we are\x01",
            "fighting may not be the individuals themselves,\x01",
            "their personalities are still being violated.\x02\x03",

            "#1443FIn light of that, I hardly find it appropriate to\x01",
            "be talking about all of this like it's some sort\x01",
            "of game orchestrated for your entertainment.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #22
        0x109,
        "#1079F#5PU-Umm... Ries...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x20,
        (
            "#262F#12P...\x02\x03",

            "#268FWhat's got you so mad all of a sudden?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#1446F#5PI'm not.\x02\x03",

            "#1445FHowever, I was under the distinct impression\x01",
            "that we were all in agreement on one thing:\x01",
            "the Lord of Phantasma was our enemy.\x02\x03",

            "#1443FSo I will not stand by and listen to them being,\x01",
            "of all things, praised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x20,
        (
            "#263F#12PReally, now?\x02\x03",

            "#260FCome to think of it, every time we've encountered\x01",
            "them, they've always made a point of taunting you\x01",
            "and Kevin, haven't they?\x02\x03",

            "#261FHeeheehee. That wouldn't have anything to do with \x01",
            "why you're angry, would it?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0x11,
        "#1441F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x20,
        (
            "#263F#12POooh. I bet it does.\x02\x03",

            "The Lord of Phantasma seems to have a peculiar\x01",
            "fascination with Kevin, and yet you just can't\x01",
            "work out why...\x02\x03",

            "#1306FThat's why you're getting so worked up, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        "#1067F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x11,
        (
            "#1443F#5P...\x02\x03",

            "#1446FThis isn't a game, Renne.\x02\x03",

            "#1805FYou might be a genius, but that doesn't mean\x01",
            "everything in life will go the way you want it to,\x01",
            "and to assume otherwise is sheer arrogance.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x1E, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206B")

    NpcTalk(    #30
        0x1E,
        "Voice",
        "#4P...Okay, okay! That's enough.\x02",
    )

    CloseMessageWindow()

    def lambda_1EB9():
        OP_6D(90000, -14000, -51430, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1EB9)
    OP_43(0x1E, 0x0, 0x3, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EF1")
    OP_62(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1EF1")

    OP_62(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F27")
    OP_62(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1F27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F46")
    OP_62(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1F46")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F6A")
    OP_62(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1F6A")

    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1F87():

        label("loc_1F87")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_1F87")

    QueueWorkItem2(0x0, 0, lambda_1F87)

    def lambda_1F98():

        label("loc_1F98")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_1F98")

    QueueWorkItem2(0x1, 0, lambda_1F98)

    def lambda_1FA9():

        label("loc_1FA9")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_1FA9")

    QueueWorkItem2(0x2, 0, lambda_1FA9)

    def lambda_1FBA():

        label("loc_1FBA")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_1FBA")

    QueueWorkItem2(0x3, 0, lambda_1FBA)

    def lambda_1FCB():

        label("loc_1FCB")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_1FCB")

    QueueWorkItem2(0x11, 0, lambda_1FCB)

    def lambda_1FDC():

        label("loc_1FDC")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_1FDC")

    QueueWorkItem2(0x20, 0, lambda_1FDC)
    WaitChrThread(0xEE, 0x3)
    Sleep(1000)

    def lambda_1FF7():
        OP_6D(95010, -14000, -50480, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1FF7)

    def lambda_200F():
        OP_67(0, 5350, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_200F)

    def lambda_2027():
        OP_6B(2160, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_2027)

    def lambda_2037():
        OP_6C(327000, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_2037)
    WaitChrThread(0x1E, 0x0)
    WaitChrThread(0xEE, 0x3)
    OP_44(0x20, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x0, 0x0)
    OP_44(0x1, 0x0)
    OP_44(0x2, 0x0)
    OP_44(0x3, 0x0)
    Sleep(200)
    Jump("loc_21AB")

    label("loc_206B")


    def lambda_2071():
        OP_6D(94660, -14000, -50260, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2071)

    def lambda_2089():
        OP_67(0, 5350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_2089)

    def lambda_20A1():
        OP_6B(2160, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_20A1)

    def lambda_20B1():
        OP_6C(327000, 2000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_20B1)
    SetChrFlags(0x1E, 0x40)

    def lambda_20C6():
        OP_8E(0xFE, 0x16F12, 0xFFFFC950, 0xFFFF38A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_20C6)
    WaitChrThread(0x1E, 0x0)

    def lambda_20E6():
        OP_8E(0xFE, 0x17552, 0xFFFFC950, 0xFFFF3936, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_20E6)

    def lambda_2101():

        label("loc_2101")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_2101")

    QueueWorkItem2(0x0, 0, lambda_2101)

    def lambda_2112():

        label("loc_2112")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_2112")

    QueueWorkItem2(0x1, 0, lambda_2112)

    def lambda_2123():

        label("loc_2123")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_2123")

    QueueWorkItem2(0x2, 0, lambda_2123)

    def lambda_2134():

        label("loc_2134")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_2134")

    QueueWorkItem2(0x3, 0, lambda_2134)
    WaitChrThread(0x1E, 0x0)
    OP_44(0x0, 0x0)
    OP_44(0x1, 0x0)
    OP_44(0x2, 0x0)
    OP_44(0x3, 0x0)
    OP_8C(0x1E, 180, 800)
    ClearChrFlags(0x1E, 0x40)
    WaitChrThread(0xEE, 0x3)

    ChrTalk(    #31
        0x1E,
        "#1007F#5P...Okay, okay! That's enough.\x02",
    )

    CloseMessageWindow()

    def lambda_2197():
        TurnDirection(0xFE, 0x1E, 400)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2197)
    Sleep(100)
    TurnDirection(0x11, 0x1E, 400)

    label("loc_21AB")


    ChrTalk(    #32
        0x1E,
        "#1009F#11PLet's stop this before it gets nasty.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1E, 135, 400)
    Sleep(300)

    ChrTalk(    #33
        0x1E,
        (
            "#1019F#5PRenne, bringing up things that clearly bother\x01",
            "people and teasing them with them isn't a very\x01",
            "nice to thing to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1E, 180, 400)
    Sleep(300)

    ChrTalk(    #34
        0x1E,
        (
            "#1007F#11PAs for you, Ries...\x02\x03",

            "#1002FShe might be smarter than other girls her age,\x01",
            "but that doesn't change the fact that Renne is\x01",
            "still an ordinary 12-year-old girl.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x20, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    ChrTalk(    #35
        0x20,
        "#264F#12P...Excuse me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        (
            "#1443F#6P...\x02\x03",

            "#1446FI'm not sure I understand what you mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x1E,
        (
            "#1003F#11PWell, let me put it this way.\x02\x03",

            "#1002FShe's smart and she's strong. We both know that.\x02\x03",

            "But do those two things really make her that much\x01",
            "different from other girls her age? Or make it so\x01",
            "that she can't act like they do?\x02\x03",

            "#1007FBecause I think you'd find plenty of 12-year-olds\x01",
            "out there who're a little selfish and cheeky or like\x01",
            "to cause trouble. That's pretty normal.\x02\x03",

            "#1006FPlus she's got tons of good points, too, like how\x01",
            "she's always considerate toward others when the\x01",
            "situation calls for it.\x02\x03",

            "#1016FSee? She's just like your average girl who goes\x01",
            "to Sunday School, right? Just a little brighter\x01",
            "and a little stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        "#1802F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x20,
        "#1307F#12P...You think so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x1E,
        (
            "#1025F#11PIt just doesn't seem fair to me to hold her to a\x01",
            "totally different standard than everyone else her\x01",
            "age because you see her as somehow different.\x02\x03",

            "#1007FThat's not to say don't tell her off if she's been\x01",
            "bad, because you do that to kids, too...\x02\x03",

            "#1003FIt's more you're being unusually hard on her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x11,
        (
            "#1445F#6P...\x02\x03",

            "#1446FI suppose you may be right.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x20, 400)
    Sleep(300)

    ChrTalk(    #42
        0x11,
        "#1446F#5PYou have my apologies, Renne.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x11, 400)
    Sleep(300)

    ChrTalk(    #43
        0x20,
        (
            "#269F#12PReally...? I wasn't expecting an apology from you.\x02\x03",

            "#263F...Although, your face says you've still got a lot\x01",
            "you want to say to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        (
            "#1447F#5PNaturally.\x02\x03",

            "#1448FAfter all, admonishing unreasonable children is\x01",
            "the duty of their elders, however special or not\x01",
            "special they may be.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x20, 400)
    Sleep(300)

    ChrTalk(    #45
        0x1E,
        (
            "#1006F#5PYup. Like I said, I'm not gonna disagree on that\x01",
            "point.\x02\x03",

            "As long as we're all here, we're basically her\x01",
            "guardians and stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x20,
        "#266F#12POh, please... You can say what you like.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x1E, 400)
    Sleep(300)

    ChrTalk(    #47
        0x20,
        (
            "#262F#12PBut by the way, Estelle...\x02\x03",

            "You said I was 'just like your average girl\x01",
            "who goes to Sunday School,' right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x1E,
        "#1011F#5PSure did. Am I wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x20,
        (
            "#266F#12PYou can think whatever you like about me--\x01",
            "I don't care.\x02\x03",

            "But I do want to make one correction.\x02\x03",

            "#269FI wouldn't be attending school as a student.\x01",
            "I'd be teaching there.\x02\x03",

            "I've got three doctorates, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #50
        0x1E,
        "#1004F#5P#3S...You what?#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #51
        0x11,
        "#1444F#5PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x20,
        (
            "#263F#12POne's in chemistry, one's in mathematics,\x01",
            "and the third is in information theory.\x01",
            "I even publish regular papers in those fields.\x02\x03",

            "#1305FI do it through someone else because I don't\x01",
            "want the hassle of someone finding out who\x01",
            "I am, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x1E,
        "#1016F#5PHaha...haha... R-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "#1446F#5P(Disciplining her appears as if it will be an even\x01",
            "more difficult task than I'd anticipated...)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_30(0x1)
    SetChrPos(0x1E, 55220, 1800, -49210, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DEE")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x101, 0x8)
    SetChrFlags(0x1E, 0x80)
    Jump("loc_2DF1")

    label("loc_2DEE")

    OP_85(0x1E)

    label("loc_2DF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E04")
    ClearChrFlags(0x10F, 0x8)

    label("loc_2E04")

    SetChrFlags(0x11, 0x80)
    SetChrPos(0x20, 97450, -14000, -47720, 37)
    OP_4B(0x20, 255)
    OP_4B(0x1E, 255)
    OP_4B(0x11, 255)
    OP_43(0x20, 0x0, 0x6, 0x2)
    OP_43(0x1E, 0x0, 0x6, 0x2)
    OP_43(0x11, 0x0, 0x6, 0x2)
    OP_6D(95860, -14000, -52680, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 95860, -14000, -52680, 90)
    SetChrPos(0x1, 95860, -14000, -52680, 90)
    SetChrPos(0x2, 95860, -14000, -52680, 90)
    SetChrPos(0x3, 95860, -14000, -52680, 90)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    SetMapFlags(0x80)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    ClearMapFlags(0x80)
    OP_A2(0x2668)
    Jump("loc_3010")

    label("loc_2F0B")

    TalkBegin(0xFE)

    ChrTalk(    #55
        0x20,
        (
            "#266F*sigh* Don't go underestimating me, if you\x01",
            "wouldn't mind.\x02\x03",

            "#262FAnd don't forget: you've got no chance of\x01",
            "getting out of this world unless I'm with you\x01",
            "to help.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_300D")

    ChrTalk(    #56
        0x101,
        (
            "#1007FWe won't, we won't...\x02\x03",

            "#1006FWe're counting on you, Renne.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_300D")

    TalkEnd(0xFE)

    label("loc_3010")

    Jump("loc_4300")

    label("loc_3013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_34A5")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3133")
    OP_51(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x107, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30C9")
    Jump("loc_310B")

    label("loc_30C9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30E5")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_310B")

    label("loc_30E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3101")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_310B")

    label("loc_3101")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_310B")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jump("loc_322A")

    label("loc_3133")

    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x12, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31C3")
    Jump("loc_3205")

    label("loc_31C3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31DF")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3205")

    label("loc_31DF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31FB")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3205")

    label("loc_31FB")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3205")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    label("loc_322A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3419")

    ChrTalk(    #57
        0x20,
        (
            "#263FI wasn't expecting the Lord of Phantasma to\x01",
            "make a copy of that narrow-eyed old man.\x02\x03",

            "#269FThey really know how to make their games\x01",
            "interesting.\x02\x03",

            "I can't wait to finally get to face off against\x01",
            "them directly...\x02\x03",

            "#261F...Maaaybe I should try and sneak on ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33A4")

    ChrTalk(    #58
        0x107,
        (
            "#562FTh-That's dangerous, Renne...\x02\x03",

            "Just be patient and stick with us, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F6")

    label("loc_33A4")


    ChrTalk(    #59
        0x12,
        (
            "#562FTh-That's dangerous, Renne...\x02\x03",

            "Just be patient and stick with us, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3413")

    ChrTalk(    #60
        0x10F,
        "#1440F...\x02",
    )

    CloseMessageWindow()

    label("loc_3413")

    OP_A2(0x0)
    Jump("loc_3491")

    label("loc_3419")


    ChrTalk(    #61
        0x20,
        (
            "#266FBeing stuck here is so boring.\x02\x03",

            "#265F...Maaaybe I should try and sneak on ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3491")

    ChrTalk(    #62
        0x10F,
        "#1440F...\x02",
    )

    CloseMessageWindow()

    label("loc_3491")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4300")

    label("loc_34A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_357F")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3526")

    ChrTalk(    #63
        0x20,
        (
            "#260FI've got looots of plushies.\x02\x03",

            "My room's full of them!\x02\x03",

            "#261FI wish I could show you them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_3574")

    label("loc_3526")


    ChrTalk(    #64
        0x20,
        (
            "#260FMy room's full of plushies.\x02\x03",

            "#261FI wish I could show you them all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3574")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_4300")

    label("loc_357F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_4300")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AF6")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x107, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3634")
    Jump("loc_3676")

    label("loc_3634")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3650")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3676")

    label("loc_3650")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_366C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3676")

    label("loc_366C")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3676")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #65
        0x107,
        "#560FOooh, Renne!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x20,
        (
            "#264FOh, are you going off with Estelle, Tita?\x02\x03",

            "#266FWhy can't I go, too? It's boring being here\x01",
            "all on my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x107,
        (
            "#065FS-Sorry...\x02\x03",

            "#066FI know! I'll go shopping with you again\x01",
            "to make up for it!\x02\x03",

            "#067FMaybe we can try to find something as\x01",
            "nice as those brooches we bought last\x01",
            "time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x20,
        (
            "#260FTeehee. I'm sure we can.\x02\x03",

            "#267FThat reminds me, though...\x01",
            "I found one exactly like them in a tiny little\x01",
            "shop a while back.\x02\x03",

            "#261FThe jewel in the middle was red, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x107,
        (
            "#064FAww... You're so lucky.\x02\x03",

            "They were all sold out of those in the shop\x01",
            "in Grancel.\x02\x03",

            "#562F*sigh* I really wanted a red one, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x20,
        (
            "#265FI know! Why don't we go on a shopping trip\x01",
            "together sometime, then? We could go to\x01",
            "somewhere reeeally far away.\x02\x03",

            "#269FYou'd like the Eastern Quarter in Calvard,\x01",
            "that's for sure. You could spend a whole day\x01",
            "shopping there and never feel bored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x107,
        (
            "#064FR-Really?\x02\x03",

            "#061FI wonder what kinds of cute accessories\x01",
            "they'd have there?\x02\x03",

            "#560FOh, yeah! Let me tell you about the pendant \x01",
            "I bought a while back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1016F(These two sure are having fun together.)\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_3DEC")

    label("loc_3AF6")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #73
        0x20,
        (
            "#261F...But guess what? I found a brooch exactly\x01",
            "like the ones we bought a while back there.\x02\x03",

            "#265FThe jewel in the middle was red, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x12,
        (
            "#064FAww... You're so lucky.\x02\x03",

            "They were all sold out of those in the shop\x01",
            "in Grancel.\x02\x03",

            "#562F*sigh* I really wanted one, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x20,
        (
            "#265FI know! Why don't we go on a shopping trip\x01",
            "together sometime, then? We could go to\x01",
            "somewhere reeeally far away.\x02\x03",

            "#269FYou'd like the Eastern Quarter in Calvard,\x01",
            "that's for sure. You could spend a whole day\x01",
            "shopping there and never feel bored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x12,
        (
            "#064FR-Really?\x02\x03",

            "#061FI wonder what kinds of cute accessories\x01",
            "they'd have there?\x02\x03",

            "#560FOh, yeah! Let me tell you about the pendant \x01",
            "I bought a while back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1016F(These two sure are having fun together.)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_3DEC")

    OP_A2(0x2662)
    Jump("loc_4300")

    label("loc_3DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40C1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FD1")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x107, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EA0")
    Jump("loc_3EE2")

    label("loc_3EA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3EBC")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE2")

    label("loc_3EBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3ED8")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE2")

    label("loc_3ED8")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EE2")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #78
        0x20,
        (
            "#261FI found a reeeally huge stuffed bear in\x01",
            "a shop in the Empire a while back.\x02\x03",

            "#265FIt was as big as a grown man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x107,
        (
            "#065FWh-What? Really?!\x02\x03",

            "#067F...I kinda want to see it now.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_40BB")

    label("loc_3FD1")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #80
        0x20,
        (
            "#260FThere are loads of big shops in the Empire,\x01",
            "too.\x02\x03",

            "#261FI found a huge stuffed bear in one of them\x01",
            "a while back.\x02\x03",

            "It was as big as a grown man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x12,
        (
            "#065FWh-What? Really?!\x02\x03",

            "#067F...I kinda want to see it now.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_40BB")

    OP_A2(0x6)
    Jump("loc_4300")

    label("loc_40C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4277")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x107, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x107, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4167")
    Jump("loc_41A9")

    label("loc_4167")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4183")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41A9")

    label("loc_4183")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_419F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41A9")

    label("loc_419F")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_41A9")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x107, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #82
        0x20,
        (
            "#260FThere are loads of big shops in the Empire,\x01",
            "too.\x02\x03",

            "#261FI found a huge stuffed bear in one of them\x01",
            "a while back.\x02\x03",

            "It was as big as a grown man!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_4300")

    label("loc_4277")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #83
        0x20,
        (
            "#261FI found a reeeally huge stuffed bear in\x01",
            "a shop in the Empire a while back.\x02\x03",

            "#265FIt was as big as a grown man!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_4300")

    Return()

    # Function_2_AC end

    def Function_3_4301(): pass

    label("Function_3_4301")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x1603A, 0xFFFFC950, 0xFFFF3508, 0xBB8, 0x0)
    OP_8E(0xFE, 0x169CC, 0xFFFFC950, 0xFFFF3ADA, 0xBB8, 0x0)
    OP_8E(0xFE, 0x17552, 0xFFFFC950, 0xFFFF3936, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    SetChrFlags(0xFE, 0x40)
    Return()

    # Function_3_4301 end

    def Function_4_434F(): pass

    label("Function_4_434F")

    SetChrFlags(0x18, 0x10)
    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43E4")

    ChrTalk(    #84
        0x18,
        "#311F...Scree! ☆\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 1200, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x18)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #85
        "\x07\x05Sieg is happily eating food from Kloe's hand.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0xF)
    Jump("loc_444C")

    label("loc_43E4")

    OP_62(0x18, 0x0, 1200, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x18)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #86
        "\x07\x05Sieg is happily eating food from Kloe's hand.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_444C")

    ClearChrFlags(0x18, 0x10)
    TalkEnd(0x18)
    Return()

    # Function_4_434F end

    SaveToFile()

Try(main)
