from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2700_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2700.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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

    ScpFunction(
        "Function_0_66",           # 00, 0
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetMapFlags(0x400000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_44(0x8, 0xFF)
    OP_6D(10100, 15000, 8500, 0)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_E9():
        OP_69(0xC, 0x1770)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E9)
    OP_6B(2800, 6000)
    OP_0D()
    WaitChrThread(0xC, 0x1)
    Sleep(1000)

    ChrTalk(    #0
        0x8,
        "#4PSo...has His Grace changed his mind?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#720FHe is not the sort to do so, once\x01",
            "he has decided on something.\x02\x03",

            "In light of that, I believe\x01",
            "he'll be staying here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "#4PHmm... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#4PThen we'll have to wait for\x01",
            "the bracers to arrive before\x01",
            "we can do anything more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "#720FI'm afraid so.\x02\x03",

            "If that's all, then, I shall\x01",
            "take my leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "#4PWish us luck.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x9, 0x578, 0x1388, 0x7D0, 0x7D0, 0x0)

    def lambda_295():
        OP_8E(0x9, 0xFFFFEDA4, 0x1388, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_295)
    OP_8C(0x8, 0, 400)
    SetChrPos(0x101, -3600, 5000, 0, 90)
    SetChrPos(0x102, -4600, 5000, -1000, 90)
    SetChrPos(0x105, -5600, 5000, 400, 90)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)

    def lambda_2F9():
        OP_94(0x1, 0x101, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F9)
    Sleep(200)

    def lambda_314():
        OP_94(0x1, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_314)
    Sleep(200)

    def lambda_32F():
        OP_94(0x1, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_32F)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    OP_8C(0x101, 315, 400)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #6
        0x101,
        (
            "#004F#2P...Huh?\x02\x03",

            "I think I know that guy...\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x80)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 400)
    Sleep(400)

    ChrTalk(    #7
        0x8,
        "#4POh, it's you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "#4PYou're bracers, aren't you?\x02",
    )

    CloseMessageWindow()
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_447():
        OP_69(0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_447)

    def lambda_455():
        OP_94(0x1, 0x8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_455)

    def lambda_46B():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46B)

    def lambda_479():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_479)
    TurnDirection(0x105, 0x8, 400)
    WaitChrThread(0x8, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_593")

    ChrTalk(    #9
        0x8,
        (
            "#4PThank Aidios you're here.\x01",
            "The name's Chief Warrant Officer Hahn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#508FIt's nice to meet you. I'm\x01",
            "Estelle, bracer in training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        (
            "#010FAnd I'm Joshua...also in training.\x02\x03",

            "The bulletin board said that a\x01",
            "traveler was causing trouble...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D3")

    label("loc_593")


    ChrTalk(    #12
        0x101,
        "#501FOh... Did it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        "#014FDo you have a situation here?\x02",
    )

    CloseMessageWindow()

    label("loc_5D3")

    OP_28(0x23, 0x4, 0x4)
    OP_28(0x23, 0x4, 0x2)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #14
        0x8,
        "#4PYes, I'm afraid so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#4PWe do have an unsavory character...\x01",
            "and dealing with him is proving most\x01",
            "difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#4PDo you think you might be able\x01",
            "to help us out?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6EF"),
        (1, "loc_78A"),
        (SWITCH_DEFAULT, "loc_8F3"),
    )


    label("loc_6EF")

    OP_28(0x23, 0x4, 0x8)

    ChrTalk(    #17
        0x101,
        "#000FSure. Why not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#4PThank you. You'll be doing us\x01",
            "a big favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#4POkay, let me fill you in on\x01",
            "the details...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/T2710   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_8F3")

    label("loc_78A")

    OP_28(0x23, 0x1, 0x4000)

    ChrTalk(    #20
        0x101,
        (
            "#003FI'm sorry, but now's really not\x01",
            "a good time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#4PI see... Well, that leaves us\x01",
            "in something of a bind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#4PI'll try to hold out on my own for\x01",
            "a while, but it's not going well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#4PWhen you can spare the time,\x01",
            "please come back...I beg you...\x01",
            "don't leave us with him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#010FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "#4PThank you.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6B(3500, 0)
    OP_8C(0x8, 270, 0)
    Jump("loc_8F3")

    label("loc_8F3")

    OP_85(0x8)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
